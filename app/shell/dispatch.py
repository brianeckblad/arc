"""ArcShell dispatch mixin — the line dispatcher (parses + routes every command)."""
from __future__ import annotations

import difflib  # For fuzzy command matching
import re as _re

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)

# ---------------------------------------------------------------------------
# Output pipe filters — PAN-OS style `<command> | match <pattern>` support.
# ---------------------------------------------------------------------------

# Commands that own the terminal (interactive sessions, screen control) —
# capturing their output for a pipe filter would break them.
_PIPE_UNSUPPORTED = {
    "connect", "configure", "conf", "setup",
    "clear", "docs", "exit", "quit", "dev",
}

_ANSI_RE = _re.compile(r"\x1b\[[0-9;]*[A-Za-z]")


def split_pipe_line(line: str) -> tuple[str, str | None]:
    """Split *line* at the first unquoted ``|``.

    Returns ``(head_command, filter_spec)`` — filter_spec is None when the
    line has no pipe. Quoted pipes (``set address "a|b" …``) are preserved.
    """
    quote = ""
    for index, char in enumerate(line):
        if quote:
            if char == quote:
                quote = ""
        elif char in "'\"":
            quote = char
        elif char == "|":
            return line[:index].strip(), line[index + 1:].strip()
    return line, None


def parse_output_filters(spec: str) -> tuple[list[tuple[str, str]] | None, str]:
    """Parse a pipe filter chain into ``[(op, pattern), …]``.

    Supported (PAN-OS / Cisco vocabulary): ``match``/``include`` <pattern>,
    ``except``/``exclude`` <pattern>, ``count``, ``json`` (render the
    command's data as JSON instead of tables — for scripts), and
    ``save <file>`` (write the filtered output to a file — must be the last
    op in the chain).  Returns ``(None, error)`` on a malformed spec.
    """
    filters: list[tuple[str, str]] = []
    for segment in spec.split("|"):
        parts = segment.strip().split(None, 1)
        if not parts:
            return None, "empty filter — usage: <command> | match <pattern>"
        op = parts[0].lower()
        if op in ("match", "include", "except", "exclude"):
            if len(parts) < 2 or not parts[1].strip():
                return None, f"'{op}' needs a pattern — usage: <command> | {op} <pattern>"
            filters.append(("match" if op in ("match", "include") else "except", parts[1].strip()))
        elif op == "count":
            filters.append(("count", ""))
        elif op == "json":
            filters.append(("json", ""))
        elif op == "save":
            if len(parts) < 2 or not parts[1].strip():
                return None, "'save' needs a filename — usage: <command> | save <file>"
            filters.append(("save", parts[1].strip()))
        else:
            return None, (
                f"unknown filter '{op}' — supported: "
                "match <pat> | except <pat> | count | json | save <file>"
            )
    for index, (op, _) in enumerate(filters):
        if op == "save" and index != len(filters) - 1:
            return None, (
                "'save' must be the last op — e.g. "
                "<command> | match <pattern> | save <file>"
            )
    return filters, ""


def _line_matches(line: str, pattern: str) -> bool:
    """Regex match (case-insensitive) with plain-substring fallback."""
    plain = _ANSI_RE.sub("", line)
    try:
        return _re.search(pattern, plain, _re.IGNORECASE) is not None
    except _re.error:
        return pattern.lower() in plain.lower()


