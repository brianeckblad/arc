"""ArcShell configure mixin — configure mode, cli theme, feature flags."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class ConfigureMixin:
    def _cmd_configure(self, args: list[str]) -> None:
        """Enter configure mode (Cisco-style).

        In configure mode, 'set' creates objects and 'exit' leaves configure mode.
        """
        if args and args[0].lower() not in ("t", "terminal"):
            console.print(
                "[yellow]Usage:[/yellow] configure | conf | conf t\n"
                "  Then use [bold]set[/bold] to create objects, [bold]cli[/bold] for theme operations."
            )
            return

        if self._state.configure_mode:
            console.print("[dim]Already in configure mode.[/dim]")
            return

        self._state.configure_mode = True
        self._state.device = None
        self._state.folder = "Shared"
        for line in _configure_banner().splitlines():
            console.print(f"[green]{line.strip()}[/green]" if line.strip() else "")

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
            console.print("  [bold]ARC CLI Theme[/bold]  [dim](settings/theme.json)[/dim]")
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
            console.print(f"[green]✓[/green] {key} = {preview}  [dim](saved to settings/theme.json)[/dim]")
            return

        if sub == "reset":
            self._theme = reset_theme()
            console.print("[green]✓[/green] Theme reset to defaults  [dim](saved to settings/theme.json)[/dim]")
            return

        console.print(
            f"[yellow]Unknown cli subcommand:[/yellow] {sub!r}\n"
            "  Usage: cli show | cli color <key> <style> | cli reset"
        )

    def _cmd_feature(self, args: list[str]) -> None:
        """Show, enable, or disable feature flags at runtime.

        Subcommands:
          feature show                 — list all flags grouped by shipped/unimplemented
          feature enable <flag>        — turn a flag on for this session
          feature disable <flag>       — turn a flag off for this session
          feature ?                    — show this usage summary
          feature enable ?             — list all flags that are currently disabled
          feature disable ?            — list all flags that are currently enabled

        Changes take effect immediately but are session-only unless you edit
        settings/features.json.  Use 'feature help' for the full docs page.
        """
        sub = args[0].lower() if args else "show"

        # ── ? suffix handling ─────────────────────────────────────────────────
        if sub == "?":
            console.print()
            console.print(f"  [bold yellow]feature[/bold yellow]  [dim]— feature flag management[/dim]")
            console.print()
            console.print(f"  [cyan]feature show[/cyan]           List all flags with current on/off status")
            console.print(f"  [cyan]feature enable <flag>[/cyan]  Turn a flag on for this session")
            console.print(f"  [cyan]feature disable <flag>[/cyan] Turn a flag off for this session")
            console.print(f"  [cyan]feature help[/cyan]           Open full feature flag documentation")
            console.print()
            console.print(f"  [dim]feature enable ?   → list flags that are OFF (can be enabled)[/dim]")
            console.print(f"  [dim]feature disable ?  → list flags that are ON  (can be disabled)[/dim]")
            console.print(f"  [dim]feature show       → full list with shipped/unimplemented grouping[/dim]")
            console.print()
            return

        # Helper: build flag→commands reverse map (used by show and enable/disable ?)
        def _flag_to_cmds() -> dict[str, list[str]]:
            result: dict[str, list[str]] = {}
            for cmd_key, cmd_def in COMMANDS.items():
                if cmd_def.feature_flag:
                    result.setdefault(cmd_def.feature_flag, []).append(cmd_key)
            return result

        # The universe of known flags = those in settings/features.json plus any
        # referenced by a command in the registry (so newly-added flags appear).
        def _all_flags() -> list[str]:
            names = set(self._features) | set(_flag_to_cmds())
            return sorted(names)

        if sub in ("enable", "disable") and len(args) >= 2 and args[1] == "?":
            flag_cmds = _flag_to_cmds()
            console.print()
            if sub == "enable":
                candidates = [f for f in _all_flags() if not is_enabled(self._features, f)]
                console.print(f"  [bold yellow]feature enable <flag>[/bold yellow]  [dim]— flags currently OFF[/dim]")
                console.print(f"  [dim]  Persist by editing settings/features.json[/dim]")
            else:
                candidates = [f for f in _all_flags() if is_enabled(self._features, f)]
                console.print(f"  [bold yellow]feature disable <flag>[/bold yellow]  [dim]— flags currently ON[/dim]")
            console.print()
            if not candidates:
                console.print(f"  [dim]No flags are currently {'OFF' if sub == 'enable' else 'ON'}.[/dim]")
            else:
                for flag in candidates:
                    cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                    console.print(f"    [bold]{flag:<35}[/bold]  [dim]{cmds}[/dim]")
            console.print()
            console.print(f"  [dim]feature enable <flag>  |  feature disable <flag>  |  feature show[/dim]")
            console.print()
            return

        if sub == "help":
            if not render_help_topic(console, "features"):
                console.print("[dim]No docs found for 'features' — run 'help features'.[/dim]")
            return

        if sub == "show":
            flag_cmds = _flag_to_cmds()
            names = _all_flags()
            on  = [f for f in names if is_enabled(self._features, f)]
            off = [f for f in names if not is_enabled(self._features, f)]

            console.print()
            console.print(
                f"  [bold yellow]Feature Flags[/bold yellow]  "
                f"[dim]— edit settings/features.json to persist[/dim]"
            )

            console.print(f"\n  [bold green]ENABLED[/bold green]  [dim]({len(on)})[/dim]")
            for flag in on:
                cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                console.print(f"    {flag:<35} [green]on[/green]   [dim]{cmds}[/dim]")

            console.print(f"\n  [bold red]DISABLED[/bold red]  [dim]({len(off)})[/dim]")
            for flag in off:
                cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                console.print(f"    {flag:<35} [red]off[/red]  [dim]{cmds}[/dim]")

            console.print()
            console.print("  [dim]  feature enable <flag>  |  feature disable <flag>  |  feature help[/dim]")
            console.print()
            return

        if sub in ("enable", "disable"):
            if len(args) < 2:
                console.print(f"[yellow]Usage:[/yellow] feature {sub} <flag_name>")
                console.print(f"  Tip: [bold]feature {sub} ?[/bold]  lists all flags that can be {sub}d")
                return
            flag_name = args[1].lower()
            if flag_name not in _all_flags():
                console.print(
                    f"[red]Unknown feature flag:[/red] {flag_name!r}\n"
                    f"  Run [bold]feature enable ?[/bold] to see all available flags."
                )
                return
            new_val = (sub == "enable")
            self._features[flag_name] = new_val   # session-only override
            state = "[green]enabled[/green]" if new_val else "[red]disabled[/red]"
            console.print(f"  {flag_name}  →  {state}  [dim](session only — edit settings/features.json to persist)[/dim]")
            return

        console.print(
            f"[yellow]Unknown feature subcommand:[/yellow] {sub!r}\n"
            "  Usage: feature show | feature enable <flag> | feature disable <flag>"
        )
