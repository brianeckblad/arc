"""ArcShell sessions mixin — connect / remote interactive SSH sessions."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class SessionsMixin:
    def _cmd_connect(self, args: list[str], require_target: bool = False) -> None:
        """Connect to a device via SSH and hand the terminal over to the remote shell."""

        if require_target and not args:
            console.print(
                "[yellow]Usage:[/yellow] remote <device-name | hostname | ip | serial>\n"
                "Tab after 'remote ' to see available devices."
            )
            return

        if not args and not self._state.device:
            # No explicit target and no device selected — resolve from the
            # current folder: auto-connect when it holds one device, prompt to
            # choose when it holds several, explain when it holds none.
            device = self._pick_folder_device()
            if device is None:
                return
            self._state.device = device

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
                name = device_display_name(match, target)
            elif self._state.devices_cache:
                # Cache populated — device genuinely not in this TSG.
                active_tsg = active_tsg_label(self._state, self._config)
                self._state.device = previous_device
                console.print(
                    f"[red]Device '{target}' not found in TSG {active_tsg}.[/red]\n"
                    f"  [dim]Use [bold]show devices[/bold] to see available devices, "
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
            name = device_display_name(self._state.device)

        host = device_ssh_host(self._state.device)
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
                "  Run [bold]arc auth configure[/bold] to store credentials so they\n"
                "  auto-fill next time, or see [bold]arc setup osx[/bold] / "
                "[bold]arc setup win[/bold] / [bold]arc setup linux[/bold].\n"
                "  [dim]Tip: prefer SSH agent ([bold]ssh-add[/bold]) over stored keys —\n"
                "  agent-based auth never writes private key material to ARC config.[/dim]\n"
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
        # The interactive session authenticated (2FA done) and left the
        # pooled transport warm — mark attached so remote commands reuse it.
        self._state.attached = True

    def _pick_folder_device(self) -> "Optional[dict]":
        """Return the device to SSH into from the current folder.

        Auto-selects when the folder holds exactly one device, prompts a numbered
        chooser when it holds several, and explains when it holds none. Returns
        ``None`` (after a message) when there is nothing to connect to or the
        user cancels the chooser.
        """
        if not self._state.devices_cache:
            self._refresh_devices()
        folder = self._state.folder
        in_folder = [
            d for d in list(self._state.devices_cache)
            if (d.get("folder") or "") == folder
        ]

        if not in_folder:
            console.print(
                f"[yellow]No devices found in folder '{folder}'.[/yellow]\n"
                "  [dim]Use [bold]show devices[/bold] to list all devices, "
                "[bold]cd folder <name>[/bold] to switch folder, "
                "or [bold]connect <name>[/bold] to target one directly.[/dim]"
            )
            return None

        if len(in_folder) == 1:
            return in_folder[0]

        # Several devices in this folder — present a numbered chooser.
        console.print(f"\n  [dim]Devices in folder '{folder}':[/dim]")
        console.print(f"  [dim]{'#':<5}{'Device':<30}{'IP':<18}Status[/dim]")
        console.print("  " + "─" * 58)
        for i, d in enumerate(in_folder, start=1):
            name   = device_display_name(d, "?")
            ip     = d.get("ip_address") or d.get("ip-address") or "—"
            status = "connected" if d.get("is_connected") else "—"
            console.print(
                f"  [cyan]{i:<5}[/cyan][green]{name:<30}[/green]"
                f"[dim]{str(ip):<18}{status}[/dim]"
            )
        console.print()

        try:
            raw = input("  Enter # or device name [1]: ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Cancelled.[/dim]")
            return None

        if not raw:
            return in_folder[0]
        if raw.isdigit():
            idx = int(raw) - 1
            if 0 <= idx < len(in_folder):
                return in_folder[idx]
            console.print(f"[red]Invalid number: {raw}  (valid range 1–{len(in_folder)})[/red]")
            return None
        match = self._find_device(raw)
        if match:
            return match
        console.print(f"[red]Device '{raw}' not found.[/red]")
        return None

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
            pass  # PTY resize is best-effort; failure does not affect the session

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
                pass  # PTY resize is best-effort; failure does not affect the session

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

        except Exception as exc:
            # Session ended unexpectedly — log for visibility, restore terminal below.
            console.print(f"\n[yellow]SSH session interrupted:[/yellow] {exc}")

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
