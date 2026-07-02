"""Small shell catalog for built-in command metadata.

This is intentionally tiny and boring: agents should edit this file before
reading `app/shell.py` when they need to add, remove, or rename a shell builtin.

String-theory model:
- `app/shell.py` is the shell spine (prompt loop, dispatch, execution).
- This file is one small attached string: builtin names + inline-help labels.
- Future strings can follow this pattern (`shell_help.py`, `shell_nav.py`, ...)
  when a section grows large enough to extract safely.
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class ShellBuiltinHelp:
    """One row in the SHELL section of `?` output."""

    name: str
    description: str
    configure_only: bool = False
    hide_in_configure: bool = False


# Shell built-ins accepted by the dispatcher/completer.
# Add the runtime behavior in `ArcShell._dispatch()` and `_cmd_*` methods.
SHELL_BUILTINS: tuple[str, ...] = (
    "cd", "remote", "connect", "docs",
    "pwd",
    "folder", "tsg", "account",
    "configure", "cli",
    "feature",
    "setup",
    "set",
    "update",
    "delete",
    "abandon",
    "clear", "exit", "quit",
    "help", "?",
)


# Rows shown in the SHELL section of quick inline help.
# `configure_only=True` means visible only while in configure mode.
# `hide_in_configure=True` means visible only outside configure mode.
SHELL_HELP_ROWS: tuple[ShellBuiltinHelp, ...] = (
    ShellBuiltinHelp("cd <device|folder>",   "Navigate context  (cd device <name> | cd folder <name> | cd ..)"),
    ShellBuiltinHelp("connect <device>",     "SSH to device — interactive session  (returns to ARC on exit)"),
    ShellBuiltinHelp("remote <device>",      "SSH to named device — interactive session  (keyboard-interactive + 2FA)"),
    ShellBuiltinHelp("folder <name>",        "Set SCM Folder scope  (Tab -> folder list | folder .. -> Shared)"),
    ShellBuiltinHelp("tsg <id>",             "Set active TSG  (Tab -> configured TSG)"),
    ShellBuiltinHelp("account <name>",       "List or switch credential profiles  (Tab -> profile names)"),
    ShellBuiltinHelp("configure",            "Enter configure mode  (arc:global #)", hide_in_configure=True),
    ShellBuiltinHelp("set <type> <name>",    "Create configuration  (configure mode)  — set ? for sub-commands", configure_only=True),
    ShellBuiltinHelp("update <type> <name>", "Modify existing object  (configure mode)  — update ? for types", configure_only=True),
    ShellBuiltinHelp("delete <type> <name>", "Delete configuration object  (configure mode)  — delete ? for types", configure_only=True),
    ShellBuiltinHelp("show config",          "List staged changes pending commit  (local — not yet in SCM)", configure_only=True),
    ShellBuiltinHelp("commit",               "Apply staged changes + push to devices  (commit watch → follow the job)", configure_only=True),
    ShellBuiltinHelp("abandon",              "Discard staged changes  (local only — SCM is never touched)", configure_only=True),
    ShellBuiltinHelp("cli <subcommand>",     "CLI theme operations  (show | color | reset)", configure_only=True),
    ShellBuiltinHelp("feature <subcommand>", "Feature flags  (show | enable <flag> | disable <flag>)"),
    ShellBuiltinHelp("setup",                "Guided credential setup wizard  (auto-detects OS, two questions)"),
    ShellBuiltinHelp("pwd",                  "Show device, folder, TSG, and active account"),
    ShellBuiltinHelp("docs",                 "Open docs in browser"),
    ShellBuiltinHelp("clear",                "Clear the terminal screen"),
    ShellBuiltinHelp("exit / quit",          "Exit ARC (or leave configure mode)", configure_only=True),
)


def shell_help_rows(configure_mode: bool) -> tuple[ShellBuiltinHelp, ...]:
    """Return SHELL help rows visible in the current shell mode."""
    if configure_mode:
        return tuple(row for row in SHELL_HELP_ROWS if row.configure_only)
    return tuple(row for row in SHELL_HELP_ROWS if not row.configure_only and not row.hide_in_configure)


def shell_help_names() -> list[str]:
    """Return all builtin help names in display order for smoke tests."""
    return [row.name for row in SHELL_HELP_ROWS]

