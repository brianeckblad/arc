"""ArcShell prompt mixin — prompt / banner / startup / goodbye / styling."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class PromptMixin:
    def _prompt(self) -> HTML:
        """Build the prompt string reflecting the active context tier.

        Tier rules:
          No device, Shared folder  → arc:global >        (global context)
          No device, named folder   → arc:Production >     (folder context)
          Device, Shared folder     → arc:fw01:device >    (device context)
          Device, named folder      → arc:fw01:Production > (folder context on device)

        While a `commit confirmed` countdown is active, a [CONFIRM: Xm Ys]
        segment is appended before the arrow so the operator always knows the
        revert timer is running.

        When SCM is not connected, a [no-scm] segment is shown so the operator
        always knows the shell is running in degraded (read-only SSH) mode.
        """
        folder    = self._state.folder or "Shared"
        at_shared = folder.lower() == "shared"
        prompt_tail = " # " if self._state.configure_mode else " > "
        # Development mode marker — makes the hidden mode visible so operators
        # always know when work-in-progress (dev) commands are exposed.
        # In the dev shell, always show the marker regardless of _dev_mode attr.
        in_dev_shell = self._state.dev_shell
        dev_seg = "<sep>:</sep><dev>dev</dev>" if (in_dev_shell or getattr(self, "_dev_mode", False)) else ""

        # commit confirmed countdown — shown while a revert timer is armed.
        confirm_seg = ""
        pending = getattr(self, "_pending_confirm", None)
        if pending:
            import time as _time
            armed_at = pending.get("armed_at", 0.0)
            total_secs = pending.get("minutes", 0) * 60
            elapsed = _time.monotonic() - armed_at
            remaining = max(0.0, total_secs - elapsed)
            mins = int(remaining) // 60
            secs = int(remaining) % 60
            confirm_seg = f"<sep> </sep><confirm>[CONFIRM: {mins}m {secs:02d}s]</confirm>"

        # SCM degraded mode — shown when no SCM client was established at startup.
        noscm_seg = ""
        if not getattr(self, "_scm", None):
            noscm_seg = "<sep> </sep><noscm>[no-scm]</noscm>"

        # Attached marker — a warm SSH session to the active device exists
        # (2FA already completed); remote commands reuse it with no re-auth.
        attach_seg = ""
        if self._state.device and getattr(self._state, "attached", False):
            attach_seg = "<sep> </sep><ssh>[ssh]</ssh>"

        if self._state.device:
            name = device_display_name(self._state.device)
            if at_shared:
                # Device selected but still at Shared — show context tier as ':device'
                return HTML(
                    f"<arc>arc</arc>"
                    f"<sep>:</sep><device>{name}</device>"
                    f"<sep>:</sep><ctx>device</ctx>"
                    f"{dev_seg}"
                    f"{confirm_seg}"
                    f"{attach_seg}"
                    f"{noscm_seg}"
                    f"<arrow>{prompt_tail}</arrow>"
                )
            # Device selected and in a specific folder — show both
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><device>{name}</device>"
                f"<sep>:</sep><folder>{folder}</folder>"
                f"{dev_seg}"
                f"{confirm_seg}"
                f"{attach_seg}"
                f"{noscm_seg}"
                f"<arrow>{prompt_tail}</arrow>"
            )

        if at_shared:
            # No device, no specific folder — global context
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><ctx>global</ctx>"
                f"{dev_seg}"
                f"{confirm_seg}"
                f"{noscm_seg}"
                f"<arrow>{prompt_tail}</arrow>"
            )

        # No device but in a specific folder — folder context
        return HTML(
            f"<arc>arc</arc>"
            f"<sep>:</sep><folder>{folder}</folder>"
            f"{dev_seg}"
            f"{confirm_seg}"
            f"{noscm_seg}"
            f"<arrow>{prompt_tail}</arrow>"
        )

    def _help_cell(self, name: str, width: int = _HELP_CMD_WIDTH) -> str:
        """Left-pad *name* to the help command column and apply the theme style.

        Every help/`?` listing renders its command column through this one
        helper so all sections align on the same visual column. Names longer
        than the column (a few PAN-OS stems) overflow with a 2-space gap
        rather than being truncated — keys must stay copy-pastable.
        """
        if len(name) > width:
            return self._styled(f"{name}  ", self._theme.command_name)
        return self._styled(f"{name:<{width}}", self._theme.command_name)

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
        # banner.txt lives in settings/ (user-editable).  It uses Rich markup
        # tags for colour and {{variable_name}} placeholders for dynamic values
        # (resolved from settings/app-variables.json + runtime).
        # Lines starting with ## are comments and are stripped before rendering.
        from app.settings.app_vars import resolve as _resolve_vars
        try:
            raw = _BANNER_FILE.read_text(encoding="utf-8")
        except OSError:
            raw = ""

        content = "\n".join(
            line for line in raw.splitlines() if not line.startswith("##")
        )
        content = _resolve_vars(content)
        console.print(content, highlight=False)

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
        """Print compact startup command hints — loaded from settings/builtin-commands.json.

        Entries with ``onlogin: true`` and a ``startup_hint`` are shown.
        To hide a hint: set ``"onlogin": false`` on that entry.
        To add a hint: set ``"onlogin": true`` and add ``"startup_hint": "..."``
        to any entry in settings/builtin-commands.json.
        """
        from app.settings.commands import load_startup_hints
        from app.settings.app_vars import resolve as _resolve

        hints = load_startup_hints()
        if not hints:
            return

        # Align: 2-space indent, descriptions start at col 28.
        # All display names are padded to the same width with trailing spaces.
        max_display = max(len(display) for display, _ in hints)
        # Use the wider of the longest name or the minimum target width
        pad_to = max(max_display, 16)

        for display, hint in hints:
            spaces = " " * (pad_to - len(display) + 2)
            line = f"  [cyan]{display}[/cyan]{spaces}{_resolve(hint)}"
            console.print(line)
        console.print()
