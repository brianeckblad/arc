"""Builtin command visibility, help rows, and alias loader.

Single source of truth: settings/builtin-commands.json.
Operators manage all shell builtins there — no Python code changes needed.

'visible' states:
  true     — shown in ? and executable
  false    — hidden from ? AND blocked
  "hidden" — executable but not shown in ? (dev mode reveals it)

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
    """Normalise a raw visibility value to STATE_VISIBLE/HIDDEN/BLOCKED."""
    if isinstance(val, dict):
        val = val.get("visible", True)
    if val is True:
        return STATE_VISIBLE
    if val is False:
        return STATE_BLOCKED
    token = str(val).strip().lower()
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


def load_shell_help_rows() -> Tuple[ShellBuiltinHelp, ...]:
    """Return ShellBuiltinHelp rows for entries that have a 'help' field.

    Deduplicates rows with the same display name (e.g. exit + quit → one row).
    """
    raw = _load_raw()
    rows: list[ShellBuiltinHelp] = []
    seen_display: set[str] = set()
    for key, val in raw.items():
        if key.startswith("_") or not isinstance(val, dict):
            continue
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
    """Return True when command_key should appear in ? / tab completion."""
    state = visibility.get(command_key, STATE_VISIBLE)
    if state == STATE_VISIBLE:
        return True
    if state == STATE_HIDDEN:
        return dev_mode
    return False


def is_command_executable(command_key: str, visibility: dict[str, str]) -> bool:
    """Return True when command_key is allowed to run."""
    state = visibility.get(command_key, STATE_VISIBLE)
    return state != STATE_BLOCKED


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
