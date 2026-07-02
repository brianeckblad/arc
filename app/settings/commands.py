"""Command visibility loader — reads settings/commands.json for per-command enable/disable.

This is INDEPENDENT of feature flags (settings/features/).
- settings/features/: enables/disables entire functional areas (e.g. "nat_rules")
- commands.json: hides/shows specific individual commands regardless of features

Use case: Deprecate a command without removing code, or hide experimental commands.
"""
from __future__ import annotations

import json
from pathlib import Path

from app.paths import SETTINGS_DIR

COMMANDS_FILE = SETTINGS_DIR / "commands.json"


def load_command_visibility() -> dict[str, bool]:
    """Load command visibility settings from settings/commands.json.
    
    Returns:
        Dict mapping command keys to visibility (True = visible, False = hidden).
        Keys starting with "_" are ignored (comments/metadata).
    
    If the file doesn't exist or is invalid JSON, returns an empty dict
    (all commands visible by default).
    """
    if not COMMANDS_FILE.exists():
        return {}
    
    try:
        data = json.loads(COMMANDS_FILE.read_text(encoding="utf-8"))
        # Filter out comment/metadata keys
        return {
            key: val
            for key, val in data.items()
            if not key.startswith("_") and isinstance(val, bool)
        }
    except (json.JSONDecodeError, IOError):
        return {}


def is_command_visible(command_key: str, visibility: dict[str, bool]) -> bool:
    """Check if a command is visible according to settings/commands.json.
    
    Args:
        command_key: Command string (e.g. "show devices")
        visibility: Dict from load_command_visibility()
    
    Returns:
        True if visible (or not in the dict), False if explicitly hidden.
    """
    return visibility.get(command_key, True)  # Default: visible