class DispatchMixin:
    def _cmd_watch(self, rest: str) -> bool:
        """Re-run *rest* every N seconds until Ctrl-C (`watch [N] <command>`).

        Works for API commands and `--remote` alike — the SSH pool keeps the
        device session alive, so 2FA happens once per device, then refreshes
        are free.
        """
        tokens = rest.split(None, 1)
        interval = 10
        if tokens and tokens[0].isdigit():
            interval = max(2, min(3600, int(tokens[0])))
            rest = tokens[1] if len(tokens) > 1 else ""
        command_line = rest.strip()
        first = command_line.split()[0].lower() if command_line.split() else ""

        if not first or first in ("?", "help"):
            console.print(
                "[yellow]Usage:[/yellow] watch [seconds] <command>\n"
                "  [dim]watch show interfaces          — repeat every 10 s\n"
                "  watch 5 show bgp-peers            — repeat every 5 s\n"
                "  watch 30 show security policy     — repeat every 30 s[/dim]"
            )
            return False
        if first in _PIPE_UNSUPPORTED or first == "watch":
            console.print(f"[yellow]'{first}' is interactive — watch doesn't apply.[/yellow]")
            return False

        console.print(
            f"[dim]watch: every {interval}s — [bold]{command_line}[/bold]  (Ctrl-C to stop)[/dim]"
        )
        iteration = 0
        try:
            while True:
                iteration += 1
                console.print(f"[dim]── watch #{iteration} ──[/dim]")
                if self._dispatch(command_line):
                    return False  # inner 'exit' stops the watch, not ARC
                time.sleep(interval)
        except KeyboardInterrupt:
            console.print(f"\n[dim]watch stopped after {iteration} run(s).[/dim]")
        return False

    def _dispatch_piped(self, head: str, spec: str) -> bool:
        """Run *head*, filter its captured output through the pipe *spec*."""
        filters, error = parse_output_filters(spec)
        if filters is None:
            console.print(f"[yellow]{error}[/yellow]")
            return False
        first = head.split()[0].lower() if head.split() else ""
        if not first:
            console.print("[yellow]Nothing to filter — usage: <command> | match <pattern>[/yellow]")
            return False
        if first in _PIPE_UNSUPPORTED:
            console.print(f"[yellow]'{first}' is interactive — output filters don't apply.[/yellow]")
            return False

        # `| json` renders the command's DATA as JSON instead of tables;
        # any remaining match/except/count filters then apply to those lines.
        json_mode = any(op == "json" for op, _ in filters)
        filters = [f for f in filters if f[0] != "json"]

        self._piping = True
        self._render_as_json = json_mode
        try:
            with console.capture() as capture:
                should_exit = self._dispatch(head)
        finally:
            self._piping = False
            self._render_as_json = False

        lines = capture.get().splitlines()
        counted = False
        save_target: str | None = None
        for op, pattern in filters:
            if op == "match":
                lines = [l for l in lines if _line_matches(l, pattern)]
            elif op == "except":
                lines = [l for l in lines if not _line_matches(l, pattern)]
            elif op == "count":
                total = sum(1 for l in lines if _ANSI_RE.sub("", l).strip())
                lines = [f"Count: {total} line(s)"]
                counted = True
            elif op == "save":
                save_target = pattern  # parser guarantees save is the last op
        if save_target is not None:
            self._save_pipe_output(lines, save_target)
            return should_exit
        if counted:
            console.print(lines[0])
            return should_exit
        for line in lines:
            console.file.write(line + "\n")
        return should_exit

    def _save_pipe_output(self, lines: list[str], target: str) -> None:
        """Write piped output *lines* to *target* as plain UTF-8 text.

        ANSI colour codes are stripped so the file is clean for scripts and
        diffs. Relative paths resolve against the current working directory;
        ``~`` expands to the operator's home.
        """
        path = Path(target).expanduser()
        if not path.is_absolute():
            path = Path.cwd() / path
        plain = [_ANSI_RE.sub("", l) for l in lines]
        try:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("\n".join(plain) + ("\n" if plain else ""), encoding="utf-8")
        except OSError as exc:
            console.print(f"[red]Could not save output:[/red] {exc}")
            return
        console.print(f"[green]Saved[/green] {len(plain)} line(s) → [bold]{path}[/bold]")

    def _cmd_history(self, rest: list[str]) -> None:
        """Print the last N commands from the prompt history (`history [n]`).

        The prompt_toolkit FileHistory format stores one entry per group of
        ``+``-prefixed lines (multi-line entries have several). Anything else
        (timestamps, comments) is ignored — parse defensively, never raise.
        """
        if rest and rest[0] in ("?", "help"):
            console.print(
                "\n  [bold]history[/bold]  — show recent commands\n\n"
                "  [cyan]history[/cyan]        Show last 20 commands\n"
                "  [cyan]history <n>[/cyan]    Show last n commands  [dim](e.g. history 50)[/dim]\n"
            )
            return
        count = 20
        if rest:
            if not rest[0].isdigit() or int(rest[0]) < 1:
                console.print("[yellow]Usage:[/yellow] history <n>   (n = how many recent commands, default 20)")
                return
            count = int(rest[0])

        try:
            raw = Path(HISTORY_FILE).read_text(encoding="utf-8", errors="replace")
        except OSError:
            console.print("[dim]No command history yet.[/dim]")
            return

        entries: list[str] = []
        current: list[str] = []
        for hist_line in raw.splitlines():
            if hist_line.startswith("+"):
                current.append(hist_line[1:])
            elif current:
                entries.append("\n".join(current))
                current = []
        if current:
            entries.append("\n".join(current))

        if not entries:
            console.print("[dim]No command history yet.[/dim]")
            return

        recent = entries[-count:]
        start_number = len(entries) - len(recent) + 1
        for offset, entry in enumerate(recent):
            console.print(f"[dim]{start_number + offset:>5}[/dim]  {entry}")

    def _cmd_alias(self, rest: list[str]) -> None:
        """User-defined aliases (`alias` / `alias <name> <expansion…>` /
        `alias delete <name>`) — Junos ``set cli alias`` style, arc-flavored.

        Aliases persist in the per-user preferences file and expand once at
        the very start of dispatch (single pass — an expansion that begins
        with another alias name is NOT re-expanded).
        """
        aliases = self._prefs.aliases

        if rest and rest[0] in ("?", "help"):
            console.print(
                "\n  [bold]alias[/bold]  — user-defined command shortcuts\n\n"
                "  [cyan]alias[/cyan]                      List all defined aliases\n"
                "  [cyan]alias <name> <expansion>[/cyan]   Create an alias\n"
                "  [cyan]alias <name>[/cyan]               Show one alias\n"
                "  [cyan]alias delete <name>[/cyan]        Remove an alias\n\n"
                "  [dim]Example:  alias sap  show address  →  type 'sap' runs 'show address'\n"
                "  Aliases expand once at dispatch — cannot be recursive.\n"
                "  Cannot shadow built-in commands or registered command words.[/dim]\n"
            )
            return

        if not rest:
            if not aliases:
                console.print(
                    "[dim]No aliases defined.[/dim]  "
                    "Use [bold]alias <name> <expansion…>[/bold] to create one."
                )
                return
            width = max(len(name) for name in aliases)
            for name in sorted(aliases):
                console.print(f"  [cyan]{name:<{width}}[/cyan]  {aliases[name]}")
            return

        if rest[0].lower() == "delete":
            if len(rest) < 2:
                console.print("[yellow]Usage:[/yellow] alias delete <name>")
                return
            name = rest[1]
            if name not in aliases:
                console.print(f"[yellow]No such alias:[/yellow] [bold]{name}[/bold]")
                return
            del aliases[name]
            save_prefs(self._prefs)
            console.print(f"[green]Deleted alias[/green] [bold]{name}[/bold]")
            return

        name = rest[0]
        expansion = " ".join(rest[1:]).strip()
        if not expansion:
            if name in aliases:
                console.print(f"  [cyan]{name}[/cyan]  {aliases[name]}")
            else:
                console.print(
                    "[yellow]Usage:[/yellow] alias [name] [expansion…]  |  alias delete <name>"
                )
            return

        # Refuse names that shadow shell builtins or command first-words
        # (show/set/delete/…) — an alias must never hijack real syntax.
        reserved = {b.lower() for b in _SHELL_BUILTINS}
        reserved.update(key.split()[0].lower() for key in COMMANDS)
        if name.lower() in reserved:
            console.print(
                f"[yellow]'{name}' is a built-in or command word — pick a different alias name.[/yellow]"
            )
            return

        aliases[name] = expansion
        save_prefs(self._prefs)
        console.print(f"[green]Alias set:[/green] [cyan]{name}[/cyan] → {expansion}")

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
        visible_commands = [
            cmd for cmd in all_commands
            if cmd not in COMMANDS or self._is_command_visible(cmd, COMMANDS[cmd])
        ]

        # Ambiguous abbreviation?  `sh s` matches several commands — list them
        # instead of a bare "unknown" so the operator learns what to type next.
        lowered = [t.lower() for t in tokens]
        prefix_matches = sorted(
            cmd for cmd in visible_commands
            if (phrase := cmd.split())
            and len(phrase) >= len(lowered)
            and all(phrase[i].startswith(lowered[i]) for i in range(len(lowered)))
        )
        if len(prefix_matches) > 1:
            console.print(
                f"\n[yellow]Ambiguous command:[/yellow] [bold]{cmd_text}[/bold] "
                f"matches {len(prefix_matches)} command(s):\n"
            )
            for match in prefix_matches[:15]:
                console.print(f"  • [cyan]{match}[/cyan]")
            if len(prefix_matches) > 15:
                console.print(f"  [dim]… and {len(prefix_matches) - 15} more — type more letters[/dim]")
            return
        
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

        # User-defined alias expansion — single pass, BEFORE watch/pipe parsing
        # so an alias body may itself contain pipes or a watch prefix. Only the
        # first token is checked, and the result is never re-expanded: an alias
        # whose expansion starts with another alias name runs that text as-is.
        aliases = getattr(getattr(self, "_prefs", None), "aliases", None) or {}
        if aliases:
            first_word, _, remainder = line.partition(" ")
            expansion = aliases.get(first_word)
            if expansion:
                line = expansion + (" " + remainder if remainder else "")

        # Dev shell — intercept dev-shell commands before normal dispatch.
        if self._state.dev_shell:
            handled = self._dispatch_dev_shell(line)
            if handled is not None:
                return handled

        # `watch [N] <command>` — re-run every N seconds until Ctrl-C.
        # Parsed before pipe filters so the whole pipeline is re-run each tick.
        # `watch ?` and `watch help` are intercepted and show usage instead.
        watch_tokens = line.split()
        if watch_tokens and watch_tokens[0].lower() == "watch":
            rest = line.split(None, 1)[1] if len(watch_tokens) > 1 else ""
            return self._cmd_watch(rest)

        # PAN-OS style output filtering: <command> | match <pat> | count …
        head, pipe_spec = split_pipe_line(line)
        if pipe_spec is not None:
            return self._dispatch_piped(head, pipe_spec)
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

        # Cisco-style shorthand expansion:
        #   e            -> exit
        #   sh sec pol   -> show security policy
        # Expansion occurs only when a prefix resolves to exactly one command.
        visible_command_keys = self._visible_command_keys()
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
            if topic_cmd is not None and not self._is_command_visible(topic, topic_cmd):
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
                    if len(prefix_tokens) == 1:
                        # bare `set ?` — show full registry listing
                        self._cmd_show_write_help("set")
                    else:
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
                # Special case: `terminal ?` / `terminal length ?` etc.
                if prefix_tokens[0].lower() == "terminal":
                    self._cmd_terminal(prefix_tokens[1:] + ["?"])
                    return False
                # Special case: `alias ?`, `history ?`, `find ?`
                if prefix_tokens[0].lower() == "alias":
                    self._cmd_alias(["?"])
                    return False
                if prefix_tokens[0].lower() == "history":
                    self._cmd_history(["?"])
                    return False
                if prefix_tokens[0].lower() in ("find",):
                    self._cmd_find(["?"])
                    return False
                # General case: prefix help for registered commands.
                self._cmd_help_inline(prefix_tokens)
                return False
            # Fall through so the bare "?" branch below fires

        cmd = tokens[0].lower()

        # ---- exit / quit ----
        if cmd in ("exit", "quit"):
            if self._state.dev_shell:
                self._dev_shell_exit()
                return False
            if self._state.configure_mode:
                if not self._confirm_configure_exit():
                    return False
                self._state.configure_mode = False
                console.print("[cyan]Exited configure mode.[/cyan]")
                return False
            return True

        # ---- abandon (configure mode): discard locally staged changes ----
        if cmd == "abandon":
            self._cmd_abandon(tokens[1:])
            return False

        # ---- terminal: per-user pager/width/spinner preferences ----
        if cmd == "terminal":
            self._cmd_terminal(tokens[1:])
            return False

        # ---- find: PAN-OS style command search (find command keyword <x>) ----
        if cmd == "find":
            self._cmd_find(tokens[1:])
            return False

        # ---- history: last N commands from the prompt history file ----
        if cmd == "history":
            self._cmd_history(tokens[1:])
            return False

        # ---- alias: user-defined command shortcuts (persisted in prefs) ----
        if cmd == "alias":
            self._cmd_alias(tokens[1:])
            return False

        # ---- commit (configure mode): apply staged changes, then push ----
        # `commit --remote` still goes through the registry → SSH path.
        if cmd == "commit" and self._state.configure_mode and not remote:
            self._cmd_commit_staged(tokens[1:])
            return False

        # ---- show config [pending|diff] — review locally staged changes ----
        if (
            cmd == "show"
            and len(tokens) > 1
            and tokens[1].lower() == "config"
            and (len(tokens) == 2 or tokens[2].lower() in ("pending", "diff"))
        ):
            self._cmd_show_pending()
            return False


        # ---- Shell built-ins ----
        # Bare `clear` clears the terminal; `clear <args>` falls through to the
        # registry (PAN-OS clear commands, e.g. `clear session all --remote`).
        if cmd == "clear" and len(tokens) == 1:
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

        if cmd == "folder":
            if not self._state.configure_mode:
                console.print(
                    "[yellow]The folder command requires configure mode.[/yellow]\n"
                    "  Enter [bold]configure[/bold] first, or use "
                    "[bold]cd folder <name>[/bold] to switch folders."
                )
                return False
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
                    if not self._is_command_visible(key, cmd_def):
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
        if key is None or not self._is_command_visible(key, cmd_def):
            # Unknown command - provide helpful suggestions
            self._show_command_not_found(tokens)
            return False

        if remote:
            self._execute_remote(key, cmd_def, args)
        else:
            self._execute_api(key, cmd_def, args)

        return False
