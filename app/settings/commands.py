"""Builtin command visibility, help rows, and alias loader.

Single source of truth: settings/builtin-commands.json.
Operators manage all shell builtins there — no Python code changes needed.

'visible' states:
  true     — shown in ? and executable (normal users)
  "dev"    — only visible and executable in dev mode (work-in-progress builtins)
  "hidden" — executable by everyone but not shown in ? (dev mode reveals it in ?)
  false    — hidden from ? AND blocked for everyone (including dev mode)

Entry format (rich):
  "cd": {"visible": true, "display": "cd <device|folder>", "help": "...", "configure_only": false}
Entry format (simple, visibility only):
  "cd": true
"""
from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from typing import Tuple

from app.paths import SETTINGS_DIR, COMMAND_ALIASES_JSON

COMMANDS_FILE = SETTINGS_DIR / "builtin-commands.json"

logger = logging.getLogger(__name__)

STATE_VISIBLE = "visible"
STATE_DEV     = "dev"
STATE_HIDDEN  = "hidden"
STATE_BLOCKED = "blocked"


@dataclass(frozen=True)
class ShellBuiltinHelp:
    """One row in the SHELL section of ``?`` output."""
    name: str
    description: str
    configure_only: bool = False
    hide_in_configure: bool = False


def _load_raw() -> dict:
    """Read and parse builtin-commands.json."""
    if not COMMANDS_FILE.exists():
        return {}
    try:
        return json.loads(COMMANDS_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        logger.warning("builtin-commands.json parse error: %s", exc)
        return {}


def _coerce_visibility(val: object) -> str:
    """Normalise a raw visibility value to STATE_VISIBLE/DEV/HIDDEN/BLOCKED."""
    if isinstance(val, dict):
        val = val.get("visible", True)
    if val is True:
        return STATE_VISIBLE
    if val is False:
        return STATE_BLOCKED
    token = str(val).strip().lower()
    if token in ("dev", "development", "wip"):
        return STATE_DEV
    if token == "hidden":
        return STATE_HIDDEN
    if token in ("true", "on", "visible", "1"):
        return STATE_VISIBLE
    if token in ("false", "off", "blocked", "0"):
        return STATE_BLOCKED
    return STATE_VISIBLE


def load_command_visibility() -> dict[str, str]:
    """Return {key: state} for all builtin commands."""
    raw = _load_raw()
    return {
        key: _coerce_visibility(val)
        for key, val in raw.items()
        if not key.startswith("_")
    }


def load_shell_builtins() -> Tuple[str, ...]:
    """Return all builtin command keys (for dispatch + completion)."""
    raw = _load_raw()
    return tuple(key for key in raw if not key.startswith("_"))


def load_builtin_docs() -> dict:
    """Return ``{name: {"display": str, "help": str}}`` for every shell builtin.

    Excludes the ``_``-prefixed meta entries.  Used to synthesize documentation
    pages for builtins (the docs-update pipeline + in-shell ``help <builtin>``)
    so every shell command is documented, mirroring the registry-synthesized
    pages generated commands get.
    """
    raw = _load_raw()
    return {
        key: {"display": entry.get("display") or key, "help": entry.get("help") or ""}
        for key, entry in raw.items()
        if not key.startswith("_")
    }


# Fields the GUI/CLI may edit on a builtin entry (others are preserved on write).
_BUILTIN_EDITABLE = {
    "visible": "state",   # true | "dev" | "hidden" | false
    "display": "text",
    "help": "text",
    "configure_only": "bool",
    "hide_in_configure": "bool",
    "onlogin": "bool",
    "startup_hint": "text",
}
_VISIBLE_TOKENS = {
    "true": True, "on": True, "visible": True, "1": True,
    "false": False, "off": False, "blocked": False, "0": False,
    "dev": "dev", "development": "dev", "wip": "dev",
    "hidden": "hidden", "stealth": "hidden",
}


def set_builtin_field(name: str, field: str, value: object) -> "Path":
    """Set one field on a builtin entry in settings/builtin-commands.json.

    Preserves comment keys and every other field on the entry.  ``visible`` is
    normalized to one of ``true`` / ``"dev"`` / ``"hidden"`` / ``false``; the
    boolean toggles coerce truthy/falsey; text fields store the string as-is.

    Raises ``ValueError`` for an unknown builtin/field or a bad ``visible``
    value; ``RuntimeError`` on I/O trouble.  Returns the file path.
    """
    from pathlib import Path

    key = (name or "").strip()
    if field not in _BUILTIN_EDITABLE:
        raise ValueError(f"field not editable: {field!r}")

    try:
        raw = json.loads(COMMANDS_FILE.read_text(encoding="utf-8")) if COMMANDS_FILE.exists() else {}
    except (json.JSONDecodeError, OSError) as exc:
        raise RuntimeError(f"Could not read {COMMANDS_FILE.name}: {exc}") from exc
    if not isinstance(raw, dict) or key not in raw or key.startswith("_"):
        raise ValueError(f"unknown builtin: {name!r}")

    entry = raw[key]
    if not isinstance(entry, dict):
        # Promote a simple bool entry to the rich form before editing.
        entry = {"visible": bool(entry)}
        raw[key] = entry

    kind = _BUILTIN_EDITABLE[field]
    if kind == "state":
        token = str(value).strip().lower()
        if token not in _VISIBLE_TOKENS:
            raise ValueError(f"invalid visible value: {value!r}")
        entry["visible"] = _VISIBLE_TOKENS[token]
    elif kind == "bool":
        entry[field] = bool(value)
    else:
        entry[field] = str(value)

    try:
        COMMANDS_FILE.write_text(json.dumps(raw, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    except OSError as exc:
        raise RuntimeError(f"Could not write {COMMANDS_FILE.name}: {exc}") from exc
    return Path(COMMANDS_FILE)


def load_builtins_full() -> dict[str, dict]:
    """Return {name: {visible,display,help,configure_only,...}} for the editor."""
    raw = _load_raw()
    out: dict[str, dict] = {}
    for key, val in raw.items():
        if key.startswith("_"):
            continue
        if isinstance(val, dict):
            out[key] = {
                "visible": _coerce_visibility(val),
                "display": val.get("display", key),
                "help": val.get("help", ""),
                "configure_only": bool(val.get("configure_only", False)),
                "hide_in_configure": bool(val.get("hide_in_configure", False)),
                "onlogin": bool(val.get("onlogin", False)),
                "startup_hint": val.get("startup_hint", ""),
            }
        else:
            out[key] = {"visible": _coerce_visibility(val), "display": key, "help": "",
                        "configure_only": False, "hide_in_configure": False,
                        "onlogin": False, "startup_hint": ""}
    return out


def load_shell_help_rows(dev_mode: bool = False) -> Tuple[ShellBuiltinHelp, ...]:
    """Return ShellBuiltinHelp rows for entries that have a 'help' field.

    In dev mode every state is included so developers see all builtins.
    Normal mode: blocked, dev, and hidden entries are omitted.
    Deduplicates rows with the same display name (e.g. exit + quit → one row).
    """
    raw = _load_raw()
    rows: list[ShellBuiltinHelp] = []
    seen_display: set[str] = set()
    for key, val in raw.items():
        if key.startswith("_") or not isinstance(val, dict):
            continue
        if not dev_mode:
            state = _coerce_visibility(val)
            if state in (STATE_BLOCKED, STATE_DEV, STATE_HIDDEN):
                continue
        else:
            state = _coerce_visibility(val)
            if state == STATE_BLOCKED:
                continue  # false is never shown, even in dev mode
        help_text = val.get("help")
        if not help_text:
            continue
        display = str(val.get("display") or key)
        if display in seen_display:
            continue
        seen_display.add(display)
        rows.append(ShellBuiltinHelp(
            name=display,
            description=str(help_text),
            configure_only=bool(val.get("configure_only", False)),
            hide_in_configure=bool(val.get("hide_in_configure", False)),
        ))
    return tuple(rows)


def is_command_visible(command_key: str, visibility: dict[str, str],
                       dev_mode: bool = False) -> bool:
    """Return True when command_key should appear in ? / tab completion.

    Dev mode reveals hidden and dev-state commands, but never blocked (false) ones.
    """
    state = visibility.get(command_key, STATE_VISIBLE)
    if state == STATE_BLOCKED:
        return False
    if state == STATE_VISIBLE:
        return True
    # STATE_DEV and STATE_HIDDEN — visible only in dev mode
    return dev_mode


def is_command_executable(command_key: str, visibility: dict[str, str],
                          dev_mode: bool = False) -> bool:
    """Return True when command_key is allowed to run.

    * visible  — always executable
    * hidden   — always executable (just not advertised in ?)
    * dev      — executable only in dev mode
    * blocked  — never executable
    """
    state = visibility.get(command_key, STATE_VISIBLE)
    if state == STATE_BLOCKED:
        return False
    if state == STATE_DEV:
        return dev_mode
    return True


def load_builtin_aliases() -> dict[str, str]:
    """Load system aliases from settings/command-aliases.json."""
    if not COMMAND_ALIASES_JSON.exists():
        return {}
    try:
        data = json.loads(COMMAND_ALIASES_JSON.read_text(encoding="utf-8"))
        return {
            str(k).strip().lower(): str(v).strip()
            for k, v in data.items()
            if not k.startswith("_") and isinstance(v, str)
        }
    except (json.JSONDecodeError, IOError):
        return {}


def shell_help_rows(configure_mode: bool, dev_mode: bool = False) -> tuple[ShellBuiltinHelp, ...]:
    """Return SHELL help rows visible in the current shell mode.

    Dev mode shows all rows regardless of configure context so developers
    have full visibility of every builtin command.
    """
    rows = load_shell_help_rows(dev_mode=dev_mode)
    if dev_mode:
        # Dev mode: show everything (no configure_mode filtering)
        return rows
    if configure_mode:
        return tuple(row for row in rows if row.configure_only)
    # Normal mode: show non-configure-only commands.
    # hide_in_configure only applies when *inside* configure mode — ignore it here.
    return tuple(row for row in rows if not row.configure_only)


def shell_help_names() -> list[str]:
    """Return all builtin help display names in order (used by smoke tests)."""
    return [row.name for row in load_shell_help_rows()]


def load_startup_hints() -> list[tuple[str, str]]:
    """Return ``[(display, hint), …]`` for entries with ``onlogin: true``.

    Order reflects the order in settings/builtin-commands.json.
    ``display`` is the ``display`` field (or key); ``hint`` is ``startup_hint``.
    Only entries where ``onlogin`` is True and ``startup_hint`` is non-empty
    are returned. Disabling a startup hint: set ``"onlogin": false`` in the file.
    """
    raw = _load_raw()
    hints: list[tuple[str, str]] = []
    for key, val in raw.items():
        if key.startswith("_") or not isinstance(val, dict):
            continue
        if val.get("onlogin") and val.get("startup_hint"):
            display = str(val.get("display") or key)
            hints.append((display, str(val["startup_hint"])))
    return hints
