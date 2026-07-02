"""ArcShell configure mixin — configure mode, cli theme, feature flags."""
from __future__ import annotations

import platform  # For OS detection in setup wizard

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
        """Show or change feature-flag states at runtime.

        Subcommands:
          feature show                 — list all flags grouped ON / DEV / OFF
          feature show on|off|dev      — list only flags in one state
          feature show <name>          — list flags matching a name fragment
          feature enable <flag>        — set a flag ON and save to settings/features.json
          feature disable <flag>       — set a flag OFF and save to settings/features.json
          feature dev <flag>           — mark a flag DEV and save to settings/features.json
          feature ?                    — show this usage summary

        Flag states: ON (everyone), DEV (only in development mode — see the
        hidden 'dev' command), OFF (hidden for everyone).  Changes take effect
        immediately and are persisted to settings/features.json.
        """
        sub = args[0].lower() if args else "show"

        # ── ? suffix handling ─────────────────────────────────────────────────
        if sub == "?":
            console.print()
            console.print(f"  [bold yellow]feature[/bold yellow]  [dim]— feature flag management[/dim]")
            console.print()
            console.print(f"  [cyan]feature show[/cyan]           List all flags grouped ON / DEV / OFF")
            console.print(f"  [cyan]feature show on[/cyan]        List only enabled flags")
            console.print(f"  [cyan]feature show off[/cyan]       List only disabled flags")
            console.print(f"  [cyan]feature show dev[/cyan]       List only development flags")
            console.print(f"  [cyan]feature show <name>[/cyan]    Show matching feature flag(s)")
            console.print(f"  [cyan]feature enable <flag>[/cyan]  Set a flag ON and save")
            console.print(f"  [cyan]feature disable <flag>[/cyan] Set a flag OFF and save")
            console.print(f"  [cyan]feature dev <flag>[/cyan]     Mark a flag DEV and save")
            console.print(f"  [cyan]feature help[/cyan]           Open full feature flag documentation")
            console.print()
            console.print(f"  [dim]DEV flags appear only after you type [bold]dev[/bold] to enter development mode.[/dim]")
            console.print(f"  [dim]feature enable ?  → flags not yet ON   |   feature disable ?  → flags not yet OFF[/dim]")
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

        def _persist_feature_state(flag_name: str, state: str) -> None:
            """Write one feature flag state to settings/features.json and memory."""
            import json  # Deferred: used only when changing a feature flag.

            from app.paths import FEATURES_FILE

            try:
                raw = json.loads(FEATURES_FILE.read_text(encoding="utf-8")) if FEATURES_FILE.exists() else {}
            except (json.JSONDecodeError, OSError) as exc:
                raise RuntimeError(f"Could not read settings/features.json: {exc}") from exc
            if not isinstance(raw, dict):
                raise RuntimeError("settings/features.json must contain a JSON object")

            raw_value: bool | str
            if state == "on":
                raw_value = True
            elif state == "dev":
                raw_value = "dev"
            else:
                raw_value = False

            raw[flag_name] = raw_value
            try:
                FEATURES_FILE.write_text(json.dumps(raw, indent=2) + "\n", encoding="utf-8")
            except OSError as exc:
                raise RuntimeError(f"Could not write settings/features.json: {exc}") from exc
            self._features[flag_name] = state

        def _print_feature_rows(title: str, flags: list[str], colour: str, flag_cmds: dict[str, list[str]]) -> None:
            """Print a compact flag list with command mappings."""
            console.print(f"\n  [bold {colour}]{title}[/bold {colour}]  [dim]({len(flags)})[/dim]")
            if not flags:
                console.print("    [dim]No matching flags.[/dim]")
                return
            for flag in flags:
                state = feature_state(self._features, flag)
                cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                console.print(f"    {flag:<35} [{colour}]{state}[/{colour}]  [dim]{cmds}[/dim]")

        if sub in ("enable", "disable", "dev") and len(args) >= 2 and args[1] == "?":
            flag_cmds = _flag_to_cmds()
            console.print()
            if sub == "enable":
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "on"]
                console.print(f"  [bold yellow]feature enable <flag>[/bold yellow]  [dim]— flags not yet ON[/dim]")
                console.print(f"  [dim]  Saves immediately to settings/features.json[/dim]")
            elif sub == "dev":
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "dev"]
                console.print(f"  [bold yellow]feature dev <flag>[/bold yellow]  [dim]— flags not yet DEV[/dim]")
            else:
                candidates = [f for f in _all_flags() if feature_state(self._features, f) != "off"]
                console.print(f"  [bold yellow]feature disable <flag>[/bold yellow]  [dim]— flags not yet OFF[/dim]")
            console.print()
            if not candidates:
                console.print(f"  [dim]No matching flags.[/dim]")
            else:
                for flag in candidates:
                    cmds = ", ".join(sorted(flag_cmds.get(flag, []))) or "—"
                    console.print(f"    [bold]{flag:<35}[/bold]  [dim]{cmds}[/dim]")
            console.print()
            console.print(f"  [dim]feature enable <flag>  |  feature disable <flag>  |  feature dev <flag>  |  feature show[/dim]")
            console.print()
            return

        if sub == "help":
            if not render_help_topic(console, "features"):
                console.print("[dim]No docs found for 'features' — run 'help features'.[/dim]")
            return

        if sub == "show":
            flag_cmds = _flag_to_cmds()
            names = _all_flags()
            on  = [f for f in names if feature_state(self._features, f) == "on"]
            dev = [f for f in names if feature_state(self._features, f) == "dev"]
            off = [f for f in names if feature_state(self._features, f) == "off"]
            filter_token = args[1].lower() if len(args) >= 2 else ""

            mode = (
                "[magenta]ON[/magenta]" if self._dev_mode
                else "[dim]off[/dim]"
            )
            console.print()
            console.print(
                f"  [bold yellow]Feature Flags[/bold yellow]  "
                f"[dim]— development mode:[/dim] {mode}  "
                f"[dim](changes save to settings/features.json)[/dim]"
            )

            if filter_token in ("on", "enabled", "true"):
                _print_feature_rows("ON — visible to everyone", on, "green", flag_cmds)
                console.print()
                return
            if filter_token in ("off", "disabled", "false"):
                _print_feature_rows("OFF — hidden for everyone", off, "red", flag_cmds)
                console.print()
                return
            if filter_token in ("dev", "development"):
                dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
                _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
                console.print()
                return
            if filter_token:
                matches = [
                    flag for flag in names
                    if filter_token in flag.lower()
                    or any(filter_token in cmd.lower() for cmd in flag_cmds.get(flag, []))
                ]
                _print_feature_rows(f"MATCHES — {filter_token}", matches, "cyan", flag_cmds)
                console.print()
                return

            _print_feature_rows("ON — visible to everyone", on, "green", flag_cmds)
            dev_hint = "shown now" if self._dev_mode else "hidden — type 'dev' to reveal"
            _print_feature_rows(f"DEV — {dev_hint}", dev, "magenta", flag_cmds)
            _print_feature_rows("OFF — hidden for everyone", off, "red", flag_cmds)

            console.print()
            console.print("  [dim]  feature show on|off|dev|<name>  |  feature enable <flag>  |  feature disable <flag>  |  feature dev <flag>[/dim]")
            console.print()
            return

        if sub in ("enable", "disable", "dev"):
            if len(args) < 2:
                console.print(f"[yellow]Usage:[/yellow] feature {sub} <flag_name>")
                console.print(f"  Tip: [bold]feature {sub} ?[/bold]  lists the flags you can {sub}")
                return
            flag_name = args[1].lower()
            if flag_name not in _all_flags():
                console.print(
                    f"[red]Unknown feature flag:[/red] {flag_name!r}\n"
                    f"  Run [bold]feature {sub} ?[/bold] to see all available flags."
                )
                return
            new_state = {"enable": "on", "disable": "off", "dev": "dev"}[sub]
            try:
                _persist_feature_state(flag_name, new_state)
            except RuntimeError as exc:
                console.print(f"[red]Could not save feature flag:[/red] {exc}")
                return
            colour = {"on": "green", "dev": "magenta", "off": "red"}[new_state]
            note = ""
            if new_state == "dev" and not self._dev_mode:
                note = "  [dim](type 'dev' to reveal dev commands)[/dim]"
            console.print(
                f"  {flag_name}  →  [{colour}]{new_state}[/{colour}]{note}  "
                f"[dim](saved to settings/features.json)[/dim]"
            )
            return

        console.print(
            f"[yellow]Unknown feature subcommand:[/yellow] {sub!r}\n"
            "  Usage: feature show [on|off|dev|<name>] | feature enable <flag> | feature disable <flag> | feature dev <flag>"
        )

    def _cmd_dev(self, args: list[str]) -> None:
        """Toggle development mode (hidden command).

        Development mode reveals every command whose feature flag is "dev" —
        work-in-progress commands that normal users never see.  This supports a
        CI/CD lifecycle: ship a command as "dev", test it in development mode,
        then flip its flag to true in settings/features.json when it is ready.

          dev            toggle development mode on/off
          dev on         force development mode on
          dev off        force development mode off
          dev status     show current state (without changing it)

        The state is session-only.  Pre-enable it in CI with ARC_DEV_MODE=1.
        """
        action = args[0].lower() if args else "toggle"

        if action == "status":
            self._print_dev_status()
            return
        if action in ("on", "enable", "true"):
            self._dev_mode = True
        elif action in ("off", "disable", "false"):
            self._dev_mode = False
        elif action == "toggle":
            self._dev_mode = not self._dev_mode
        else:
            console.print(
                f"[yellow]Usage:[/yellow] dev [on|off|status]  [dim](no argument toggles)[/dim]"
            )
            return
        self._print_dev_status()

    def _print_dev_status(self) -> None:
        """Print the current development-mode state and the dev-flag count."""
        dev_flags = [f for f in self._features if feature_state(self._features, f) == "dev"]
        if self._dev_mode:
            console.print(
                f"[magenta]● Development mode ON[/magenta] — "
                f"{len(dev_flags)} dev command group(s) now visible.  "
                f"[dim]Type 'dev off' to hide them again.[/dim]"
            )
        else:
            console.print(
                f"[dim]○ Development mode OFF[/dim] — "
                f"{len(dev_flags)} dev command group(s) hidden.  "
                f"[dim]Type 'dev' to reveal them.[/dim]"
            )

    def _cmd_setup(self, args: list[str]) -> None:  # noqa: C901 (acceptable complexity)
        """Interactive credential setup wizard.

        Auto-detects the host OS, asks two short questions (SCM auth method and
        SSH auth method), then prints the exact commands the operator needs to
        run — nothing is written to disk until the operator follows those steps.

        Side effects: prints to console only.  Does not modify any config files.
        """
        # If any args were given treat them as a passthrough to `help setup`.
        if args:
            from app.docs import render_help_topic  # Deferred: avoids circular at module level
            render_help_topic(console, "setup")
            return

        os_name = platform.system()  # "Darwin" | "Linux" | "Windows"
        os_label = {"Darwin": "macOS", "Linux": "Linux / WSL", "Windows": "Windows"}.get(os_name, os_name)
        keychain_name = {
            "Darwin":  "macOS Keychain",
            "Linux":   "Secret Service (libsecret) or config file",
            "Windows": "Windows Credential Manager",
        }.get(os_name, "the OS keychain")

        console.print()
        console.print("[bold cyan]ARC Credential Setup Wizard[/bold cyan]")
        console.print(f"[dim]Detected platform: {os_label}  ·  Secrets stored in: {keychain_name}[/dim]")
        console.print()

        # ── Question 1: SCM auth method ──────────────────────────────────────
        console.print(
            "[bold]Q1[/bold]  What SCM credentials do you have?\n"
            "  [bold cyan]1[/bold cyan]  A pre-issued bearer token\n"
            "  [bold cyan]2[/bold cyan]  OAuth client ID + secret  (service account)\n"
            "  [bold cyan]3[/bold cyan]  Neither — I need to create a service account first"
        )
        try:
            scm_choice = console.input("  → ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Setup cancelled.[/dim]")
            return

        if scm_choice not in ("1", "2", "3"):
            console.print("[yellow]Invalid choice — please type 1, 2, or 3.[/yellow]")
            return

        # ── Question 2: SSH auth method ──────────────────────────────────────
        console.print()
        console.print(
            "[bold]Q2[/bold]  How will you SSH to managed devices?\n"
            "  [bold cyan]1[/bold cyan]  SSH key file  (recommended — no password stored)\n"
            "  [bold cyan]2[/bold cyan]  Password"
        )
        try:
            ssh_choice = console.input("  → ").strip()
        except (EOFError, KeyboardInterrupt):
            console.print("\n[dim]Setup cancelled.[/dim]")
            return

        if ssh_choice not in ("1", "2"):
            console.print("[yellow]Invalid choice — please type 1 or 2.[/yellow]")
            return

        console.print()
        console.print("[bold]─── Steps to follow (run these outside ARC) ───[/bold]")
        console.print()

        # ── SCM instructions ─────────────────────────────────────────────────
        if scm_choice == "1":
            console.print("[bold cyan]SCM — bearer token:[/bold cyan]")
            _setup_bearer_instructions(console, os_name)
        elif scm_choice == "2":
            console.print("[bold cyan]SCM — OAuth client credentials:[/bold cyan]")
            _setup_oauth_instructions(console, os_name)
        else:
            console.print("[bold cyan]SCM — create a service account first:[/bold cyan]")
            console.print(
                "  1. Log in to https://stratacloudmanager.paloaltonetworks.com/\n"
                "  2. Navigate to Settings → Identity & Access → Service Accounts\n"
                "  3. Add a service account; copy Client ID, Client Secret, and TSG ID.\n"
                "     (The secret is shown only once — save it now.)\n"
                "  4. Come back and run [bold]setup[/bold] again — choose option 2 (OAuth)."
            )
            console.print()

        # ── SSH instructions ─────────────────────────────────────────────────
        if ssh_choice == "1":
            console.print()
            console.print("[bold cyan]SSH — key file:[/bold cyan]")
            console.print(
                "  # Generate a dedicated key (run once):\n"
                "  ssh-keygen -t ed25519 -f ~/.ssh/panos_key -C arc-panos\n\n"
                "  # Tell ARC to use it:\n"
                "  arc auth configure --ssh-key ~/.ssh/panos_key"
            )
        else:
            console.print()
            console.print("[bold cyan]SSH — password:[/bold cyan]")
            console.print(
                "  arc auth configure\n"
                "  # When prompted:\n"
                "  #   SSH username: admin\n"
                f"  #   SSH password: <paste>   ← stored in {keychain_name}"
            )

        # ── Final verification ────────────────────────────────────────────────
        console.print()
        console.print("[bold]─── Verify afterwards ───[/bold]")
        console.print(
            "  arc auth show    # confirm config values (secrets masked)\n"
            "  arc auth test    # live API call to SCM\n"
            "  Then restart ARC — the prompt should show [green]✓ SCM connected[/green]."
        )
        console.print()
        console.print(
            "[dim]Full setup guide: [bold]help setup[/bold]  ·  "
            "Platform details: [bold]help config osx[/bold] / [bold]help config nix[/bold] / [bold]help config win[/bold][/dim]"
        )
        console.print()


