"""Interactive REPL shell for ARC — Assisted Remote Console."""

from __future__ import annotations

import os
import select
import shutil
import signal
import sys
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
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
from app.commands.registry import (
    COMMANDS,
    CATEGORIES,
    CommandDef,
    ExecutionContext,
    match_command,
)
from app.config import ArcConfig
from app.docs import available_help_topics, open_docs_in_browser, render_help_topic
from app.ssh.manager import SSHManager
from app.utils import formatter as fmt

console = Console()

HISTORY_FILE = os.path.join(platformdirs.user_data_dir("arc"), "history")


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

        # ---- folder → SCM folder name completion ----
        if first == "folder" and has_arg_space:
            for folder in self._shell._state.folders_cache:
                if folder.lower().startswith(partial_arg.lower()):
                    yield Completion(folder, start_position=-len(partial_arg))
            return

        # ---- help → command/topic completion ----
        if first == "help" and has_arg_space:
            partial_topic = " ".join(parts[1:]).lower()
            for topic in available_help_topics():
                if topic.startswith(partial_topic):
                    yield Completion(topic[len(partial_topic):], start_position=-len(partial_topic))
            return

        # ---- Default: ARC command + built-in completion ----
            return

        # ---- Default: ARC command + built-in completion ----
        include_remote_suffix = " --" in text
        for name in sorted(self._all_commands(include_remote_suffix=include_remote_suffix)):
            if name.startswith(text):
                yield Completion(name[len(text):], start_position=0)

    def _all_commands(self, include_remote_suffix: bool) -> list[str]:
        builtins = [
            "cd", "remote", "connect", "docs",
            "ls", "devices", "pwd",
            "folder",
            "clear", "exit", "quit",
            "help", "?",
        ]
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
    devices_cache: list[dict] = field(default_factory=list)
    # SCM folder names cached at startup for tab completion
    folders_cache: list[str] = field(default_factory=lambda: ["Shared", "Global"])


