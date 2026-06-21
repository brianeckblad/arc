"""ArcShell dispatch mixin — the line dispatcher (parses + routes every command)."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class DispatchMixin:
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

        # Detect a trailing help trigger: '?' (brief, context-sensitive) or
        # '??' (full help).  Both are appended by the '?' key binding.
        help_token = "??" if "??" in tokens else ("?" if "?" in tokens else None)
        help_full = help_token == "??"

        # Expand the command/topic portion before trailing "help".
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            tokens = _expand_unambiguous_prefix(tokens[:-1], phrases) + ["help"]

        # Expand prefix before the '?' / '??' context-help trigger.
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

        # Cisco-style context help: a trailing '?' shows the next syntax options
        # (brief); a trailing '??' shows the full command help.
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
                if not help_full and self._print_context_help(prefix_tokens):
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
            if help_full:
                # Bare '??' → the full unfiltered command reference.
                self._cmd_help_full()
                return False
            # Fall through so the bare "?" branch below fires

        # A real command line was entered — reset the '?'-repeat tracker so the
        # next single '?' starts fresh (brief) rather than escalating to full.
        self._last_q_prefix = None

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
                self._cmd_help_docs(" ".join(rest).lower())
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
            console.print(
                f"[red]Unknown command:[/red] [bold]{' '.join(tokens)}[/bold]  "
                "— type [bold]?[/bold] or [bold]help[/bold] for available commands."
            )
            return False

        if remote:
            self._execute_remote(key, cmd_def, args)
        else:
            self._execute_api(key, cmd_def, args)

        return False