# ---------------------------------------------------------------------------
# Private helpers — per-platform SCM setup instructions.
# ---------------------------------------------------------------------------

def _setup_bearer_instructions(console, os_name: str) -> None:  # type: ignore[type-arg]
    """Print bearer-token setup commands for the detected OS."""
    if os_name == "Darwin":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored in macOS Keychain, NOT on disk\n\n"
            "  # Or store manually via the security CLI:\n"
            "  security add-generic-password -U -s arc -a arc.bearer.token -w YOUR_TOKEN"
        )
    elif os_name == "Windows":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored in Windows Credential Manager\n\n"
            "  # Or set for this PowerShell session only:\n"
            "  $env:SCM_BEARER_TOKEN = 'YOUR_TOKEN'"
        )
    else:
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 1 (bearer token)\n"
            "  #   Token: <paste>   ← stored via libsecret or config file (0600)\n\n"
            "  # Or set for this terminal session only:\n"
            "  export SCM_BEARER_TOKEN=your-bearer-token"
        )


def _setup_oauth_instructions(console, os_name: str) -> None:  # type: ignore[type-arg]
    """Print OAuth client credential setup commands for the detected OS."""
    if os_name == "Darwin":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored in macOS Keychain\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file"
        )
    elif os_name == "Windows":
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored in Windows Credential Manager\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file"
        )
    else:
        console.print(
            "  arc auth configure\n"
            "  # When prompted:\n"
            "  #   SCM auth method: 2 (OAuth)\n"
            "  #   Client ID:     <paste>  ← safe to store in config file\n"
            "  #   Client secret: <paste>  ← stored via libsecret / config file 0600\n"
            "  #   TSG ID:        <paste>  ← safe to store in config file\n\n"
            "  # Or export for this session:\n"
            "  export SCM_CLIENT_ID=...\n"
            "  export SCM_CLIENT_SECRET=...\n"
            "  export SCM_TSG_ID=..."
        )

