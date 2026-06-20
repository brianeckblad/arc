"""ArcShell write_cmd mixin — set / set folder (create) write operations."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class WriteMixin:
    def _cmd_set(self, args: list[str]) -> None:
        """Create or modify SCM configuration objects (configure mode only).

        Mirrors PAN-OS `set` syntax.  All write operations require configure
        mode — `set` outside configure mode prints a friendly error.

        Usage:
          set folder <name>                  Create a folder (prompts for parent)
          set folder <name> parent <parent>  Create a folder under a specific parent
          set folder new subfolder <name>    Create a subfolder under the active folder
          set ?                              Show available set sub-commands
        """
        if not self._state.configure_mode:
            console.print(
                "[yellow]Write operation blocked:[/yellow] 'set' requires configure mode.\n"
                "  Type [bold]configure[/bold] first, then use [bold]set[/bold]."
            )
            return

        # `set ?` — show what set can do
        if not args or (len(args) == 1 and args[0] == "?"):
            t = self._theme
            console.print()
            console.print(f"  {self._styled('set — Create or modify configuration', t.section_header)}")
            console.print()
            set_ops = [
                ("set folder <name>",                   "Create a folder (prompts for parent placement)"),
                ("set folder <name> parent <parent>",   "Create a folder under a specific parent"),
                ("set folder new subfolder <name>",     "Create a subfolder under the active folder"),
            ]
            for cmd_str, desc in set_ops:
                cmd_cell = self._styled(f"{cmd_str:<50}", t.command_name)
                console.print(f"    {cmd_cell} {self._styled(desc, t.description_dim)}")
            console.print()
            console.print(f"  {self._styled('<set command> help  → full docs  |  exit → leave configure mode', t.description_dim)}")
            console.print()
            return

        sub = args[0].lower()

        # `set <resource> ?` — user wants help on a specific resource
        if len(args) >= 2 and args[-1] == "?":
            resource = sub
            candidate_key = f"set {resource}"
            if candidate_key in COMMANDS:
                cmd_def = COMMANDS[candidate_key]
                flag = cmd_def.feature_flag
                if flag and not is_enabled(self._features, flag, self._dev_mode):
                    console.print(
                        f"\n  [bold cyan]{candidate_key}[/bold cyan]  [dim]— {cmd_def.description}[/dim]\n\n"
                        f"  [yellow]Feature not enabled.[/yellow]  Flag: [bold]{flag}[/bold]\n"
                        f"  Enable with: [bold]feature enable {flag}[/bold]\n"
                        f"  Then run:    [bold]{candidate_key} help[/bold]  for full usage.\n"
                    )
                else:
                    from app.docs import render_help_topic as _rht
                    if not _rht(console, f"set-{resource}"):
                        console.print(f"  [bold]{candidate_key}[/bold]  —  {cmd_def.description}")
            else:
                console.print(
                    f"\n  [yellow]No 'set {resource}' command found.[/yellow]\n"
                    "  Type [bold]set ?[/bold] to see all create operations.\n"
                    "  Type [bold]feature enable ?[/bold] to see commands that can be enabled.\n"
                )
            return

        # ── set folder ──────────────────────────────────────────────────
        if sub == "folder":
            # `set folder ?` — show folder sub-commands
            if args[1:] == ["?"] or args[1:] == ["?"]:
                console.print(
                    "\n  [bold yellow]set folder[/bold yellow]  — create SCM folders\n\n"
                    "    [cyan]set folder <name>[/cyan]                  Create a folder (interactive parent selection)\n"
                    "    [cyan]set folder <name> parent <parent>[/cyan]  Create with an explicit parent\n"
                    "    [cyan]set folder new subfolder <name>[/cyan]    Create subfolder under the active folder\n"
                )
                return
            self._cmd_set_folder(args[1:])
            return

        # Before saying "unknown" — check if a matching `set <sub>` command exists
        # in the registry but is feature-disabled.  If so, give a targeted message.
        candidate_key = f"set {sub}"
        if candidate_key in COMMANDS:
            cmd_def = COMMANDS[candidate_key]
            flag = cmd_def.feature_flag
            if flag and not is_enabled(self._features, flag, self._dev_mode):
                console.print(
                    f"[yellow]Feature not enabled:[/yellow] [bold]{candidate_key}[/bold]\n"
                    f"  Flag [bold]{flag}[/bold] is currently off.\n"
                    f"  To enable this session: [bold]feature enable {flag}[/bold]\n"
                    f"  To persist: add [bold]{{\"{flag}\": true}}[/bold] to [bold]settings/features.json[/bold]\n"
                    f"  Or use env var: [bold]ARC_FEATURE_{flag.upper()}=1 arc[/bold]"
                )
            else:
                # Command exists but something else is wrong
                console.print(
                    f"[yellow]Cannot run:[/yellow] [bold]{candidate_key}[/bold]  "
                    "— type [bold]set ?[/bold] to see available create operations."
                )
        else:
            console.print(
                f"[yellow]Unknown set sub-command:[/yellow] [bold]{sub}[/bold]\n"
                "  Type [bold]set ?[/bold] to see available create operations.\n"
                f"  Tip: [bold]feature enable ?[/bold] shows commands that can be enabled."
            )

    def _cmd_set_folder(self, args: list[str]) -> None:
        """Create an SCM folder via the set command.

        set folder <name>                  — interactive parent selection
        set folder <name> parent <parent>  — explicit parent
        set folder new subfolder <name>    — subfolder under active folder
        """
        if not args:
            console.print(
                "[yellow]Usage:[/yellow]\n"
                "  set folder <name>                  — create a folder\n"
                "  set folder <name> parent <parent>  — create with explicit parent\n"
                "  set folder new subfolder <name>    — create subfolder under active folder"
            )
            return

        # `set folder new subfolder <name>` — create under current folder
        if len(args) >= 3 and args[0].lower() == "new" and args[1].lower() == "subfolder":
            subfolder_name = " ".join(args[2:])
            if not subfolder_name:
                console.print("[yellow]Usage:[/yellow] set folder new subfolder <name>")
                return
            parent = self._state.folder  # create under the active folder
            if not self._scm:
                console.print("[red]SCM not configured — cannot create folders.[/red]")
                return
            try:
                self._scm.create_folder(subfolder_name, parent)
                console.print(
                    f"[green]✓[/green] Folder [bold]{subfolder_name}[/bold] created under [bold]{parent}[/bold]."
                )
                self._refresh_folders(silent=True)
            except Exception as exc:
                console.print(f"[red]Failed to create subfolder:[/red] {exc}")
            return

        # `set folder <name> parent <parent>` — explicit parent
        folder_name = args[0]
        if len(args) >= 3 and args[1].lower() == "parent":
            parent_name = " ".join(args[2:])
            if not self._scm:
                console.print("[red]SCM not configured — cannot create folders.[/red]")
                return
            try:
                self._scm.create_folder(folder_name, parent_name)
                console.print(
                    f"[green]✓[/green] Folder [bold]{folder_name}[/bold] created under [bold]{parent_name}[/bold]."
                )
                self._refresh_folders(silent=True)
            except Exception as exc:
                console.print(f"[red]Failed to create folder:[/red] {exc}")
            return

        # `set folder <name>` — interactive parent selection
        self._cmd_folder_create(folder_name)
