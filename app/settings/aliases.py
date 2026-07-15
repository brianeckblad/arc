"""Shared command-alias helpers — used by the CLI, the GUI, and manual edits.

Two kinds of aliases:

* **System aliases** — ``settings/command-aliases.json``: ship with ARC, shared
  by all users (e.g. ``sh`` -> ``show``).  Read via
  ``app.settings.commands.load_builtin_aliases``; written here so the GUI and a
  hand-edit produce the same file.
* **Personal aliases** — ``config/<user>/preferences.json``: per-user, managed by
  the ``alias`` builtin (and the GUI, via ``shell._prefs``).  Not handled here —
  the shell owns the prefs object.

Both surfaces validate names the same way (``alias_conflict``): an alias must
never shadow a shell builtin or a registered command's first word.
"""

from __future__ import annotations

import json
import logging

from app.paths import COMMAND_ALIASES_JSON

logger = logging.getLogger(__name__)


def load_system_aliases() -> dict[str, str]:
    """Return {alias -> expansion} from settings/command-aliases.json (no comments)."""
    from app.settings.commands import load_builtin_aliases
    return load_builtin_aliases()


def _raw_system_file() -> dict:
    try:
        raw = json.loads(COMMAND_ALIASES_JSON.read_text(encoding="utf-8")) \
            if COMMAND_ALIASES_JSON.exists() else {}
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Could not read {COMMAND_ALIASES_JSON.name}: {exc}") from exc
    if not isinstance(raw, dict):
        raise RuntimeError(f"{COMMAND_ALIASES_JSON.name} must contain a JSON object")
    return raw


def set_system_alias(name: str, expansion: str | None) -> None:
    """Create/update (expansion given) or delete (None) a system alias.

    Preserves the file's comment keys (``_README`` etc.) and ordering of other
    entries.  Raises ``RuntimeError`` on I/O trouble.
    """
    key = name.strip().lower()
    if not key:
        raise ValueError("alias name is required")
    raw = _raw_system_file()

    if expansion is None:
        # Delete: remove the exact key if present (case-insensitive match).
        for existing in [k for k in raw if not k.startswith("_") and k.lower() == key]:
            raw.pop(existing)
    else:
        exp = expansion.strip()
        if not exp:
            raise ValueError("alias expansion is required")
        # Replace any existing case-variant, then set canonical lower-case key.
        for existing in [k for k in raw if not k.startswith("_") and k.lower() == key]:
            if existing != key:
                raw.pop(existing)
        raw[key] = exp

    try:
        COMMAND_ALIASES_JSON.write_text(
            json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"Could not write {COMMAND_ALIASES_JSON.name}: {exc}") from exc


def alias_conflict(name: str, *, builtins: set[str] | None = None) -> str | None:
    """Return a human reason if *name* may not be used as an alias, else None.

    An alias must not shadow a shell builtin or the first word of any registered
    command (``show``, ``set``, ``delete`` …) — otherwise it would hijack real
    syntax.  ``builtins`` lets the caller pass the shell's builtin set; when
    omitted only command-word conflicts are checked.
    """
    key = name.strip().lower()
    if not key:
        return "alias name is required"
    if " " in key:
        # Multi-word alias keys are allowed for system aliases (e.g. "conf t"),
        # so only flag a leading reserved word for single-token names.
        first = key.split()[0]
    else:
        first = key
    from app.commands.registry import COMMANDS
    command_words = {k.split()[0].lower() for k in COMMANDS}
    if builtins and first in {b.lower() for b in builtins}:
        return f"'{first}' is a shell builtin"
    if " " not in key and key in command_words:
        return f"'{key}' is a command word"
    return None
