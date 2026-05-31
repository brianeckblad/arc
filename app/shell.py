"""Interactive REPL shell for ARC — Assisted Remote Console."""

from __future__ import annotations

import os
import select
import shutil
import signal
import sys
import time
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

        # SCM sometimes returns an empty device list on the very first request
        # right after OAuth (token propagation / eventual consistency).  Retry
        # once after a short pause before giving up and showing the hint.
        if not self._state.devices_cache:
            time.sleep(1.5)
            self._refresh_devices(silent=True)

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

        if self._state.device:
            name = self._state.device.get("hostname") or self._state.device.get("name") or "device"
            if at_shared:
                # Device selected but still at Shared — show context tier as ':device'
                return HTML(
                    f"<arc>arc</arc>"
                    f"<sep>:</sep><device>{name}</device>"
                    f"<sep>:</sep><ctx>device</ctx>"
                    f"<arrow> > </arrow>"
                )
            # Device selected and in a specific folder — show both
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><device>{name}</device>"
                f"<sep>:</sep><folder>{folder}</folder>"
                f"<arrow> > </arrow>"
            )

        if at_shared:
            # No device, no specific folder — global context
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><ctx>global</ctx>"
                f"<arrow> > </arrow>"
            )

        # No device but in a specific folder — folder context
        return HTML(
            f"<arc>arc</arc>"
            f"<sep>:</sep><folder>{folder}</folder>"
            f"<arrow> > </arrow>"
        )

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
        # Folder is always shown — it is the primary SCM scope for all API calls.
        console.print(
            f"[bold cyan]SCM folder:[/bold cyan] [bold green]{self._state.folder}[/bold green]"
            "  [dim](all API calls scoped to this folder — change with 'folder <name>')[/dim]"
        )
        active_tsg = self._state.tsg_id or "(root / config default)"
        console.print(f"[bold cyan]TSG:[/bold cyan] {active_tsg}")

    # ------------------------------------------------------------------
    # Command: folder
    # ------------------------------------------------------------------

    def _cmd_folder(self, args: list[str]) -> None:
        """Set or display the active SCM folder context.

        The active folder is passed as the ``?folder=`` query parameter on
        every SCM REST call.  It is always visible in the prompt so there is
        no ambiguity about which folder a command is scoped to.

        Usage:
          folder             — list available folders and show the active one
          folder <name>      — switch to <name>
          folder ..          — switch to 'Shared' (root / default)
        """
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

        previous_tsg    = self._state.tsg_id
        previous_device = self._state.device
        previous_folder = self._state.folder
        has_client_creds = bool(
            self._config.scm.client_id and self._config.scm.client_secret
        )

        if not has_client_creds:
            # Bearer-token-only mode: record context change, clear stale
            # device/folder state from the old TSG, then refresh caches.
            self._state.tsg_id = new_tsg
            self._state.device = None
            self._state.folder = self._config.default_folder
            self._state.devices_cache = []
            self._state.folders_cache = ["Shared", "Global"]
            console.print(f"[dim]Refreshing caches for TSG {new_tsg}…[/dim]")
            self._refresh_devices(silent=True)
            self._refresh_folders(silent=True)
            device_count = len(self._state.devices_cache)
            console.print(
                f"[cyan]TSG context set to:[/cyan] [bold]{new_tsg}[/bold]  "
                f"({device_count} device(s) visible)\n"
                "[dim]Bearer token used as-is — SCM enforces TSG-level access.[/dim]"
            )
            if device_count == 0:
                console.print(
                    "[yellow]No devices visible in this TSG.[/yellow]  "
                    "[dim]cd and device-scope commands unavailable here — "
                    "use [bold]tsg <id>[/bold] to switch to a TSG with devices.[/dim]"
                )
            return

        # OAuth mode: re-authenticate with the new TSG scope.
        console.print(f"[dim]Re-authenticating with TSG {new_tsg}…[/dim]")
        # Clear stale context immediately so nothing from the old TSG leaks.
        self._state.tsg_id = new_tsg
        self._state.device = None
        self._state.folder = self._config.default_folder
        try:
            if self._scm:
                self._scm.reauthenticate(new_tsg)
            else:
                import copy  # Deferred: avoids circular import
                new_scm_cfg = copy.copy(self._config.scm)
                new_scm_cfg.tsg_id = new_tsg
                self._scm = SCMClient(new_scm_cfg)

            # Refresh all caches for the new TSG context.
            console.print(f"[dim]Refreshing device and folder lists for TSG {new_tsg}…[/dim]")
            self._refresh_devices(silent=True)
            self._refresh_folders(silent=True)
            self._refresh_tsgs(silent=True)

            device_count = len(self._state.devices_cache)
            console.print(
                f"[green]✓[/green] Switched to TSG [bold]{new_tsg}[/bold]  "
                f"({device_count} device(s) visible)"
            )
            if device_count == 0:
                console.print(
                    "[yellow]No devices visible in this TSG.[/yellow]  "
                    "[dim]cd and device-scope commands unavailable here — "
                    "use [bold]tsg <id>[/bold] to switch to a TSG with devices.[/dim]"
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
            self._cmd_help_contextual()

    def _cmd_help_contextual(self) -> None:
        """Print context-aware help organised in three tiers.

        Tier 1 — GLOBAL: always available regardless of navigation context.
        Tier 2 — FOLDER COMMANDS: scoped to the active folder (always callable,
                  most meaningful in a specific non-Shared folder).
        Tier 3 — DEVICE COMMANDS: require an active device context (cd <device>).

        This mirrors the PAN-OS / Panorama CLI mental model where the command set
        visible to the operator expands as they navigate deeper into context.
        Operators at root see global commands clearly, folder commands with a
        "Shared" annotation and a hint to navigate, and device commands clearly
        locked behind 'cd <device>'.
        """
        device = self._state.device
        folder = self._state.folder
        device_name = (device.get("hostname") or device.get("name") or "device") if device else ""

        # Build context header line
        if device:
            ctx_line = (
                f"[bold cyan]Context:[/bold cyan]  "
                f"folder [bold green]{folder}[/bold green]  "
                f"device [bold yellow]{device_name}[/bold yellow]"
            )
        elif folder and folder.lower() != "shared":
            ctx_line = (
                f"[bold cyan]Context:[/bold cyan]  "
                f"folder [bold green]{folder}[/bold green]  "
                f"[dim](cd <device> to unlock device commands)[/dim]"
            )
        else:
            ctx_line = (
                f"[bold cyan]Context:[/bold cyan]  "
                f"folder [bold green]{folder}[/bold green]  "
                f"[dim](root — folder <name> to scope | cd <device> for device commands)[/dim]"
            )

        console.print()
        console.print(Panel(
            f"{ctx_line}\n"
            "[dim]Commands shown by context level — navigate deeper to unlock more.\n"
            "Type [bold]help all[/bold] for the full unfiltered reference  |  "
            "[bold]help <command>[/bold] for command docs[/dim]",
            title="Help  (? also works)", border_style="cyan",
        ))

        # --- Tier 1: GLOBAL — always available ---
        global_keys = sorted(k for k, cmd in COMMANDS.items() if cmd.scope == "global")
        if global_keys:
            console.print("\n[bold yellow]GLOBAL[/bold yellow]  [dim]— always available[/dim]")
            for k in global_keys:
                cmd = COMMANDS[k]
                ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command and cmd.api_handler else ""
                console.print(f"  [cyan]{k:<45}[/cyan] {cmd.description}{ssh_note}")

        # --- Tier 2: FOLDER COMMANDS ---
        folder_keys = sorted(k for k, cmd in COMMANDS.items() if cmd.scope == "folder")
        if folder_keys:
            if folder and folder.lower() != "shared":
                folder_header = (
                    f"[bold yellow]FOLDER COMMANDS[/bold yellow]  "
                    f"[dim]— folder: {folder}[/dim]"
                )
            else:
                folder_header = (
                    f"[bold yellow]FOLDER COMMANDS[/bold yellow]  "
                    f"[dim]— folder: {folder}  "
                    f"(use 'folder <name>' to scope to a specific folder)[/dim]"
                )
            console.print(f"\n{folder_header}")
            for k in folder_keys:
                cmd = COMMANDS[k]
                ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command and cmd.api_handler else ""
                ctx_note = self._context_annotation(k)
                console.print(f"  [cyan]{k:<45}[/cyan] {cmd.description}{ssh_note}{ctx_note}")

        # --- Tier 3: DEVICE COMMANDS ---
        device_keys = sorted(k for k, cmd in COMMANDS.items() if cmd.scope == "device")
        if device_keys:
            if device:
                device_header = (
                    f"[bold yellow]DEVICE COMMANDS[/bold yellow]  "
                    f"[dim]— device: {device_name}  "
                    f"(append --remote to target another device)[/dim]"
                )
                console.print(f"\n{device_header}")
                for k in device_keys:
                    cmd = COMMANDS[k]
                    ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command else ""
                    console.print(f"  [cyan]{k:<45}[/cyan] {cmd.description}{ssh_note}")
            else:
                console.print(
                    "\n[dim bold]DEVICE COMMANDS[/dim bold]  "
                    "[dim]— requires cd <device>  "
                    "(or append --remote <device> to any command)[/dim]"
                )
                for k in device_keys:
                    cmd = COMMANDS[k]
                    console.print(f"  [dim]{k:<45}  {cmd.description}[/dim]")
                console.print(
                    "  [dim]→ [bold dim]cd <device>[/bold dim][dim] to unlock.  "
                    "Tab after 'cd ' lists all managed devices.[/dim]"
                )

        self._print_shell_builtins()
        console.print()

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
            title="Help  (? also works | help all → this view)", border_style="cyan",
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
                console.print(f"  [cyan]{k:<45}[/cyan] {cmd.description}{scope_tag}{ssh_note}")

        self._print_shell_builtins()
        console.print()

    def _print_shell_builtins(self) -> None:
        """Print the shell built-in commands table (shared by contextual and full help)."""
        console.print("\n[bold yellow]SHELL[/bold yellow]")
        builtins = [
            ("cd <device>",           "Change Device in SCM"),
            ("connect [device]",      "SSH to device — full interactive session  [dim](returns to ARC on exit)[/dim]"),
            ("remote <device>",       "SSH to device — full interactive session  [dim](also sets device context)[/dim]"),
            ("folder <name>",         "Set SCM Folder — always shown in prompt  [dim](Tab → available folders | folder .. → Shared)[/dim]"),
            ("tsg <id>",              "Set the active TSG (Tenant Services Group)  [dim](Tab → configured TSG)[/dim]"),
            ("ls",                    "List devices (root) or device detail + snippets (in device context)"),
            ("pwd",                   "Show current device, SCM folder, and active TSG"),
            ("docs / docs <command>", "Show Documentation  [dim]docs <command> shows help in shell[/dim]"),
            ("? / help",              "Context-sensitive help  [dim](help all → full list)[/dim]"),
            ("help <topic>",          "Open topic doc  [dim]e.g. help config, help config osx|win|nix[/dim]"),
            ("clear",                 "Clear the terminal screen"),
            ("exit / quit",           "Exit ARC"),
        ]
        for name, desc in builtins:
            console.print(f"  [cyan]{name:<45}[/cyan] {desc}")


    def _cmd_context_help(self, prefix_tokens: list[str]) -> None:
        """Show scoped help for a partial command prefix typed before '?'.

        Behaviour mirrors the PAN-OS CLI convention:
        - Exact registry match  → render its doc page (description + Markdown)
        - Partial prefix match  → list every command that begins with the prefix
        - Shell built-in        → render its doc page
        - No match anywhere     → friendly fallback to the full command list

        Context annotations are added where relevant (e.g. what 'show snippets'
        will actually return given the current folder/device context).
        """
        prefix = " ".join(prefix_tokens).lower()

        # 1. Exact match in the command registry — show its full doc page.
        if prefix in COMMANDS:
            if render_help_topic(console, prefix):
                return
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
            # Inline context hint for snippet/folder-scoped commands
            self._print_context_hint_for(prefix)
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
                # Add live context annotation for snippet commands
                ctx_note = self._context_annotation(k)
                console.print(
                    f"  [cyan]{k:<45}[/cyan] {cmd_def.description}{ssh_note}{ctx_note}"
                )
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

    def _context_annotation(self, command_key: str) -> str:
        """Return a short inline context note for commands whose output depends on state.

        All folder-scope commands show the active folder.
        All device-scope commands show the active device when one is set.
        Returns empty string when there is nothing context-specific to note.
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
        """Print a one-line context note below an exact-match help result."""
        note = self._context_annotation(command_key)
        if note:
            # Strip Rich markup for the plain print (it will re-render via console.print)
            console.print(f"[dim]Current context:[/dim]{note}")

    # ------------------------------------------------------------------
    # API execution
    # ------------------------------------------------------------------

    def _execute_api(self, key: str, cmd_def: CommandDef, args: dict) -> None:
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

    def _cleanup(self) -> None:
        self._ssh.close_all()
        if self._scm:
            self._scm.close()
        console.print("\n[cyan]Goodbye.[/cyan]")

    def _print_banner(self) -> None:
        # Each letter is 8 chars wide; 5-space left indent centres on an 80-col terminal.
        #
        # A:            R:            C:
        #  █████╗       ██████╗        ██████╗
        # ██╔══██╗      ██╔══██╗      ██╔════╝
        # ███████║      ███████║      ██║
        # ██╔══██║      ██╔═══╝       ██║
        # ██║  ██║      ██║  ██╗      ╚██████╗
        # ╚═╝  ╚═╝      ╚═╝  ╚═╝       ╚═════╝
        art = (
            "\n"
            "      \u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2557  \u2588\u2588\u2588\u2588\u2588\u2588\u2557\n"
            "     \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\n"
            "     \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2551\u2588\u2588\u2551     \n"
            "     \u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2550\u255d \u2588\u2588\u2551     \n"
            "     \u2588\u2588\u2551  \u2588\u2588\u2551\u2588\u2588\u2551  \u2588\u2588\u2557\u255a\u2588\u2588\u2588\u2588\u2588\u2588\u2557\n"
            "     \u255a\u2550\u255d  \u255a\u2550\u255d\u255a\u2550\u255d  \u255a\u2550\u255d \u255a\u2550\u2550\u2550\u2550\u2550\u255d\n"
        )
        console.print()
        console.print(f"[bold cyan]{art}[/bold cyan]")
        console.print("  [dim]Assisted Remote Console  —  Palo Alto Networks SCM + PAN-OS[/dim]")
        console.print()
        console.print(
            "  [cyan]cd <device>[/cyan]               Change Device in SCM  [dim](Tab → device list)[/dim]\n"
            "  [cyan]remote <device>[/cyan]           SSH to device  [dim](keyboard-interactive + 2FA)[/dim]\n"
            "  [cyan]connect[/cyan]                   SSH to current device\n"
            "  [cyan]folder <name>[/cyan]             Set SCM Folder  [dim](Tab → folder list)[/dim]\n"
            "  [cyan]?[/cyan]                         Context-aware help  [dim](or  help <topic>)[/dim]"
        )
        console.print()
