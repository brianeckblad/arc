# `app/shell/` — The Interactive REPL (mixin package)

`ArcShell` is composed from one-concern-per-file mixins. Edit one mixin, not
the whole shell. Method line ranges live in `app/scripts/CODE_MAP.md` — read the range
you need, never a whole file.

## What lives here

| File | One line |
|---|---|
| `__init__.py` | Composes the mixins into `ArcShell` + the run loop; keeps the public surface (`ArcShell`, `ShellState`, `console`) stable |
| `_base.py` | The shared spine: imports, constants, helpers, `ShellState` — re-exported to every mixin via an auto-built `__all__` |
| `dispatch.py` | `_dispatch()`: parses + routes every input line; aliases, prefix expansion, pipes (`| match/except/count/json/save`), `watch`, `history` |
| `navigation.py` | `cd` / `folder` / `tsg` / `account` / `pwd` + device/folder/TSG caches |
| `execution.py` | `_execute_api` / `_execute_remote` / `_render()`; converts API errors into operator messages; PAN-OS drift warning |
| `configure.py` | Configure mode, `_stage_write` (local staging), `commit`/`commit check`/`watch`/`confirmed`/`confirm`, `abandon`, `feature`, `cli` theme |
| `write_cmd.py` | `set` / `set folder` (immediate folder creation) write parsing |
| `help.py` | The `?` system; **`_is_command_visible()` — the canonical visibility check** |
| `completer.py` | Context-aware Tab completion: usage slots, structure-aware curated `set`, live object-name completion (cached ~60 s) |
| `sessions.py` | `connect` / `remote` — transparent interactive SSH sessions |
| `prompt.py` | Prompt string, banner, startup help, goodbye |

## How the pieces relate

`_base.py` holds everything shared; each mixin does
`from app.shell._base import *`. Builtin **names** (and their help rows/visibility)
live in `settings/builtin-commands.json`, loaded via `app/settings/commands.py`
(edit the JSON first); their **behavior** is a `_cmd_*`
method plus an `elif` branch in `dispatch.py`. All visibility flows through
`help.py::_is_command_visible()` — dispatch, completion, fuzzy suggestions,
and `?` all call it.

## How to change things here

- Find the method via `app/scripts/CODE_MAP.md`, edit that one range, then validate:
  `python app/scripts/smoke_test.py --file app/shell/<file>.py`.
- New builtin: add the entry (name + 7 fields) in `settings/builtin-commands.json`,
  the `_cmd_*` method in the owning mixin, the dispatch branch in `dispatch.py`.
  Validate: `python app/scripts/smoke_test.py --only 8,9,12` (enforces builtin ↔
  help-row ↔ visibility sync).
- Banner changes (`prompt.py::_print_startup_help`): update `_BANNER_LINES`
  in `_base.py`; smoke §8 checks alignment.
- Completion changes: smoke `--only 9` (structure completion + context help).

## Do not

- Do not grow a mixin with unrelated concerns — new shared helpers go in
  `_base.py` (its `__all__` is built automatically; F401 is ignored there).
- Do not inline a bare `is_enabled()` check for command visibility — use
  `_is_command_visible()`.
- Do not add a write path that bypasses `_stage_write`, and never show
  `:Shared` in the prompt (it is the default state).
- Do not make `cd` open SSH — only `connect`/`remote` do.
