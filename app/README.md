# `app/` — Application Code

Everything that runs at `arc` / `python run.py` time lives here. Code only —
user-editable assets are in `settings/`, secrets in `config/<user>/`
(the three-folder rule; see the root [README](../README.md)).

## What lives here

| Path | One line |
|---|---|
| `cli.py` | Typer entry point: `arc`, `arc auth …`, `arc config …`, `arc scm …`, `arc cliup` |
| `paths.py` | Single source of truth for asset paths — never hard-code a path elsewhere |
| `config.py` | `ArcConfig` + named profiles; secrets in the OS keychain, non-sensitive in `config/<user>/config.json` |
| `docs.py` | `help <topic>` renderer + `synthesize_command_help` for commands with no doc file |
| `shell/` | The REPL as mixins — see [shell/README.md](shell/README.md) |
| `commands/` | CommandDef registry (curated + generated + PAN-OS) — see [commands/README.md](commands/README.md) |
| `api/` | `SCMClient` (REST) + SLS log-query client — see [api/README.md](api/README.md) |
| `settings/` | Loaders for `settings/*` files + generated field catalog — see [settings/README.md](settings/README.md) |
| `ssh/manager.py` | Paramiko connection pool: agent → key file → keyboard-interactive (password + 2FA) → password |
| `utils/formatter.py` | Rich renderers — `_simple_table` + special-case formatters keyed by `render=` |
| `__init__.py` | Version: `0.1.<commit-count>` — never hand-edit |

## How the pieces relate

`cli.py` bootstraps config and starts `shell.ArcShell`. The shell dispatches
each line: builtins (names + help from `settings/builtin-commands.json`, loaded
via `settings/commands.py`) first, then `registry.match_command()`
over the merged CommandDef dict. Handlers get an `ExecutionContext` carrying
`.scm` (SCMClient), `.ssh` (SSHManager), `.config`, `.device`, `.folder`,
`.tsg_id`. Results are rendered by `_render()` → `utils/formatter.py`.
Writes never execute directly — they are staged in configure mode and replayed
at `commit` (see `shell/configure.py`).

## How to change things here

- Find code without reading whole files: `app/scripts/CODE_MAP.md` maps methods in
  300+ line files to exact line ranges.
- New command → `app/commands/<domain>.py` (recipe in AGENTS.md; stub via
  `python app/scripts/scaffold.py "show x" <module>`). Validate: `python app/scripts/smoke_test.py --only 1,2,3`.
- Output/table change → `utils/formatter.py` + `_render()` in
  `shell/execution.py`. Validate: `python app/scripts/smoke_test.py --file app/utils/formatter.py`.
- Auth/profiles → `config.py` + the auth group in `cli.py`. Validate:
  `python app/scripts/smoke_test.py --file app/config.py`.
- Any `.py` change: at minimum `python app/scripts/smoke_test.py --only 1,2`;
  full suite before commit.

## Do not

- Do not hand-edit `commands/resource_catalog.py`, `commands/panos_catalog.py`,
  or `settings/field_catalog.py` — AUTO-GENERATED (headers say so).
- Do not hard-code paths to `settings/`, `docs/`, or `config/` — import from `paths.py`.
- Do not add a write path that bypasses staging, or an inline `is_enabled()`
  visibility check (use `ArcShell._is_command_visible()`).
- Do not bump the version in `__init__.py` by hand.
