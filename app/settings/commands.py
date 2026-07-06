"""Builtin command visibility — reads settings/builtin_commands.json.

INDEPENDENT of feature flags (settings/features/).
- settings/features/: enables/disables functional command areas
- builtin_commands.json: per-command visibility/execution for builtins

Three states:
  true     — visible in ? and executable (default when absent)
  false    — hidden from ? AND blocked from execution
  "hidden" — works (executable) but NOT shown in ? or tab completion;
             dev mode reveals hidden commands in ? (like "dev" feature flags)

Use cases:
  hidden → backwards-compat aliases (quit vs exit), power-user shortcuts
  false  → deprecated commands you want to fully remove from UX
"""
from __future__ import annotations

import json
from pathlib import Path

from app.paths import SETTINGS_DIR, COMMAND_ALIASES_JSON

COMMANDS_FILE = SETTINGS_DIR / "builtin_commands.json"

# Canonical state strings
STATE_VISIBLE = "visible"
STATE_HIDDEN  = "hidden"
STATE_BLOCKED = "blocked"


def _coerce_visibility(val: object) -> str:
    """Normalise a raw builtin_commands.json value to a state string."""
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
    return STATE_VISIBLE  # unknown → safe default (visible)


def load_command_visibility() -> dict[str, str]:
    """Load builtin command visibility from settings/builtin_commands.json.

    Returns a dict mapping command key → state ("visible" | "hidden" | "blocked").
    Keys starting with "_" are ignored. Missing file → empty dict (all visible).
    """
    if not COMMANDS_FILE.exists():
        return {}
    try:
        data = json.loads(COMMANDS_FILE.read_text(encoding="utf-8"))
        return {
            key: _coerce_visibility(val)
            for key, val in data.items()
            if not key.startswith("_")
        }
    except (json.JSONDecodeError, IOError):
        return {}


def is_command_visible(command_key: str, visibility: dict[str, str],
                       dev_mode: bool = False) -> bool:
    """Return True when *command_key* should appear in ``?`` / tab completion.

    hidden + dev_mode → True   (dev mode reveals hidden commands)
    hidden + normal   → False
    blocked           → False  (never shown)
    visible / absent  → True
    """
    state = visibility.get(command_key, STATE_VISIBLE)
    if state == STATE_VISIBLE:
        return True
    if state == STATE_HIDDEN:
        return dev_mode   # revealed in dev mode, hidden otherwise
    return False          # STATE_BLOCKED


def load_builtin_aliases() -> dict[str, str]:
    """Load system command aliases from settings/command_aliases.json.

    Returns ``{input_line: canonical_line}`` (keys lowercased, stripped).
    Applied in dispatch before prefix expansion — ``conf t`` → ``configure``.
    User-defined aliases live in config/<user>/preferences.json.
    Missing file → empty dict.
    """
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


def is_command_executable(command_key: str, visibility: dict[str, str]) -> bool:
    """Return True when *command_key* is allowed to run.

    hidden → executable (works without appearing in help)
    blocked → not executable
    visible / absent → executable
    """
    state = visibility.get(command_key, STATE_VISIBLE)
    return state != STATE_BLOCKED
