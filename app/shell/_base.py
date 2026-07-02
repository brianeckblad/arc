"""Interactive REPL shell for ARC — Assisted Remote Console.

# ============================================================================
th# SHELL.PY — the shell spine (prompt loop, dispatch, execution, rendering)
# ============================================================================
#
# AGENT READ STRATEGY — do NOT read this whole file.
#   `dev/CODE_MAP.md` has the exact, always-current line range of every method
#   here. Read that map, then read_file(offset=START, limit=END-START+1) for the
#   one method you need. Regenerate the map with: python dev/generate_code_map.py
#   (smoke_test.py section 10 fails if the map is stale.)
#
# SMALL "STRINGS" attached to this spine (edit these first when relevant):
#   app/shell_catalog.py       — builtin command names + SHELL `?` help rows
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
)
from app.docs import available_help_topics, open_docs_in_browser, render_help_topic
from app.settings.features import dev_mode_from_env, feature_state, is_enabled, load_features
from app.settings.commands import load_command_visibility, is_command_visible
from app.shell_catalog import SHELL_BUILTINS, shell_help_rows
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
# Metadata lives in app/shell_catalog.py so agents can edit a tiny file first.
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
    "arc":    "bold ansicyan",
    "device": "bold ansiyellow",
    "folder": "bold ansigreen",
    "ctx":    "ansicyan dim",        # context-tier label (:global, :device)
    "sep":    "ansicyan",
    "arrow":  "bold ansicyan",
    "dev":    "bold ansimagenta",     # development-mode marker in the prompt
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

    '?' is bound to submit immediately — no Enter required.  This mirrors the
    Cisco / PAN-OS convention where '?' instantly shows context-sensitive help.
    Pressing '?' a second time on the same unchanged prefix escalates to full
    help (the typed-`??` gesture, which an instant-submit '?' cannot enter
    literally).
    """
    kb = KeyBindings()

    @kb.add("?")
    def _handle_question(event) -> None:
        buf = event.current_buffer
        # Preserve any partial command the user has already typed so that
        # dispatch can show context-sensitive help instead of the full menu.
        # e.g.  "show address" + ? → submit "show address ?"
        # Cisco/Palo-style: single ? always shows next options in context.
        # For full docs, use "<command> help" instead.
        prefix = buf.text.rstrip()
        buf.text = (prefix + " ?") if prefix else "?"
        buf.validate_and_handle()

    @kb.add("tab")
    def _handle_tab(event) -> None:
        # First Tab shows the completion menu (so value hints like "<name>"
        # are always visible, even when a slot has a single, non-inserting
        # hint); subsequent Tabs cycle through the entries.  This is the
        # vendor-CLI / bash behaviour and avoids silently auto-filling.
        buf = event.current_buffer
        if buf.complete_state:
            buf.complete_next()
        else:
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
    # Active TSG ID — overrides the value from ArcConfig when set.
    # Useful when a bearer token was issued at the root and the user needs
    # to work within a specific child TSG without re-authenticating.
    tsg_id: str = ""
    devices_cache: list[dict] = field(default_factory=list)
    # SCM folder names cached at startup for tab completion
    folders_cache: list[str] = field(default_factory=lambda: ["Shared", "Global"])
    # TSG entries fetched from /iam/v1/tenants — each dict has 'id' and 'display_name'
    tsgs_cache: list[dict] = field(default_factory=list)


# Auto-export every module global so mixins can `from app.shell._base import *`
__all__ = [n for n in dir() if not n.startswith('__') and n != 'annotations']
