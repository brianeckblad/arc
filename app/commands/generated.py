"""Spec-generated SCM endpoint commands.

``dev/generate_resource_catalog.py`` reads every pulled OpenAPI spec and writes
``app/commands/resource_catalog.py``.  This module turns those entries into
feature-gated ``CommandDef`` objects.  Defaults live in ``settings/features.json``
and are intentionally OFF until an operator enables the feature.

GET endpoints are directly usable as ``show`` commands.  Generic write endpoints
(``set`` / ``update`` / ``delete``) are available for advanced use with raw JSON
payloads, while curated hand-written commands still override generated ones.
"""

from __future__ import annotations

import json
import logging
import re
from pathlib import Path
from typing import Any, Callable

from rich.markup import escape as _rich_escape

from app.commands.base import CommandDef, ExecutionContext, require_scm

try:
    from app.commands.resource_catalog import CATALOG
except Exception:  # noqa: BLE001 — missing/older catalog must never break startup
    CATALOG = []

try:
    from app.settings.field_catalog import FIELD_CATALOG
except Exception:  # noqa: BLE001 — missing/broken field catalog degrades to json|file
    FIELD_CATALOG = {}

logger = logging.getLogger(__name__)


def _validate_constraints(command: str, cli_name: str, text: str, meta: dict) -> None:
    """Enforce schema-declared maxLength/pattern on one CLI field value.

    Raises an actionable ValueError before anything is staged. Spec patterns
    carry their own anchors (e.g. the fqdn pattern is ^…$), so ``re.search``
    respects them rather than forcing a full match. A broken pattern in a
    spec must never crash the CLI — it is skipped with a debug note.
    """
    max_length = meta.get("max_length")
    if isinstance(max_length, int) and max_length > 0 and len(text) > max_length:
        raise ValueError(
            f"'{command}': {cli_name} is too long — "
            f"{len(text)} characters (maximum {max_length})"
        )
    pattern = meta.get("pattern")
    if isinstance(pattern, str) and pattern:
        try:
            matched = re.search(pattern, text) is not None
        except re.error as exc:
            logger.debug("%s: skipping invalid spec pattern for %s (%s): %r",
                         command, cli_name, exc, pattern)
            return
        if not matched:
            # Escape the regex so its [character classes] survive Rich markup.
            raise ValueError(
                f"'{text}' does not match the required format for {cli_name} "
                f"[dim](pattern: {_rich_escape(pattern)})[/dim]"
            )


def _payload_from_fields(
    command: str, catalog_entry: dict, args: dict, defaults: dict | None = None
) -> dict:
    """Build a request body from structured CLI fields (prompt-time validation).

    Enforces required fields, variant type/value pairing, enum choices, and
    schema pattern/maxLength constraints
    with actionable ValueErrors BEFORE anything is staged — the vendor-CLI
    "invalid input" experience, driven by the OpenAPI schema. *defaults*
    supplies context-derived values (e.g. the active folder) for fields the
    operator did not type.
    """
    defaults = defaults or {}
    spec_args = {a["name"]: a for a in catalog_entry.get("args") or []}
    payload_spec = catalog_entry.get("payload") or {}
    list_fields = set(payload_spec.get("list_fields") or [])
    body: dict[str, Any] = {}

    variant = payload_spec.get("variant")
    if variant:
        type_field, value_field = variant["type_field"], variant["value_field"]
        chosen = str(args.get(type_field) or "").strip().lower()
        value = str(args.get(value_field) or "").strip()
        choices = variant.get("choices") or {}
        if chosen not in choices:
            raise ValueError(
                f"'{command}' needs a type: one of {', '.join(sorted(choices))}"
            )
        if not value:
            raise ValueError(f"'{command}' needs a value for type '{chosen}'")
        body[choices[chosen]] = value

    for cli_name, api_name in (payload_spec.get("fields") or {}).items():
        meta = spec_args.get(cli_name, {})
        raw = args.get(cli_name)
        if raw is None or str(raw).strip() == "":
            raw = defaults.get(cli_name)
        text = str(raw).strip() if raw is not None else ""
        if not text:
            if meta.get("required"):
                raise ValueError(f"'{command}' requires <{cli_name}>")
            continue
        choices = meta.get("choices")
        if choices and text not in choices:
            match = next((c for c in choices if c.lower() == text.lower()), None)
            if match is None:
                shown = ", ".join(choices[:8]) + (", …" if len(choices) > 8 else "")
                raise ValueError(f"'{command}': {cli_name} must be one of: {shown}")
            text = match  # accept case-insensitive input, send canonical casing
        _validate_constraints(command, cli_name, text, meta)
        if cli_name in list_fields:
            body[api_name] = [part.strip() for part in text.split(",") if part.strip()]
        else:
            body[api_name] = text
    return body


