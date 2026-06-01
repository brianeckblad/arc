"""Interactive REPL shell for ARC — Assisted Remote Console."""

from __future__ import annotations

import os
import random
import select
import shutil
import signal
import sys
import time
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional

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
from app.commands.registry import (
    COMMANDS,
    CATEGORIES,
    CommandDef,
    ExecutionContext,
    match_command,
)
from app.config import ArcConfig, list_profiles, load_config, set_active_profile
from app.docs import available_help_topics, open_docs_in_browser, render_help_topic
from app.ssh.manager import SSHManager
from app.theme import ArcTheme, THEME_KEYS, load_theme, reset_theme, save_theme
from app.utils import formatter as fmt

console = Console()

HISTORY_FILE = os.path.join(platformdirs.user_data_dir("arc"), "history")
GOODBYE_FILE = Path(__file__).parent / "goodbye.txt"

# Width of the command column in all inline help output.
# All sections (GLOBAL / FOLDER / DEVICE / SHELL) use the same value so
# descriptions land on the same visual column regardless of indent level.
# 4-space-indented tiers: 4 + _HELP_CMD_WIDTH = visual col 47
# 2-space-indented (scoped / full ref): uses +2 → also visual col 47
_HELP_CMD_WIDTH = 43

# Shell built-ins accepted by the dispatcher/completer.
_SHELL_BUILTINS: tuple[str, ...] = (
    "cd", "remote", "connect", "docs",
    "ls", "devices", "pwd",
    "folder", "tsg", "account",
    "configure", "cli",
    "clear", "exit", "quit",
    "help", "?",
)


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


# ---------------------------------------------------------------------------
# Tab completion
# ---------------------------------------------------------------------------

class ArcCompleter(Completer):
    """Context-aware tab completer.

    - After `cd` / `remote` / `connect` → completes with managed device names
    - After `folder`           → completes with SCM folder names
    - Otherwise               → completes with ARC command names + shell built-ins
    """


    def __init__(self, shell: "ArcShell") -> None:
        self._shell = shell

    def get_completions(self, document, complete_event):
        text = document.text_before_cursor.lstrip()
        parts = text.split()

        if not parts:
            for name in sorted(self._all_commands(include_remote_suffix=False)):
                yield Completion(name, start_position=0)
            return

        first = parts[0].lower()
        # True if the user has typed at least one space after the first token
        has_arg_space = len(parts) > 1 or text.endswith(" ")
        partial_arg = parts[1] if len(parts) > 1 else ""

        # ---- cd / remote / connect → device name completion ----
        if first in ("cd", "remote", "connect") and has_arg_space:
            for device in self._shell._state.devices_cache:
                candidate = device.get("hostname") or device.get("name") or ""
                if candidate and candidate.lower().startswith(partial_arg.lower()):
                    yield Completion(candidate, start_position=-len(partial_arg))
            return

        # ---- ls → 'folder' sub-command offers folder tree view ----
        if first == "ls" and has_arg_space:
            if "folder".startswith(partial_arg.lower()):
                yield Completion(
                    "folder",
                    start_position=-len(partial_arg),
                    display_meta="folder hierarchy with devices",
                )
            return

        # ---- folder → SCM folder name completion + 'create' subcommand ----
        if first == "folder" and has_arg_space:
            # 'create' is a special subcommand — offer it before folder names.
            if len(parts) <= 2 and "create".startswith(partial_arg.lower()):
                yield Completion(
                    "create",
                    start_position=-len(partial_arg),
                    display_meta="create a new folder",
                )
            # Don't complete further after 'folder create <name>' (arbitrary name).
            if len(parts) >= 2 and parts[1].lower() == "create":
                return
            for folder in self._shell._state.folders_cache:
                if folder.lower().startswith(partial_arg.lower()):
                    yield Completion(folder, start_position=-len(partial_arg))
            return

        # ---- configure → mode-entry completion ----
        if first == "configure" and has_arg_space:
            for sub in ("t", "terminal"):
                if sub.startswith(partial_arg.lower()):
                    yield Completion(sub, start_position=-len(partial_arg))
            return

        # ---- cli → theme operations in configure mode ----
        if first == "cli" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            if len(parts) <= 2:
                for sub in ("show", "color", "reset"):
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg))
            elif second == "color" and len(parts) <= 3:
                partial_key = parts[2] if len(parts) > 2 else ""
                for key in THEME_KEYS:
                    if key.startswith(partial_key.lower()):
                        yield Completion(key, start_position=-len(partial_key))
            return

        # ---- account → profile name completion ----
        if first == "account" and has_arg_space:
            for p in list_profiles():
                if p["name"].lower().startswith(partial_arg.lower()):
                    meta = "(active)" if p["active"] else (p["tsg_id"] or p["client_id"] or "")
                    yield Completion(
                        p["name"],
                        start_position=-len(partial_arg),
                        display_meta=meta,
                    )
            return

        # ---- tsg → hint with TSGs from SCM IAM cache (or config fallback) ----
        if first == "tsg" and has_arg_space:
            tsgs = self._shell._state.tsgs_cache
            if tsgs:
                # Cache populated — show real TSG IDs with their display names.
                for entry in tsgs:
                    tsg_id = str(entry.get("id") or entry.get("tsg_id") or "")
                    display_name = str(entry.get("display_name") or entry.get("name") or "")
                    if not tsg_id:
                        continue
                    if tsg_id.lower().startswith(partial_arg.lower()):
                        yield Completion(
                            tsg_id,
                            start_position=-len(partial_arg),
                            display_meta=display_name,
                        )
            else:
                # Cache empty (IAM not accessible) — fall back to configured values.
                config_tsg = self._shell._config.scm.tsg_id
                active_tsg = self._shell._state.tsg_id
                for tsg in dict.fromkeys(filter(None, [config_tsg, active_tsg])):
                    if tsg.lower().startswith(partial_arg.lower()):
                        yield Completion(tsg, start_position=-len(partial_arg))
            return

        # ---- show device <name> [snippets] → device name completion ----
        if text.lower().startswith("show device ") and len(parts) >= 2:
            # Parts: ["show", "device", <partial_name>, ...]
            if len(parts) == 3 or (len(parts) == 2 and text.endswith(" ")):
                # Completing device name
                partial_name = parts[2] if len(parts) > 2 else ""
                for device in self._shell._state.devices_cache:
                    candidate = device.get("hostname") or device.get("name") or ""
                    if candidate and candidate.lower().startswith(partial_name.lower()):
                        yield Completion(candidate, start_position=-len(partial_name))
                return
            if len(parts) == 4 or (len(parts) == 3 and text.endswith(" ")):
                # Completing "snippets" after the device name
                partial_sub = parts[3] if len(parts) > 3 else ""
                if "snippets".startswith(partial_sub.lower()):
                    yield Completion("snippets", start_position=-len(partial_sub))
                return

        # ---- show snippet <name> [details] → context-aware completion ----
        # "show snippet "          → complete snippet name
        # "show snippet <name> "   → offer "details" subcommand
        # "show snippet <name> d"  → complete "details"
        if text.lower().startswith("show snippet ") and not text.lower().startswith("show snippets"):
            # parts[0]="show", parts[1]="snippet", parts[2]=name-or-partial, parts[3]=subcommand
            name_part    = parts[2] if len(parts) > 2 else ""
            subcmd_part  = parts[3] if len(parts) > 3 else ""
            has_subcmd_space = len(parts) > 3 or (len(parts) == 3 and text.endswith(" "))

            # Collect candidate snippet names
            device = self._shell._state.device
            if device and device.get("snippets"):
                candidates = list(device.get("snippets") or [])
            else:
                seen: set[str] = set()
                for d in self._shell._state.devices_cache:
                    for sn in (d.get("snippets") or []):
                        seen.add(sn)
                candidates = sorted(seen)

            if has_subcmd_space:
                # Name is already complete — offer "details" subcommand
                if "details".startswith(subcmd_part.lower()):
                    yield Completion(
                        "details",
                        start_position=-len(subcmd_part),
                        display_meta="show full configured objects",
                    )
            else:
                # Still completing the name
                for name in candidates:
                    if name.lower().startswith(name_part.lower()):
                        yield Completion(name, start_position=-len(name_part))
            return

        # ---- help → command/topic completion ----
        if first == "help" and has_arg_space:
            partial_topic = " ".join(parts[1:]).lower()
            for topic in available_help_topics():
                if topic.startswith(partial_topic):
                    yield Completion(topic[len(partial_topic):], start_position=-len(partial_topic))
            return


        # ---- Default: ARC command + built-in completion ----
        include_remote_suffix = " --" in text
        for name in sorted(self._all_commands(include_remote_suffix=include_remote_suffix)):
            if name.startswith(text):
                # Show full candidates in the menu instead of suffix fragments.
                yield Completion(name, start_position=-len(text))

    def _all_commands(self, include_remote_suffix: bool) -> list[str]:
        builtins = list(_SHELL_BUILTINS)
        commands = list(COMMANDS.keys())
        if not include_remote_suffix:
            return builtins + commands
        with_remote = [f"{c} --remote" for c in commands]
        return builtins + commands + with_remote


# ---------------------------------------------------------------------------
# Shell
# ---------------------------------------------------------------------------

PROMPT_STYLE = Style.from_dict({
    "arc":    "bold ansicyan",
    "device": "bold ansiyellow",
    "folder": "bold ansigreen",
    "ctx":    "ansicyan dim",        # context-tier label (:global, :device)
    "sep":    "ansicyan",
    "arrow":  "bold ansicyan",
})


def _make_key_bindings() -> KeyBindings:
    """Return key bindings for the ARC shell.

    '?' is bound to submit immediately — no Enter required.
    This mirrors the PAN-OS CLI convention where '?' instantly
    shows context-sensitive help.
    """
    kb = KeyBindings()

    @kb.add("?")
    def _handle_question(event) -> None:
        buf = event.current_buffer
        # Preserve any partial command the user has already typed so that
        # dispatch can show context-sensitive help instead of the full menu.
        # e.g.  "show address" + ? → submit "show address ?"
        existing = buf.text
        if existing.strip():
            buf.text = existing.rstrip() + " ?"
        else:
            buf.text = "?"
        buf.validate_and_handle()

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


