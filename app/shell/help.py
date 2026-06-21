"""ArcShell help mixin — The ? help system (inline / full / docs / verb options)."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)
from app.settings import command_structure


class HelpMixin:
    def _match_structured(self, prefix_tokens: list[str]) -> tuple[str | None, list[str]]:
        """Find the longest command key (with a structure spec) inside *prefix_tokens*.

        Returns ``(key, remainder_tokens)`` or ``(None, [])`` when no command in
        ``settings/command-structure.csv`` matches the typed prefix.
        """
        lowered = [t.lower() for t in prefix_tokens]
        for count in range(len(lowered), 0, -1):
            key = " ".join(lowered[:count])
            cmd_def = COMMANDS.get(key)
            if (
                cmd_def is not None
                and self._is_command_available(key, cmd_def)
                and command_structure.arg_spec(key) is not None
            ):
                return key, prefix_tokens[count:]
        return None, []

    def _print_context_help(self, prefix_tokens: list[str]) -> bool:
        """Print Cisco-style context-sensitive help for a structured command.

        ``<command> ?`` lists only the *next* syntax options — the fixed choices,
        a user-supplied variable, or the trailing keywords — driven by the
        command's structure.  Returns True when it handled the prefix (so the
        caller skips the generic full-help path); False when the command has no
        structure spec.
        """
        key, remainder = self._match_structured(prefix_tokens)
        if key is None:
            return False
        spec = command_structure.arg_spec(key)
        if spec is None:
            return False
        rows = command_structure.help_options(spec, remainder)
        self._render_context_help(rows)
        return True

    def _render_context_help(self, rows: list[dict]) -> None:
        """Render the next-option rows: ``  token   description`` (token column aligned)."""
        t = self._theme
        console.print()
        if not rows:
            # Nothing more to type — the command is complete.
            console.print("  <cr>")
            console.print()
            return
        width = max((len(row["token"]) for row in rows), default=4)
        width = max(width, 12)
        for row in rows:
            token_cell = self._styled(f"{row['token']:<{width}}", t.command_name)
            description = row.get("description") or ""
            if description:
                console.print(f"  {token_cell}  {description}")
            else:
                console.print(f"  {token_cell}")
        console.print()

    def _cmd_help(self, args: list[str]) -> None:
        """Print the command reference.

        Bare `?` / `help` is always context-aware.
        `help all` forces the full unfiltered reference.
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
            self._cmd_help_inline([])

    def _cmd_help_inline(self, prefix_tokens: list[str]) -> None:
        """Cisco-style compact inline help — one line per command, no panels.

        prefix_tokens empty  → 3-tier listing: global / folder / device / shell.
        prefix_tokens set    → all registered commands starting with that prefix.

        This is the `?` mode. It is intentionally compact and panel-free so
        operators get a fast visual scan — identical to how Cisco IOS presents
        context-sensitive completion help.
        """
        t = self._theme  # shorthand

        if prefix_tokens:
            # When the typed prefix is itself a complete command (e.g.
            # "packet-tracer", "show interface"), show how to use it — its usage
            # syntax — not just a bare <enter>.  Sub-command options (e.g.
            # "show jobs ?" → all | id) are still listed below.
            exact_key = " ".join(prefix_tokens).lower()
            exact_cmd = COMMANDS.get(exact_key)
            exact_available = exact_cmd is not None and self._is_command_available(exact_key, exact_cmd)

            options = self._collapsed_prefix_help_options(prefix_tokens)
            if exact_available:
                # The usage block covers "press enter to run", so drop the
                # generic <enter> row to avoid repeating the description.
                options = [(tok, desc) for tok, desc in options if tok != "<enter>"]

            if exact_available or options:
                console.print()
                if exact_available:
                    self._print_inline_usage(exact_key, exact_cmd)
                for token, desc in options:
                    token_cell = self._styled(f"{token:<20}", t.command_name)
                    if desc:
                        console.print(f"  {token_cell} {desc}")
                    else:
                        console.print(f"  {token_cell}")
                # Single footer covering both the docs pointer and the
                # progressive-help reminder (only the parts that apply).
                footer_parts: list[str] = []
                if exact_available:
                    footer_parts.append(f"{exact_key} help  → full docs & examples")
                if options:
                    footer_parts.append("Use ? progressively: e.g. show jobs ? -> all | id")
                if footer_parts:
                    console.print()
                    console.print(f"  {self._styled('  |  '.join(footer_parts), t.description_dim)}")
            else:
                prefix = " ".join(prefix_tokens).lower()
                _builtin_names = {
                    "cd", "connect", "remote", "folder", "tsg", "configure",
                    "pwd", "docs", "help", "clear", "exit", "quit",
                }
                if prefix in _builtin_names:
                    console.print(
                        f"\n  {self._styled(prefix, t.command_name)}  is a shell built-in.  "
                        f"Type [bold]{prefix} help[/bold] for full docs.\n"
                    )
                else:
                    console.print(
                        f"\n  [yellow]No commands match:[/yellow] [bold]{prefix}[/bold]  "
                        "— type [bold]?[/bold] for the full command list.\n"
                    )
            return

        # --- Bare ? or help — Cisco/Palo-style root prompt listing ---
        sh = t.section_header
        dd = t.description_dim

        console.print()

        root_verbs = self._root_verb_options()
        if root_verbs:
            hdr   = _section_label("commands_header", "COMMANDS")
            hint  = _section_label("commands_hint", "type <verb> ? for sub-commands")
            console.print(f"  {self._styled(hdr, sh)}  {self._styled(f'— {hint}', dd)}")
            for verb, desc in root_verbs:
                cmd_cell  = self._styled(f"{verb:<{_HELP_CMD_WIDTH}}", t.command_name)
                desc_text = self._styled(desc, t.description) if (desc and t.description) else desc
                console.print(f"    {cmd_cell} {desc_text}".rstrip())

        self._print_shell_builtins()

        console.print()
        console.print(f"  {self._styled(_help_footer(), dd)}")
        console.print()

    def _cmd_help_docs(self, topic: str) -> None:
        """Show the full documentation page for a command or topic.

        Resolution order:
        1. Render Markdown from docs/ when a matching file exists.
        2. Exact registry match — print inline description + context hint.
        3. Friendly fallback pointing the operator to ? or help all.

        Called by  `<command> help`  and  `help <topic>`.
        """
        # 1. Exact registry match. Disabled feature commands are treated as not
        # available, even if a generated Markdown page exists on disk.
        if topic in COMMANDS:
            cmd_def = COMMANDS[topic]
            if not self._is_command_available(topic, cmd_def):
                console.print(
                    f"\n[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
                    "  Type [bold]?[/bold] for available commands.\n"
                )
                return
            api_note = (
                "  [dim](API only — no SSH equivalent)[/dim]"
                if cmd_def.ssh_command is None
                else "  [dim](API + SSH via --remote)[/dim]"
            )
            console.print(
                f"\n[bold cyan]{topic}[/bold cyan]  —  {cmd_def.description}{api_note}\n"
                "  Append [bold]--remote[/bold] to run via SSH instead of the SCM API.\n"
            )
            self._print_context_hint_for(topic)
            return

        # 2. Try docs/ Markdown page (covers built-ins and general topics).
        if render_help_topic(console, topic):
            return

        # 3. Nothing found.
        console.print(
            f"\n[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
            "  Type [bold]?[/bold] for available commands  |  "
            "[bold]help all[/bold] for the full reference\n"
        )

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
            title="Full Command Reference  (help all)", border_style="cyan",
        ))

        for category, keys in sorted(CATEGORIES.items()):
            available_keys = [
                key for key in sorted(keys)
                if self._is_command_available(key, COMMANDS[key])
            ]
            if not available_keys:
                continue
            console.print(f"\n[bold yellow]{category.upper()}[/bold yellow]")
            for k in available_keys:
                cmd = COMMANDS[k]
                scope_tag = (
                    "  [dim][global][/dim]" if cmd.scope == "global"
                    else "  [dim][device][/dim]" if cmd.scope == "device"
                    else ""
                )
                ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command else ""
                console.print(f"  [cyan]{k:<{_HELP_CMD_WIDTH + 2}}[/cyan] {cmd.description}{scope_tag}{ssh_note}")

        self._print_shell_builtins()
        console.print()

    def _cmd_show_write_help(self, verb: str) -> None:
        """Show available delete/update commands in configure mode."""
        t = self._theme
        dd = t.description_dim
        _LABELS = {
            "delete": ("delete — Remove configuration objects", "No delete commands enabled. Enable flags: feature enable delete_objects"),
            "update": ("update — Modify existing objects (GET→merge→PUT)", "No update commands enabled. Run: feature enable update_objects"),
        }
        label, empty_msg = _LABELS.get(verb, (verb, f"No {verb} commands enabled."))
        matching = [
            (k, v.description) for k, v in COMMANDS.items()
            if k.startswith(f"{verb} ") and self._is_command_available(k, v)
        ]
        console.print()
        console.print(f"  [bold yellow]{label}[/bold yellow]  [dim](configure mode)[/dim]")
        console.print()
        if matching:
            for k, desc in sorted(matching):
                cmd_cell = self._styled(f"{k:<50}", t.command_name)
                console.print(f"    {cmd_cell} {self._styled(desc, dd)}")
        else:
            console.print(f"  [dim]{empty_msg}[/dim]")
        console.print()

    def _print_shell_builtins(self) -> None:
        """Print the shell built-in commands section (shared by inline and full help)."""
        t = self._theme
        hdr  = _section_label("shell_header", "SHELL")
        hint = _section_label("shell_hint", "navigation & session")
        console.print(
            f"\n  {self._styled(hdr, t.section_header)}  "
            f"{self._styled(f'— {hint}', t.description_dim)}"
        )
        for row in shell_help_rows(self._state.configure_mode):
            name = row.name
            desc = row.description
            cmd_cell = self._styled(f"{name:<{_HELP_CMD_WIDTH}}", t.command_name)
            console.print(f"    {cmd_cell} {desc}")

    def _is_command_available(self, key: str, cmd_def: CommandDef) -> bool:
        """Return True when a registered command is executable in the current context."""
        if cmd_def.scope == "device" and not self._state.device:
            return False
        if key == "commit" and not self._state.configure_mode:
            return False
        # Feature-flagged commands are hidden when the flag is off (or "dev"
        # while development mode is inactive).
        if not is_enabled(self._features, cmd_def.feature_flag, self._dev_mode):
            return False
        return True

    @staticmethod
    def _is_config_command(key: str, cmd_def: CommandDef) -> bool:
        """Return True when a command should appear in configure-mode `?` help."""
        del cmd_def
        # Configure mode keeps write workflows and read-only show navigation.
        return key == "commit" or key.startswith("show ")

    def _root_verb_options(self) -> list[tuple[str, str]]:
        """Return top-level verb stems for bare `?` — Cisco/Palo root-prompt style.

        Collapses every available command down to its first token, then deduplicates.
        'show devices', 'show address', 'show jobs' → just one entry: 'show'.
        Descriptions come from config/cli-structure.yaml (editable without code changes).
        In configure mode, also shows 'set' since it's the primary write verb.
        """
        verb_counts: dict[str, int] = {}
        for key, cmd_def in COMMANDS.items():
            if not self._is_command_available(key, cmd_def):
                continue
            if self._state.configure_mode and not self._is_config_command(key, cmd_def):
                continue
            verb = key.split()[0]
            verb_counts[verb] = verb_counts.get(verb, 0) + 1

        # In configure mode, always show 'set', 'update', and 'delete' as primary write verbs.
        if self._state.configure_mode:
            verb_counts.setdefault("set", 1)
            verb_counts.setdefault("update", 1)
            verb_counts.setdefault("delete", 1)

        options: list[tuple[str, str]] = []
        for verb in sorted(verb_counts):
            # A verb that is itself a complete command (e.g. packet-tracer,
            # commit) takes its description from the command — which honours the
            # doc front-matter — so editing that doc updates bare `?`.
            # Multi-command verbs (show, set, …) use cli-structure.yaml.
            if verb in COMMANDS:
                desc = COMMANDS[verb].description
            else:
                desc = _verb_description(verb, verb_counts[verb])
            options.append((verb, desc))

        return options

    def _collapsed_prefix_help_options(
        self,
        prefix_tokens: list[str],
        scope: Optional[str] = None,
    ) -> list[tuple[str, str]]:
        """Return collapsed next-token help options for a command prefix.

        This mirrors Cisco-style progressive help: users type a partial command
        and `?` shows only the next valid token(s) rather than every full command.
        """
        prefix = [p.lower() for p in prefix_tokens]

        option_map: dict[str, list[str]] = {}
        exact_matches: list[str] = []

        for key, cmd_def in COMMANDS.items():
            if scope is not None and cmd_def.scope != scope:
                continue
            if not self._is_command_available(key, cmd_def):
                continue
            if self._state.configure_mode and not self._is_config_command(key, cmd_def):
                continue

            cmd_tokens = key.split()
            if len(cmd_tokens) < len(prefix):
                continue
            if not all(cmd_tokens[i].startswith(prefix[i]) for i in range(len(prefix))):
                continue

            if len(cmd_tokens) == len(prefix):
                # Exact/full command completion (allow Enter now).
                if all(cmd_tokens[i] == prefix[i] for i in range(len(prefix))):
                    exact_matches.append(key)
                else:
                    # Same token count but current token still ambiguous (e.g. device -> devices).
                    token = cmd_tokens[-1]
                    option_map.setdefault(token, []).append(key)
                continue

            next_token = cmd_tokens[len(prefix)]
            option_map.setdefault(next_token, []).append(key)

        options: list[tuple[str, str]] = []
        if exact_matches:
            desc = COMMANDS[exact_matches[0]].description if len(exact_matches) == 1 else "Complete command"
            options.append(("<enter>", desc))

        for token in sorted(option_map):
            keys = option_map[token]
            # Use command description when token maps cleanly to one leaf command.
            desc = ""
            if len(keys) == 1:
                desc = COMMANDS[keys[0]].description
            options.append((token, desc))

        return options

    def _collapsed_tier_help_options(self, scope: str) -> list[tuple[str, str]]:
        """Return collapsed bare-tier help options for one scope.

        For multi-token commands, show a two-token stem so bare `?` is concise
        but still useful (e.g. `show jobs` instead of only `show`).
        """
        eligible: list[str] = []
        for key, cmd_def in COMMANDS.items():
            if cmd_def.scope != scope:
                continue
            if not self._is_command_available(key, cmd_def):
                continue
            if self._state.configure_mode and not self._is_config_command(key, cmd_def):
                continue
            eligible.append(key)

        if not eligible:
            return []

        stem_map: dict[str, list[str]] = {}
        for key in eligible:
            tokens = key.split()
            if len(tokens) >= 2:
                stem = " ".join(tokens[:2])
            else:
                stem = tokens[0]
            stem_map.setdefault(stem, []).append(key)

        options: list[tuple[str, str]] = []
        for stem in sorted(stem_map):
            keys = stem_map[stem]
            desc = ""
            if len(keys) == 1 and keys[0] == stem:
                desc = COMMANDS[keys[0]].description
            options.append((stem, desc))
        return options

    def _context_annotation(self, command_key: str) -> str:
        """Return a short inline context note for commands whose output depends on state.

        Folder-scope commands show the active folder.
        Device-scope commands show the active device when one is set.
        Returns an empty string when there is nothing context-specific to note.
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
        """Print a one-line context note below an exact-match docs result."""
        note = self._context_annotation(command_key)
        if note:
            console.print(f"[dim]Current context:[/dim]{note}")

    def _print_inline_usage(self, key: str, cmd_def: CommandDef) -> None:
        """Print the description + usage syntax for a complete command in `?` help.

        Shows how to invoke the command (its arguments/options).  When a command
        has no explicit ``usage`` string, the command name itself is shown as the
        minimal usage.  The ``<command> help`` pointer is printed by the caller's
        footer, so this method ends after the usage block.
        """
        t = self._theme
        usage = cmd_def.usage or key
        remote_hint = (
            "  [dim](append --remote to run on the device via SSH)[/dim]"
            if cmd_def.ssh_command is not None else ""
        )

        # Header: command name + one-line description.
        desc = (
            self._styled(cmd_def.description, t.description)
            if (cmd_def.description and t.description) else cmd_def.description
        )
        console.print(f"  {self._styled(key, t.command_name)}  {desc}")
        console.print()
        console.print(f"  {self._styled('Usage:', t.section_header)}")
        for index, line in enumerate(usage.split("\n")):
            suffix = remote_hint if index == 0 else ""
            console.print(f"    {line}{suffix}")

