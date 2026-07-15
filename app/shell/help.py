"""ArcShell help mixin — The ? help system (inline / full / docs / verb options)."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)
from app.settings import command_structure


class HelpMixin:
    def _match_structured(self, prefix_tokens: list[str]) -> tuple[str | None, list[str]]:
        """Find the longest command key (with a structure spec) inside *prefix_tokens*.

        Returns ``(key, remainder_tokens)`` or ``(None, [])`` when no command in
        ``settings/command-structure.json`` matches the typed prefix.
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
        console.print()
        if not rows:
            # Nothing more to type — the command is complete.
            console.print("  <cr>")
            console.print()
            return
        width = max((len(row["token"]) for row in rows), default=4)
        width = max(width, 12)
        for row in rows:
            token_cell = self._help_cell(row['token'], width=width)
            description = row.get("description") or ""
            if description:
                console.print(f"  {token_cell}  {description}")
            else:
                console.print(f"  {token_cell}")
        console.print()

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
                    token_cell = self._help_cell(token, width=20)
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
            elif exact_cmd is not None:
                # Command exists in the registry but isn't available right now
                # (wrong context — no device, not in configure mode, etc.).
                # Show the description and a context hint rather than "Unknown command".
                console.print()
                self._print_inline_usage(exact_key, exact_cmd)
                if self.resolve_scope(exact_key, exact_cmd) == "device" and not self._state.device:
                    console.print(
                        f"  [dim]Requires device context — "
                        f"[bold]cd <device>[/bold] first, or "
                        f"[bold]{exact_key} --remote <device>[/bold][/dim]"
                    )
                console.print(f"  [dim]{exact_key} help[/dim]  → full docs & examples")
                console.print()
            else:
                prefix = " ".join(prefix_tokens).lower()
                _builtin_names = {
                    "cd", "connect", "folder", "tsg", "configure",
                    "pwd", "docs", "help", "clear", "exit", "quit",
                }
                if prefix in _builtin_names:
                    # Special handling for setup - show config help
                    if prefix == "setup":
                        self._show_command_not_found([prefix])
                    else:
                        console.print(
                            f"\n  {self._styled(prefix, t.command_name)}  is a shell built-in.  "
                            f"Type [bold]{prefix} help[/bold] for full docs.\n"
                        )
                else:
                    # Prefix-only input (not an exact command) — show which next
                    # words exist in the registry, regardless of current context.
                    pfx = " ".join(prefix_tokens).lower()
                    next_words: dict[str, str] = {}
                    for key, cmd_def in COMMANDS.items():
                        if not self._is_command_visible(key, cmd_def):
                            continue
                        if not key.lower().startswith(pfx + " "):
                            continue
                        nw = key[len(pfx)+1:].split()[0]
                        if nw not in next_words:
                            desc = cmd_def.description if len(key.split()) == len(prefix_tokens) + 1 else ""
                            next_words[nw] = desc
                    if next_words:
                        console.print()
                        w = max(len(k) for k in next_words)
                        for nw in sorted(next_words):
                            token_cell = self._help_cell(nw, width=max(w, 12))
                            desc = next_words[nw]
                            if desc:
                                console.print(f"  {token_cell}  {desc}")
                            else:
                                console.print(f"  {token_cell}")
                        console.print()
                    else:
                        self._show_command_not_found(prefix_tokens)
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
                cmd_cell  = self._help_cell(verb)
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
        """Print the full command reference regardless of context.
        
        Uses pagination automatically since this is a long output.
        """
        def _print_full_help():
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
                    eff_scope = self.resolve_scope(k, cmd)
                    scope_tag = (
                        "  [dim][global][/dim]" if eff_scope == "global"
                        else "  [dim][device][/dim]" if eff_scope == "device"
                        else ""
                    )
                    ssh_note = " [dim](SSH)[/dim]" if cmd.ssh_command else ""
                    console.print(f"  [cyan]{k:<{_HELP_CMD_WIDTH + 2}}[/cyan] {cmd.description}{scope_tag}{ssh_note}")

            self._print_shell_builtins()
            console.print()
        
        # Page the full reference only when the user enabled paging
        # (`terminal length <n>`; 0 = print everything).
        if page_length() > 0:
            with console.pager(styles=True):
                _print_full_help()
        else:
            _print_full_help()

    def _cmd_show_write_help(self, verb: str) -> None:
        """Show available set/delete/update commands in configure mode."""
        t = self._theme
        dd = t.description_dim
        _LABELS = {
            "set":    ("set — Create or modify configuration objects", "No set commands enabled. Run: feature enable <flag>"),
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
                cmd_cell = self._help_cell(k, width=50)
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
        for row in shell_help_rows(self._state.configure_mode, dev_mode=self._dev_mode):
            name = row.name
            desc = row.description
            cmd_cell = self._help_cell(name)
            console.print(f"    {cmd_cell} {desc}")

    def _is_command_visible(self, key: str, cmd_def: CommandDef) -> bool:
        """Single source of truth: does this command appear in ``?`` for this operator?

        Context-independent gates only — settings/builtin-commands.json visibility
        (honoring dev mode for "hidden" state) and the feature flag
        (settings/features/, honoring dev mode).
        Dispatch, tab completion, and help must all use this same check.
        """
        if not is_command_visible(key, self._command_visibility, self._dev_mode):
            return False
        # A disabled area is a master OFF switch — its commands vanish from ?,
        # completion and help (and are blocked at execution; see dispatch).
        if getattr(cmd_def, "category", "") in getattr(self, "_disabled_areas", set()):
            return False
        return is_feature_visible(self._features, cmd_def.feature_flag, self._dev_mode)


    def _cmd_find(self, args: list[str]) -> None:
        """PAN-OS style command search: ``find command <text>``.

        Searches ALL registered commands (including feature-disabled ones —
        finding hidden capability is the point) by key and description. Each
        row shows the gating flag and its state so the operator can enable
        what they found. Composable: ``find command address | match cngfw``.

        Sub-commands:
          command <text>   Search all registered commands by name or description
        """
        tokens = list(args)
        if tokens and tokens[0] in ("?", "help"):
            console.print(
                "\n  [bold]find[/bold]  — search commands and configuration\n\n"
                "  [cyan]find command <text>[/cyan]              Search all commands by name or description\n"
                "  [cyan]find command <text> | match <w>[/cyan]  Narrow results further\n\n"
                "  [dim]Searches both the command name and its description.\n"
                "  Shows every command including disabled ones (with their feature flag).\n"
                "  Example:  find command bgp\n"
                "            find command address | match group[/dim]\n"
            )
            return
        # Accept legacy syntax "find command keyword <text>" and "find command <text>"
        if [t.lower() for t in tokens[:2]] == ["command", "keyword"]:
            tokens = tokens[2:]
        elif tokens and tokens[0].lower() == "command":
            tokens = tokens[1:]
        else:
            sub = tokens[0].lower() if tokens else ""
            console.print(
                f"[yellow]Unknown find sub-command:[/yellow] [bold]{sub or '(none)'}[/bold]\n"
                "  Available: [cyan]find command <text>[/cyan]"
            )
            return
        pattern = " ".join(tokens).strip().lower()
        if not pattern:
            console.print(
                "[yellow]Usage:[/yellow] find command <text>\n"
                "  [dim]e.g. find command address   |   find command bgp | match peer[/dim]"
            )
            return

        matches = [
            (key, cmd_def) for key, cmd_def in COMMANDS.items()
            if pattern in key.lower() or pattern in (cmd_def.description or "").lower()
        ]
        if not matches:
            console.print(f"[yellow]No commands match:[/yellow] [bold]{pattern}[/bold]")
            return

        # Useful verbs first, debug noise last; key matches beat description-only.
        verb_rank = {"show": 0, "set": 1, "update": 2, "delete": 3, "clear": 4,
                     "request": 5, "test": 6, "ping": 6, "traceroute": 6}
        matches.sort(key=lambda kv: (
            pattern not in kv[0].lower(),
            verb_rank.get(kv[0].split()[0], 8 if kv[0].startswith("debug") else 7),
            kv[0],
        ))

        shown = matches[:100]
        console.print()
        for key, cmd_def in shown:
            state = feature_state(self._features, cmd_def.feature_flag)
            if not cmd_def.feature_flag or state == "on":
                marker, flag_note = "[green]on [/green]", ""
            elif state == "dev":
                marker, flag_note = "[magenta]dev[/magenta]", f"  [dim]{cmd_def.feature_flag}[/dim]"
            else:
                marker, flag_note = "[red]off[/red]", f"  [dim]{cmd_def.feature_flag}[/dim]"
            console.print(f"  {self._help_cell(key)} {marker}{flag_note}")
        footer = f"{len(matches)} command(s) match '{pattern}'"
        if len(matches) > len(shown):
            footer += f" — showing {len(shown)}; narrow the keyword or pipe: | match <text>"
        console.print(f"\n[dim]{footer}  |  off → feature enable <flag>[/dim]\n")

    def _visible_command_keys(self) -> list[str]:
        """Cached list of visible registry keys — the per-keystroke hot path.

        With the PAN-OS catalog the registry holds ~3k keys; recomputing
        visibility per keystroke costs milliseconds. Invalidated whenever a
        feature flag or dev mode changes (_invalidate_visible_keys).
        """
        cache = getattr(self, "_visible_keys_cache", None)
        if cache is None:
            cache = [k for k, v in COMMANDS.items() if self._is_command_visible(k, v)]
            self._visible_keys_cache = cache
        return cache

    def _invalidate_visible_keys(self) -> None:
        self._visible_keys_cache = None

    def resolve_scope(self, key: str, cmd_def: CommandDef) -> str:
        """Return the effective run scope for a command.

        The code-default ``CommandDef.scope`` is the source of truth; an operator
        may override it per command (see settings/features/ ``_scope_overrides``),
        loaded into ``self._scope_overrides`` and updated live by the feature
        editor / CLI.  Used by availability checks and help scope tags so the
        GUI, CLI, and enforcement all agree.
        """
        overrides = getattr(self, "_scope_overrides", None) or {}
        return overrides.get(key, cmd_def.scope)

    def _is_command_available(self, key: str, cmd_def: CommandDef) -> bool:
        """_is_command_visible plus the current-context gates.

        A visible command is still unavailable when it needs a device context
        (scope="device" with no `cd <device>`) or configure mode (`commit`,
        `set *`, `delete *`, `update *`, `load *`).
        """
        if not self._is_command_visible(key, cmd_def):
            return False
        if self.resolve_scope(key, cmd_def) == "device" and not self._state.device:
            return False
        _configure_only = key == "commit" or key.startswith(
            ("set ", "delete ", "update ", "load ")
        )
        if _configure_only and not self._state.configure_mode:
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
            # Respect verb-level visibility from cli-structure.yaml.
            if not _verb_visible(verb, dev_mode=self._dev_mode):
                continue
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
            if scope is not None and self.resolve_scope(key, cmd_def) != scope:
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
            if self.resolve_scope(key, cmd_def) != scope:
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

        eff_scope = self.resolve_scope(command_key, cmd)
        if eff_scope == "folder":
            return f"  [dim]→ folder: {folder}[/dim]"

        if eff_scope == "device" and device:
            device_name = device_display_name(device)
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
