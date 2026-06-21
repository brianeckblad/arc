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
from pathlib import Path
from typing import Any, Callable

from app.commands.base import CommandDef, ExecutionContext, require_scm

try:
    from app.commands.resource_catalog import CATALOG
except Exception:  # noqa: BLE001 — missing/older catalog must never break startup
    CATALOG = []


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
        body = _json_payload(args) if method in {"POST", "PUT", "PATCH"} else None
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


def _usage(entry: dict) -> str:
    command = entry["command"]
    path_params = " ".join(f"{name} <value>" for name in entry.get("path_params") or [])
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

