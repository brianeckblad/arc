"""Loader for the per-command argument *order* that drives Tab completion.

``settings/command-structure.json`` lists, for curated commands, the
**fields in the order you type them**.  Keys can be full command strings
(preferred) or bare object names that are implicitly prefixed with ``set``:

    {
      "set address":       ["name", "type", "value", "description", "tag"],
      "set address-group": ["name", "type", "value", "description", "tag"],
      "update address":    ["name", "type", "value"],
      "delete address":    ["name"]
    }

Bare object keys (legacy) are still supported and get the ``set `` prefix.

Reorder a command by moving field names.  Everything else — choices,
required flags, Tab hints — comes from ``_FIELD_LIBRARY`` / ``_GENERIC_FIELDS``
below.  A non-programmer only ever touches the JSON field lists.

``update <obj>`` and ``delete <obj>`` entries are auto-derived from ``set <obj>``
when not explicitly listed: update reuses the same fields; delete uses only
``name``.

Generated OpenAPI commands use the field_catalog instead.  Add a JSON entry
when you want a curated parser that beats the generated form.

Any missing/malformed file falls back to usage-string completion.
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass, field

from app.paths import COMMAND_STRUCTURE_JSON

logger = logging.getLogger(__name__)

# Read once per session (edit the file + restart, or call invalidate_cache()).
_cache: dict[str, dict] | None = None

# Field metadata cache — loaded from settings/command-structure.json "field_metadata" section.
# Call _get_field_libraries() to access; cleared when invalidate_cache() is called.
_field_library_cache: dict[tuple[str, str], dict] | None = None
_generic_fields_cache: dict[str, dict] | None = None


def _get_field_libraries() -> tuple[dict[tuple[str, str], dict], dict[str, dict]]:
    """Load field metadata from settings/command-structure.json field_metadata section.

    Returns (field_library, generic_fields):
      field_library:  {(object, field): meta_dict}  — specific field overrides
      generic_fields: {field: meta_dict}             — fallbacks by field name only

    Keys in field_metadata:
      "address.type"     → ("address", "type")
      "_generic.name"    → generic fallback for any "name" field
    """
    global _field_library_cache, _generic_fields_cache
    if _field_library_cache is not None and _generic_fields_cache is not None:
        return _field_library_cache, _generic_fields_cache

    field_lib: dict[tuple[str, str], dict] = {}
    generic: dict[str, dict] = {}

    try:
        raw = json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
        metadata = raw.get("field_metadata", {})
        for key, val in metadata.items():
            if key.startswith("_comment") or not isinstance(val, dict):
                continue
            if key.startswith("_generic."):
                field_name = key[len("_generic."):]
                generic[field_name] = val
            elif "." in key:
                obj, field = key.split(".", 1)
                field_lib[(obj, field)] = val
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        logger.warning("field_metadata load error from command-structure.json: %s", exc)

    _field_library_cache = field_lib
    _generic_fields_cache = generic
    return field_lib, generic


def _field_meta(obj: str, field: str) -> dict:
    """Return metadata for *field* of *object* — JSON library → generic → default.

    Loads from settings/command-structure.json field_metadata section.
    """
    field_lib, generic = _get_field_libraries()
    found = field_lib.get((obj, field))
    if found is None:
        found = generic.get(field)
    if found is None:
        found = {"kind": "value", "required": True, "hint": f"Enter {field}"}
    return found


def _resolve_field(obj: str, field: str) -> dict:
    """Build one arg dict for *field* of *object*, from the field library.

    Looks up ``(object, field)`` first, then a generic fallback by field name,
    then a last-resort free value.  This is where a bare CSV field name gains its
    kind / choices / hint without the user having to specify any of it.
    """
    meta = _field_meta(obj, field)
    kind = str(meta.get("kind", "value"))
    hint = str(meta.get("hint") or f"Enter {field}")
    arg: dict = {
        "name": field,
        "kind": kind,
        "required": bool(meta.get("required", True)),
        "hint": hint,
    }
    if kind == "choice":
        arg["choices"] = list(meta.get("choices") or [])
        choice_hints = meta.get("choice_hints") or {}
        if choice_hints:
            arg["choice_hints"] = dict(choice_hints)
    if kind == "keyword":
        arg["value_hint"] = str(meta.get("value_hint") or hint)
    return arg


def _resolve_arg(obj: str, item) -> dict:
    """Resolve one arg item — either a field name string or an inline arg dict."""
    if isinstance(item, str):
        return _resolve_field(obj, item.strip())
    if isinstance(item, dict) and "name" in item:
        return dict(item)
    return {"name": str(item), "kind": "value", "required": True, "hint": f"Enter {item}"}


def _load_json() -> dict[str, dict]:
    """Parse ``settings/command-structure.json`` into command arg specs.

    Supported entry formats:

    Legacy (backward compat) — bare list, treated as override:true:
      ``"address": ["name", "type", ...]``          bare object → prefixed set
      ``"set address-group": ["name", "type", ...]`` full command key

    Current format:
      ``"set address": {"override": true,  "fields": ["name", "type", ...]}``
      ``"set tag":     {"override": false, "args":   [{...}, ...]}``

    ``override: true``  — hand-curated; commandupdate will not overwrite.
    ``override: false`` — auto-generated; commandupdate may refresh.
    Both are stored with the override flag so callers can distinguish tiers.

    Auto-derives ``update <obj>`` and ``delete <obj>`` from override:true
    ``set <obj>`` entries that aren't explicitly listed.
    """
    structure: dict[str, dict] = {}
    raw = json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return {}

    for key, value in raw.items():
        if key.startswith("_"):
            continue

        # Normalise key to full command string
        cmd_key = key if " " in key else f"set {key}"
        obj = cmd_key.split()[-1]

        if isinstance(value, list) and value:
            # Legacy bare list → override:true hand-curated
            structure[cmd_key] = {
                "args": [_resolve_arg(obj, f) for f in value],
                "override": True,
            }
        elif isinstance(value, dict):
            fields = value.get("fields") or value.get("args") or []
            if not fields:
                continue
            override = bool(value.get("override", False))
            structure[cmd_key] = {
                "args": [_resolve_arg(obj, f) for f in fields],
                "override": override,
            }

    # Auto-derive update/delete from override:true set entries only
    set_entries = {k: v for k, v in structure.items()
                   if k.startswith("set ") and v.get("override")}
    for set_key, entry in set_entries.items():
        obj = set_key[4:]
        update_key = f"update {obj}"
        delete_key = f"delete {obj}"
        if update_key not in structure:
            structure[update_key] = {**entry}
        if delete_key not in structure:
            name_only = [a for a in entry["args"] if a["name"] == "name"]
            if name_only:
                structure[delete_key] = {"args": name_only, "override": True}

    return structure


def _generated_entries() -> dict[str, dict]:
    """Arg specs for generated `set` commands, from the spec-derived catalog.

    ``app/settings/field_catalog.py`` is AUTO-GENERATED from the OpenAPI specs
    (``python app/scripts/generate_field_library.py``, run by docsupdate).
    """
    try:
        from app.settings.field_catalog import FIELD_CATALOG
    except Exception:  # noqa: BLE001 — a missing/broken catalog must never break startup
        return {}
    entries: dict[str, dict] = {}
    for key, entry in FIELD_CATALOG.items():
        args = entry.get("args") if isinstance(entry, dict) else None
        if isinstance(args, list) and args:
            entries[key] = {"args": args, "override": False}
    return entries


def load_command_structure() -> dict[str, dict]:
    """Return ``{command_key: entry}`` — single file + field_catalog fallback.

    Priority (highest wins):
      1. ``settings/command-structure.json`` override:true  — hand-curated
      2. ``settings/command-structure.json`` override:false — cli-generated
      3. ``app/settings/field_catalog.py``                  — OpenAPI auto-generated

    Any read/parse failure degrades gracefully to the usage-string fallback.
    """
    global _cache
    if _cache is not None:
        return _cache

    # Layer 3: OpenAPI auto-generated (lowest priority)
    structure: dict[str, dict] = _generated_entries()
    # Layer 1+2: single command-structure.json (override:true beats override:false,
    # but both beat field_catalog since json.update() runs last)
    try:
        if COMMAND_STRUCTURE_JSON.exists():
            structure.update(_load_json())
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        logger.warning("command-structure parse error: %s", exc)

    _cache = structure
    return structure


def _parse_usage_spec(command_key: str, usage: str) -> list[dict] | None:
    """Derive a basic arg spec from a CommandDef ``usage`` string.

    Parses the portion of the usage string *after* the command key tokens and
    produces a list of arg dicts compatible with ``help_options`` / ``_walk``.

    Recognised patterns (PAN-OS-style):
      ``<name>``                  → required value
      ``[keyword <value>]``       → optional keyword
      ``choice1|choice2``         → required choice (no brackets)
      ``[choice1|choice2]``       → optional choice
      ``<range>``  e.g. ``<0-4>`` → required value (with range hint)

    Returns ``None`` when the usage string is absent, trivial, or cannot be
    meaningfully parsed (so the caller falls back to plain inline help).
    """
    import re as _re

    if not usage:
        return None

    # Strip the command key prefix from the usage string.
    suffix = usage
    for tok in command_key.split():
        suffix = suffix.lstrip()
        if suffix.lower().startswith(tok.lower()):
            suffix = suffix[len(tok):]
    suffix = suffix.strip()

    if not suffix:
        return None  # command takes no args — nothing to show

    args: list[dict] = []
    # Tokenise into top-level chunks: bracket groups or bare words.
    # We walk char-by-char to handle nested brackets correctly.
    chunks: list[str] = []
    depth = 0
    current: list[str] = []
    for ch in suffix:
        if ch == "[":
            if depth == 0 and current:
                chunks.append("".join(current).strip())
                current = []
            depth += 1
            current.append(ch)
        elif ch == "]":
            depth -= 1
            current.append(ch)
            if depth == 0:
                chunks.append("".join(current).strip())
                current = []
        elif ch == " " and depth == 0:
            if current:
                chunks.append("".join(current).strip())
                current = []
        else:
            current.append(ch)
    if current:
        chunks.append("".join(current).strip())

    chunks = [c for c in chunks if c]

    for chunk in chunks:
        optional = chunk.startswith("[") and chunk.endswith("]")
        inner = chunk[1:-1].strip() if optional else chunk

        # [keyword <value>] or [keyword value]
        if optional:
            parts = inner.split(None, 1)
            if len(parts) == 2 and not parts[0].startswith("<") and "|" not in parts[0]:
                keyword = parts[0]
                val_hint = parts[1].strip("<>[]")
                args.append({
                    "name": keyword, "kind": "keyword", "required": False,
                    "hint": f"Enter {keyword}", "value_hint": val_hint,
                })
                continue
            # [choice1|choice2]
            if "|" in inner:
                choices = [c.strip("<>") for c in inner.split("|")]
                args.append({
                    "name": choices[0], "kind": "choice", "required": False,
                    "choices": choices, "choice_hints": {},
                    "hint": "Choose one (optional)",
                })
                continue
            # bare optional keyword with no value
            args.append({
                "name": inner.strip("<>"), "kind": "keyword", "required": False,
                "hint": f"Enter {inner.strip('<>')}",
                "value_hint": inner.strip("<>"),
            })
            continue

        # Required choice:  choice1|choice2  or  <choice1|choice2>
        if "|" in inner:
            choices = [c.strip("<>[]") for c in inner.split("|")]
            args.append({
                "name": "type", "kind": "choice", "required": True,
                "choices": choices, "choice_hints": {},
                "hint": "Choose one",
            })
            continue

        # Required value: <name>, <value>, <0-4>, <ip/netmask>, etc.
        if inner.startswith("<") and inner.endswith(">"):
            field_name = inner[1:-1]
            # Range hint like <1-1440>
            hint = f"Enter {field_name}"
            if _re.match(r"^\d+[-–]\d+$", field_name):
                hint = f"Enter a value ({field_name})"
            args.append({
                "name": field_name.split("/")[0].split("-")[0] if "/" in field_name or (
                    field_name[0].isdigit()
                ) else field_name,
                "kind": "value", "required": True, "hint": hint,
            })
            continue

        # Bare word that isn't a choice/variable — a fixed keyword (subcommand token)
        # Skip it: it's already consumed by the command key matching.

    return args if args else None


def arg_spec(command_key: str) -> list[dict] | None:
    """Return the ordered ``args`` list for *command_key*, or ``None`` if absent.

    Priority:
    1. Hand-curated ``settings/command-structure.json`` entry
    2. Auto-generated ``field_catalog.py`` entry
    3. Parsed from the CommandDef ``usage`` string (automatic fallback)

    ``None`` is returned only when all three sources produce nothing, signalling
    the caller to fall back to plain inline help.
    """
    entry = load_command_structure().get(command_key)
    if entry:
        args = entry.get("args")
        if isinstance(args, list) and args:
            return args

    # Automatic fallback: derive basic arg spec from the CommandDef usage string.
    try:
        from app.commands.registry import COMMANDS
        cmd_def = COMMANDS.get(command_key)
        if cmd_def and cmd_def.usage:
            return _parse_usage_spec(command_key, cmd_def.usage)
    except Exception:  # noqa: BLE001
        pass
    return None


def invalidate_cache() -> None:
    """Force a re-read on next access (used by tools/tests that rewrite the file)."""
    global _cache, _field_library_cache, _generic_fields_cache
    _cache = None
    _field_library_cache = None
    _generic_fields_cache = None


# ---------------------------------------------------------------------------
# Structure-aware tokenizing — the application figures out where each field
# ends so the user never has to add quotes around a string field.
#
# A free `value` field is consumed *greedily*:
#   - if a fixed `choice` field comes next, the value absorbs words until a word
#     matches one of the choices (so a multi-word name ends when the type keyword
#     appears: `set address my web host fqdn x` → name = "my web host").
#   - if it is the last positional, it absorbs words until a known trailing
#     keyword (description / tag) appears.
# A trailing `keyword` value likewise absorbs words until the next known keyword.
# Quotes still work as an escape hatch for the rare value that collides with a
# choice/keyword word.
# ---------------------------------------------------------------------------


@dataclass
class _NextState:
    """What the *next* token can be — used to drive Tab completion.

    ``value_slot``    a free value slot to fill (show its "Enter …" hint).
    ``choice_slot``   a fixed-choice slot whose options to offer.
    ``keyword_slots`` trailing keyword fields still available.
    """

    value_slot: dict | None = None
    choice_slot: dict | None = None
    keyword_slots: list = field(default_factory=list)


def _walk(spec: list[dict], tokens: list[str]) -> tuple[dict, list[str], _NextState]:
    """Consume *tokens* against *spec*, returning (assignments, positionals, next).

    *assignments* maps field name → value (joined for greedy fields).
    *positionals* is the ordered list of resolved positional values.
    *next* describes what the following token may be (for completion).
    """
    positional = [a for a in spec if a.get("kind") in ("value", "choice")]
    keyword_defs = {a["name"].lower(): a for a in spec if a.get("kind") == "keyword"}
    keyword_order = [a["name"].lower() for a in spec if a.get("kind") == "keyword"]

    assignments: dict = {}
    positionals: list[str] = []
    i, n = 0, len(tokens)

    p = 0
    while p < len(positional):
        slot = positional[p]
        if slot.get("kind") == "choice":
            if i >= n:
                return assignments, positionals, _NextState(choice_slot=slot)
            assignments[slot["name"]] = tokens[i]
            positionals.append(tokens[i])
            i += 1
            p += 1
            continue

        # Free value slot.
        if i >= n:
            # Nothing typed for it yet → prompt for this value only.
            return assignments, positionals, _NextState(value_slot=slot)

        nxt = positional[p + 1] if p + 1 < len(positional) else None
        collected = [tokens[i]]
        i += 1
        if nxt is not None and nxt.get("kind") == "choice":
            boundary = {c.lower() for c in nxt.get("choices", [])}
            while i < n and tokens[i].lower() not in boundary:
                collected.append(tokens[i])
                i += 1
            assignments[slot["name"]] = " ".join(collected)
            positionals.append(assignments[slot["name"]])
            p += 1
            if i >= n:
                # Value has ≥1 word; the natural next step is the choice.
                return assignments, positionals, _NextState(choice_slot=nxt)
            continue
        if nxt is not None and nxt.get("kind") == "value":
            # Two free values in a row — cannot be greedy; one token each.
            assignments[slot["name"]] = collected[0]
            positionals.append(collected[0])
            p += 1
            continue
        # Last positional → greedy until a trailing keyword.
        while i < n and tokens[i].lower() not in keyword_defs:
            collected.append(tokens[i])
            i += 1
        assignments[slot["name"]] = " ".join(collected)
        positionals.append(assignments[slot["name"]])
        p += 1
        if i >= n:
            return assignments, positionals, _NextState(
                keyword_slots=[keyword_defs[k] for k in keyword_order]
            )

    # Trailing keyword region.
    used: set[str] = set()
    while i < n:
        tok = tokens[i].lower()
        if tok in keyword_defs:
            used.add(tok)
            i += 1
            collected = []
            while i < n and tokens[i].lower() not in keyword_defs:
                collected.append(tokens[i])
                i += 1
            assignments[tok] = " ".join(collected)
            if i >= n and not collected:
                remaining = [keyword_defs[k] for k in keyword_order if k not in used]
                return assignments, positionals, _NextState(
                    value_slot=keyword_defs[tok], keyword_slots=remaining
                )
        else:
            i += 1

    remaining = [keyword_defs[k] for k in keyword_order if k not in used]
    return assignments, positionals, _NextState(keyword_slots=remaining)


def parse(spec: list[dict], remainder: list[str]) -> dict:
    """Parse *remainder* tokens into an args dict using the command structure.

    Handles greedy string fields so the operator never needs quotes.  Returns the
    same shape the registry's positional parser does (``_positional`` + name/id/host
    shortcuts) so existing handlers keep working unchanged.
    """
    assignments, positionals, _state = _walk(spec, remainder)
    result = dict(assignments)
    result["_positional"] = positionals
    if positionals:
        result.setdefault("id", positionals[0])
        result.setdefault("name", positionals[0])
        result.setdefault("host", positionals[0])
    return result


def help_options(spec: list[dict], typed: list[str]) -> list[dict]:
    """Return Cisco-style ``?`` help rows for the next token after *typed*.

    Each row is ``{token, description, variable}``:
      - a fixed choice → ``token`` is the choice, ``variable`` is False.
      - a free value   → ``token`` is ``<field>`` and ``variable`` is True
        (a user-supplied variable, e.g. ``<name>``).
      - a trailing keyword → ``token`` is the keyword name.
    """
    _assign, _pos, state = _walk(spec, typed)
    rows: list[dict] = []

    if state.choice_slot is not None:
        choice = state.choice_slot
        hints = choice.get("choice_hints") or {}
        default = choice.get("hint") or ""
        for token in choice.get("choices", []):
            rows.append({"token": token, "description": hints.get(token, default),
                         "variable": False})

    if state.value_slot is not None:
        slot = state.value_slot
        rows.append({"token": f"<{slot.get('name', 'value')}>",
                     "description": slot.get("hint", ""), "variable": True})

    for keyword in state.keyword_slots:
        rows.append({"token": keyword["name"],
                     "description": keyword.get("hint", ""), "variable": False})

    return rows


def completion_options(spec: list[dict], typed: list[str]) -> list[dict]:
    """Return ``{text, display, meta}`` options for the next token after *typed*.

    A free value slot yields one non-inserting hint whose *display* is the clear
    "Enter …" instruction for that field (e.g. "Enter a description for this
    object"), so Tab on a required string never shows a silent empty result.
    """
    _assign, _pos, state = _walk(spec, typed)
    options: list[dict] = []

    if state.choice_slot is not None:
        choice = state.choice_slot
        hints = choice.get("choice_hints") or {}
        default = choice.get("hint") or "choose one"
        for token in choice.get("choices", []):
            options.append({"text": token, "display": token,
                            "meta": hints.get(token, default)})

    if state.value_slot is not None:
        slot = state.value_slot
        message = slot.get("hint") or f"Enter {slot.get('name', 'value')}"
        options.append({"text": "", "display": message,
                        "meta": "required" if slot.get("required") else "optional"})

    for keyword in state.keyword_slots:
        options.append({"text": keyword["name"], "display": keyword["name"],
                        "meta": "optional" if not keyword.get("required") else "required"})

    return options


