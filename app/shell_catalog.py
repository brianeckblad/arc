"""Shell catalog — loads builtin command metadata from settings/builtin-commands.json.

This file is intentionally thin: all data lives in the settings file.
Add, rename, or update a shell builtin by editing settings/builtin-commands.json.
"""
from __future__ import annotations

from app.settings.commands import (
    ShellBuiltinHelp,
    load_shell_builtins,
    load_shell_help_rows,
)

# Shell built-ins for dispatch and tab completion — loaded from settings.
SHELL_BUILTINS: tuple[str, ...] = load_shell_builtins()

# Help rows for the SHELL section of ? output — loaded from settings.
SHELL_HELP_ROWS: tuple[ShellBuiltinHelp, ...] = load_shell_help_rows()


def shell_help_rows(configure_mode: bool) -> tuple[ShellBuiltinHelp, ...]:
    """Return SHELL help rows visible in the current shell mode."""
    if configure_mode:
        return tuple(row for row in SHELL_HELP_ROWS if row.configure_only)
    return tuple(
        row for row in SHELL_HELP_ROWS
        if not row.configure_only and not row.hide_in_configure
    )


def shell_help_names() -> list[str]:
    """Return all builtin help names in display order (used by smoke tests)."""
    return [row.name for row in SHELL_HELP_ROWS]
