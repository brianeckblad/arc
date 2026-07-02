"""ArcShell — the interactive REPL.

Split into mixins (one concern per file). This package __init__ composes them
into the ArcShell class and keeps the public surface stable:
    from app.shell import ArcShell, ShellState, console
    from app.shell import _SHELL_BUILTINS, _expand_unambiguous_prefix

Method line ranges live in dev/CODE_MAP.md. Edit one mixin file, not the whole
shell. Shared imports/constants/helpers live in app/shell/_base.py.
"""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)
from app.shell._base import (  # explicit re-exports for external importers
    ShellState, console, _SHELL_BUILTINS, _expand_unambiguous_prefix,
)
from app.shell.completer import ArcCompleter
from app.shell.navigation import NavigationMixin
from app.shell.sessions import SessionsMixin
from app.shell.help import HelpMixin
from app.shell.execution import ExecutionMixin
from app.shell.configure import ConfigureMixin
from app.shell.write_cmd import WriteMixin
from app.shell.prompt import PromptMixin
from app.shell.dispatch import DispatchMixin


class ArcShell(
    NavigationMixin, SessionsMixin, HelpMixin, ExecutionMixin, ConfigureMixin, WriteMixin, PromptMixin, DispatchMixin,
):
    """Main interactive REPL (composed from the shell mixins)."""

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

        # Feature flags — loaded once at startup; apply to all command dispatch.
        # Each flag is "on" / "dev" / "off".  Edit settings/features.json or set
        # ARC_FEATURE_<NAME>=on|dev|off env vars.
        self._features: dict[str, str] = load_features()
        
        # Command visibility — independent of feature flags.  Loaded from
        # settings/commands.json.  Set false to hide specific commands.
        self._command_visibility: dict[str, bool] = load_command_visibility()

        # Development mode reveals "dev" (under-construction) commands.  Off by
        # default; toggled by the hidden `dev` command, or pre-enabled in CI/CD
        # with ARC_DEV_MODE=1.  Session-only — never written to disk.
        self._dev_mode: bool = dev_mode_from_env()

        # Build clients
        self._scm: Optional[SCMClient] = None
        self._ssh = SSHManager()

        # Load CLI theme (colours for ? help, banner, etc.)
        self._theme: ArcTheme = load_theme()

        # Per-user preferences (config/<user>/preferences.json) — pager length,
        # render width, spinner. Changed at runtime via the `terminal` command.
        self._prefs: UserPrefs = load_prefs()
        set_page_length(self._prefs.terminal_length)
        if self._prefs.terminal_width > 0:
            console.width = self._prefs.terminal_width

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
            key_bindings=_make_key_bindings(self),
            style=PROMPT_STYLE,
        )

    def _init_clients(self) -> None:
        # Keychain trouble is easy to mistake for "wrong credentials" — say it
        # up front, once, with the way out.
        from app.config import keychain_read_failed
        if keychain_read_failed():
            console.print(
                "[yellow]⚠[/yellow]  OS keychain unavailable — stored credentials could not be read.  "
                "[dim]Use SCM_* env vars for this session, or run [bold]arc auth test[/bold] to diagnose.[/dim]"
            )

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
                "[red]✗[/red] [bold red]SCM not connected.[/bold red]  "
                "Type [bold cyan]setup[/bold cyan] for a guided credential wizard, "
                "or [bold cyan]help setup[/bold cyan] to browse setup steps.\n"
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
                "[dim]No devices loaded — run [bold]show devices[/bold] to retry, "
                "or check your service account has Device Administrator access.[/dim]"
            )

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


__all__ = ["ArcShell", "ShellState", "console", "ArcCompleter",
           "_SHELL_BUILTINS", "_expand_unambiguous_prefix"]
