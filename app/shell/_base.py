"""Interactive REPL shell for ARC — Assisted Remote Console.

# ============================================================================
th# SHELL.PY — the shell spine (prompt loop, dispatch, execution, rendering)
# ============================================================================
#
# AGENT READ STRATEGY — do NOT read this whole file.
#   `app/scripts/CODE_MAP.md` has the exact, always-current line range of every method
#   here. Read that map, then read_file(offset=START, limit=END-START+1) for the
#   one method you need. Regenerate the map with: python app/scripts/generate_code_map.py
#   (smoke_test.py section 10 fails if the map is stale.)
#
# SMALL "STRINGS" attached to this spine (edit these first when relevant):
#   settings/builtin-commands.json  — builtin command names, display, help rows (no code change needed)
#   app/settings/features.py   — feature flags that gate commands
#   app/settings/theme.py      — colour roles for `?` help and prompt
#   app/commands/*.py          — registered command handlers + CommandDefs
#
# FEATURE FLAGS:
#   CommandDef.feature_flag = 'flag_name' gates a command behind app/settings/features.py.
#   _is_command_available() enforces flags in `?` help; _execute_api() at runtime.
# ============================================================================
"""

from __future__ import annotations

import os
import re
import random
import select
import shlex
import shutil
import signal
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

import httpx

# termios / tty are Unix-only.  On Windows the interactive PTY session will
# fall back to a friendlier error rather than crashing at import time.
try:
    import termios
    import tty
    _TTY_AVAILABLE = True
except ImportError:
    _TTY_AVAILABLE = False

from prompt_toolkit import PromptSession
from prompt_toolkit.application import run_in_terminal
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
from prompt_toolkit.completion import Completer, Completion
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.history import FileHistory
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.styles import Style
from rich.console import Console
from rich.panel import Panel
import platformdirs
from app.api.client import SCMClient
from app import __version__
from app.paths import BANNER_FILE as _BANNER_FILE, GOODBYE_FILE as _GOODBYE_FILE
from app.commands.registry import (
    COMMANDS,
    CATEGORIES,
    CommandDef,
    ExecutionContext,
    match_command,
)
from app.config import ArcConfig, list_profiles, load_config, set_active_profile
from app.settings.cli_structure import (
    cd_hint as _cd_hint,
    configure_banner as _configure_banner,
    help_footer as _help_footer,
    section_label as _section_label,
    verb_description as _verb_description,
    verb_visible as _verb_visible,
)
from app.docs import (
    available_help_topics,
    cisco_pager,
    open_docs_in_browser,
    page_length,
    paging_stdout,
    _PAGING_EXEMPT,
    render_help_topic,
    set_page_length,
)
from app.settings.user_prefs import UserPrefs, load_prefs, save_prefs
from app.settings.features import dev_mode_from_env, effective_scope, feature_state, is_area_enabled, is_enabled, is_feature_visible, load_disabled_areas, load_features, load_scope_overrides
from app.settings.commands import load_command_visibility, is_command_visible, is_command_executable, load_builtin_aliases
from app.settings.commands import (
    load_shell_builtins as _load_shell_builtins,
    shell_help_rows,
)

# All shell builtin metadata comes from settings/builtin-commands.json.
# No code change needed to add/rename/reorder builtins — edit that file.
SHELL_BUILTINS: tuple[str, ...] = _load_shell_builtins()
from app.ssh.manager import SSHManager
from app.settings.theme import ArcTheme, THEME_KEYS, load_theme, reset_theme, save_theme
from app.utils import formatter as fmt

console = Console()


HISTORY_FILE = os.path.join(platformdirs.user_data_dir("arc"), "history")
GOODBYE_FILE = _GOODBYE_FILE  # settings/goodbye.txt (imported below)

# Width of the command column in all inline help output.
# All sections (GLOBAL / FOLDER / DEVICE / SHELL) use the same value so
# descriptions land on the same visual column regardless of indent level.
# 4-space-indented tiers: 4 + _HELP_CMD_WIDTH = visual col 48
# 2-space-indented (scoped / full ref): uses +2 → also visual col 48
_HELP_CMD_WIDTH = 44

# Shell built-ins accepted by the dispatcher/completer.
# Shell built-in names for dispatch and completion — loaded from settings.
_SHELL_BUILTINS: tuple[str, ...] = SHELL_BUILTINS


