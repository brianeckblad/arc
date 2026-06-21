"""Loader for the per-command argument *order* that drives Tab completion.

The user-facing file is intentionally tiny and curated:
``settings/command-structure.csv`` lists, for selected friendly commands, just
the **fields in the order you type them** — nothing else.  One row per curated
``set <object>`` command::

    # object,field,field,...
    address,name,type,value,description,tag

Reorder a command by moving the field names.  Everything else — which field is a
fixed choice (and what the choices are), which are required, the Tab hints — is
*not* in the CSV.  It comes from the code-side field library below (seeded from
the SCM API schema), keyed by ``(object, field)`` with a generic fallback by
field name.  So a non-programmer only ever touches field order.

The loader compiles each row into the internal shape the completer consumes: an
ordered list of arg dicts with keys ``name``, ``kind`` (``value`` | ``choice`` |
``keyword``), ``required`` (bool), ``choices`` (list), ``choice_hints`` (dict),
``hint`` and optional ``value_hint``.

Generated OpenAPI commands are intentionally **not** all copied into this CSV.
They use each command's ``usage`` string instead (for example generic writes
offer ``json|file <payload-or-path>``).  Add a CSV row only when a command has a
curated, human-friendly parser that is better than the generic generated form.

An advanced ``settings/command-structure.json`` (fully-specified arg dicts) is
still read as a fallback when no CSV exists.  Any missing/malformed file leaves
every command on its usage-string fallback, so the shell always starts cleanly.
"""

from __future__ import annotations

import csv
import json
import logging
from dataclasses import dataclass, field

from app.paths import COMMAND_STRUCTURE_CSV, COMMAND_STRUCTURE_JSON

logger = logging.getLogger(__name__)

# Read once per session (edit the file + restart, or call invalidate_cache()).
_cache: dict[str, dict] | None = None


# ---------------------------------------------------------------------------
# Field library — the API-derived metadata for each field.
#
# The CSV only says *which* fields a command has and in *what order*.  This
# library says what each field *is*: a free value, a fixed choice (with its
# options), or an optional trailing keyword — plus the human hint shown on Tab.
#
# Seeded by hand from the SCM schema today (the address `oneOf` → ip-netmask /
# ip-range / ip-wildcard / fqdn).  It can later be generated from the specs the
# same way `app/commands/resource_catalog.py` is.
# ---------------------------------------------------------------------------

# Per-(object, field) definitions.  Keys are the object name (CSV column 1) and
# the field name (the remaining CSV columns).
_FIELD_LIBRARY: dict[tuple[str, str], dict] = {
    ("address", "name"): {
        "kind": "value", "required": True,
        "hint": "Enter a unique name for the address object",
    },
    ("address", "type"): {
        "kind": "choice", "required": True,
        "choices": ["ip-netmask", "ip-range", "ip-wildcard", "fqdn"],
        "choice_hints": {
            "ip-netmask":  "Single IP or CIDR (10.1.2.3/32)",
            "ip-range":    "Inclusive range (10.0.0.1-10.0.0.9)",
            "ip-wildcard": "Wildcard mask (10.0.0.0/0.0.0.255)",
            "fqdn":        "Domain name (api.example.com)",
        },
        "hint": "Choose the address type",
    },
    ("address", "value"): {
        "kind": "value", "required": True,
        "hint": "Enter the value for the chosen type (e.g. 10.1.2.3/32)",
    },
}

# Generic fallbacks by field name — apply to any object that has these fields.
_GENERIC_FIELDS: dict[str, dict] = {
    "name": {
        "kind": "value", "required": True,
        "hint": "Enter a unique name",
    },
    "description": {
        "kind": "keyword", "required": False,
        "hint": "Enter a description for this object",
    },
    "tag": {
        "kind": "keyword", "required": False,
        "hint": "Enter a tag name (the tag must already exist in this folder)",
    },
}


def _field_meta(obj: str, field: str) -> dict:
    """Return the raw metadata dict for *field* of *object* (library → generic → default)."""
    found = _FIELD_LIBRARY.get((obj, field))
    if found is None:
        found = _GENERIC_FIELDS.get(field)
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


def _load_csv() -> dict[str, dict]:
    """Parse the simple CSV (``object,field,field,...``) into command arg specs.

    Each non-comment row becomes one ``set <object>`` command whose ordered
    arguments are resolved through the field library.
    """
    structure: dict[str, dict] = {}
    with COMMAND_STRUCTURE_CSV.open(encoding="utf-8", newline="") as handle:
        for cells in csv.reader(handle):
            if not cells:
                continue
            obj = cells[0].strip()
            if not obj or obj.startswith("#"):
                continue
            fields = [c.strip() for c in cells[1:] if c.strip()]
            if not fields:
                continue
            structure[f"set {obj}"] = {"args": [_resolve_field(obj, f) for f in fields]}
    return structure


def _load_json() -> dict[str, dict]:
    """Parse the JSON structure file into ``{command: entry}``."""
    raw = json.loads(COMMAND_STRUCTURE_JSON.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return {}
    return {
        key: value
        for key, value in raw.items()
        if not key.startswith("_") and isinstance(value, dict)
    }


def load_command_structure() -> dict[str, dict]:
    """Return ``{command_key: entry}`` from the structure file (cached).

    CSV is used when present; otherwise JSON.  Any read/parse failure returns
    ``{}`` so completion falls back to usage strings gracefully.
    """
    global _cache
    if _cache is not None:
        return _cache

    structure: dict[str, dict] = {}
    try:
        if COMMAND_STRUCTURE_CSV.exists():
            structure = _load_csv()
        elif COMMAND_STRUCTURE_JSON.exists():
            structure = _load_json()
    except (OSError, csv.Error, json.JSONDecodeError, ValueError) as exc:
        logger.warning("command-structure parse error: %s", exc)
        structure = {}

    _cache = structure
    return structure


def arg_spec(command_key: str) -> list[dict] | None:
    """Return the ordered ``args`` list for *command_key*, or ``None`` if absent.

    ``None`` signals the caller to fall back to usage-string parsing.
    """
    entry = load_command_structure().get(command_key)
    if not entry:
        return None
    args = entry.get("args")
    if isinstance(args, list) and args:
        return args
    return None


def invalidate_cache() -> None:
    """Force a re-read on next access (used by tools/tests that rewrite the file)."""
    global _cache
    _cache = None


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


