"""ArcShell dispatch mixin — the line dispatcher (parses + routes every command)."""
from __future__ import annotations

import difflib  # For fuzzy command matching

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class DispatchMixin:
    def _show_command_not_found(self, tokens: list[str]) -> None:
        """Show a helpful message when a command is not recognized.
        
        Special handling for common cases like 'setup' or 'config' to guide
        users to the correct help resources.
        """
        cmd_text = " ".join(tokens)
        first_word = tokens[0].lower() if tokens else ""
        
        # Special case: setup/config-related terms
        config_terms = ["setup", "config", "configure", "configuration", "credential", "auth", "login"]
        if first_word in config_terms or any(word in config_terms for word in [t.lower() for t in tokens]):
            console.print(
                f"\n[yellow]No command:[/yellow] [bold]{cmd_text}[/bold]\n\n"
                "[cyan]Looking for setup/configuration help?[/cyan]\n\n"
                "  [bold]Platform-specific guides:[/bold]\n"
                "    • [cyan]help config osx[/cyan]      — macOS (Keychain, Touch ID)\n"
                "    • [cyan]help config nix[/cyan]      — Linux (libsecret / Secret Service)\n"
                "    • [cyan]help config win[/cyan]      — Windows (Credential Manager)\n"
                "    • [cyan]help config generate[/cyan] — generate a starter config file\n"
                "    • [cyan]help configuration[/cyan]   — full configuration reference\n\n"
                "  [bold]Configuration commands:[/bold]\n"
                "    • [cyan]arc auth configure[/cyan]   — (outside shell) credential setup wizard\n"
                "    • [cyan]arc config generate[/cyan]  — (outside shell) create config file\n"
            )
            return
        
        # Try fuzzy matching against available commands
        all_commands = list(_SHELL_BUILTINS) + list(COMMANDS.keys())
        # Filter to visible commands
        def _feature_visible(command_def: CommandDef) -> bool:
            return is_enabled(self._features, command_def.feature_flag, self._dev_mode)
        
        visible_commands = [
            cmd for cmd in all_commands 
            if cmd not in COMMANDS or _feature_visible(COMMANDS[cmd])
        ]
        
        # Get fuzzy matches
        matches = difflib.get_close_matches(first_word, visible_commands, n=5, cutoff=0.5)
        
        if matches:
            console.print(
                f"\n[yellow]Unknown command:[/yellow] [bold]{cmd_text}[/bold]\n\n"
                "[cyan]Did you mean:[/cyan]\n"
            )
            for match in matches:
                console.print(f"  • [cyan]{match}[/cyan]")
            console.print(
                "\nType [bold]?[/bold] for all commands or [bold]help[/bold] for docs."
            )
        else:
            console.print(
                f"\n[yellow]Unknown command:[/yellow] [bold]{cmd_text}[/bold]\n"
                "Type [bold]?[/bold] for all commands or [bold]help <topic>[/bold] for docs."
            )

    def _dispatch(self, line: str) -> bool:
        """Process one input line.  Returns True when the user wants to exit ARC."""
        # Normalize whitespace: collapse tabs and multiple spaces to a single space.
        line = re.sub(r"[ \t]+", " ", line).strip()
        # Strip --remote flag before any other parsing.
        # Quote-aware tokenization: a value with spaces must be quoted, e.g.
        #   set address "My Host" fqdn x description "DMZ network"
        # so quoted segments stay single tokens (vendor-CLI / shell convention).
        remote = False
        tokens = tokenize(line)
        if "--remote" in tokens:
            remote = True
            tokens = [t for t in tokens if t != "--remote"]

        if not tokens:
            return False

        def _feature_visible(command_def: CommandDef) -> bool:
            """Return True when a registered command's feature flag is visible."""
            return is_enabled(self._features, command_def.feature_flag, self._dev_mode)

        # Cisco-style shorthand expansion:
        #   e            -> exit
        #   sh sec pol   -> show security policy
        # Expansion occurs only when a prefix resolves to exactly one command.
        visible_command_keys = [k for k, v in COMMANDS.items() if _feature_visible(v)]
        phrases = [[b] for b in _SHELL_BUILTINS if b != "?"] + [k.split() for k in visible_command_keys]

        # Detect a trailing help trigger: '?' (brief, context-sensitive).
        # Cisco/Palo-style: single ? shows next options. Use "<command> help" for full docs.
        help_token = "?" if "?" in tokens else None

        # Expand the command/topic portion before trailing "help".
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            tokens = _expand_unambiguous_prefix(tokens[:-1], phrases) + ["help"]

        # Expand prefix before the '?' context-help trigger.
        if help_token is not None:
            qidx = tokens.index(help_token)
            tokens = _expand_unambiguous_prefix(tokens[:qidx], phrases) + tokens[qidx:]
        else:
            tokens = _expand_unambiguous_prefix(tokens, phrases)

        # "<command> help" — trailing 'help' opens the full docs page for that command.
        # This must be checked before any individual builtin dispatcher so that
        # e.g. "cd help" shows docs instead of treating "help" as a device name.
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            topic = " ".join(tokens[:-1]).lower()
            topic_cmd = COMMANDS.get(topic)
            if topic_cmd is not None and not _feature_visible(topic_cmd):
                console.print(
                    f"\n[yellow]No docs found for:[/yellow] [bold]{topic}[/bold]\n"
                    "  Type [bold]?[/bold] for available commands.\n"
                )
                return False
            self._cmd_help_docs(topic)
            return False

        # Cisco/Palo-style context help: a trailing '?' shows the next syntax options.
        # Use "<command> help" for full documentation instead of ??.
        if help_token is not None:
            question_idx = tokens.index(help_token)
            prefix_tokens = tokens[:question_idx]
            if prefix_tokens:
                # Always restore the prompt prefix after displaying ? help so the operator
                # can continue typing without re-entering what they had.
                # For sub-command variants (feature enable ?, set address ?) restore
                # the immediate parent prefix (e.g. "feature enable " or "set ").
                self._pending_default = " ".join(prefix_tokens) + " "

                # Brief '?' on a structured command → next syntax options only.
                if self._print_context_help(prefix_tokens):
                    return False

                # Special case: `set ?` / `set <sub> ?` in configure mode.
                if prefix_tokens[0].lower() == "set" and self._state.configure_mode:
                    self._cmd_set(prefix_tokens[1:] + ["?"])
                    return False
                # Special case: `delete ?` in configure mode.
                if prefix_tokens[0].lower() == "delete" and self._state.configure_mode:
                    self._cmd_show_write_help("delete")
                    return False
                # Special case: `update ?` in configure mode.
                if prefix_tokens[0].lower() == "update" and self._state.configure_mode:
                    self._cmd_show_write_help("update")
                    return False
                # Special case: `feature ?` / `feature enable ?` / `feature disable ?`
                if prefix_tokens[0].lower() == "feature":
                    self._cmd_feature(prefix_tokens[1:] + ["?"])
                    return False
                # General case: prefix help for registered commands.
                self._cmd_help_inline(prefix_tokens)
                return False
            # Fall through so the bare "?" branch below fires

        cmd = tokens[0].lower()

        # ---- exit / quit ----
        if cmd in ("exit", "quit"):
            if self._state.configure_mode:
                self._state.configure_mode = False
                console.print("[cyan]Exited configure mode.[/cyan]")
                return False
            return True


        # ---- Shell built-ins ----
        if cmd == "clear":
            console.clear()
            return False

        if cmd == "pwd":
            self._cmd_pwd()
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

        if cmd == "account":
            self._cmd_account(tokens[1:])
            return False

        if cmd == "configure":
            self._cmd_configure(tokens[1:])
            return False

        if cmd == "cli":
            self._cmd_cli(tokens[1:])
            return False

        if cmd == "feature":
            self._cmd_feature(tokens[1:])
            return False

        if cmd == "setup":
            self._cmd_setup(tokens[1:])
            return False

        # Hidden command — not advertised in ? or tab completion.  Reveals
        # commands whose feature flag is "dev" (work-in-progress).
        if cmd == "dev":
            self._cmd_dev(tokens[1:])
            return False

        if cmd in ("set", "delete", "update"):
            matched_write: tuple[str, CommandDef, dict] | None = None
            if len(tokens) >= 2 and tokens[1].lower() not in ("?", "folder"):
                key, cmd_def, cmd_args = match_command(tokens)
                if key is not None:
                    if not _feature_visible(cmd_def):
                        console.print(
                            f"[red]Unknown command:[/red] [bold]{' '.join(tokens)}[/bold]  "
                            "— type [bold]?[/bold] or [bold]help[/bold] for available commands."
                        )
                        return False
                    matched_write = (key, cmd_def, cmd_args)

            # Write operations require configure mode
            if not self._state.configure_mode:
                console.print(
                    f"[yellow]The {cmd} command is only available in configure mode.[/yellow]\n"
                    "  Type [bold]configure[/bold] to enter configure mode."
                )
                return False

            # Bare verb ? — show available commands for that verb
            if len(tokens) >= 2 and tokens[1] == "?":
                if cmd == "set":
                    self._cmd_set(["?"])
                else:
                    self._cmd_show_write_help(cmd)
                return False

            # Route set/delete/update to registry if subcommand is not a builtin
            if matched_write is not None:
                key, cmd_def, cmd_args = matched_write
                if remote:
                    self._execute_remote(key, cmd_def, cmd_args)
                else:
                    self._execute_api(key, cmd_def, cmd_args)
                return False
            if cmd == "set":
                self._cmd_set(tokens[1:])
                return False
            if cmd == "update":
                console.print(
                    f"[yellow]Unknown update target:[/yellow] [bold]{' '.join(tokens[1:])}[/bold]\n"
                    "  Type [bold]update ?[/bold] to see updatable object types."
                )
                return False
            # delete with no registry match
            console.print(
                f"[yellow]Unknown delete target:[/yellow] [bold]{' '.join(tokens[1:])}[/bold]\n"
                "  Type [bold]delete ?[/bold] to see deletable object types."
            )
            return False

        if cmd in ("help", "?"):
            rest = tokens[1:]
            if rest and rest[0].lower() == "all":
                self._cmd_help_full()
            elif rest:
                # "help <topic>" — render docs page for the topic
                topic_text = " ".join(rest).lower()
                # Special case: if the topic matches a builtin like "setup",
                # and it's asking for help, show the setup wizard help
                if topic_text == "setup":
                    from app.docs import render_help_topic
                    render_help_topic(console, "setup")
                    return False
                self._cmd_help_docs(topic_text)
            else:
                # Bare "help" or "?" — Cisco-style compact inline listing
                self._cmd_help_inline([])
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

        # Convenience alias: show folder / show folders
        if cmd == "show" and len(tokens) > 1 and tokens[1].lower() in ("folder", "folders"):
            self._cmd_folder([])
            return False

        # Convenience alias: show feature [on|off|dev|<name>]
        if cmd == "show" and len(tokens) > 1 and tokens[1].lower() in ("feature", "features"):
            self._cmd_feature(["show"] + tokens[2:])
            return False

        # ---- Registry commands ----
        key, cmd_def, args = match_command(tokens)
        if key is None or not _feature_visible(cmd_def):
            # Unknown command - provide helpful suggestions
            self._show_command_not_found(tokens)
            return False

        if remote:
            self._execute_remote(key, cmd_def, args)
        else:
            self._execute_api(key, cmd_def, args)

        return False
