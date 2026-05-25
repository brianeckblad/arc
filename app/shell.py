"""Interactive REPL shell for ARC — Assisted Remote Console."""

from __future__ import annotations

import os
import traceback
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from typing import Optional

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
    - In SSH mode              → completes with common PAN-OS CLI commands
    - Otherwise               → completes with ARC command names + shell built-ins
    """

    # Common PAN-OS CLI commands offered when in SSH passthrough mode
    _SSH_HINTS = [
        "show system info",
        "show system resources",
        "show interface all",
        "show routing route",
        "show routing summary",
        "show high-availability all",
        "show jobs all",
        "show log system",
        "show security policy",
        "ping host",
        "commit",
        "exit",
    ]

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

        # ---- SSH mode → offer common PAN-OS CLI hints ----
        if self._shell._state.ssh_mode:
            for hint in self._SSH_HINTS:
                if hint.startswith(text):
                    yield Completion(hint[len(text):], start_position=0)
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
        if self._shell._state.ssh_mode:
            builtins.insert(3, "disconnect")
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
    "ssh":    "bold ansigreen",
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
    # True when 'connect' is active — all non-built-in commands route via SSH
    ssh_mode: bool = False


class ArcShell:
    """Main interactive REPL."""

    def __init__(self, config: ArcConfig) -> None:
        self._config = config
        self._state = ShellState(folder=config.default_folder)

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
            if self._state.ssh_mode:
                return HTML(
                    f"<arc>arc</arc><sep>:</sep><device>{name}</device>"
                    f"<ssh>[ssh]</ssh><arrow> > </arrow>"
                )
            return HTML(f"<arc>arc</arc><sep>:</sep><device>{name}</device><arrow> > </arrow>")
        return HTML("<arc>arc</arc><arrow> > </arrow>")

    # ------------------------------------------------------------------
    # Main loop
    # ------------------------------------------------------------------

    def run(self) -> None:
        self._print_banner()
        while True:
            try:
                line = self._session.prompt(self._prompt()).strip()
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

        cmd = tokens[0].lower()

        # ---- exit / quit ----
        # In SSH mode, 'exit' leaves SSH passthrough and returns to API mode.
        # At the top level it exits ARC entirely.
        if cmd in ("exit", "quit"):
            if self._state.ssh_mode:
                self._state.ssh_mode = False
                name = self._state.device.get("hostname") or self._state.device.get("name", "device")
                console.print(
                    f"[cyan]SSH mode ended.[/cyan] Still at device context "
                    f"[bold]{name}[/bold] in API mode."
                )
                return False
            return True

        # ---- disconnect: explicit SSH mode exit ----
        if cmd == "disconnect":
            if self._state.ssh_mode:
                self._state.ssh_mode = False
                console.print("[cyan]SSH mode disconnected.  Remaining at device API context.[/cyan]")
            else:
                console.print("[yellow]Not in SSH mode.[/yellow]")
            return False

        # ---- SSH passthrough mode ----
        # When 'connect' is active, every command that isn't a shell built-in
        # is forwarded verbatim to the device over SSH.
        _shell_builtins = {
            "cd", "pwd", "ls", "devices", "folder", "clear", "help", "?", "docs",
            "connect", "remote", "disconnect",
        }
        if self._state.ssh_mode and cmd not in _shell_builtins:
            self._exec_ssh_passthrough(line)
            return False

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
        """Connect to a device via SSH and enter SSH passthrough mode.

        In SSH mode every subsequent command is forwarded verbatim to the
        device over SSH.  Type 'exit' or 'disconnect' to return to API mode.

        `connect` with no argument uses the current `cd` device. `remote <device>`
        requires a target and changes to that device before connecting.
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
        console.print(f"[dim]Testing SSH: {ssh_user}@{host}:{ssh_port}…[/dim]")

        try:
            self._ssh.verify_connection(
                host=host,
                user=ssh_user,
                key_path=ssh_key_path,
                password=ssh_password,
                port=ssh_port,
            )
        except Exception as exc:
            console.print(f"[red]SSH connection failed:[/red] {exc}")
            return

        self._state.ssh_mode = True
        console.print(
            f"[green]✓[/green] SSH connected to [bold]{name}[/bold] "
            f"([dim]{ssh_user}@{host}[/dim])\n"
            "[dim]All non-shell commands now execute directly on the device via SSH.\n"
            "Type [bold]exit[/bold] or [bold]disconnect[/bold] to return to API mode.[/dim]"
        )

    # ------------------------------------------------------------------
    # SSH passthrough: raw command forwarding
    # ------------------------------------------------------------------

    def _exec_ssh_passthrough(self, command: str) -> None:
        """Forward *command* verbatim to the connected device via SSH and print output."""
        device = self._state.device
        host = (device.get("ip_address") or device.get("hostname") or "") if device else ""
        if not host:
            console.print("[red]No device host configured. Use 'cd <device>' then 'connect', or 'remote <device>'.[/red]")
            return

        cfg_ssh = self._config.ssh
        ssh_user = str(cfg_ssh.user)
        ssh_key_path = str(cfg_ssh.key_path)
        ssh_password = str(cfg_ssh.password)
        ssh_port = int(cfg_ssh.port)
        output = self._ssh.execute(
            host=host,
            command=command,
            user=ssh_user,
            key_path=ssh_key_path,
            password=ssh_password,
            port=ssh_port,
        )
        console.print(fmt.format_raw(output, title=command))

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
        """Show current device context, SSH mode state, and active SCM folder."""
        if self._state.device:
            name = self._state.device.get("hostname") or self._state.device.get("name")
            serial = self._state.device.get("serial") or "n/a"
            ip = self._state.device.get("ip_address") or "n/a"
            mode = "[green]SSH mode[/green]" if self._state.ssh_mode else "API mode"
            console.print(
                f"[bold cyan]Device:[/bold cyan] {name}  "
                f"serial: {serial}  ip: {ip}  [{mode}]"
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
        if args and args[0] == "config":
            self._print_help_config()
            return

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
            ("cd <device>",         "Change Device in SCM"),
            ("remote <device>",     "SSH Passthrough to <device>"),
            ("connect <device>",    "SSH Connect to <device>"),
            ("folder <name>",       "Set the SCM Folder  [dim](Tab → available folders)[/dim]"),
            ("ls",                  "List managed devices under the current folder"),
            ("pwd",                 "Show current device, mode, and SCM folder"),
            ("docs / docs <command>", "Show Documentation  [dim]docs <command> shows help in shell[/dim]"),
            ("? / help",            "Print this command reference"),
            ("help config",         "Show configuration / credential help"),
            ("clear",               "Clear the terminal screen"),
            ("exit / quit",         "Exit the Application"),
        ]
        if self._state.ssh_mode:
            # In SSH mode clarify that exit returns to API mode
            builtins[-1] = ("exit / quit", "Return to API mode  [dim](at top level: exit ARC)[/dim]")
        for name, desc in builtins:
            console.print(f"  [cyan]{name:<45}[/cyan] {desc}")
        console.print()

    def _print_help_config(self) -> None:
        console.print()
        console.print(Panel(
            "[bold]Environment Variables[/bold]\n\n"
            "  [cyan]SCM_BEARER_TOKEN[/cyan]    Pre-issued SCM bearer token\n"
            "  [cyan]SCM_CLIENT_ID[/cyan]       SCM OAuth client ID\n"
            "  [cyan]SCM_CLIENT_SECRET[/cyan]   SCM OAuth client secret\n"
            "  [cyan]SCM_TSG_ID[/cyan]          Tenant Services Group ID\n\n"
            "  [cyan]ARC_SSH_USER[/cyan]        Default SSH username (default: admin)\n"
            "  [cyan]ARC_SSH_KEY[/cyan]         Path to SSH private key\n"
            "  [cyan]ARC_SSH_PASS[/cyan]        SSH password fallback\n"
            "  [cyan]ARC_DEBUG[/cyan]           Set to 1 for verbose error output\n\n"
            "[bold]Config File[/bold]  ~/.arc/config.json\n"
            "  Copy config/config.example.json and fill in credentials.",
            title="Configuration", border_style="cyan",
        ))

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
