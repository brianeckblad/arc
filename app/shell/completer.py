"""ArcCompleter — context-aware tab completion for the ARC shell."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)
from app.settings import command_structure



# ── Usage-string parser — drives argument tab completion ─────────────────────
#
# A command's `usage` (from its docs/commands/<slug>.md front-matter) is parsed
# into an ordered list of "slots" the user fills in after the command, plus the
# trailing optional `[keyword <value>]` pairs.  Example:
#
#   "set address <name> ip-netmask|ip-range|ip-wildcard|fqdn <value>
#       [description <text>] [tag <name>]"
#
#   required = [ ('free', None),                       # <name>
#               ('options', ['ip-netmask', ...]),      # the type choice
#               ('free', None) ]                       # <value>
#   optional = ['description', 'tag']
#
# So after `set address myaddr ` Tab offers the type choices; after the value,
# Tab offers `description` / `tag`.

def _parse_usage(usage: str, command_key: str) -> tuple[list[tuple[str, list | None]], list[str]]:
    """Parse a usage string into (required_slots, optional_keywords).

    Each required slot is a ``(kind, value)`` pair where *kind* is:
      - ``"options"`` → one of a fixed set of choices (``value`` is the list)
      - ``"free"``    → a free user value; ``value`` is the placeholder (e.g. ``<name>``)
      - ``"literal"`` → a fixed keyword that must be typed verbatim
    """
    body = usage
    if body.lower().startswith(command_key.lower()):
        body = body[len(command_key):]
    tokens = body.split()
    required: list[tuple[str, list | None]] = []
    optional: list[str] = []
    i = 0
    while i < len(tokens):
        tok = tokens[i]
        if tok.startswith("["):
            group = [tok]
            while not tokens[i].endswith("]") and i < len(tokens) - 1:
                i += 1
                group.append(tokens[i])
            words = " ".join(group).strip("[]").split()
            # A keyword option is "[<keyword> <value>]" — keyword then a <placeholder>.
            # Repeat groups like "[svc2 ...]" are values, not keywords — skip them.
            if len(words) >= 2 and words[1].startswith("<") and not words[0].startswith("<"):
                optional.append(words[0].lower())
            i += 1
            continue
        if "|" in tok and "<" not in tok:
            required.append(("options", [o.lower() for o in tok.split("|")]))
        elif tok.startswith("<"):
            required.append(("free", [tok]))      # keep the placeholder text
        else:
            required.append(("literal", [tok.lower()]))
        i += 1
    return required, optional


def _usage_options(usage: str, command_key: str, typed: list[str]) -> list[tuple[str, str]]:
    """Return (token, display_meta) completions for the slot after *typed* args.

    When the current slot is a free value (e.g. ``<name>``) but a *later* slot is
    a fixed choice (e.g. the ``ip-netmask|ip-range|…`` type), the choices are
    surfaced immediately so the operator sees the meaningful options right after
    the command — they just type the name first, then pick one.
    """
    # Multi-variant usage (PAN-OS catalog entries join variants with \n):
    # the walker consumes the canonical variant — always the first line.
    usage = usage.split("\n")[0]
    required, optional = _parse_usage(usage, command_key)
    n = len(typed)
    if n < len(required):
        kind, val = required[n]
        if kind == "options":
            return [(o, "type") for o in (val or [])]
        if kind == "literal":
            return [(val[0], "keyword")]
        # Free value slot.  Look ahead to the next *options* slot and show those
        # choices, prefixed with a hint about what to type for this free slot.
        placeholder = (val or ["<value>"])[0]
        for kind2, val2 in required[n + 1:]:
            if kind2 == "options":
                hint = f"type {placeholder} then choose"
                return [(o, hint) for o in (val2 or [])]
            if kind2 == "free":
                break  # two free values in a row — can't usefully guess
        return []  # free value with no upcoming choices
    # Past the required slots → trailing optional [keyword <value>] pairs.
    consumed = typed[len(required):]
    if len(consumed) % 2 == 0:  # at a keyword position
        used = {t.lower() for t in consumed[::2]}
        return [(k, "optional") for k in optional if k not in used]
    return []  # at a value position


def _tokenize_partial(text: str) -> tuple[list[str], str]:
    """Split *text* for completion, honouring quotes, tracking the in-progress token.

    Returns ``(completed_tokens, partial)`` where *completed_tokens* are fully
    entered tokens (quotes stripped) and *partial* is the token currently being
    typed — empty when the cursor sits at a fresh boundary (a space outside any
    quote).  An unterminated quote keeps everything after it in *partial*, so
    ``set address "this is`` stays on the name slot rather than wrongly advancing.
    """
    tokens: list[str] = []
    buf = ""
    quote: str | None = None
    in_token = False
    for ch in text:
        if quote is not None:
            in_token = True
            if ch == quote:
                quote = None
            else:
                buf += ch
        elif ch in ('"', "'"):
            quote = ch
            in_token = True
        elif ch.isspace():
            if in_token:
                tokens.append(buf)
                buf = ""
                in_token = False
        else:
            buf += ch
            in_token = True
    if in_token:
        return tokens, buf  # in-progress (also covers an open-quote partial)
    return tokens, ""


class ArcCompleter(Completer):
    """Context-aware tab completer.

    - After `cd` / `remote` / `connect` → completes with managed device names
    - After `folder`           → completes with SCM folder names
    - Otherwise               → completes with ARC command names + shell built-ins
    """


    def __init__(self, shell: "ArcShell") -> None:
        self._shell = shell

    def _command_visible(self, key: str) -> bool:
        """Return True when a registered command is visible in this shell mode.

        Delegates to the shell's canonical check so completion, help, and
        dispatch can never disagree about which commands exist.
        """
        command_def = COMMANDS.get(key)
        if command_def is None:
            return False
        return self._shell._is_command_visible(key, command_def)

    def _command_is_dev_gated(self, key: str) -> bool:
        """Return True when the command exists but is gated behind dev mode.

        Used to surface `[dev mode]` hints in tab completion so operators
        know the command exists and how to unlock it, rather than seeing nothing.
        """
        command_def = COMMANDS.get(key)
        if command_def is None or not command_def.feature_flag:
            return False
        features = getattr(self._shell, "_features", {})
        return feature_state(features, command_def.feature_flag) == "dev"

    def get_completions(self, document, complete_event):
        raw = document.text_before_cursor.lstrip()
        # Normalize internal whitespace: multiple spaces and tabs → single space.
        # Preserve whether the user just pressed space/tab (trailing whitespace = new token).
        ends_with_space = bool(raw) and raw[-1] in (" ", "\t")
        text = re.sub(r"[ \t]+", " ", raw).strip()
        if ends_with_space:
            text = text + " "  # restore single trailing space for has_arg_space detection

        parts = text.split()

        # ---- dev shell mode: complete dev-shell sub-commands first ----
        if getattr(self._shell._state, "dev_shell", False):
            yield from self._complete_dev_shell(parts, text)
            return

        if not parts:
            for name in sorted(self._all_commands(include_remote_suffix=False)):
                yield Completion(name, start_position=0)
            return

        yield from self._complete_normal(parts, text)

    def _complete_normal(self, parts: list[str], text: str):
        """Yield completions for non-dev-shell commands.

        Handles all built-in argument completions (feature, find, cd, etc.)
        and falls through to registry-based and prefix-name completion.
        Called from both get_completions and _complete_dev_shell fallthrough.
        """
        first = parts[0].lower()
        # True if the user has typed at least one space after the first token
        has_arg_space = len(parts) > 1 or text.endswith(" ")
        partial_arg = parts[1] if len(parts) > 1 else ""

        # ---- cd / remote / connect → device name or subcommand completion ----
        if first in ("cd", "connect") and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            # cd device / cd folder sub-commands
            if first == "cd" and len(parts) <= 2:
                for sub in ("device", "folder", "..", "/"):
                    if sub.startswith(partial_arg.lower()):
                        meta = "set device context" if sub == "device" else (
                               "set folder scope" if sub == "folder" else "clear context"
                        )
                        yield Completion(sub, start_position=-len(partial_arg), display_meta=meta)
                # Also offer device names directly (backward compat)
                for device in self._shell._state.devices_cache:
                    candidate = device_display_name(device, "")
                    if candidate and candidate.lower().startswith(partial_arg.lower()):
                        yield Completion(candidate, start_position=-len(partial_arg), display_meta="device")
                return
            # cd device <name> → complete device name
            if first == "cd" and second == "device":
                partial_name = parts[2] if len(parts) > 2 else ""
                for device in self._shell._state.devices_cache:
                    candidate = device_display_name(device, "")
                    if candidate and candidate.lower().startswith(partial_name.lower()):
                        yield Completion(candidate, start_position=-len(partial_name))
                return
            # cd folder <name> → complete folder name
            if first == "cd" and second == "folder":
                partial_folder = parts[2] if len(parts) > 2 else ""
                for folder in self._shell._state.folders_cache:
                    if folder.lower().startswith(partial_folder.lower()):
                        yield Completion(folder, start_position=-len(partial_folder))
                return
            # remote/connect → device names
            for device in self._shell._state.devices_cache:
                candidate = device_display_name(device, "")
                if candidate and candidate.lower().startswith(partial_arg.lower()):
                    yield Completion(candidate, start_position=-len(partial_arg))
            return


        # ---- folder → 'create' subcommand only (switching uses 'cd folder') ----
        if first == "folder" and has_arg_space:
            if len(parts) <= 2 and "create".startswith(partial_arg.lower()):
                yield Completion(
                    "create",
                    start_position=-len(partial_arg),
                    display_meta="create a new folder",
                )
            return

        # ---- catalog → subcommand completion (dev mode only) ----
        if first == "catalog" and has_arg_space:
            if len(parts) <= 2 and "rebuild".startswith(partial_arg.lower()):
                yield Completion("rebuild", start_position=-len(partial_arg),
                                 display_meta="run all generators (no network)")
            return

        # ---- command-structure → subcommand completion (dev mode only) ----
        if first == "command-structure" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            if len(parts) <= 2:
                for sub, meta in (("list", "show all enabled commands + tiers"),
                                  ("update", "auto-generate help specs for missing commands"),
                                  ("clear", "wipe auto-generated specs")):
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg), display_meta=meta)
            elif second == "list" and len(parts) <= 3:
                for opt in ("enabled", "disabled"):
                    if opt.startswith(partial_arg.lower() if len(parts) > 2 else ""):
                        p = parts[2] if len(parts) > 2 else ""
                        yield Completion(opt, start_position=-len(p), display_meta="filter")
            elif second == "update" and len(parts) <= 3:
                # Complete command names for targeted update
                from app.commands.registry import COMMANDS as _CMDS
                from app.settings.features import is_enabled as _is_en
                feats = getattr(self._shell, "_features", {})
                dev_mode = getattr(self._shell, "_dev_mode", False)
                p = parts[2] if len(parts) > 2 else ""
                for key in sorted(_CMDS):
                    cmd = _CMDS[key]
                    if cmd.feature_flag and _is_en(feats, cmd.feature_flag, dev_mode):
                        if key.startswith(p.lower()):
                            yield Completion(key, start_position=-len(p),
                                             display_meta=cmd.description[:50])
            return

        # ---- feature → subcommand + flag name completion ----
        if first == "feature" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            if len(parts) <= 2:
                # Complete subcommands: show, enable, disable, dev, help
                for sub in ("show", "enable", "disable", "dev", "help"):
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg))
            elif second == "show" and len(parts) <= 3:
                partial_filter = parts[2] if len(parts) > 2 else ""
                for option in ("on", "off", "dev"):
                    if option.startswith(partial_filter.lower()):
                        yield Completion(option, start_position=-len(partial_filter), display_meta="filter")
                for flag in sorted(self._shell._features):
                    if flag.startswith(partial_filter.lower()):
                        yield Completion(flag, start_position=-len(partial_filter), display_meta="feature")
            elif second in ("enable", "disable", "dev") and len(parts) <= 3:
                # Complete feature flag names from the settings/features/ glossary
                flag_dict = self._shell._features
                partial_flag = parts[2] if len(parts) > 2 else ""
                for flag, enabled in sorted(flag_dict.items()):
                    if flag.startswith(partial_flag.lower()):
                        # Only suggest flags that make sense for this subcommand
                        if second == "enable" and not enabled:
                            meta = "currently OFF"
                        elif second == "disable" and enabled:
                            meta = "currently ON"
                        else:
                            meta = "on" if enabled else "off"
                        yield Completion(flag, start_position=-len(partial_flag), display_meta=meta)
            return

        # ---- find → subcommand completion ----
        if first == "find" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            # Sub-commands available under find (extend this tuple as new ones are added)
            _FIND_SUBS: tuple[tuple[str, str], ...] = (
                ("command", "search all commands by name or description"),
            )
            if len(parts) <= 2:
                for sub, meta in _FIND_SUBS:
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg), display_meta=meta)
            # Search text after sub-command is free-form — no further completion
            return


        if first == "configure" and has_arg_space:
            for sub in ("t", "terminal"):
                if sub.startswith(partial_arg.lower()):
                    yield Completion(sub, start_position=-len(partial_arg))
            return

        # ---- terminal → subcommand + value completion ----
        if first == "terminal" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            _sub_meta = {
                "length":  "lines per page  (0 = off)",
                "width":   "render width    (0 = auto)",
                "height":  "render height   (0 = auto)",
                "spinner": "show/hide spinner",
            }
            if len(parts) <= 2:
                for sub, meta in _sub_meta.items():
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg), display_meta=meta)
            elif second == "spinner" and len(parts) <= 3:
                partial_val = parts[2] if len(parts) > 2 else ""
                for val in ("on", "off"):
                    if val.startswith(partial_val.lower()):
                        yield Completion(val, start_position=-len(partial_val))
            elif second in ("length", "width", "height") and len(parts) <= 3:
                partial_val = parts[2] if len(parts) > 2 else ""
                p = self._shell._prefs
                current = {"length": p.terminal_length, "width": p.terminal_width, "height": p.terminal_height}.get(second, 0)
                hint = str(current) if current else "0"
                if hint.startswith(partial_val):
                    yield Completion(hint, start_position=-len(partial_val),
                                     display_meta=f"current value")
            return

        # ---- show terminal (builtin — inject alongside registry show-commands) ----
        if first == "show" and has_arg_space and len(parts) <= 2:
            if "terminal".startswith(partial_arg.lower()):
                yield Completion("terminal", start_position=-len(partial_arg),
                                 display_meta="display terminal settings")
            # No return — falls through to registry-based show <command> completion

        # ---- cli → theme operations in configure mode ----
        if first == "cli" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            if len(parts) <= 2:
                for sub in ("show", "color", "reset"):
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg))
            elif second == "color" and len(parts) <= 3:
                partial_key = parts[2] if len(parts) > 2 else ""
                for key in THEME_KEYS:
                    if key.startswith(partial_key.lower()):
                        yield Completion(key, start_position=-len(partial_key))
            return

        # ---- account → profile name completion ----
        if first == "account" and has_arg_space:
            for p in list_profiles():
                if p["name"].lower().startswith(partial_arg.lower()):
                    meta = "(active)" if p["active"] else (p["tsg_id"] or p["client_id"] or "")
                    yield Completion(
                        p["name"],
                        start_position=-len(partial_arg),
                        display_meta=meta,
                    )
            return

        # ---- tsg → hint with TSGs from SCM IAM cache (or config fallback) ----
        if first == "tsg" and has_arg_space:
            tsgs = self._shell._state.tsgs_cache
            if tsgs:
                # Cache populated — show real TSG IDs with their display names.
                for entry in tsgs:
                    tsg_id, display_name = tsg_display(entry)
                    if not tsg_id:
                        continue
                    if tsg_id.lower().startswith(partial_arg.lower()):
                        yield Completion(
                            tsg_id,
                            start_position=-len(partial_arg),
                            display_meta=display_name,
                        )
            else:
                # Cache empty (IAM not accessible) — fall back to configured values.
                config_tsg = self._shell._config.scm.tsg_id
                active_tsg = self._shell._state.tsg_id
                for tsg in dict.fromkeys(filter(None, [config_tsg, active_tsg])):
                    if tsg.lower().startswith(partial_arg.lower()):
                        yield Completion(tsg, start_position=-len(partial_arg))
            return

        # ---- show device <name> [snippets] → device name completion ----
        if text.lower().startswith("show device ") and len(parts) >= 2:
            # Parts: ["show", "device", <partial_name>, ...]
            if len(parts) == 3 or (len(parts) == 2 and text.endswith(" ")):
                # Completing device name
                partial_name = parts[2] if len(parts) > 2 else ""
                for device in self._shell._state.devices_cache:
                    candidate = device_display_name(device, "")
                    if candidate and candidate.lower().startswith(partial_name.lower()):
                        yield Completion(candidate, start_position=-len(partial_name))
                return
            if len(parts) == 4 or (len(parts) == 3 and text.endswith(" ")):
                # Completing "snippets" after the device name
                partial_sub = parts[3] if len(parts) > 3 else ""
                if "snippets".startswith(partial_sub.lower()):
                    yield Completion("snippets", start_position=-len(partial_sub))
                return

        # ---- show snippet <name> [details] → context-aware completion ----
        # "show snippet "          → complete snippet name
        # "show snippet <name> "   → offer "details" subcommand
        # "show snippet <name> d"  → complete "details"
        if text.lower().startswith("show snippet ") and not text.lower().startswith("show snippets"):
            # parts[0]="show", parts[1]="snippet", parts[2]=name-or-partial, parts[3]=subcommand
            name_part    = parts[2] if len(parts) > 2 else ""
            subcmd_part  = parts[3] if len(parts) > 3 else ""
            has_subcmd_space = len(parts) > 3 or (len(parts) == 3 and text.endswith(" "))

            # Collect candidate snippet names
            device = self._shell._state.device
            if device and device.get("snippets"):
                candidates = list(device.get("snippets") or [])
            else:
                seen: set[str] = set()
                for d in self._shell._state.devices_cache:
                    for sn in (d.get("snippets") or []):
                        seen.add(sn)
                candidates = sorted(seen)

            if has_subcmd_space:
                # Name is already complete — offer "details" subcommand
                if "details".startswith(subcmd_part.lower()):
                    yield Completion(
                        "details",
                        start_position=-len(subcmd_part),
                        display_meta="show full configured objects",
                    )
            else:
                # Still completing the name
                for name in candidates:
                    if name.lower().startswith(name_part.lower()):
                        yield Completion(name, start_position=-len(name_part))
            return

        # ---- help → command/topic completion ----
        if first == "help" and has_arg_space:
            partial_topic = " ".join(parts[1:]).lower()
            for topic in available_help_topics():
                if topic.startswith(partial_topic):
                    yield Completion(topic[len(partial_topic):], start_position=-len(partial_topic))
            return


        # ---- Argument completion for a fully-typed command ----
        # Once the user has finished a command word, Tab offers its sub-commands
        # and its usage option keywords — NOT a different command that merely
        # shares a prefix (e.g. `set address ` must not autofill `address-group`).
        #
        # Quote-aware here: a value with spaces is one token when quoted, so
        # `set address "this is a test" ` correctly lands on the *type* slot.
        qtokens, qpartial = _tokenize_partial(text)
        qparts = qtokens + ([qpartial] if qpartial else [])
        at_boundary = qpartial == ""
        matched_key = self._match_complete_command(qparts, at_boundary)
        if matched_key is not None:
            yield from self._complete_arguments(matched_key, qparts, at_boundary, qpartial)
            return

        # ---- Default: command-name prefix completion (still typing the command) ----
        text_trim = text.rstrip(" ")
        include_remote_suffix = " --" in text
        full_is_command = text_trim in COMMANDS and self._command_visible(text_trim)
        for name in sorted(self._all_commands(include_remote_suffix=include_remote_suffix)):
            if name == text_trim:
                continue
            if full_is_command:
                # The typed text is already a complete command — only offer true
                # sub-commands (`K <more>`), never prefix-siblings.
                if not name.startswith(text_trim + " "):
                    continue
            elif not name.startswith(text_trim):
                continue
            yield Completion(name, start_position=-len(text))

        # Also surface dev-gated commands with a hint so operators can discover them.
        if not full_is_command:
            for name in sorted(self._dev_gated_commands()):
                if not name.startswith(text_trim):
                    continue
                if name == text_trim:
                    continue
                yield Completion(
                    name, start_position=-len(text),
                    display_meta="[dim][dev mode][/dim]",
                )

        # When the typed text is itself a complete command but has no trailing
        # space yet, also surface its first argument slot (with a leading space)
        # so `set address` + Tab reveals what comes next instead of nothing.
        # Sub-command continuations are already offered by the prefix loop above,
        # so here we emit only the argument options.
        if full_is_command and not text.endswith(" "):
            for opt in self._arg_options(text_trim, []):
                text_ins = opt["text"]
                display = opt.get("display") or text_ins
                if text_ins == "":
                    yield Completion(" ", start_position=0,
                                     display=display, display_meta=opt["meta"])
                else:
                    yield Completion(" " + text_ins, start_position=0,
                                     display=display, display_meta=opt["meta"])

    def _complete_dev_shell(self, parts: list[str], text: str):
        """Yield completions for dev shell commands.

        Dev shell is normal mode + a few extra commands (status, catalog,
        command-structure, docs sub-commands). Top-level names come from
        _all_commands() (which includes the dev builtins via builtin-commands.json
        when dev_mode=True).  Only the dev-command sub-trees need special handling
        here; everything else falls through to _complete_normal.
        """
        # Sub-command trees for dev-shell-specific commands
        _DEV_SUBS = {
            "docs":              [("update", "Pull latest pan.dev specs + regenerate"),
                                  ("status", "Last pull date and spec ages")],
            "docs update":       [("--scm", "SCM API specs only"),
                                  ("--panos", "PAN-OS CLI docs only")],
            "catalog":           [("rebuild", "Run all generators (no network)")],
            "command-structure": [("list",    "Show all enabled commands + tiers"),
                                  ("update",  "Auto-generate help specs for missing commands"),
                                  ("clear",   "Wipe auto-generated specs")],
            "command-structure list": [("enabled",  "Show enabled commands only"),
                                       ("disabled", "Show disabled commands only")],
        }

        ends_with_space = text.endswith(" ")
        first = parts[0].lower() if parts else ""
        partial = parts[-1] if not ends_with_space and len(parts) > 1 else ""

        if not parts or (len(parts) == 1 and not ends_with_space):
            # Top-level: all commands via normal pipeline (dev mode reveals
            # status/catalog/command-structure/feature/etc. automatically).
            for name in sorted(self._all_commands(include_remote_suffix=False)):
                if name.startswith(first):
                    yield Completion(name, start_position=-len(first))
            return

        # Build the command prefix seen so far (excluding the partial last token)
        if ends_with_space:
            prefix = " ".join(p.lower() for p in parts)
        else:
            prefix = " ".join(p.lower() for p in parts[:-1])

        if prefix in _DEV_SUBS:
            for sub, meta in _DEV_SUBS[prefix]:
                if sub.startswith(partial.lower()):
                    yield Completion(sub, start_position=-len(partial), display_meta=meta)
            return

        # command-structure update <cmd> — complete enabled command names
        if prefix.startswith("command-structure update"):
            from app.commands.registry import COMMANDS
            from app.settings.features import is_enabled
            features = getattr(self._shell, "_features", {})
            dev_mode = getattr(self._shell, "_dev_mode", False)
            for key in sorted(COMMANDS):
                cmd = COMMANDS[key]
                if cmd.feature_flag and is_enabled(features, cmd.feature_flag, dev_mode):
                    if key.startswith(partial.lower()):
                        yield Completion(key, start_position=-len(partial),
                                        display_meta=cmd.description[:50])
            return

        # Fall through to normal completion — handles feature, find, etc. argument
        # completion and the default command-name prefix completion.
        if parts:
            yield from self._complete_normal(parts, text)

    def _match_complete_command(self, parts: list[str], ends_with_space: bool) -> str | None:
        """Return the longest complete command key the user has fully entered.

        Returns the key only when the cursor is in the *argument* region — either
        a trailing space after the command, or extra tokens beyond it.  When the
        text is exactly the command with no trailing space, returns None so the
        default branch can still offer sub-commands.
        """
        lowered = [p.lower() for p in parts]
        for n in range(len(parts), 0, -1):
            key = " ".join(lowered[:n])
            if key in COMMANDS and self._command_visible(key):
                if n < len(parts) or ends_with_space:
                    return key
                return None
        return None

    def _complete_arguments(self, key: str, qparts: list[str], at_boundary: bool, partial: str = ""):
        """Yield completions for the argument region of a complete command.

        *qparts* are quote-aware tokens (a quoted value with spaces is one token);
        *at_boundary* is True when the cursor is positioned to start a new token
        (so *partial* is empty), otherwise *partial* is the in-progress token.

        Combines sub-command next-tokens (e.g. `show interface` → `all`) with the
        command's argument options.  Argument options come from the per-command
        structure file when present (`settings/command-structure.json`), else from
        parsing the command's usage string.  Required value slots yield a single
        non-inserting hint (e.g. `<name>`) so Tab never returns a silent result.
        """
        key_tokens = key.split()
        after = qparts[len(key_tokens):]
        if at_boundary:
            typed = [t.lower() for t in after]
            partial = ""
        else:
            typed = [t.lower() for t in after[:-1]] if after else []
            partial = (after[-1].lower() if after else "")

        offered: set[str] = set()

        # 1. Sub-command next tokens — keys that extend this command by more tokens.
        for ckey in COMMANDS:
            if ckey == key or not ckey.startswith(key + " "):
                continue
            if not self._command_visible(ckey):
                continue
            sub = ckey.split()[len(key_tokens):]
            if len(typed) < len(sub) and sub[:len(typed)] == typed:
                nxt = sub[len(typed)]
                if nxt.startswith(partial) and nxt not in offered:
                    offered.add(nxt)
                    yield Completion(nxt, start_position=-len(partial),
                                     display_meta="sub-command")

        # 2. Argument options for the current slot (structure file, then usage).
        for opt in self._arg_options(key, typed):
            text_ins = opt["text"]
            display = opt.get("display") or text_ins
            if text_ins == "":
                # Non-inserting hint (e.g. <name>) — selecting it leaves the line
                # unchanged but the menu still shows what to enter.
                yield Completion("", start_position=0,
                                 display=display, display_meta=opt["meta"])
                continue
            if not text_ins.startswith(partial) or text_ins in offered:
                continue
            offered.add(text_ins)
            yield Completion(text_ins, start_position=-len(partial),
                             display=display, display_meta=opt["meta"])

    # Dynamic value completion — PAN-OS completes EXISTING object names from
    # config (`delete address <TAB>` lists your addresses). Maps curated
    # delete/update resources to the SCMClient list getter that names them.
    _NAME_SOURCES = {
        # objects
        "address":               "get_addresses",
        "address-group":         "get_address_groups",
        "service":               "get_services",
        "service-group":         "get_service_groups",
        "tag":                   "get_tags",
        "external-dynamic-list": "get_external_dynamic_lists",
        # security
        "url-categories":        "get_url_categories",
        "security":              "get_security_policy",
        # network
        "interface":             "get_interfaces",
        "zone":                  "get_zones",
        "nat-rules":             "get_nat_rules",
        "ike-gateway":           "get_ike_gateways",
        "ipsec-tunnel":          "get_ipsec_tunnels",
    }
    _NAME_TTL_S = 60

    def _object_names(self, resource: str, local_only: bool = False) -> list[str]:
        """Existing object names in the active folder, cached for a minute.

        local_only=True: only return objects owned at the current folder level
                         (obj["folder"] == active folder). Use for delete/update/set
                         so operators can't accidentally target inherited objects.
        local_only=False: return all names including inherited. Use for show.
        """
        scm = getattr(self._shell, "_scm", None)
        if scm is None:
            return []
        folder = self._shell._state.folder
        cache = getattr(self, "_name_cache", None)
        if cache is None:
            cache = self._name_cache = {}
        cache_key = (resource, folder)
        hit = cache.get(cache_key)
        now = time.monotonic()
        if hit and now - hit[1] < self._NAME_TTL_S:
            objects = hit[0]
        else:
            getter = getattr(scm, self._NAME_SOURCES[resource], None)
            if getter is None:
                return []
            try:
                objects = getter(folder=folder)
            except Exception:  # noqa: BLE001
                cache[cache_key] = ([], now)
                return []
            cache[cache_key] = (objects[:200], now)
            objects = cache[cache_key][0]

        if local_only:
            # Only names where obj["folder"] matches the active folder
            return [
                str(o.get("name")) for o in objects
                if isinstance(o, dict) and o.get("name")
                and (o.get("folder") or "").lower() == folder.lower()
            ]
        return [str(o.get("name")) for o in objects if isinstance(o, dict) and o.get("name")]

    def _dynamic_name_options(self, key: str, typed: list[str]) -> list[dict]:
        """Live object names for name-completion slots.

        show <resource>   → all names including inherited (read-only ok)
        delete/update/set → only locally-owned names (cannot edit inherited objects)
        """
        parts = key.split()
        verb = parts[0] if parts else ""
        if verb not in ("show", "delete", "update", "set") or len(parts) != 2:
            return []
        resource = parts[1]
        if resource not in self._NAME_SOURCES:
            return []
        if len(typed) > 1:
            return []
        partial = typed[0].lower() if typed else ""
        folder = self._shell._state.folder
        # For write verbs: only show locally-owned objects (not inherited)
        local_only = verb in ("delete", "update", "set")
        names = self._object_names(resource, local_only=local_only)
        results = [
            {"text": name, "display": name,
             "meta": f"in {folder}" if local_only else f"(type to filter)"}
            for name in names
            if not partial or name.lower().startswith(partial)
        ]
        return results

    def _arg_options(self, key: str, typed: list[str]) -> list[dict]:
        """Resolve next-slot argument options: structure file first, usage fallback.

        Returns a list of ``{text, display, meta}`` records.  Always non-None so a
        required value slot shows a hint rather than an empty (silent) result.
        Live object names are offered first when the slot names an existing object.
        """
        dynamic = self._dynamic_name_options(key, typed)
        spec = command_structure.arg_spec(key)
        if spec is not None:
            return dynamic + command_structure.completion_options(spec, typed)
        cmd = COMMANDS.get(key)
        if cmd and cmd.usage and self._command_visible(key):
            return dynamic + [
                {"text": opt, "display": opt, "meta": meta}
                for opt, meta in _usage_options(cmd.usage, key, typed)
            ]
        return dynamic


    def _all_commands(self, include_remote_suffix: bool) -> list[str]:
        dev_mode = getattr(self._shell, "_dev_mode", False)
        vis = getattr(self._shell, "_command_visibility", {})
        # Filter builtins the same way ? does — dev mode reveals everything.
        builtins = [b for b in _SHELL_BUILTINS if is_command_visible(b, vis, dev_mode)]
        commands = self._shell._visible_command_keys()
        if not include_remote_suffix:
            return builtins + commands
        with_remote = [f"{c} --remote" for c in commands]
        return builtins + commands + with_remote

    def _dev_gated_commands(self) -> list[str]:
        """Return command keys that are gated by a 'dev' feature flag.

        These are visible only in dev mode, but we surface them in normal
        tab completion with a '[dev mode]' hint so operators know they exist.
        """
        dev_mode = getattr(self._shell, "_dev_mode", False)
        if dev_mode:
            return []  # already visible in normal listing
        features = getattr(self._shell, "_features", {})
        result = []
        for key, cmd in COMMANDS.items():
            if cmd.feature_flag and feature_state(features, cmd.feature_flag) == "dev":
                result.append(key)
        return result