def device_display_name(device: Optional[dict], fallback: str = "device") -> str:
    """Best human-readable name for a device inventory entry.

    SCM device records vary by source: SSH-era entries carry ``hostname``,
    folder inventory carries ``display_name`` / ``name``. Every mixin must
    render the same name for the same device, so this is the one place that
    ordering lives.
    """
    if not device:
        return fallback
    return (
        device.get("hostname")
        or device.get("display_name")
        or device.get("name")
        or fallback
    )


def device_ssh_host(device: Optional[dict]) -> str:
    """Address ARC should SSH to for a device entry (IP wins over hostname)."""
    if not device:
        return ""
    return str(device.get("ip_address") or device.get("hostname") or "")


def tsg_display(entry: dict) -> tuple[str, str]:
    """Return ``(tsg_id, display_name)`` for a tenant-service-group entry."""
    tsg_id = str(entry.get("id") or entry.get("tsg_id") or "")
    name = str(entry.get("display_name") or entry.get("name") or "")
    return tsg_id, name


def active_tsg_label(state: "ShellState", config: ArcConfig) -> str:
    """The TSG identifier to show in user-facing messages."""
    return state.tsg_id or config.scm.tsg_id or "current TSG"


def _expand_unambiguous_prefix(tokens: list[str], phrases: list[list[str]]) -> list[str]:
    """Expand command-token prefixes when they resolve to exactly one phrase.

    Example:
        ["e"]            -> ["exit"]
        ["sh", "sec", "pol"] -> ["show", "security", "policy"]

    Rules:
      - Match is token-wise prefix.
      - Longest consumed-prefix length wins.
      - Expansion occurs only when exactly one phrase matches.
      - Ambiguous prefixes are left unchanged.
    """
    if not tokens:
        return tokens

    lowered = [t.lower() for t in tokens]
    max_consumed = min(len(tokens), max((len(p) for p in phrases), default=0))

    for consumed in range(max_consumed, 0, -1):
        prefix = lowered[:consumed]
        matches: list[list[str]] = []
        for phrase in phrases:
            if len(phrase) < consumed:
                continue
            if all(phrase[i].startswith(prefix[i]) for i in range(consumed)):
                matches.append(phrase)

        if len(matches) == 1:
            expanded = matches[0] + tokens[consumed:]
            return expanded

    return tokens


PROMPT_STYLE = Style.from_dict({
    "arc":     "bold ansicyan",
    "device":  "bold ansiyellow",
    "folder":  "bold ansigreen",
    "ctx":     "ansicyan dim",        # context-tier label (:global, :device)
    "sep":     "ansicyan",
    "arrow":   "bold ansicyan",
    "dev":     "bold ansimagenta",    # development-mode marker in the prompt
    "confirm": "bold ansired",        # commit confirmed countdown
    "noscm":   "ansired dim",         # degraded mode: no SCM connection
})


def tokenize(line: str) -> list[str]:
    """Split a command line into tokens, honouring single/double quotes.

    A value that contains spaces must be quoted (vendor-CLI / shell convention),
    e.g. ``set address "My Host" fqdn x description "DMZ host"`` → the quoted
    parts stay single tokens.  Unbalanced quotes fall back to a plain split so a
    half-typed line never raises.
    """
    try:
        return shlex.split(line, posix=True)
    except ValueError:
        return line.split()


def _make_key_bindings(shell=None) -> KeyBindings:
    """Return key bindings for the ARC shell.

    '?' is bound to show inline context-sensitive help WITHOUT submitting the
    line.  After help is printed the prefix is restored to the buffer so the
    user can keep typing — exactly the Cisco / PAN-OS UX convention.

    Pressing '?' a second time on the same unchanged prefix escalates to full
    help (the typed-`??` gesture, which an instant-submit '?' cannot enter
    literally).
    """
    kb = KeyBindings()

    @kb.add("?")
    def _handle_question(event) -> None:
        buf = event.current_buffer
        prefix = buf.text.rstrip()
        query = (prefix + " ?") if prefix else "?"

        # Print help inline via run_in_terminal so prompt_toolkit temporarily
        # hides the prompt, lets the help output print cleanly, then redraws
        # the prompt with the original prefix restored — Cisco/PAN-OS style.
        if shell is not None:
            def _show() -> None:
                shell._dispatch(query)
            run_in_terminal(_show)

        # Restore prefix + trailing space so the user can continue typing
        # without having to retype the command they already had.
        new_text = (prefix + " ") if prefix else ""
        buf.text = new_text
        buf.cursor_position = len(new_text)

    @kb.add("tab")
    def _handle_tab(event) -> None:
        buf = event.current_buffer
        if buf.complete_state:
            buf.complete_next()
            return

        # Peek at available completions: auto-fill if exactly one match,
        # otherwise show the dropdown menu.
        session = getattr(shell, "_session", None) if shell is not None else None
        completer = getattr(session, "completer", None) if session is not None else None
        if completer is not None:
            from prompt_toolkit.completion import CompleteEvent
            completions = list(completer.get_completions(
                buf.document, CompleteEvent(completion_requested=True)
            ))
            if len(completions) == 1:
                buf.apply_completion(completions[0])
                return

        buf.start_completion(select_first=False)

    @kb.add("s-tab")
    def _handle_back_tab(event) -> None:
        buf = event.current_buffer
        if buf.complete_state:
            buf.complete_previous()
        else:
            buf.start_completion(select_last=True)

    return kb