class ArcShell:
    """Main interactive REPL."""

    def __init__(self, config: ArcConfig) -> None:
        self._config = config
        self._state = ShellState(
            folder=config.default_folder,
            # Seed from config so pwd shows the right TSG from the start.
            tsg_id=config.scm.tsg_id,
        )
        # Prefix to restore in the next prompt after a '?' context-help lookup.
        # e.g. "show ?" prints help then re-seeds the prompt with "show ".
        self._pending_default: str = ""

        # Build clients
        self._scm: Optional[SCMClient] = None
        self._ssh = SSHManager()

        # Load CLI theme (colours for ? help, banner, etc.)
        self._theme: ArcTheme = load_theme()

        # Print banner before init so the logo appears above the SCM connection line.
        self._print_banner()
        self._print_startup_help()
        self._init_clients()

        # Prompt session
        os.makedirs(os.path.dirname(HISTORY_FILE), exist_ok=True)
        self._session: PromptSession = PromptSession(
            history=FileHistory(HISTORY_FILE),
            auto_suggest=AutoSuggestFromHistory(),
            completer=ArcCompleter(self),
            complete_while_typing=False,
            key_bindings=_make_key_bindings(),
            style=PROMPT_STYLE,
        )

    # ------------------------------------------------------------------
    # Client init
    # ------------------------------------------------------------------

    def _init_clients(self) -> None:
        if self._config.scm.is_configured:
            try:
                self._scm = SCMClient(self._config.scm)
                tsg_id = self._config.scm.tsg_id or "n/a"

                # Derive a human-readable identity label:
                #   1. client_id present → strip the @domain suffix (e.g. "pa-api-beckblad")
                #   2. non-default named profile → use the profile name
                #   3. default single profile with no client_id → omit the label entirely
                client_id = self._config.scm.client_id
                if client_id:
                    identity = client_id.split("@")[0]
                elif self._config.profile_name != "default":
                    identity = self._config.profile_name
                else:
                    identity = None

                identity_part = (
                    f"  [dim]account:[/dim] [bold]{identity}[/bold]"
                    if identity else ""
                )
                console.print(
                    f"[green]✓[/green] SCM connected"
                    f"{identity_part}"
                    f"  [dim]TSG:[/dim] [cyan]{tsg_id}[/cyan]"
                    f"  [dim]v{__version__}[/dim]"
                )
            except Exception as exc:
                console.print(f"[red]✗[/red] SCM not connected: {exc}")

        if not self._scm:
            console.print(
                "[red]✗[/red] [red]SCM not connected.[/red] "
                "Commands will fail unless you use [bold]remote <device>[/bold] or "
                "[bold]--remote[/bold] with SSH credentials, "
                "or set SCM credentials and restart.\n"
                "Run [bold]arc auth login[/bold] to configure."
            )
            return

        # Pre-populate caches — failures are silent; the cache just stays empty
        # and tab completion falls back to defaults.
        console.print("[dim]Loading caches…[/dim]", end="\r")
        self._refresh_devices(silent=True)
        self._refresh_folders(silent=True)
        self._refresh_tsgs(silent=True)
        console.print(" " * 40, end="\r")

        # SCM sometimes returns an empty device list on the very first request
        # right after OAuth (token propagation / eventual consistency).  Retry
        # once after a short pause before giving up and showing the hint.
        if not self._state.devices_cache:
            time.sleep(1.5)
            self._refresh_devices(silent=True)

        # Report what was actually loaded so users know their access level.
        parts: list[str] = []
        if self._state.devices_cache:
            device_count = len(self._state.devices_cache)
            connected_count = sum(1 for d in self._state.devices_cache if d.get("is_connected") is True)
            disconnected_count = sum(1 for d in self._state.devices_cache if d.get("is_connected") is False)
            parts.append(
                f"{device_count} device(s), ([green]{connected_count}[/green])[dim]connected[/dim], "
                f"([red]{disconnected_count}[/red])[dim]disconnected[/dim]"
            )
        if self._state.tsgs_cache:
            parts.append(f"({len(self._state.tsgs_cache)})[dim]TSG(s)[/dim]")

        if parts:
            console.print(f"[dim]Loaded:[/dim] {', '.join(parts)}")
        else:
            console.print(
                "[dim]API connected — device/folder list not available with this service "
                "account role (policy commands will still work)[/dim]"
            )

        if not self._state.devices_cache:
            console.print(
                "[dim]No devices loaded — run [bold]ls[/bold] to retry, "
                "or check your service account has Device Administrator access.[/dim]"
            )

    # ------------------------------------------------------------------
    # Prompt
    # ------------------------------------------------------------------

    def _prompt(self) -> HTML:
        """Build the prompt string reflecting the active context tier.

        Tier rules:
          No device, Shared folder  → arc:global >        (global context)
          No device, named folder   → arc:Production >     (folder context)
          Device, Shared folder     → arc:fw01:device >    (device context)
          Device, named folder      → arc:fw01:Production > (folder context on device)
        """
        folder    = self._state.folder or "Shared"
        at_shared = folder.lower() == "shared"
        prompt_tail = " # " if self._state.configure_mode else " > "

        if self._state.device:
            name = self._state.device.get("hostname") or self._state.device.get("name") or "device"
            if at_shared:
                # Device selected but still at Shared — show context tier as ':device'
                return HTML(
                    f"<arc>arc</arc>"
                    f"<sep>:</sep><device>{name}</device>"
                    f"<sep>:</sep><ctx>device</ctx>"
                    f"<arrow>{prompt_tail}</arrow>"
                )
            # Device selected and in a specific folder — show both
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><device>{name}</device>"
                f"<sep>:</sep><folder>{folder}</folder>"
                f"<arrow>{prompt_tail}</arrow>"
            )

        if at_shared:
            # No device, no specific folder — global context
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><ctx>global</ctx>"
                f"<arrow>{prompt_tail}</arrow>"
            )

        # No device but in a specific folder — folder context
        return HTML(
            f"<arc>arc</arc>"
            f"<sep>:</sep><folder>{folder}</folder>"
            f"<arrow>{prompt_tail}</arrow>"
        )

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def run(self) -> None:
        while True:
            try:
                # Re-seed the prompt with any prefix saved by a '?' context-help lookup
                # so the user can keep typing without re-entering what they had.
                default = self._pending_default
                self._pending_default = ""
                line = self._session.prompt(self._prompt(), default=default).strip()
            except KeyboardInterrupt:
                continue
            except EOFError:
                break
            if not line:
                continue
            try:
                should_exit = self._dispatch(line)
                if should_exit:
                    break
            except Exception as exc:
                if self._config.debug:
                    traceback.print_exc()
                console.print(f"[red]Error:[/red] {exc}")

        self._cleanup()

    # ------------------------------------------------------------------
    # Dispatch
    # ------------------------------------------------------------------

    def _dispatch(self, line: str) -> bool:
        """Process one input line.  Returns True when the user wants to exit ARC."""
        # Strip --remote flag before any other parsing
        remote = False
        tokens = line.split()
        if "--remote" in tokens:
            remote = True
            tokens = [t for t in tokens if t != "--remote"]

        if not tokens:
            return False

        # Cisco-style shorthand expansion:
        #   e            -> exit
        #   sh sec pol   -> show security policy
        # Expansion occurs only when a prefix resolves to exactly one command.
        phrases = [[b] for b in _SHELL_BUILTINS if b != "?"] + [k.split() for k in COMMANDS]

        # Expand the command/topic portion before trailing "help".
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            tokens = _expand_unambiguous_prefix(tokens[:-1], phrases) + ["help"]

        # Expand prefix before '?' context help trigger.
        if "?" in tokens:
            qidx = tokens.index("?")
            tokens = _expand_unambiguous_prefix(tokens[:qidx], phrases) + tokens[qidx:]
        else:
            tokens = _expand_unambiguous_prefix(tokens, phrases)

        # "<command> help" — trailing 'help' opens the full docs page for that command.
        # This must be checked before any individual builtin dispatcher so that
        # e.g. "cd help" shows docs instead of treating "help" as a device name.
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            topic = " ".join(tokens[:-1]).lower()
            self._cmd_help_docs(topic)
            return False

        # Cisco-style inline help: trailing '?' shows a compact one-liner per command.
        # e.g.  "show address ?"  → all commands starting with "show address"
        #        "show ?"         → all commands starting with "show"
        #        "?"              → full 3-tier inline listing
        if "?" in tokens:
            question_idx = tokens.index("?")
            prefix_tokens = tokens[:question_idx]
            if prefix_tokens:
                # Restore the prefix so the user can keep typing after help renders.
                self._pending_default = " ".join(prefix_tokens) + " "
                self._cmd_help_inline(prefix_tokens)
                return False
            # Fall through so the bare "?" branch below fires

        cmd = tokens[0].lower()

        # ---- exit / quit ----
        if cmd in ("exit", "quit"):
            if self._state.configure_mode:
                self._state.configure_mode = False
                console.print("[cyan]Exited configure mode.[/cyan]")
                return False
            return True


        # ---- Shell built-ins ----
        if cmd == "clear":
            console.clear()
            return False

        if cmd == "pwd":
            self._cmd_pwd()
            return False

        if cmd in ("ls", "devices"):
            self._cmd_devices(tokens[1:])
            return False

        if cmd == "cd":
            self._cmd_cd(tokens[1:])
            return False

        if cmd == "connect":
            self._cmd_connect(tokens[1:])
            return False

        if cmd == "remote":
            self._cmd_connect(tokens[1:], require_target=True)
            return False

        if cmd == "folder":
            self._cmd_folder(tokens[1:])
            return False

        if cmd == "tsg":
            self._cmd_tsg(tokens[1:])
            return False

        if cmd == "account":
            self._cmd_account(tokens[1:])
            return False

        if cmd == "configure":
            self._cmd_configure(tokens[1:])
            return False

        if cmd == "cli":
            self._cmd_cli(tokens[1:])
            return False

        if cmd in ("help", "?"):
            rest = tokens[1:]
            if rest and rest[0].lower() == "all":
                self._cmd_help_full()
            elif rest:
                # "help <topic>" — render docs page for the topic
                self._cmd_help_docs(" ".join(rest).lower())
            else:
                # Bare "help" or "?" — Cisco-style compact inline listing
                self._cmd_help_inline([])
            return False

        if cmd == "docs":
            # `docs` alone → open browser; `docs <topic>` → render in shell
            if len(tokens) > 1:
                topic = " ".join(tokens[1:])
                if render_help_topic(console, topic):
                    return False
                console.print(
                    f"[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
                    "Type [bold]docs[/bold] to open the full browser docs, or "
                    "[bold]help commands[/bold] to list documented topics."
                )
                return False
            url = open_docs_in_browser()
            console.print(f"[green]Docs opened in browser:[/green] {url}")
            return False

        # Convenience alias: show folder / show folders
        if cmd == "show" and len(tokens) > 1 and tokens[1].lower() in ("folder", "folders"):
            self._cmd_folder([])
            return False

        # ---- Registry commands ----
        key, cmd_def, args = match_command(tokens)
        if key is None:
            console.print(
                f"[red]Unknown command:[/red] [bold]{' '.join(tokens)}[/bold]  "
                "— type [bold]?[/bold] or [bold]help[/bold] for available commands."
            )
            return False

        if remote:
            self._execute_remote(key, cmd_def, args)
        else:
            self._execute_api(key, cmd_def, args)

        return False

    # ------------------------------------------------------------------
    # Command: cd
    # ------------------------------------------------------------------

    def _cmd_cd(self, args: list[str]) -> None:
        """Change the active SCM/API device context.

        This never starts SSH. Use `connect` for the current device or
        `remote <device>` to open an interactive SSH session.
        """
        if not args or args[0] in ("..", "/"):
            self._state.device = None
            console.print(
                f"[cyan]Device context cleared.[/cyan]  "
                f"SCM / global  folder: [bold green]{self._state.folder}[/bold green]"
            )
            return

        target = " ".join(args)

        # Always try to refresh if cache is empty so we give the most
        # accurate answer about whether the device exists in this TSG.
        if not self._state.devices_cache:
            self._refresh_devices()

        match = self._find_device(target)
        if match:
            self._state.device = match
            name    = match.get("hostname") or match.get("display_name") or match.get("name") or target
            serial  = match.get("serial_number") or match.get("serial") or match.get("name") or "n/a"
            ip_raw  = match.get("ip_address") or match.get("ip-address") or ""
            ip      = ip_raw if ip_raw and ip_raw.lower() not in ("unknown", "none") else "n/a"
            model   = match.get("model") or ""
            sw_ver  = match.get("software_version") or match.get("sw_version") or ""
            connected = (
                "  [green]connected[/green]" if match.get("is_connected")
                else "  [red]disconnected[/red]" if match.get("is_connected") is False
                else ""
            )
            parts = [f"[cyan]SCM device:[/cyan] [bold]{name}[/bold]"]
            parts.append(f"serial: [bold]{serial}[/bold]")
            parts.append(f"ip: {ip}")
            if model:
                parts.append(f"model: {model}")
            if sw_ver:
                parts.append(f"sw: {sw_ver}")
            console.print("  ".join(parts) + connected)
            return

        # Device not found.
        if self._state.devices_cache:
            # Cache is populated — this TSG has no such device. Hard stop.
            active_tsg = self._state.tsg_id or self._config.scm.tsg_id or "current TSG"
            console.print(
                f"[red]Device '{target}' not found in TSG {active_tsg}.[/red]\n"
                f"  [dim]Use [bold]ls[/bold] or [bold]show devices[/bold] to see "
                f"the {len(self._state.devices_cache)} device(s) visible in this TSG.\n"
                "  Use [bold]tsg <id>[/bold] to switch to a different tenant.[/dim]"
            )
        else:
            # Cache empty even after refresh (API unavailable / empty tenant).
            # Permit a stub only in this case so SSH still works when SCM
            # device inventory is inaccessible.
            console.print(
                f"[yellow]Device list unavailable — creating stub for '{target}'.[/yellow]\n"
                "  [dim]SSH with [bold]remote[/bold] / [bold]connect[/bold] may still "
                "work if the device is reachable directly.[/dim]"
            )
            self._state.device = {
                "name": target,
                "hostname": target,
                "ip_address": target,
                "serial_number": "",
            }

    def _find_device(self, query: str) -> Optional[dict]:
        """Find a device in the cache by hostname, serial, name, or IP.

        Checks all field-name variants the SCM API may return.
        """
        q = query.lower()
        for d in self._state.devices_cache:
            if (
                (d.get("hostname") or "").lower() == q
                or (d.get("display_name") or "").lower() == q
                or (d.get("name") or "").lower() == q
                or (d.get("serial_number") or "").lower() == q
                or (d.get("serial") or "").lower() == q
                or (d.get("ip_address") or "").lower() == q
            ):
                return d
        return None

    def _refresh_devices(self, silent: bool = False) -> None:
        """Fetch managed devices and populate the cache used by tab completion and cd.

        Uses self._scm directly (same pattern as _refresh_folders / _refresh_tsgs)
        rather than going through _make_context().  The devices endpoint returns
        all managed devices TSG-wide regardless of the active folder, so no folder
        parameter is passed.
        """
        if not self._scm:
            return
        try:
            devices = self._scm.get_devices()
            if devices:
                self._state.devices_cache = devices
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh device list: {exc}[/yellow]")

    def _refresh_folders(self, silent: bool = False) -> None:
        """Fetch SCM folder names and populate the cache used by 'folder' tab completion."""
        if not self._scm:
            return
        try:
            folders = self._scm.get_folders()
            if folders:
                self._state.folders_cache = folders
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh folder list: {exc}[/yellow]")

    def _refresh_tsgs(self, silent: bool = False) -> None:
        """Fetch TSG entries from SCM IAM and populate the cache used by 'tsg' tab completion.

        Each entry is a dict with at minimum 'id' and 'display_name'.  The list
        may be empty if the token lacks IAM read permissions — the completer falls
        back to the configured TSG ID in that case.
        """
        if not self._scm:
            return
        try:
            tenants = self._scm.get_tenants()
            if tenants:
                self._state.tsgs_cache = tenants
        except Exception as exc:
            if not silent:
                console.print(f"[yellow]Could not refresh TSG list: {exc}[/yellow]")

    # ------------------------------------------------------------------
    # Command: connect  (SSH passthrough mode)
    # ------------------------------------------------------------------

    def _cmd_connect(self, args: list[str], require_target: bool = False) -> None:
        """Connect to a device via SSH and hand the terminal over to the remote shell."""

        if require_target and not args:
            console.print(
                "[yellow]Usage:[/yellow] remote <device-name | hostname | ip | serial>\n"
                "Tab after 'remote ' to see available devices."
            )
            return

        if not args and not self._state.device:
            console.print(
                "[yellow]Usage:[/yellow] cd <device> then connect, "
                "or remote <device-name | hostname | ip | serial>\n"
                "Tab after 'remote ' to see available devices."
            )
            return

        # Snapshot the current device context so we can restore it if the
        # connection fails.  A failed connect should not permanently change
        # which device is active — only a successful session should do that.
        previous_device = self._state.device

        if args:
            target = " ".join(args)
            if not self._state.devices_cache:
                self._refresh_devices()
            match = self._find_device(target)
            if match:
                self._state.device = match
                name = match.get("hostname") or match.get("name") or target
            elif self._state.devices_cache:
                # Cache populated — device genuinely not in this TSG.
                active_tsg = self._state.tsg_id or self._config.scm.tsg_id or "current TSG"
                self._state.device = previous_device
                console.print(
                    f"[red]Device '{target}' not found in TSG {active_tsg}.[/red]\n"
                    f"  [dim]Use [bold]ls[/bold] to see available devices, "
                    "or [bold]tsg <id>[/bold] to switch tenant.[/dim]"
                )
                return
            else:
                # Cache empty — allow direct SSH by hostname/IP as a fallback.
                console.print(
                    f"[yellow]Device '{target}' not in cache — "
                    "attempting SSH directly.[/yellow]"
                )
                self._state.device = {
                    "name": target, "hostname": target,
                    "ip_address": target, "serial_number": "",
                }
                name = target
        else:
            name = self._state.device.get("hostname") or self._state.device.get("name") or "device"

        host = self._state.device.get("ip_address") or self._state.device.get("hostname") or ""
        if not host:
            self._state.device = previous_device
            console.print("[red]Cannot determine SSH target — no IP or hostname for this device.[/red]")
            return

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)

        if not ssh_key_path and not ssh_password:
            console.print(
                "[yellow]⚠  No SSH credentials stored for ARC.[/yellow]\n"
                "  Trying SSH agent and default key files — if those are absent\n"
                "  you will be prompted during the keyboard-interactive exchange.\n"
                "  Run [bold]arc auth login[/bold] to store credentials so they\n"
                "  auto-fill next time, or see [bold]help config osx[/bold] / "
                "[bold]help config win[/bold] / [bold]help config nix[/bold].\n"
            )

        console.print(f"[dim]Connecting SSH: {ssh_user}@{host}:{ssh_port}…[/dim]")

        try:
            channel = self._ssh.open_shell(
                host=host,
                user=ssh_user,
                key_path=ssh_key_path,
                password=ssh_password,
                port=ssh_port,
            )
        except Exception as exc:
            # Restore the previous device context so a failed connect
            # does not strand the user at a broken device stub.
            self._state.device = previous_device
            console.print(f"[red]SSH connection failed:[/red] {exc}")
            return

        self._run_interactive_shell(channel, name)

    # ------------------------------------------------------------------
    # True interactive PTY session
    # ------------------------------------------------------------------

    def _run_interactive_shell(self, channel, device_name: str) -> None:
        """Hand the terminal over to *channel* for a fully interactive SSH session.

        ARC is not a middle layer here — every keystroke goes directly to the
        device and every byte from the device is written straight to stdout.
        ARC command dispatch, completers, and key bindings are all inactive
        for the duration.

        The session ends when the remote device closes the channel (the user
        types 'exit' or the device terminates the session).  The ARC prompt
        reappears automatically once the channel closes.
        """
        if not _TTY_AVAILABLE:
            console.print(
                "[red]Interactive SSH sessions require a Unix terminal (termios/tty).[/red]\n"
                "On Windows use `--remote` to run individual commands via SSH."
            )
            channel.close()
            return

        # Resize the remote PTY to match the current local terminal.
        cols, rows = shutil.get_terminal_size()
        try:
            channel.resize_pty(width=cols, height=rows)
        except Exception:
            pass

        console.print(
            f"\n[green]✓[/green] Authenticated — handing terminal to "
            f"[bold]{device_name}[/bold]\n"
            "[dim]ARC is now a transparent pipe. "
            "Every keystroke goes directly to the device.\n"
            "Type 'exit' on the device to close the session and return to ARC.[/dim]\n"
        )

        def _handle_resize(_sig, _frame) -> None:
            """Forward terminal resize events to the remote PTY."""
            try:
                c, r = shutil.get_terminal_size()
                channel.resize_pty(width=c, height=r)
            except Exception:
                pass

        old_sigwinch = signal.signal(signal.SIGWINCH, _handle_resize)
        old_tty = termios.tcgetattr(sys.stdin)

        try:
            tty.setraw(sys.stdin.fileno())
            channel.settimeout(0.0)

            while True:
                r_ready, _, _ = select.select([channel, sys.stdin], [], [], 0.1)

                # Drain and print any output from the device.
                if channel in r_ready:
                    data = channel.recv(1024)
                    if not data:
                        break
                    sys.stdout.buffer.write(data)
                    sys.stdout.buffer.flush()

                # Forward keystrokes to the device.
                if sys.stdin in r_ready:
                    data = os.read(sys.stdin.fileno(), 1024)
                    if not data:
                        break
                    channel.send(data)

                # Exit when the device closes the channel.
                if channel.closed or channel.exit_status_ready():
                    # Drain any final bytes.
                    while channel.recv_ready():
                        data = channel.recv(1024)
                        if data:
                            sys.stdout.buffer.write(data)
                    sys.stdout.buffer.flush()
                    break

        except Exception:
            pass  # Session ended unexpectedly — restore terminal below.

        finally:
            termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_tty)
            signal.signal(signal.SIGWINCH, old_sigwinch)
            try:
                channel.close()
            except Exception:
                pass

        # Print on a fresh line (device may not have emitted a trailing newline).
        console.print(
            f"\n[cyan]SSH session ended.[/cyan]  "
            f"Back in ARC — device context [bold]{device_name}[/bold] preserved."
        )


    # ------------------------------------------------------------------
    # Command: ls / devices
    # ------------------------------------------------------------------

    def _cmd_devices(self, args: list[str] | None = None) -> None:
        """Context-aware ls/devices command.

        At root (no device selected) → refresh and show the device list.
        In device context (after cd <device>) → show that device's detail
        and its attached snippets.

        Subcommands:
          ls folder  — show full folder hierarchy with devices in each folder
        """
        # Subcommand: ls folder
        if args and args[0].lower() == "folder":
            self._cmd_ls_folder()
            return

        if not self._state.device:
            # Root context — show all devices
            self._refresh_devices()
            if not self._state.devices_cache:
                console.print("[yellow]No devices found or API not configured.[/yellow]")
                return
            console.print(fmt.format_devices(self._state.devices_cache))
            return

        # Device context — show detail + snippets for the current device
        if not self._scm:
            console.print("[yellow]SCM not configured — cannot fetch device detail.[/yellow]")
            return
        device = self._state.device
        hostname = device.get("hostname") or device.get("name") or ""
        console.print(fmt.format_device_detail(device))

        # Fetch and display snippets attached to this device
        snippet_names: list[str] = device.get("snippets") or []
        if not snippet_names:
            console.print(f"[dim]No snippets attached to {hostname}.[/dim]")
            return

        all_snippets = self._scm.get_snippets()
        by_name = {s.get("name"): s for s in all_snippets}
        enriched: list[dict] = []
        for name in snippet_names:
            s = by_name.get(name)
            if s and s.get("id"):
                try:
                    enriched.append(self._scm.get_snippet_detail(s["id"]))
                except Exception:
                    enriched.append(s)
            else:
                enriched.append({"name": name})

        console.print(fmt.format_snippets(enriched, device_filter=hostname))

    # ------------------------------------------------------------------
    # Command: ls folder
    # ------------------------------------------------------------------

    def _cmd_ls_folder(self) -> None:
        """Show the full folder hierarchy with devices placed in their folder.

        Fetches the live folder list (with parent relationships) and the device
        list, then renders a Rich tree that shows the folder structure and which
        devices live in each folder.

        Use this to answer "which folder is my device in?" or "what's the
        folder hierarchy for this tenant?".
        """
        if not self._scm:
            console.print("[yellow]SCM not configured — cannot fetch folder structure.[/yellow]")
            return

        console.print("[dim]Loading folder structure and devices…[/dim]", end="\r")
        folders = self._scm.get_folders_full()
        devices = self._scm.get_devices()
        # Clear the loading line before rendering.
        console.print(" " * 55, end="\r")

        if not folders:
            console.print("[yellow]No folders returned by the SCM API.[/yellow]")
            return

        tree = fmt.format_folder_tree(folders, devices)
        console.print(tree)

        total_folders = len(folders)
        total_devices = len(devices)
        assigned = sum(
            1 for d in devices
            if d.get("folder") and d.get("folder") != "Shared"
        )
        unassigned = total_devices - assigned
        notes: list[str] = [f"{total_folders} folder(s)", f"{total_devices} device(s)"]
        if unassigned and total_devices:
            notes.append(f"{unassigned} in Shared/unassigned")
        console.print(f"\n[dim]{', '.join(notes)}[/dim]")
        console.print(
            "[dim]  folder <name> → switch active folder  |  "
            "folder create <name> → create a new folder[/dim]"
        )

    # ------------------------------------------------------------------
    # Command: pwd
    # ------------------------------------------------------------------

    def _cmd_pwd(self) -> None:
        """Show current device context, active SCM folder, TSG, and SSH credential status."""
        if self._state.device:
            d = self._state.device
            name    = d.get("hostname") or d.get("name") or "?"
            serial  = d.get("serial_number") or d.get("name") or "n/a"
            ip      = d.get("ip_address") or "n/a"
            model   = d.get("model") or ""
            sw_ver  = d.get("software_version") or ""
            connected = "[green]connected[/green]" if d.get("is_connected") else "[red]disconnected[/red]"
            snippets = d.get("snippets") or []
            console.print(
                f"[bold cyan]Device:[/bold cyan] {name}  "
                f"serial: {serial}  ip: {ip}  {model}  {sw_ver}  {connected}"
            )
            if snippets:
                console.print(
                    f"[bold cyan]Snippets:[/bold cyan] {', '.join(snippets)}"
                )
            console.print(
                "[dim]  ls → device detail + snippets  |  "
                "show device snippets → full snippet list  |  "
                "show snippet <name> → snippet detail[/dim]"
            )
        else:
            console.print("[bold cyan]Context:[/bold cyan] SCM / global  [API mode]")
            console.print(
                "[dim]  ls → device list  |  "
                "cd <device> → enter device context  |  "
                "show devices → full device table[/dim]"
            )
        # Folder is always shown — it is the primary SCM scope for all API calls.
        console.print(
            f"[bold cyan]SCM folder:[/bold cyan] [bold green]{self._state.folder}[/bold green]"
            "  [dim](all API calls scoped to this folder — change with 'folder <name>')[/dim]"
        )
        active_tsg = self._state.tsg_id or "(root / config default)"
        console.print(f"[bold cyan]TSG:[/bold cyan] [cyan]{active_tsg}[/cyan]")

        # Show active profile — always useful to see which account you are on.
        profile_name = self._config.profile_name
        client_id    = self._config.scm.client_id or "(bearer token)"
        console.print(
            f"[bold cyan]Account profile:[/bold cyan] [bold]{profile_name}[/bold]  "
            f"[dim]{client_id}[/dim]"
        )

    # ------------------------------------------------------------------
    # Command: folder
    # ------------------------------------------------------------------

    def _cmd_folder(self, args: list[str]) -> None:
        """Set or display the active SCM folder context.

        The active folder is passed as the ``?folder=`` query parameter on
        every SCM REST call.  It is always visible in the prompt so there is
        no ambiguity about which folder a command is scoped to.

        Usage:
          folder                  — list available folders and show the active one
          folder <name>           — switch to <name>
          folder ..               — switch to 'Shared' (root / default)
          folder create <name>    — create a new folder (interactive parent selection)
        """
        # Subcommand: folder create <name>
        if args and args[0].lower() == "create":
            folder_name = args[1] if len(args) > 1 else None
            if not self._state.configure_mode:
                console.print(
                    "[yellow]Write operation blocked:[/yellow] folder creation requires configure mode.\n"
                    "  Enter [bold]configure[/bold] first, then run [bold]folder create <name>[/bold]."
                )
                return
            self._cmd_folder_create(folder_name)
            return

        if not args:
            # Show current folder and available options, same pattern as `tsg` with no args.
            console.print(f"[cyan]Active SCM folder:[/cyan] [bold]{self._state.folder}[/bold]")
            if self._state.folders_cache:
                console.print("\n[bold yellow]Available Folders[/bold yellow]  "
                              "[dim](Tab after 'folder ' to complete)[/dim]")
                for name in sorted(self._state.folders_cache):
                    marker = " [green]◀ active[/green]" if name == self._state.folder else ""
                    console.print(f"  [green]{name}[/green]{marker}")
            else:
                console.print(
                    "[dim]No folder list cached — run [bold]ls[/bold] or "
                    "[bold]folder[/bold] after SCM is connected to populate.[/dim]"
                )
                self._refresh_folders(silent=False)
                if self._state.folders_cache:
                    console.print("\n[bold yellow]Available Folders[/bold yellow]")
                    for name in sorted(self._state.folders_cache):
                        marker = " [green]◀ active[/green]" if name == self._state.folder else ""
                        console.print(f"  [green]{name}[/green]{marker}")
            console.print(
                "\n[dim]  folder <name> → switch  |  "
                "folder .. → back to Shared  |  "
                "Tab after 'folder ' → complete folder name[/dim]"
            )
            return

        # `folder ..` or `folder /` → reset to default (Shared).
        if args[0] in ("..", "/"):
            self._state.folder = "Shared"
            console.print("[cyan]SCM folder reset to:[/cyan] [bold]Shared[/bold]")
            return

        new_folder = args[0]

        # Validate against the known folder list when the cache is populated.
        # This prevents silently setting a folder that doesn't exist in the
        # active TSG — same principle as cd refusing unknown devices.
        if (
            self._state.folders_cache
            and self._state.folders_cache != ["Shared", "Global"]
            and new_folder not in self._state.folders_cache
        ):
            active_tsg = self._state.tsg_id or self._config.scm.tsg_id or "current TSG"
            console.print(
                f"[red]Folder '{new_folder}' not found in TSG {active_tsg}.[/red]\n"
                f"  [dim]Available folders: {', '.join(sorted(self._state.folders_cache))}\n"
                "  Tab after 'folder ' to complete, or 'folder' alone to list folders.[/dim]"
            )
            return

        self._state.folder = new_folder
        # Clear device context when switching folder — a device cd'd to in one
        # folder may not be visible or relevant in another.
        if self._state.device:
            device_name = (
                self._state.device.get("hostname") or
                self._state.device.get("name") or "device"
            )
            self._state.device = None
            console.print(
                f"[cyan]SCM folder set to:[/cyan] [bold]{new_folder}[/bold]  "
                f"[dim](device context {device_name} cleared — use cd to re-enter)[/dim]"
            )
        else:
            console.print(f"[cyan]SCM folder set to:[/cyan] [bold]{new_folder}[/bold]")

    # ------------------------------------------------------------------
    # Command: folder create
    # ------------------------------------------------------------------

    def _cmd_folder_create(self, name: Optional[str]) -> None:
        """Interactive folder creation: prompt for a parent, confirm, and POST to SCM.

        Displays the full folder hierarchy as a numbered list so the operator
        can see the tree and pick the parent by number or by name.

        "above" = pick a folder closer to the root (shorter path).
        "below" = pick a folder deeper in the tree (longer path / a child folder).
        The new folder will be created as a direct child of the selected parent.
        """
        if not name or not name.strip():
            console.print(
                "[yellow]Usage:[/yellow] folder create <name>\n"
                "  Example: folder create Production-West"
            )
            return

        name = name.strip()

        if not self._scm:
            console.print("[red]SCM not configured — cannot create folders.[/red]")
            return

        console.print("[dim]Fetching folder list…[/dim]", end="\r")
        folders = self._scm.get_folders_full()
        console.print(" " * 40, end="\r")

        if not folders:
            console.print("[yellow]No folders returned — cannot determine placement.[/yellow]")
            return

        # Build a flat ordered list: [(depth, name, full_path), …]
        flat = fmt._folder_flat_list(folders)

        # Display the numbered selection table.
        console.print(f"\n[bold]Creating folder:[/bold] [cyan]{name}[/cyan]\n")
        console.print(
            "[bold yellow]Select parent folder[/bold yellow]  "
            "[dim]('above' → pick a shorter path; 'below' → pick a deeper path)[/dim]\n"
        )

        # Header row
        console.print(f"  [dim]{'#':<5}{'Folder':<35}Path[/dim]")
        console.print("  " + "─" * 65)

        for i, (depth, fname, path) in enumerate(flat, start=1):
            indent   = "  " * depth
            name_col = f"{indent}{fname}"
            console.print(
                f"  [cyan]{i:<5}[/cyan]"
                f"[green]{name_col:<35}[/green]"
                f"[dim]{path}[/dim]"
            )

        console.print()

        # Prompt for the parent.
        try:
            raw = input("  Enter # or folder name for parent [Shared]: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return

        # Resolve selection to a folder name.
        parent_name = "Shared"  # sensible default
        if raw:
            if raw.isdigit():
                idx = int(raw) - 1
                if 0 <= idx < len(flat):
                    parent_name = flat[idx][1]
                else:
                    console.print(f"[red]Invalid number: {raw}  (valid range 1–{len(flat)})[/red]")
                    return
            else:
                # Accept a raw folder name too.
                known_names = {f[1] for f in flat}
                if raw in known_names:
                    parent_name = raw
                else:
                    console.print(
                        f"[red]Folder '{raw}' not found.[/red]\n"
                        "  Enter a number from the list or an exact folder name."
                    )
                    return

        # Confirm.
        console.print(
            f"\n  Create [bold cyan]{name}[/bold cyan] "
            f"inside [bold green]{parent_name}[/bold green]?"
        )
        try:
            confirm = input("  [y/n]: ").strip().lower()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return

        if confirm not in ("y", "yes"):
            console.print("[dim]Cancelled.[/dim]")
            return

        # Create via API.
        try:
            result       = self._scm.create_folder(name, parent_name)
            created_id   = result.get("id", "")
            created_name = result.get("name") or name
            console.print(
                f"\n[green]✓[/green] Folder [bold cyan]{created_name}[/bold cyan] created "
                f"inside [bold green]{parent_name}[/bold green]"
                + (f"  [dim](id: {created_id})[/dim]" if created_id else "")
            )
        except Exception as exc:
            console.print(f"[red]Failed to create folder:[/red] {exc}")
            return

        # Refresh folder cache so the new folder appears in completions immediately.
        self._refresh_folders(silent=True)
        total = len(self._state.folders_cache)
        console.print(
            f"[dim]Folder list refreshed — {total} folder(s) total.  "
            f"Use [bold]folder {created_name}[/bold] to switch into it.[/dim]"
        )

    # ------------------------------------------------------------------
    # Command: tsg
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------

    def _cmd_tsg(self, args: list[str]) -> None:
        """Switch the active Tenant Services Group (TSG) context.

        ARC authenticates to the parent / root TSG at startup.  Use this
        command to switch into a child TSG so that all subsequent API calls
        (devices, policy, addresses…) are scoped to that tenant.

        ARC re-authenticates automatically via OAuth to obtain a token
        scoped to the new TSG — no manual token management needed.

        Usage:
          tsg                  — show current TSG and list available child TSGs
          tsg <id>             — switch to the given TSG ID
        """
        if not args:
            active = self._state.tsg_id or self._config.scm.tsg_id or "(not set)"
            console.print(f"[cyan]Active TSG:[/cyan] [bold]{active}[/bold]")

            # Show cached child TSGs if available
            if self._state.tsgs_cache:
                console.print("\n[bold yellow]Available TSGs[/bold yellow]  "
                              "[dim](Tab after 'tsg ' to complete)[/dim]")
                for entry in self._state.tsgs_cache:
                    tsg_id = str(entry.get("id") or entry.get("tsg_id") or "")
                    name   = str(entry.get("display_name") or entry.get("name") or "")
                    marker = " [green]◀ active[/green]" if tsg_id == active else ""
                    console.print(f"  [cyan]{tsg_id:<20}[/cyan] {name}{marker}")
            else:
                console.print(
                    "[dim]No TSG list cached — ARC will attempt to fetch child TSGs.[/dim]"
                )
                self._refresh_tsgs(silent=False)
                if self._state.tsgs_cache:
                    console.print("\n[bold yellow]Available TSGs[/bold yellow]")
                    for entry in self._state.tsgs_cache:
                        tsg_id = str(entry.get("id") or entry.get("tsg_id") or "")
                        name   = str(entry.get("display_name") or entry.get("name") or "")
                        console.print(f"  [cyan]{tsg_id:<20}[/cyan] {name}")
                else:
                    console.print(
                        "[yellow]No child TSGs found.[/yellow]  "
                        "Your service account may only have access to "
                        f"TSG [bold]{active}[/bold] itself.\n"
                        "Use [bold]tsg <id>[/bold] to switch if you know the child TSG ID."
                    )
            return

        new_tsg = args[0].strip()
        if not new_tsg:
            console.print("[yellow]TSG ID cannot be blank.[/yellow]")
            return

        previous_tsg    = self._state.tsg_id
        previous_device = self._state.device
        previous_folder = self._state.folder
        has_client_creds = bool(
            self._config.scm.client_id and self._config.scm.client_secret
        )

        if not has_client_creds:
            # Bearer-token-only mode: we cannot mint a new token scoped to a
            # different TSG. Keep a local context switch so operators can still
            # organize state, but make it explicit that API visibility may not
            # actually change until re-auth with client credentials.
            self._state.tsg_id = new_tsg
            self._state.device = None
            self._state.folder = self._config.default_folder
            self._state.devices_cache = []
            self._state.folders_cache = ["Shared", "Global"]
            self._state.tsgs_cache = []
            self._refresh_devices(silent=True)
            self._refresh_folders(silent=True)
            self._refresh_tsgs(silent=True)
            console.print(
                f"[yellow]⚠[/yellow] Set active TSG to [bold]{new_tsg}[/bold] in bearer-token mode.\n"
                "  [dim]To fully re-scope API access, configure OAuth client credentials and restart ARC.[/dim]"
            )
            return

        # OAuth client credentials available — perform a real token re-scope.
        try:
            if not self._scm:
                self._scm = SCMClient(self._config.scm)
            self._scm.reauthenticate(new_tsg)

            # Commit new context
            self._state.tsg_id = new_tsg
            self._state.device = None
            self._state.folder = self._config.default_folder
            self._state.devices_cache = []
            self._state.folders_cache = ["Shared", "Global"]
            self._state.tsgs_cache = []

            # Refresh caches for the new tenant scope.
            self._refresh_devices(silent=True)
            self._refresh_folders(silent=True)
            self._refresh_tsgs(silent=True)

            console.print(
                f"[green]✓[/green] Switched active TSG to [bold]{new_tsg}[/bold]  "
                f"[dim]{len(self._state.devices_cache)} device(s), {len(self._state.folders_cache)} folder(s)[/dim]"
            )
            if not self._state.devices_cache:
                console.print(
                    "[yellow]No devices visible in this TSG.[/yellow]  "
                    "[dim]Use [bold]tsg[/bold] to list alternatives or verify account permissions.[/dim]"
                )

        except Exception as exc:
            # Roll back fully on failure so context is consistent.
            self._state.tsg_id = previous_tsg
            self._state.device = previous_device
            self._state.folder = previous_folder
            if self._scm:
                try:
                    self._scm.reauthenticate(previous_tsg or self._config.scm.tsg_id)
                except Exception:
                    pass
            console.print(
                f"[red]TSG switch failed:[/red] {exc}\n"
                f"[dim]Context restored to TSG {previous_tsg or self._config.scm.tsg_id}.[/dim]"
            )

    # ------------------------------------------------------------------
    # Command: account
    # ------------------------------------------------------------------

    def _cmd_account(self, args: list[str]) -> None:
        """List or switch named credential profiles.

        Profiles hold a separate set of SCM credentials (client_id, client_secret,
        tsg_id) stored under their own keychain entries.  A typical setup has a
        read-only profile for day-to-day monitoring and a read-write profile for
        making policy changes.

        Create profiles outside the shell with:
          arc auth login --profile <name>

        Usage:
          account               — list all profiles with active marker
          account <name>        — switch to the named profile
        """
        profiles = list_profiles()

        if not args:
            # List all configured profiles.
            active_name = self._config.profile_name

            if len(profiles) == 1 and profiles[0]["name"] == "default":
                p = profiles[0]
                client_id = p["client_id"] or "(not set)"
                tsg_id    = p["tsg_id"]    or "(not set)"
                console.print(
                    f"\n[cyan]Active account:[/cyan] [bold]{active_name}[/bold]\n"
                    f"  client_id : {client_id}\n"
                    f"  tsg_id    : {tsg_id}\n\n"
                    "[dim]Create additional profiles with: "
                    "[bold]arc auth login --profile <name>[/bold][/dim]"
                )
                return

            console.print(
                "\n[bold yellow]Credential Profiles[/bold yellow]  "
                "[dim](use [bold]account <name>[/bold] to switch)[/dim]\n"
            )
            for p in profiles:
                marker      = " [green]◀ active[/green]" if p["active"] else ""
                name_col    = f"[bold]{p['name']}[/bold]" if p["active"] else p["name"]
                client_id   = p["client_id"] or "[dim](not set)[/dim]"
                tsg_id      = p["tsg_id"]    or "[dim](not set)[/dim]"
                console.print(f"  {name_col:<22} {client_id:<55} {tsg_id}{marker}")
            return

        target       = args[0].strip()
        profile_names = [p["name"] for p in profiles]

        if target not in profile_names:
            console.print(
                f"[red]Profile '{target}' not found.[/red]\n"
                f"  Available: [bold]{', '.join(profile_names)}[/bold]\n"
                f"  Create it with: [bold]arc auth login --profile {target}[/bold]"
            )
            return

        if target == self._config.profile_name:
            p = next(p for p in profiles if p["name"] == target)
            console.print(
                f"[cyan]Already using profile:[/cyan] [bold]{target}[/bold]  "
                f"[dim](TSG: {p['tsg_id'] or 'n/a'})[/dim]"
            )
            return

        console.print(f"[dim]Loading profile '{target}'…[/dim]")

        previous_config = self._config
        previous_scm    = self._scm

        try:
            new_cfg = load_config(profile=target)
            new_cfg.debug = self._config.debug  # preserve session debug flag

            if new_cfg.scm.is_configured:
                new_scm: Optional[SCMClient] = SCMClient(new_cfg.scm)
            else:
                new_scm = None

            # Swap config and client atomically.
            self._config = new_cfg
            self._scm    = new_scm

            # Clear all context — new account = different TSG + devices.
            self._state.device         = None
            self._state.folder         = new_cfg.default_folder
            self._state.tsg_id         = new_cfg.scm.tsg_id
            self._state.devices_cache  = []
            self._state.folders_cache  = ["Shared", "Global"]
            self._state.tsgs_cache     = []

            # Persist the new active profile to disk so the next launch uses it.
            set_active_profile(target)

            if new_scm:
                console.print(f"[dim]Refreshing caches for profile '{target}'…[/dim]")
                self._refresh_devices(silent=True)
                self._refresh_folders(silent=True)
                self._refresh_tsgs(silent=True)

                device_count = len(self._state.devices_cache)
                client_id    = new_cfg.scm.client_id or "(bearer token)"
                console.print(
                    f"[green]✓[/green] Switched to profile [bold]{target}[/bold]  "
                    f"[dim]|  TSG:[/dim] [cyan]{new_cfg.scm.tsg_id}[/cyan]  "
                    f"[dim]{device_count} device(s)[/dim]"
                )
                if device_count == 0:
                    console.print(
                        "[yellow]No devices visible.[/yellow]  "
                        "[dim]Check your service account has Device Administrator access, "
                        "or use [bold]tsg <id>[/bold] to switch to a TSG with devices.[/dim]"
                    )
            else:
                console.print(
                    f"[yellow]⚠[/yellow] Switched to profile [bold]{target}[/bold] "
                    f"but SCM is not configured for this profile.\n"
                    f"  Run [bold]arc auth login --profile {target}[/bold] to add credentials."
                )

        except Exception as exc:
            # Roll back to the previous config on any failure.
            self._config = previous_config
            self._scm    = previous_scm
            console.print(
                f"[red]Failed to switch to profile '{target}':[/red] {exc}\n"
                f"[dim]Still using profile '{previous_config.profile_name}'.[/dim]"
            )

    # ------------------------------------------------------------------
    # Command: conf / configure
    # ------------------------------------------------------------------

    def _cmd_configure(self, args: list[str]) -> None:
        """Enter configure mode (Cisco-style)."""
        if args and args[0].lower() not in ("t", "terminal"):
            console.print(
                "[yellow]Usage:[/yellow] configure | conf | conf t\n"
                "  Then use [bold]cli[/bold] for CLI theme operations in configure mode."
            )
            return

        if self._state.configure_mode:
            console.print("[dim]Already in configure mode.[/dim]")
            return

        # Enter from a predictable base context: arc:global #
        self._state.configure_mode = True
        self._state.device = None
        self._state.folder = "Shared"
        console.print(
            "[green]Entered configure mode.  Write operations are enabled:[/green]"
        )
        console.print(
            "[dim]  cli show  |  cli color <key> <style>  |  cli reset[/dim]"
        )

    def _cmd_cli(self, args: list[str]) -> None:
        """Read/write CLI theme settings (configure mode only)."""
        if not self._state.configure_mode:
            console.print(
                "[yellow]Write operation blocked:[/yellow] enter [bold]configure[/bold] mode first.\n"
                "  Then use: [bold]cli show[/bold], [bold]cli color <key> <style>[/bold], [bold]cli reset[/bold]."
            )
            return

        t = self._theme
        sub = args[0].lower() if args else "show"

        if sub == "show":
            console.print()
            console.print("  [bold]ARC CLI Theme[/bold]  [dim](app/cli_theme.json)[/dim]")
            console.print()
            for key, label in THEME_KEYS.items():
                current = getattr(t, key)
                display = self._styled(f"  {current or '(none)'}  ", current) if current else "[dim](none)[/dim]"
                console.print(f"    [cyan]{key:<28}[/cyan] {display}  [dim]{label}[/dim]")
            console.print()
            console.print("  [dim]cli color <key> <style>  → change colour  |  cli reset  → defaults[/dim]")
            console.print()
            return

        if sub == "color":
            if len(args) < 2:
                console.print(
                    "[yellow]Usage:[/yellow] cli color <key> <style>\n"
                    f"  Keys: {', '.join(THEME_KEYS)}"
                )
                return
            key = args[1].lower()
            if not hasattr(self._theme, key):
                console.print(
                    f"[yellow]Unknown theme key:[/yellow] {key!r}\n"
                    f"  Valid keys: {', '.join(THEME_KEYS)}"
                )
                return
            style = " ".join(args[2:])
            setattr(self._theme, key, style)
            save_theme(self._theme)
            preview = self._styled(f"  {style or '(none)'}  ", style) if style else "[dim](none)[/dim]"
            console.print(f"[green]✓[/green] {key} = {preview}  [dim](saved to app/cli_theme.json)[/dim]")
            return

        if sub == "reset":
            self._theme = reset_theme()
            console.print("[green]✓[/green] Theme reset to defaults  [dim](saved to app/cli_theme.json)[/dim]")
            return

        console.print(
            f"[yellow]Unknown cli subcommand:[/yellow] {sub!r}\n"
            "  Usage: cli show | cli color <key> <style> | cli reset"
        )

    # ------------------------------------------------------------------
    # Command: help
    # ------------------------------------------------------------------

    def _cmd_help(self, args: list[str]) -> None:
        """Print the command reference.

        Bare `?` / `help` is always context-aware — commands are shown in three
        tiers (global → folder → device) so the operator sees what is available
        at the current navigation level, mirroring PAN-OS/Panorama CLI behaviour.

        `help all` always forces the full unfiltered reference.
        """
        if args and args[0].lower() != "all":
            topic = " ".join(args)
            if render_help_topic(console, topic):
                return
            console.print(
                f"[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
                "Type [bold]help commands[/bold] to see documented command topics."
            )
            return

        if args and args[0].lower() == "all":
            self._cmd_help_full()
        else:
            self._cmd_help_inline([])

    def _cmd_help_inline(self, prefix_tokens: list[str]) -> None:
        """Cisco-style compact inline help — one line per command, no panels.

        prefix_tokens empty  → 3-tier listing: global / folder / device / shell.
        prefix_tokens set    → all registered commands starting with that prefix.

        This is the `?` mode. It is intentionally compact and panel-free so
        operators get a fast visual scan — identical to how Cisco IOS presents
        context-sensitive completion help.
        """
        device = self._state.device
        folder = self._state.folder
        device_name = (
            (device.get("hostname") or device.get("name") or "device") if device else ""
        )
        t = self._theme  # shorthand

        if prefix_tokens:
            options = self._collapsed_prefix_help_options(prefix_tokens)
            if options:
                console.print()
                for token, desc in options:
                    token_cell = self._styled(f"{token:<20}", t.command_name)
                    if desc:
                        console.print(f"  {token_cell} {desc}")
                    else:
                        console.print(f"  {token_cell}")
                console.print()
                console.print(
                    f"  {self._styled('Use ? progressively: e.g. show jobs ? -> all | id', t.description_dim)}"
                )
            else:
                prefix = " ".join(prefix_tokens).lower()
                _builtin_names = {
                    "cd", "connect", "remote", "folder", "tsg", "configure",
                    "ls", "devices", "pwd", "docs", "help", "clear", "exit", "quit",
                }
                if prefix in _builtin_names:
                    console.print(
                        f"\n  {self._styled(prefix, t.command_name)}  is a shell built-in.  "
                        f"Type [bold]{prefix} help[/bold] for full docs.\n"
                    )
                else:
                    console.print(
                        f"\n  [yellow]No commands match:[/yellow] [bold]{prefix}[/bold]  "
                        "— type [bold]?[/bold] for the full command list.\n"
                    )
            return

        # --- Bare ? or help — compact 3-tier listing ---
        sh = t.section_header
        dd = t.description_dim

        console.print()

        # Tier 1: GLOBAL — collapsed to concise stems (e.g. `show jobs`).
        global_options = self._collapsed_tier_help_options(scope="global")
        if global_options:
            console.print(f"  {self._styled('GLOBAL', sh)}  {self._styled('— always available', dd)}")
            for token, desc in global_options:
                cmd_cell = self._styled(f"{token:<{_HELP_CMD_WIDTH}}", t.command_name)
                desc_text = self._styled(desc, t.description) if (desc and t.description) else desc
                console.print(f"    {cmd_cell} {desc_text}".rstrip())

        # Tier 2: FOLDER — collapsed to concise stems (e.g. `show address`).
        folder_options = self._collapsed_tier_help_options(scope="folder")
        if folder_options:
            if folder.lower() != "shared":
                folder_label = (
                    f"{self._styled('FOLDER', sh)}  "
                    f"{self._styled(f'— folder: {folder}', dd)}"
                )
            else:
                scope_hint = f"— folder: {folder}  (use 'folder <name>' to scope)"
                folder_label = (
                    f"{self._styled('FOLDER', sh)}  "
                    f"{self._styled(scope_hint, dd)}"
                )
            console.print(f"\n  {folder_label}")
            for token, desc in folder_options:
                cmd_cell = self._styled(f"{token:<{_HELP_CMD_WIDTH}}", t.command_name)
                desc_text = self._styled(desc, t.description) if (desc and t.description) else desc
                console.print(f"    {cmd_cell} {desc_text}".rstrip())

        # Tier 3: DEVICE — collapsed to concise stems.
        device_options = self._collapsed_tier_help_options(scope="device")
        if device_options:
            console.print(
                f"\n  {self._styled('DEVICE', sh)}  "
                f"{self._styled(f'— device: {device_name}', dd)}"
            )
            for token, desc in device_options:
                cmd_cell = self._styled(f"{token:<{_HELP_CMD_WIDTH}}", t.command_name)
                desc_text = self._styled(desc, t.description) if (desc and t.description) else desc
                console.print(f"    {cmd_cell} {desc_text}".rstrip())

        self._print_shell_builtins()

        console.print()
        console.print(
            f"  {self._styled('<command> help  → full docs page  |  help all        → complete reference', dd)}"
        )
        console.print()

    def _cmd_help_docs(self, topic: str) -> None:
        """Show the full documentation page for a command or topic.

        Resolution order:
        1. Render Markdown from docs/ when a matching file exists.
        2. Exact registry match — print inline description + context hint.
        3. Friendly fallback pointing the operator to ? or help all.

        Called by  `<command> help`  and  `help <topic>`.
        """
        # 1. Try docs/ Markdown page (covers commands, aliases, general topics).
        if render_help_topic(console, topic):
            return

        # 2. Exact registry match — print description inline.
        if topic in COMMANDS:
            cmd_def = COMMANDS[topic]
            api_note = (
                "  [dim](API only — no SSH equivalent)[/dim]"
                if cmd_def.ssh_command is None
                else "  [dim](API + SSH via --remote)[/dim]"
            )
            console.print(
                f"\n[bold cyan]{topic}[/bold cyan]  —  {cmd_def.description}{api_note}\n"
                "  Append [bold]--remote[/bold] to run via SSH instead of the SCM API.\n"
            )
            self._print_context_hint_for(topic)
            return

        # 3. Nothing found.
        console.print(
            f"\n[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
            "  Type [bold]?[/bold] for available commands  |  "
            "[bold]help all[/bold] for the full reference\n"
        )

    def _cmd_help_full(self) -> None:
        """Print the full command reference regardless of context."""
        console.print()
        console.print(Panel(
            "[bold cyan]ARC — Assisted Remote Console[/bold cyan]\n"
            "A PAN-OS-style interactive shell for Palo Alto Networks SCM environments.\n"
            "Commands are routed through SCM APIs by default.\n"
            "Use [bold]connect[/bold] or [bold]remote <device>[/bold] to open an\n"
            "interactive SSH session on a device.\n\n"
            "[dim]Scope tags:  (folder) → scoped to active folder  "
            "(device) → requires cd <device>  "
            "(global) → no context filtering[/dim]",
            title="Full Command Reference  (help all)", border_style="cyan",
        ))

        for category, keys in sorted(CATEGORIES.items()):
            console.print(f"\n[bold yellow]{category.upper()}[/bold yellow]")
            for k in sorted(keys):
                cmd = COMMANDS[k]
                scope_tag = (
                    "  [dim][global][/dim]" if cmd.scope == "global"
                    else "  [dim][device][/dim]" if cmd.scope == "device"
                    else ""
                )
                ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command else ""
                console.print(f"  [cyan]{k:<{_HELP_CMD_WIDTH + 2}}[/cyan] {cmd.description}{scope_tag}{ssh_note}")

        self._print_shell_builtins()
        console.print()

    def _print_shell_builtins(self) -> None:
        """Print the shell built-in commands section (shared by inline and full help)."""
        t = self._theme
        console.print(
            f"\n  {self._styled('SHELL', t.section_header)}  "
            f"{self._styled('— navigation & session', t.description_dim)}"
        )
        builtins = [
            ("cd <device>",           "Change Device in SCM  (Tab -> device list)"),
            ("connect <device>",      "SSH to device — interactive session  (returns to ARC on exit)"),
            ("remote <device>",       "SSH to named device — interactive session  (keyboard-interactive + 2FA)"),
            ("folder <name>",         "Set SCM Folder scope  (Tab -> folder list | folder .. -> Shared)"),
            ("folder create <name>",  "Create a new folder  (configure mode required)"),
            ("tsg <id>",              "Set active TSG  (Tab -> configured TSG)"),
            ("account <name>",        "List or switch credential profiles  (Tab -> profile names)"),
            ("configure",             "Enter configure mode  (arc:global #)"),
            ("cli <subcommand>",      "CLI theme operations in configure mode  (show | color | reset)"),
            ("ls",                    "List devices and refresh cache  (ls folder -> folder tree view)"),
            ("pwd",                   "Show device, folder, TSG, and active account"),
            ("docs",                  "Open docs in browser"),
            ("clear",                 "Clear the terminal screen"),
            ("exit / quit",           "Exit ARC"),
        ]
        if self._state.configure_mode:
            configure_only = {
                "folder create <name>",
                "cli <subcommand>",
                "exit / quit",
            }
            builtins = [b for b in builtins if b[0] in configure_only]
        for name, desc in builtins:
            # Configure-mode filtering keeps ? strictly context-aware.
            if name == "folder create <name>" and not self._state.configure_mode:
                continue
            if name == "cli <subcommand>" and not self._state.configure_mode:
                continue
            if name == "configure" and self._state.configure_mode:
                continue
            cmd_cell = self._styled(f"{name:<{_HELP_CMD_WIDTH}}", t.command_name)
            console.print(f"    {cmd_cell} {desc}")

    def _is_command_available(self, key: str, cmd_def: CommandDef) -> bool:
        """Return True when a registered command is executable in the current context."""
        if cmd_def.scope == "device" and not self._state.device:
            return False
        if key == "commit" and not self._state.configure_mode:
            return False
        return True

    @staticmethod
    def _is_config_command(key: str, cmd_def: CommandDef) -> bool:
        """Return True when a command should appear in configure-mode `?` help."""
        del cmd_def
        # Configure mode keeps write workflows and read-only show navigation.
        return key == "commit" or key.startswith("show ")

    def _collapsed_prefix_help_options(
        self,
        prefix_tokens: list[str],
        scope: Optional[str] = None,
    ) -> list[tuple[str, str]]:
        """Return collapsed next-token help options for a command prefix.

        This mirrors Cisco-style progressive help: users type a partial command
        and `?` shows only the next valid token(s) rather than every full command.
        """
        prefix = [p.lower() for p in prefix_tokens]

        option_map: dict[str, list[str]] = {}
        exact_matches: list[str] = []

        for key, cmd_def in COMMANDS.items():
            if scope is not None and cmd_def.scope != scope:
                continue
            if not self._is_command_available(key, cmd_def):
                continue
            if self._state.configure_mode and not self._is_config_command(key, cmd_def):
                continue

            cmd_tokens = key.split()
            if len(cmd_tokens) < len(prefix):
                continue
            if not all(cmd_tokens[i].startswith(prefix[i]) for i in range(len(prefix))):
                continue

            if len(cmd_tokens) == len(prefix):
                # Exact/full command completion (allow Enter now).
                if all(cmd_tokens[i] == prefix[i] for i in range(len(prefix))):
                    exact_matches.append(key)
                else:
                    # Same token count but current token still ambiguous (e.g. device -> devices).
                    token = cmd_tokens[-1]
                    option_map.setdefault(token, []).append(key)
                continue

            next_token = cmd_tokens[len(prefix)]
            option_map.setdefault(next_token, []).append(key)

        options: list[tuple[str, str]] = []
        if exact_matches:
            desc = COMMANDS[exact_matches[0]].description if len(exact_matches) == 1 else "Complete command"
            options.append(("<enter>", desc))

        for token in sorted(option_map):
            keys = option_map[token]
            # Use command description when token maps cleanly to one leaf command.
            desc = ""
            if len(keys) == 1:
                desc = COMMANDS[keys[0]].description
            options.append((token, desc))

        return options

    def _collapsed_tier_help_options(self, scope: str) -> list[tuple[str, str]]:
        """Return collapsed bare-tier help options for one scope.

        For multi-token commands, show a two-token stem so bare `?` is concise
        but still useful (e.g. `show jobs` instead of only `show`).
        """
        eligible: list[str] = []
        for key, cmd_def in COMMANDS.items():
            if cmd_def.scope != scope:
                continue
            if not self._is_command_available(key, cmd_def):
                continue
            if self._state.configure_mode and not self._is_config_command(key, cmd_def):
                continue
            eligible.append(key)

        if not eligible:
            return []

        stem_map: dict[str, list[str]] = {}
        for key in eligible:
            tokens = key.split()
            if len(tokens) >= 2:
                stem = " ".join(tokens[:2])
            else:
                stem = tokens[0]
            stem_map.setdefault(stem, []).append(key)

        options: list[tuple[str, str]] = []
        for stem in sorted(stem_map):
            keys = stem_map[stem]
            desc = ""
            if len(keys) == 1 and keys[0] == stem:
                desc = COMMANDS[keys[0]].description
            options.append((stem, desc))
        return options

    def _context_annotation(self, command_key: str) -> str:
        """Return a short inline context note for commands whose output depends on state.

        Folder-scope commands show the active folder.
        Device-scope commands show the active device when one is set.
        Returns an empty string when there is nothing context-specific to note.
        """
        device = self._state.device
        folder = self._state.folder

        cmd = COMMANDS.get(command_key)
        if not cmd:
            return ""

        if cmd.scope == "folder":
            return f"  [dim]→ folder: {folder}[/dim]"

        if cmd.scope == "device" and device:
            device_name = device.get("hostname") or device.get("name") or "device"
            return f"  [dim]→ device: {device_name}[/dim]"

        return ""

    def _print_context_hint_for(self, command_key: str) -> None:
        """Print a one-line context note below an exact-match docs result."""
        note = self._context_annotation(command_key)
        if note:
            console.print(f"[dim]Current context:[/dim]{note}")

    # ------------------------------------------------------------------
    # API execution
    # ------------------------------------------------------------------

    def _execute_api(self, key: str, cmd_def: CommandDef, args: dict) -> None:
        if key == "commit" and not self._state.configure_mode:
            console.print(
                f"[yellow]Write operation blocked:[/yellow] [bold]{key}[/bold] requires configure mode.\n"
                "  Enter [bold]configure[/bold] first, then retry."
            )
            return

        ctx = self._make_context()

        # Enforce scope declared on the CommandDef before calling the handler.
        if cmd_def.scope == "device" and not ctx.device:
            device_hint = (
                "Use [bold]cd <device>[/bold] to select a device first, "
                "then run this command again.\n"
                f"Or run [bold]{key} --remote <device>[/bold] to target a "
                "device directly without changing context.\n"
                "Tab after 'cd ' or '--remote ' to see available devices."
            )
            console.print(
                f"[yellow]'{key}'[/yellow] requires a device context  "
                f"[dim](scope: device)[/dim]\n  {device_hint}"
            )
            return

        if cmd_def.api_handler is None:
            console.print(f"[yellow]No API handler for '{key}'.[/yellow]")
            return

        data = cmd_def.api_handler(ctx, args)
        self._render(key, cmd_def, data)

    # ------------------------------------------------------------------
    # SSH (--remote) execution
    # ------------------------------------------------------------------

    def _execute_remote(self, key: str, cmd_def: CommandDef, args: dict) -> None:
        if cmd_def.ssh_command is None:
            console.print(
                f"[yellow]'{key}' has no SSH equivalent — it is a config/API-only command.[/yellow]\n"
                "Falling back to API path."
            )
            self._execute_api(key, cmd_def, args)
            return

        device = self._state.device
        if not device:
            console.print(
                "[red]--remote requires a device context.[/red] "
                "Use [bold]cd <device>[/bold] first."
            )
            return

        host = str(device.get("ip_address") or device.get("hostname") or "")
        if not host:
            console.print("[red]Cannot determine device IP/hostname for SSH.[/red]")
            return

        ssh_cmd = self._resolve_ssh_command(cmd_def, args)

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)
        console.print(
            f"[dim]SSH → {ssh_user}@{host}:{ssh_port}  cmd: {ssh_cmd}[/dim]"
        )

        output = self._ssh.execute(
            host=host,
            command=ssh_cmd,
            user=ssh_user,
            key_path=ssh_key_path,
            password=ssh_password,
            port=ssh_port,
        )
        console.print(fmt.format_raw(output, title=f"SSH: {key}"))

    def _resolve_ssh_command(self, cmd_def: CommandDef, args: dict) -> str:
        """Return the concrete SSH command string for a registered command."""
        ssh_command = cmd_def.ssh_command
        if ssh_command is None:
            raise RuntimeError("Command has no SSH equivalent.")
        if isinstance(ssh_command, str):
            return ssh_command
        return ssh_command(args)

    # ------------------------------------------------------------------
    # Rendering
    # ------------------------------------------------------------------

    def _render(self, key: str, cmd_def: CommandDef, data) -> None:  # noqa: C901
        render_hint = cmd_def.render

        # Unwrap log tuple
        if render_hint == "logs" and isinstance(data, tuple):
            log_type, rows = data
            if isinstance(rows, list):
                console.print(fmt.format_logs(rows, log_type=log_type))
            else:
                console.print(fmt.format_raw(str(rows), title=key))
            return

        # XML element fallback — ET is imported at module level
        if isinstance(data, ET.Element):
            raw = ET.tostring(data, encoding="unicode")
            console.print(fmt.format_raw(raw, title=key))
            return

        if isinstance(data, str):
            console.print(fmt.format_raw(data, title=key))
            return

        # If the handler embedded a _render override key (e.g. snippet_detail_full
        # returned from show snippet <name> details), honour it BEFORE consulting
        # the dispatch table — otherwise cmd_def.render would call the wrong formatter.
        if isinstance(data, dict) and "_render" in data:
            render_hint = data["_render"]
        else:
            render_hint = cmd_def.render

        dispatch = {
            "system_info":     lambda d: fmt.format_system_info(d),
            "raw":             lambda d: fmt.format_raw(str(d), title=key),
            "devices":         lambda d: fmt.format_devices(d),
            "device_detail":   lambda d: fmt.format_device_detail(
                                   d.get("device", d) if isinstance(d, dict) else d),
            "device_snippets": lambda d: fmt.format_snippets(
                                   d.get("snippets", []) if isinstance(d, dict) else d,
                                   device_filter=d.get("device_name", "") if isinstance(d, dict) else ""),
            "snippets":        lambda d: fmt.format_snippets(d if isinstance(d, list) else []),
            "snippets_scoped": lambda d: fmt.format_snippets_scoped(d if isinstance(d, dict) else {}),
            "snippet_detail":  lambda d: fmt.format_snippet_detail(d if isinstance(d, dict) else {}) or [],
            "snippet_detail_full": lambda d: fmt.format_snippet_detail_full(d if isinstance(d, dict) else {}) or [],
            "interfaces":      lambda d: fmt.format_interfaces(d),
            "routes":          lambda d: fmt.format_routes(d),
            "security_policy": lambda d: fmt.format_security_policy(d),
            "jobs":            lambda d: fmt.format_jobs(d),
            "logs":            lambda d: fmt.format_logs(d),
            "address_objects": lambda d: fmt.format_address_objects(d),
            "address_groups":  lambda d: fmt.format_address_groups(d),
            "services":        lambda d: fmt.format_services(d),
            "tags":            lambda d: fmt.format_tags(d if isinstance(d, list) else []),
            "edl_list":        lambda d: fmt.format_edl_list(d if isinstance(d, list) else []),
            "url_categories":  lambda d: fmt._list_table(d if isinstance(d, list) else [], title="URL Categories"),
            "zones":           lambda d: fmt.format_zones(d),
            "ha":              lambda d: fmt.format_ha(d, title=key),
            "dict":            lambda d: fmt.format_dict(d, title=key),
        }
        renderer = dispatch.get(render_hint)
        if renderer:
            result = renderer(data)
            # format_snippet_detail returns a list of renderables; others return one.
            if isinstance(result, list):
                for renderable in result:
                    console.print(renderable)
            else:
                console.print(result)
        elif isinstance(data, list):
            if data and isinstance(data[0], dict):
                console.print(fmt._list_table(data, title=key))
            else:
                for item in data:
                    console.print(item)
        elif isinstance(data, dict):
            console.print(fmt.format_dict(data, title=key))
        else:
            console.print(fmt.format_raw(str(data), title=key))

    # ------------------------------------------------------------------
    # Context factory
    # ------------------------------------------------------------------

    def _make_context(self) -> ExecutionContext:
        return ExecutionContext(
            scm=self._scm,
            ssh=self._ssh,
            config=self._config,
            device=self._state.device,
            folder=self._state.folder,
            tsg_id=self._state.tsg_id,
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    @staticmethod
    def _styled(text: str, style: str) -> str:
        """Wrap *text* in a Rich markup tag for *style*.

        Returns plain *text* when *style* is empty so that callers don't need
        to special-case the no-style case themselves.
        """
        if not style:
            return text
        return f"[{style}]{text}[/{style}]"

    def _cleanup(self) -> None:
        self._ssh.close_all()
        if self._scm:
            self._scm.close()
        console.print(f"\n[cyan]{self._random_goodbye_message()}[/cyan]")

    @staticmethod
    def _random_goodbye_message() -> str:
        """Return a random goodbye line from app/goodbye.txt.

        Ignores blank lines and comment lines that start with '##'.
        Falls back to a plain Goodbye when the file is missing or empty.
        """
        try:
            raw = GOODBYE_FILE.read_text(encoding="utf-8")
        except OSError:
            return "Goodbye."

        lines = [
            line.strip()
            for line in raw.splitlines()
            if line.strip() and not line.strip().startswith("##")
        ]
        if not lines:
            return "Goodbye."
        return random.choice(lines)

    def _print_banner(self) -> None:
        # banner.txt lives in app/ alongside the source code.
        # It uses Rich markup tags for colour — edit it to change the logo,
        # subtitle, or add a legal notice.  Lines starting with ## are comments.
        # The theme's banner_logo / banner_subtitle keys are the DEFAULT styles
        # written into a fresh banner.txt, but the file is the single source of
        # truth — change colours there, not here.
        _BANNER_FILE = Path(__file__).parent / "banner.txt"
        try:
            raw = _BANNER_FILE.read_text(encoding="utf-8")
        except OSError:
            raw = ""

        content = "\n".join(
            line for line in raw.splitlines() if not line.startswith("##")
        )

        console.print(content)

        # Show active profile when multiple profiles exist — so operators
        # always know which credential set is in use before touching anything.
        profiles = list_profiles()
        if len(profiles) > 1:
            active_name = self._config.profile_name
            console.print(
                f"  [dim]Account:[/dim] [bold]{active_name}[/bold]  "
                f"[dim](use [bold]account <name>[/bold] to switch)[/dim]\n"
            )

    def _print_startup_help(self) -> None:
        """Print compact startup command hints shown after SCM connection status."""

        # Alignment: 2-space indent, descriptions all start at visual col 28.
        # Spaces after [/cyan] = 28 − 2 − len(visible command text):
        #   cd <device>    11 → 15 sp   remote <device> 16 → 10 sp
        #   connect         7 → 19 sp   folder <name>   13 → 13 sp
        #   account <name> 14 → 12 sp   ?                1 → 25 sp
        console.print(
            "  [cyan]cd <device>[/cyan]               Change Device in SCM  [dim](Tab → device list)[/dim]\n"
            "  [cyan]remote <device>[/cyan]           SSH to device  [dim](keyboard-interactive + 2FA)[/dim]\n"
            "  [cyan]connect[/cyan]                   SSH to current device\n"
            "  [cyan]folder <name>[/cyan]             Set SCM Folder  [dim](Tab → folder list | always shown in prompt)[/dim]\n"
            "  [cyan]account <name>[/cyan]            List / switch credential profiles\n"
            "  [cyan]?[/cyan]                         Context-aware help  [dim](or  help <topic>)[/dim]"
        )
        console.print()