class ArcShell:
    """Main interactive REPL."""

    def __init__(self, config: ArcConfig) -> None:
        self._config = config
        self._state = ShellState(folder=config.default_folder)
        # Prefix to restore in the next prompt after a '?' context-help lookup.
        # e.g. "show ?" prints help then re-seeds the prompt with "show ".
        self._pending_default: str = ""

        # Build clients
        self._scm: Optional[SCMClient] = None
        self._ssh = SSHManager()

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
                console.print("[green]✓[/green] Connected to Strata Cloud Manager")
            except Exception as exc:
                console.print(f"[yellow]⚠[/yellow] SCM unavailable: {exc}")

        if not self._scm:
            console.print(
                "[yellow]⚠  No API backend configured.[/yellow] "
                "Commands will fail unless you use [bold]remote <device>[/bold] or "
                "[bold]--remote[/bold] with SSH credentials, "
                "or set SCM_BEARER_TOKEN / SCM_CLIENT_ID credentials and restart.\n"
                "Run [bold]help config[/bold] to see configuration options."
            )
            return

        # Pre-populate caches so Tab completion works immediately on first keystroke
        console.print("[dim]Loading device list...[/dim]", end="\r")
        self._refresh_devices(silent=True)
        if self._scm:
            self._refresh_folders(silent=True)
        # Clear the loading line
        console.print(" " * 30, end="\r")

    # ------------------------------------------------------------------
    # Prompt
    # ------------------------------------------------------------------

    def _prompt(self) -> HTML:
        if self._state.device:
            name = self._state.device.get("hostname") or self._state.device.get("name") or "device"
            return HTML(f"<arc>arc</arc><sep>:</sep><device>{name}</device><arrow> > </arrow>")
        return HTML("<arc>arc</arc><arrow> > </arrow>")

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def run(self) -> None:
        self._print_banner()
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

        # Context-sensitive help: trailing '?' means "what can I do here?"
        # e.g.  "show address ?"  → scoped help for 'show address'
        #        "show ?"         → list every command that starts with 'show'
        #        "?"              → full command reference (existing behaviour)
        if "?" in tokens:
            question_idx = tokens.index("?")
            prefix_tokens = tokens[:question_idx]
            if prefix_tokens:
                # Restore the prefix in the next prompt so the user can keep typing.
                self._pending_default = " ".join(prefix_tokens) + " "
                self._cmd_context_help(prefix_tokens)
                return False
            # Fall through so the existing `cmd in ("help", "?")` branch fires

        cmd = tokens[0].lower()

        # ---- exit / quit ----
        if cmd in ("exit", "quit"):
            return True


        # ---- Shell built-ins ----
        if cmd == "clear":
            console.clear()
            return False

        if cmd == "pwd":
            self._cmd_pwd()
            return False

        if cmd in ("ls", "devices"):
            self._cmd_devices()
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

        if cmd in ("help", "?"):
            self._cmd_help(tokens[1:])
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
        `remote <device>` for SSH passthrough.
        """
        if not args or args[0] in ("..", "/"):
            self._state.device = None
            self._state.ssh_mode = False
            console.print("[cyan]Device context cleared.[/cyan] SCM / global")
            return

        # Entering a new device context always drops SSH mode
        self._state.ssh_mode = False

        target = " ".join(args)
        if not self._state.devices_cache:
            self._refresh_devices()

        match = self._find_device(target)
        if match:
            self._state.device = match
            name = match.get("hostname") or match.get("name") or target
            console.print(
                f"[cyan]SCM device:[/cyan] [bold]{name}[/bold]  "
                f"serial: {match.get('serial', 'n/a')}  "
                f"ip: {match.get('ip_address', 'n/a')}"
            )
        else:
            console.print(
                f"[yellow]Device '{target}' not found in cache.[/yellow] "
                "Creating a stub — run [bold]ls[/bold] to refresh the device list."
            )
            self._state.device = {
                "name": target,
                "hostname": target,
                "ip_address": target,
                "serial": "",
            }

    def _find_device(self, query: str) -> Optional[dict]:
        q = query.lower()
        for d in self._state.devices_cache:
            if (
                (d.get("hostname") or "").lower() == q
                or (d.get("name") or "").lower() == q
                or (d.get("serial") or "").lower() == q
                or (d.get("ip_address") or "").lower() == q
            ):
                return d
        return None

    def _refresh_devices(self, silent: bool = False) -> None:
        """Fetch managed devices and populate the cache used by tab completion and cd."""
        try:
            ctx = self._make_context()
            if ctx.scm:
                self._state.devices_cache = ctx.scm.get_devices(folder=self._state.folder)
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

    # ------------------------------------------------------------------
    # Command: connect  (SSH passthrough mode)
    # ------------------------------------------------------------------

    def _cmd_connect(self, args: list[str], require_target: bool = False) -> None:
        """Connect to a device via SSH and hand the terminal over to the remote shell.

        This is a true PTY session — ARC steps out of the way completely.
        Every keystroke goes directly to the device; every byte from the device
        is written straight to stdout.  ARC command dispatch is bypassed for the
        duration.  When the user types 'exit' on the device the SSH channel closes
        and ARC's prompt reappears.

        ``connect``              — SSH to the current ``cd`` device.
        ``remote <device>``      — SSH to a named device (also sets device context).
        """
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

        if args:
            target = " ".join(args)
            if not self._state.devices_cache:
                self._refresh_devices()
            match = self._find_device(target)
            if match:
                self._state.device = match
                name = match.get("hostname") or match.get("name") or target
            else:
                console.print(
                    f"[yellow]Device '{target}' not found in cache — using as hostname/IP directly.[/yellow]"
                )
                self._state.device = {
                    "name": target, "hostname": target,
                    "ip_address": target, "serial": "",
                }
                name = target
        else:
            name = self._state.device.get("hostname") or self._state.device.get("name") or "device"

        host = self._state.device.get("ip_address") or self._state.device.get("hostname") or ""
        if not host:
            console.print("[red]Cannot determine SSH target — no IP or hostname for this device.[/red]")
            return

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)

        # Pre-flight: if no auth method at all, prompt now so the user knows
        # what's happening before the connection attempt starts.
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

    def _cmd_devices(self) -> None:
        """Refresh and display the managed device list."""
        self._refresh_devices()
        if not self._state.devices_cache:
            console.print("[yellow]No devices found or API not configured.[/yellow]")
            return
        table = fmt.format_devices(self._state.devices_cache)
        console.print(table)

    # ------------------------------------------------------------------
    # Command: pwd
    # ------------------------------------------------------------------

    def _cmd_pwd(self) -> None:
        """Show current device context, active SCM folder, and SSH credential status."""
        if self._state.device:
            name = self._state.device.get("hostname") or self._state.device.get("name")
            serial = self._state.device.get("serial") or "n/a"
            ip = self._state.device.get("ip_address") or "n/a"
            console.print(
                f"[bold cyan]Device:[/bold cyan] {name}  "
                f"serial: {serial}  ip: {ip}  [API mode]"
            )
        else:
            console.print("[bold cyan]Context:[/bold cyan] SCM / global  [API mode]")
        console.print(f"[bold cyan]SCM folder:[/bold cyan] {self._state.folder}")

    # ------------------------------------------------------------------
    # Command: folder
    # ------------------------------------------------------------------

    def _cmd_folder(self, args: list[str]) -> None:
        if not args:
            console.print(f"[cyan]Current SCM folder:[/cyan] {self._state.folder}")
            return
        self._state.folder = args[0]
        console.print(f"[cyan]SCM folder set to:[/cyan] {self._state.folder}")

    # ------------------------------------------------------------------
    # Command: help
    # ------------------------------------------------------------------

    def _cmd_help(self, args: list[str]) -> None:

        if args:
            topic = " ".join(args)
            if render_help_topic(console, topic):
                return
            console.print(
                f"[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
                "Type [bold]help commands[/bold] to see documented command topics."
            )
            return

        console.print()
        console.print(Panel(
            "[bold cyan]ARC — Assisted Remote Console[/bold cyan]\n"
            "A PAN-OS-style interactive shell for Palo Alto Networks SCM environments.\n"
            "Commands are routed through SCM APIs by default.\n"
            "Use [bold]remote <device>[/bold] for SSH passthrough, or [bold]connect[/bold]\n"
            "after [bold]cd <device>[/bold] to SSH into the current device.",
            title="Help  (? also works)", border_style="cyan",
        ))

        # Registered commands grouped by category
        for category, keys in sorted(CATEGORIES.items()):
            console.print(f"\n[bold yellow]{category.upper()}[/bold yellow]")
            for k in sorted(keys):
                desc = COMMANDS[k].description
                ssh_note = " [dim](API only)[/dim]" if COMMANDS[k].ssh_command is None else ""
                console.print(f"  [cyan]{k:<45}[/cyan] {desc}{ssh_note}")

        # Shell built-ins
        console.print("\n[bold yellow]SHELL[/bold yellow]")
        builtins = [
            ("cd <device>",           "Change Device in SCM"),
            ("connect [device]",      "SSH to device — full interactive session  [dim](returns to ARC on exit)[/dim]"),
            ("remote <device>",       "SSH to device — full interactive session  [dim](also sets device context)[/dim]"),
            ("folder <name>",         "Set the SCM Folder  [dim](Tab → available folders)[/dim]"),
            ("ls",                    "List managed devices under the current folder"),
            ("pwd",                   "Show current device and SCM folder"),
            ("docs / docs <command>", "Show Documentation  [dim]docs <command> shows help in shell[/dim]"),
            ("? / help",              "Print this command reference"),
            ("help <topic>",          "Open topic doc  [dim]e.g. help config, help config osx|win|nix[/dim]"),
            ("help config",           "Configuration overview  [dim](osx / win / nix for platform guides)[/dim]"),
            ("clear",                 "Clear the terminal screen"),
            ("exit / quit",           "Exit ARC"),
        ]
        for name, desc in builtins:
            console.print(f"  [cyan]{name:<45}[/cyan] {desc}")
        console.print()


    def _cmd_context_help(self, prefix_tokens: list[str]) -> None:
        """Show scoped help for a partial command prefix typed before '?'.

        Behaviour mirrors the PAN-OS CLI convention:
        - Exact registry match  → render its doc page (description + Markdown)
        - Partial prefix match  → list every command that begins with the prefix
        - Shell built-in        → render its doc page
        - No match anywhere     → friendly fallback to the full command list
        """
        prefix = " ".join(prefix_tokens).lower()

        # 1. Exact match in the command registry — show its full doc page.
        if prefix in COMMANDS:
            if render_help_topic(console, prefix):
                return
            # Doc file missing — fall back to showing description inline.
            cmd_def = COMMANDS[prefix]
            ssh_note = (
                "  [dim](API only — no SSH equivalent)[/dim]"
                if cmd_def.ssh_command is None
                else ""
            )
            console.print(
                f"\n[bold cyan]{prefix}[/bold cyan]  —  {cmd_def.description}{ssh_note}\n"
                "  Append [bold]--remote[/bold] to run via SSH instead of the SCM API.\n"
            )
            return

        # 2. Try to render a doc page by topic name (covers aliases / general topics).
        if render_help_topic(console, prefix):
            return

        # 3. Partial prefix: list every registered command that begins with the prefix.
        matches = sorted(k for k in COMMANDS if k.startswith(prefix))
        if matches:
            console.print(
                f"\n[bold yellow]Commands matching[/bold yellow] "
                f"'[cyan]{prefix}[/cyan]':\n"
            )
            for k in matches:
                cmd_def = COMMANDS[k]
                ssh_note = " [dim](API only)[/dim]" if cmd_def.ssh_command is None else ""
                console.print(f"  [cyan]{k:<45}[/cyan] {cmd_def.description}{ssh_note}")
            console.print()
            return

        # 4. Shell built-ins (cd, remote, connect, …) — render their doc page.
        _shell_topic_keys = {
            "cd", "remote", "connect", "exit", "quit",
            "ls", "devices", "pwd", "folder", "clear", "help", "docs",
        }
        if prefix in _shell_topic_keys:
            if render_help_topic(console, prefix):
                return

        # 5. Nothing matched — point the user to the full reference.
        console.print(
            f"[yellow]No help found for:[/yellow] [bold]{prefix}[/bold]  "
            "— type [bold]?[/bold] for the full command list."
        )

    # ------------------------------------------------------------------
    # API execution
    # ------------------------------------------------------------------

    def _execute_api(self, key: str, cmd_def: CommandDef, args: dict) -> None:
        ctx = self._make_context()
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

        dispatch = {
            "system_info":     lambda d: fmt.format_system_info(d),
            "raw":             lambda d: fmt.format_raw(str(d), title=key),
            "devices":         lambda d: fmt.format_devices(d),
            "interfaces":      lambda d: fmt.format_interfaces(d),
            "routes":          lambda d: fmt.format_routes(d),
            "security_policy": lambda d: fmt.format_security_policy(d),
            "jobs":            lambda d: fmt.format_jobs(d),
            "logs":            lambda d: fmt.format_logs(d),
            "address_objects": lambda d: fmt.format_address_objects(d),
            "address_groups":  lambda d: fmt.format_address_groups(d),
            "services":        lambda d: fmt.format_services(d),
            "zones":           lambda d: fmt.format_zones(d),
            "ha":              lambda d: fmt.format_ha(d, title=key),
            "dict":            lambda d: fmt.format_dict(d, title=key),
        }
        renderer = dispatch.get(render_hint)
        if renderer:
            result = renderer(data)
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
        )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def _cleanup(self) -> None:
        self._ssh.close_all()
        if self._scm:
            self._scm.close()
        console.print("\n[cyan]Goodbye.[/cyan]")

    def _print_banner(self) -> None:
        # Compact ASCII art — Unicode block characters used verbatim to avoid Rich markup.
        art = (
            "\n"
            "      \u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2588\u2588\u2588\u2588\u2557   \u2588\u2588\u2588\u2588\u2588\u2588\u2557\n"
            "     \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557 \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557 \u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\n"
            "     \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551 \u2588\u2588\u2588\u2588\u2588\u2588\u2554\u255d \u2588\u2588\u2551\n"
            "     \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2551 \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557 \u2588\u2588\u2551\n"
            "     \u2588\u2588\u2551  \u2588\u2588\u2551 \u2588\u2588\u2551  \u2588\u2588\u2551 \u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2557\n"
            "     \u255a\u2550\u255d  \u255a\u2550\u255d \u255a\u2550\u255d  \u255a\u2550\u255d  \u255a\u2550\u2550\u2550\u2550\u2550\u255d\n"
        )
        console.print()
        console.print(f"[bold cyan]{art}[/bold cyan]")
        console.print()
        console.print(
            "  [cyan]cd <device>[/cyan]               Change Device in SCM  [dim](Tab → device list)[/dim]\n"
            "  [cyan]remote <device>[/cyan]           SSH Passthrough to device\n"
            "  [cyan]connect <device>[/cyan]          SSH Connect to device\n"
            "  [cyan]folder <name>[/cyan]             Set SCM Folder  [dim](Tab → folder list)[/dim]\n"
            "  [cyan]?[/cyan]                         List all commands"
        )
        console.print()