@dataclass
class ShellState:
    device: Optional[dict] = None
    folder: str = "Shared"
    configure_mode: bool = False
    # Configure-mode writes staged LOCALLY — nothing is sent to SCM until
    # `commit` replays these operations. Each entry:
    #   {"command": key, "detail": name-ish, "folder": str,
    #    "ops": [{"method", "base_url", "path", "params", "json"}]}
    # `abandon` (or exit → abandon) just clears this list; SCM is untouched.
    staged_ops: list[dict] = field(default_factory=list)
    # Active TSG ID — overrides the value from ArcConfig when set.
    # Useful when a bearer token was issued at the root and the user needs
    # to work within a specific child TSG without re-authenticating.
    tsg_id: str = ""
    devices_cache: list[dict] = field(default_factory=list)
    # SCM folder names cached at startup for tab completion
    folders_cache: list[str] = field(default_factory=lambda: ["Shared", "Global"])
    # monotonic timestamps of the last cache refresh — a cd/folder miss on a
    # stale cache triggers one silent re-fetch before hard-erroring, so a
    # device onboarded an hour into the session is still found.
    devices_loaded_at: float = 0.0
    folders_loaded_at: float = 0.0
    # TSG entries fetched from /iam/v1/tenants — each dict has 'id' and 'display_name'
    tsgs_cache: list[dict] = field(default_factory=list)
    # Dev shell mode — entered via `dev` command, exited with `exit`.
    # While active: dev-flagged commands visible, dev sub-commands available.
    dev_shell: bool = False


# Explicit re-export list for `from app.shell._base import *`.
# Mixins depend on every symbol listed here — add here when adding a new
# module-level export to this file (functions, constants, imported names).
__all__ = [
    # stdlib re-exports (used across multiple mixins)
    "os", "re", "random", "select", "shlex", "shutil", "signal", "sys",
    "time", "traceback", "ET", "Path", "Optional",
    # third-party re-exports
    "httpx", "termios", "tty", "_TTY_AVAILABLE",
    "PromptSession", "run_in_terminal", "AutoSuggestFromHistory",
    "Completer", "Completion", "HTML", "FileHistory", "KeyBindings", "Style",
    "Console", "Panel", "platformdirs",
    # app imports
    "SCMClient", "__version__", "_BANNER_FILE", "_GOODBYE_FILE",
    "COMMANDS", "CATEGORIES", "CommandDef", "ExecutionContext", "match_command",
    "ArcConfig", "list_profiles", "load_config", "set_active_profile",
    "_cd_hint", "_configure_banner", "_help_footer", "_section_label",
    "_verb_description", "_verb_visible",
    "available_help_topics", "cisco_pager", "open_docs_in_browser", "page_length",
    "paging_stdout", "_PAGING_EXEMPT", "render_help_topic", "set_page_length",
    "UserPrefs", "load_prefs", "save_prefs",
    "dev_mode_from_env", "feature_state", "is_enabled", "is_feature_visible", "load_features",
    "effective_scope", "load_scope_overrides", "load_disabled_areas", "is_area_enabled",
    "load_command_visibility", "is_command_visible", "is_command_executable", "load_builtin_aliases",
    "_load_shell_builtins", "shell_help_rows",
    "SHELL_BUILTINS", "_SHELL_BUILTINS",
    "SSHManager",
    "ArcTheme", "THEME_KEYS", "load_theme", "reset_theme", "save_theme",
    "fmt",
    # module-level constants and helpers
    "console", "HISTORY_FILE", "GOODBYE_FILE", "_HELP_CMD_WIDTH",
    "PROMPT_STYLE",
    # functions
    "device_display_name", "device_ssh_host", "tsg_display", "active_tsg_label",
    "_expand_unambiguous_prefix", "tokenize", "_make_key_bindings",
    # dataclass
    "ShellState",
]
