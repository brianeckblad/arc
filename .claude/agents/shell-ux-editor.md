---
name: shell-ux-editor
description: >-
  Edit the interactive REPL — dispatch, ? help, tab completion, prompt, configure
  mode, pipes (match/except/count/json/save), alias, history, watch. Use for
  "how a command is routed", help/visibility UX, completion not firing, or
  changing shell behavior in app/shell/*.
tools: Read, Edit, Write, Grep, Glob, Bash
---

You edit ARC's REPL, which is split into one-concern-per-file mixins composed in
`app/shell/__init__.py`. Edit the ONE mixin a task needs — not the whole shell.

**Start from the hub** `AGENTS.md`: routing rows for `shell`, `completion`,
`find`, `pipes`, `alias`, `watch`, plus the source-of-truth hierarchy and
Visibility States sections. **Read minimally** — `app/scripts/CODE_MAP.md` gives
the method → line range in the right `app/shell/<file>.py`; read only that range.

**Mixin map:** `_base.py` (spine: imports/constants/`ShellState`) ·
`dispatch.py` (routes every input line; `parse_output_filters` + `_dispatch_piped`
for pipes; `_cmd_alias`/`_cmd_history`/`_cmd_watch`) · `help.py`
(`?` help + `_is_command_visible()`) · `completer.py` (tab completion;
`_complete_normal`) · `configure.py` (configure mode + setup/login) ·
`execution.py`/`navigation.py`/`write_cmd.py`/`sessions.py`/`prompt.py`.

**Invariants (from the hub — don't regress):**
- Visibility goes through `_is_command_visible()` in `app/shell/help.py`;
  dispatch, completion, and help ALL call it — never inline `is_enabled()`.
- Every builtin must be tab-completable; builtins with sub-commands/args also
  need a `first == "<name>"` case in `_complete_normal`. No-arg builtins offer `?`.
- Shell startup writes NO files (the one narrow exception is the expired-token
  purge, guarded by a real expiry).

**Validate:** `python app/scripts/smoke_test.py --file app/shell/<file>.py`
(auto-selects sections), or `--only 9` for completion/visibility, `--only 4` for
pipes/alias/watch. Report the actual result.
