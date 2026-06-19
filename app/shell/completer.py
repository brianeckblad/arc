"""ArcCompleter — context-aware tab completion for the ARC shell."""
from __future__ import annotations

from app.shell._base import *  # noqa: F401,F403  (shared spine namespace)


class ArcCompleter(Completer):
    """Context-aware tab completer.

    - After `cd` / `remote` / `connect` → completes with managed device names
    - After `folder`           → completes with SCM folder names
    - Otherwise               → completes with ARC command names + shell built-ins
    """


    def __init__(self, shell: "ArcShell") -> None:
        self._shell = shell

    def get_completions(self, document, complete_event):
        raw = document.text_before_cursor.lstrip()
        # Normalize internal whitespace: multiple spaces and tabs → single space.
        # Preserve whether the user just pressed space/tab (trailing whitespace = new token).
        ends_with_space = bool(raw) and raw[-1] in (" ", "\t")
        text = re.sub(r"[ \t]+", " ", raw).strip()
        if ends_with_space:
            text = text + " "  # restore single trailing space for has_arg_space detection

        parts = text.split()

        if not parts:
            for name in sorted(self._all_commands(include_remote_suffix=False)):
                yield Completion(name, start_position=0)
            return

        first = parts[0].lower()
        # True if the user has typed at least one space after the first token
        has_arg_space = len(parts) > 1 or text.endswith(" ")
        partial_arg = parts[1] if len(parts) > 1 else ""

        # ---- cd / remote / connect → device name or subcommand completion ----
        if first in ("cd", "remote", "connect") and has_arg_space:
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
                    candidate = device.get("hostname") or device.get("name") or ""
                    if candidate and candidate.lower().startswith(partial_arg.lower()):
                        yield Completion(candidate, start_position=-len(partial_arg), display_meta="device")
                return
            # cd device <name> → complete device name
            if first == "cd" and second == "device":
                partial_name = parts[2] if len(parts) > 2 else ""
                for device in self._shell._state.devices_cache:
                    candidate = device.get("hostname") or device.get("name") or ""
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
                candidate = device.get("hostname") or device.get("name") or ""
                if candidate and candidate.lower().startswith(partial_arg.lower()):
                    yield Completion(candidate, start_position=-len(partial_arg))
            return


        # ---- folder → SCM folder name completion + 'create' subcommand ----
        if first == "folder" and has_arg_space:
            # 'create' is a special subcommand — offer it before folder names.
            if len(parts) <= 2 and "create".startswith(partial_arg.lower()):
                yield Completion(
                    "create",
                    start_position=-len(partial_arg),
                    display_meta="create a new folder",
                )
            # Don't complete further after 'folder create <name>' (arbitrary name).
            if len(parts) >= 2 and parts[1].lower() == "create":
                return
            for folder in self._shell._state.folders_cache:
                if folder.lower().startswith(partial_arg.lower()):
                    yield Completion(folder, start_position=-len(partial_arg))
            return

        # ---- feature → subcommand + flag name completion ----
        if first == "feature" and has_arg_space:
            second = parts[1].lower() if len(parts) > 1 else ""
            if len(parts) <= 2:
                # Complete subcommands: show, enable, disable, help
                for sub in ("show", "enable", "disable", "help"):
                    if sub.startswith(partial_arg.lower()):
                        yield Completion(sub, start_position=-len(partial_arg))
            elif second in ("enable", "disable") and len(parts) <= 3:
                # Complete feature flag names from settings/features.json
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

        # ---- configure → mode-entry completion ----
        if first == "configure" and has_arg_space:
            for sub in ("t", "terminal"):
                if sub.startswith(partial_arg.lower()):
                    yield Completion(sub, start_position=-len(partial_arg))
            return

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
                    tsg_id = str(entry.get("id") or entry.get("tsg_id") or "")
                    display_name = str(entry.get("display_name") or entry.get("name") or "")
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
                    candidate = device.get("hostname") or device.get("name") or ""
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


        # ---- Default: ARC command + built-in completion ----
        # Trim trailing space before prefix matching so that typing "show address "
        # (with a space) still matches "show address-group" for Tab completion.
        include_remote_suffix = " --" in text
        text_trim = text.rstrip(" ")  # e.g. "show address " → "show address"
        for name in sorted(self._all_commands(include_remote_suffix=include_remote_suffix)):
            if name.startswith(text_trim) and name != text_trim:
                # Replace from the start of the last typed word.
                # start_position: how many chars to delete before inserting the completion.
                yield Completion(name, start_position=-len(text))

    def _all_commands(self, include_remote_suffix: bool) -> list[str]:
        builtins = list(_SHELL_BUILTINS)
        commands = list(COMMANDS.keys())
        if not include_remote_suffix:
            return builtins + commands
        with_remote = [f"{c} --remote" for c in commands]
        return builtins + commands + with_remote
