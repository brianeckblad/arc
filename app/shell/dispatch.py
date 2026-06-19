"""ArcShell dispatch mixin — the line dispatcher (parses + routes every command)."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class DispatchMixin:
    def _dispatch(self, line: str) -> bool:
        """Process one input line.  Returns True when the user wants to exit ARC."""
        # Normalize whitespace: collapse tabs and multiple spaces to a single space.
        line = re.sub(r"[ \t]+", " ", line).strip()
        # Strip --remote flag before any other parsing
        remote = False
        tokens = line.split()
        if "--remote" in tokens:
            remote = True
            tokens = [t for t in tokens if t != "--remote"]

        if not tokens:
            return False

        # Cisco-style shorthand expansion:
        #   e            -> exit
        #   sh sec pol   -> show security policy
        # Expansion occurs only when a prefix resolves to exactly one command.
        phrases = [[b] for b in _SHELL_BUILTINS if b != "?"] + [k.split() for k in COMMANDS]

        # Expand the command/topic portion before trailing "help".
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            tokens = _expand_unambiguous_prefix(tokens[:-1], phrases) + ["help"]

        # Expand prefix before '?' context help trigger.
        if "?" in tokens:
            qidx = tokens.index("?")
            tokens = _expand_unambiguous_prefix(tokens[:qidx], phrases) + tokens[qidx:]
        else:
            tokens = _expand_unambiguous_prefix(tokens, phrases)

        # "<command> help" — trailing 'help' opens the full docs page for that command.
        # This must be checked before any individual builtin dispatcher so that
        # e.g. "cd help" shows docs instead of treating "help" as a device name.
        if len(tokens) >= 2 and tokens[-1].lower() == "help":
            topic = " ".join(tokens[:-1]).lower()
            self._cmd_help_docs(topic)
            return False

        # Cisco-style inline help: trailing '?' shows a compact one-liner per command.
        if "?" in tokens:
            question_idx = tokens.index("?")
            prefix_tokens = tokens[:question_idx]
            if prefix_tokens:
                # Always restore the prompt prefix after displaying ? help so the operator
                # can continue typing without re-entering what they had.
                # For sub-command variants (feature enable ?, set address ?) restore
                # the immediate parent prefix (e.g. "feature enable " or "set ").
                self._pending_default = " ".join(prefix_tokens) + " "

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

        if cmd in ("set", "delete", "update"):
            # Bare verb ? — show available commands for that verb
            if len(tokens) >= 2 and tokens[1] == "?":
                if cmd == "set":
                    self._cmd_set(["?"])
                else:
                    self._cmd_show_write_help(cmd)
                return False

            # Route set/delete/update to registry if subcommand is not a builtin
            if len(tokens) >= 2 and tokens[1].lower() not in ("?", "folder"):
                key, cmd_def, cmd_args = match_command(tokens)
                if key is not None:
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

        # ---- Registry commands ----
        key, cmd_def, args = match_command(tokens)
        if key is None:
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
