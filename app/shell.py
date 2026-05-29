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

        # ---- show snippet <name> → snippet name completion ----
        if text.lower().startswith("show snippet ") and len(parts) >= 2:
            partial_name = parts[2] if len(parts) > 2 else ""
            # Use device snippets if in device context, else all
            device = self._shell._state.device
            if device and device.get("snippets"):
                candidates = device.get("snippets") or []
            else:
                candidates = [s.get("name", "") for s in getattr(self._shell, "_snippets_cache", [])]
                if not candidates:
                    # Fall back to device caches' snippet union
                    seen: set[str] = set()
                    for d in self._shell._state.devices_cache:
                        for sn in (d.get("snippets") or []):
                            seen.add(sn)
                    candidates = sorted(seen)
            for name in candidates:
                if name.lower().startswith(partial_name.lower()):
                    yield Completion(name, start_position=-len(partial_name))
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
            "folder", "tsg",
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
                console.print(
                    f"[green]✓[/green] SCM connected  "
                    f"[dim](TSG {self._config.scm.tsg_id})[/dim]"
                )
            except Exception as exc:
                console.print(f"[yellow]⚠[/yellow] SCM unavailable: {exc}")

        if not self._scm:
            console.print(
                "[yellow]⚠  No API backend configured.[/yellow] "
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

        # Report what was actually loaded so users know their access level.
        parts: list[str] = []
        if self._state.devices_cache:
            parts.append(f"{len(self._state.devices_cache)} device(s)")
        if self._state.folders_cache and self._state.folders_cache != ["Shared", "Global"]:
            parts.append(f"{len(self._state.folders_cache)} folder(s)")
        if self._state.tsgs_cache:
            parts.append(f"{len(self._state.tsgs_cache)} TSG(s)")

        if parts:
            console.print(f"[dim]Loaded: {', '.join(parts)}[/dim]")
        else:
            console.print(
                "[dim]API connected — device/folder list not available with this service "
                "account role (policy commands will still work)[/dim]"
            )

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

        if cmd == "tsg":
            self._cmd_tsg(tokens[1:])
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
        `remote <device>` to open an interactive SSH session.
        """
        if not args or args[0] in ("..", "/"):
            self._state.device = None
            console.print("[cyan]Device context cleared.[/cyan] SCM / global")
            return


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
        # Treat 'connect help' / 'connect ?' as a help request, not a hostname.
        if args and args[0].lower() in ("help", "?"):
            self._cmd_context_help(["connect"])
            return

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

    def _cmd_devices(self) -> None:
        """Context-aware ls/devices command.

        At root (no device selected) → refresh and show the device list.
        In device context (after cd <device>) → show that device's detail
        and its attached snippets.
        """
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
        console.print(f"[bold cyan]SCM folder:[/bold cyan] {self._state.folder}")
        active_tsg = self._state.tsg_id or "(root / config default)"
        console.print(f"[bold cyan]TSG:[/bold cyan] {active_tsg}")

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
    # Command: tsg
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

        previous_tsg = self._state.tsg_id
        has_client_creds = bool(
            self._config.scm.client_id and self._config.scm.client_secret
        )

        if not has_client_creds:
            # Bearer-token-only mode: just record the context change.
            # The token covers all TSGs it was issued for; SCM enforces access.
            self._state.tsg_id = new_tsg
            console.print(
                f"[cyan]TSG context set to:[/cyan] [bold]{new_tsg}[/bold]\n"
                "[dim]Bearer token used as-is — SCM enforces TSG-level access.[/dim]"
            )
            return

        # OAuth mode: re-authenticate with the new TSG scope so every subsequent
        # API call carries a token that explicitly claims this TSG.
        console.print(f"[dim]Re-authenticating with TSG {new_tsg}…[/dim]")
        self._state.tsg_id = new_tsg
        try:
            if self._scm:
                self._scm.reauthenticate(new_tsg)
            else:
                # SCM client was never initialised — build it now.
                import copy  # Deferred: avoids import at module level
                new_scm_cfg = copy.copy(self._config.scm)
                new_scm_cfg.tsg_id = new_tsg
                self._scm = SCMClient(new_scm_cfg)

            # Refresh caches for the new TSG context
            console.print(f"[dim]Refreshing device and folder lists for TSG {new_tsg}…[/dim]")
            self._refresh_devices(silent=True)
            self._refresh_folders(silent=True)
            self._refresh_tsgs(silent=True)

            console.print(
                f"[green]✓[/green] Switched to TSG [bold]{new_tsg}[/bold]  "
                f"({len(self._state.devices_cache)} device(s) visible)"
            )
        except Exception as exc:
            # Roll back so a failed switch doesn't strand the user.
            self._state.tsg_id = previous_tsg
            if self._scm:
                # Restore the old token by re-authing back to the previous TSG.
                try:
                    self._scm.reauthenticate(previous_tsg or self._config.scm.tsg_id)
                except Exception:
                    pass
            console.print(
                f"[red]TSG switch failed:[/red] {exc}\n"
                f"[dim]TSG context restored to {previous_tsg or self._config.scm.tsg_id}.[/dim]"
            )

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
            "Use [bold]connect[/bold] or [bold]remote <device>[/bold] to open an\n"
            "interactive SSH session on a device.",
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
            ("tsg <id>",              "Set the active TSG (Tenant Services Group)  [dim](Tab → configured TSG)[/dim]"),
            ("ls",                    "List devices (root) or device detail + snippets (in device context)"),
            ("pwd",                   "Show current device, SCM folder, and active TSG"),
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
            "ls", "devices", "pwd", "folder", "tsg", "clear", "help", "docs",
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
            "device_detail":   lambda d: fmt.format_device_detail(
                                   d.get("device", d) if isinstance(d, dict) else d),
            "device_snippets": lambda d: fmt.format_snippets(
                                   d.get("snippets", []) if isinstance(d, dict) else d,
                                   device_filter=d.get("device_name", "") if isinstance(d, dict) else ""),
            "snippets":        lambda d: fmt.format_snippets(d if isinstance(d, list) else []),
            "snippet_detail":  lambda d: fmt.format_snippet_detail(d if isinstance(d, dict) else {}),
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
            # Check for the sentinel _render key used by some handlers
            if "_render" in data:
                sentinel_render = data["_render"]
                r = dispatch.get(sentinel_render)
                if r:
                    console.print(r(data))
                    return
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