def _json_payload(args: dict) -> Any:
    """Return JSON from ``json <payload>`` or ``file <path>`` command args."""
    if "json" in args:
        return json.loads(args["json"])
    if "file" in args:
        payload_path = Path(str(args["file"])).expanduser()
        return json.loads(payload_path.read_text(encoding="utf-8"))
    raise RuntimeError(
        "This generated write command needs a JSON payload. Use: "
        "json '{\"name\":\"example\"}' or file payload.json"
    )


def _fill_path(path: str, path_params: list[str], args: dict) -> str:
    """Substitute OpenAPI ``{param}`` slots from named or positional args."""
    filled = path
    positional = list(args.get("_positional") or [])
    for idx, param in enumerate(path_params):
        value = args.get(param) or (positional[idx] if idx < len(positional) else None)
        if value is None:
            raise RuntimeError(f"Missing required path parameter: {param}")
        filled = filled.replace("{" + param + "}", str(value))
    return filled


def _query(entry: dict, ctx: ExecutionContext, args: dict) -> dict:
    """Populate known query params from context first, then command args."""
    query: dict[str, Any] = {}
    for name in entry.get("query_params") or []:
        if name == "folder":
            query[name] = ctx.folder
        elif name == "device" and ctx.target:
            query[name] = ctx.target
        elif name in args:
            query[name] = args[name]
    return query


def _make_handler(entry: dict) -> Callable[[ExecutionContext, dict], Any]:
    """Return a generic endpoint handler for one catalog entry."""

    def _run(ctx: ExecutionContext, args: dict) -> Any:
        scm = require_scm(ctx)
        method = entry["method"]
        field_entry = FIELD_CATALOG.get(entry["command"])
        if method in {"POST", "PUT", "PATCH"}:
            if method == "POST" and field_entry:
                # Flat resource with spec-derived field syntax — build the
                # payload from parsed CLI fields (validates before staging).
                # A body-level folder falls back to the active folder context.
                body = _payload_from_fields(
                    entry["command"], field_entry, args,
                    defaults={"folder": ctx.folder},
                )
            else:
                body = _json_payload(args)
        else:
            body = None
        return scm.request_api(
            entry["base_url"],
            method,
            _fill_path(entry["path"], entry.get("path_params") or [], args),
            params=_query(entry, ctx, args),
            json=body,
        )

    _run.__name__ = "_auto_" + entry["command"].replace(" ", "_").replace("-", "_")
    return _run


def _humanize(command: str) -> str:
    """'show syslog-server-profiles' -> 'Show syslog server profiles'."""
    verb, _, rest = command.partition(" ")
    return f"{verb.title()} {rest.replace('-', ' ')}"


def _field_usage(command: str, catalog_entry: dict) -> str:
    """Build a usage line from spec-derived CLI fields (drives Tab + `?`)."""
    parts = [command]
    for arg in catalog_entry.get("args") or []:
        kind, name = arg.get("kind"), arg.get("name", "value")
        if kind == "choice":
            choices = arg.get("choices") or []
            shown = "|".join(choices[:5]) + ("|…" if len(choices) > 5 else "")
            parts.append(shown)
        elif kind == "keyword":
            parts.append(f"[{name} <value>]")
        else:
            parts.append(f"<{name}>")
    return " ".join(parts)


def _usage(entry: dict) -> str:
    command = entry["command"]
    path_params = " ".join(f"{name} <value>" for name in entry.get("path_params") or [])
    if command.startswith("set ") and command in FIELD_CATALOG:
        return _field_usage(command, FIELD_CATALOG[command])
    if command.startswith(("set ", "update ")):
        parts = [command]
        if path_params:
            parts.append(path_params)
        parts.append("json|file <payload-or-path>")
        return " ".join(parts)
    if command.startswith("delete ") and path_params:
        return f"{command} {path_params}"
    return command


def _build() -> dict[str, CommandDef]:
    commands: dict[str, CommandDef] = {}
    for entry in CATALOG:
        command = entry["command"]
        commands[command] = CommandDef(
            description=entry.get("summary") or _humanize(command),
            category=entry["category"],
            scope="folder" if "folder" in (entry.get("query_params") or []) else "global",
            api_handler=_make_handler(entry),
            ssh_command=None,
            render="",          # generic list-table fallback in _render()
            feature_flag=entry["feature_flag"],
            usage=_usage(entry),
        )
    return commands


COMMANDS: dict[str, CommandDef] = _build()

