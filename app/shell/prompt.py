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
        """
        folder    = self._state.folder or "Shared"
        at_shared = folder.lower() == "shared"
        prompt_tail = " # " if self._state.configure_mode else " > "
        # Development mode marker — makes the hidden mode visible so operators
        # always know when work-in-progress (dev) commands are exposed.
        dev_seg = "<sep>:</sep><dev>dev</dev>" if getattr(self, "_dev_mode", False) else ""

        if self._state.device:
            name = device_display_name(self._state.device)
            if at_shared:
                # Device selected but still at Shared — show context tier as ':device'
                return HTML(
                    f"<arc>arc</arc>"
                    f"<sep>:</sep><device>{name}</device>"
                    f"<sep>:</sep><ctx>device</ctx>"
                    f"{dev_seg}"
                    f"<arrow>{prompt_tail}</arrow>"
                )
            # Device selected and in a specific folder — show both
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><device>{name}</device>"
                f"<sep>:</sep><folder>{folder}</folder>"
                f"{dev_seg}"
                f"<arrow>{prompt_tail}</arrow>"
            )

        if at_shared:
            # No device, no specific folder — global context
            return HTML(
                f"<arc>arc</arc>"
                f"<sep>:</sep><ctx>global</ctx>"
                f"{dev_seg}"
                f"<arrow>{prompt_tail}</arrow>"
            )

        # No device but in a specific folder — folder context
        return HTML(
            f"<arc>arc</arc>"
            f"<sep>:</sep><folder>{folder}</folder>"
            f"{dev_seg}"
            f"<arrow>{prompt_tail}</arrow>"
        )

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
        # tags for colour — edit it to change the logo, subtitle, or add a legal
        # notice.  Lines starting with ## are comments.
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
        #   cd <device>    11 → 15 sp   remote <device> 15 → 11 sp
        #   folder <name>  13 → 13 sp   account <name>  14 → 12 sp
        #   ?               1 → 25 sp
        console.print(
            "  [cyan]cd <device>[/cyan]               Change to Device\n"
            "  [cyan]remote <device>[/cyan]           SSH to device  [dim](keyboard-interactive + 2FA)[/dim]\n"
            "  [cyan]folder <name>[/cyan]             Change to Folder\n"
            "  [cyan]account <name>[/cyan]            List / switch credential profiles\n"
            "  [cyan]?[/cyan]                         Context-Aware Help  [dim](or  help <topic>)[/dim]"
        )
        console.print()
