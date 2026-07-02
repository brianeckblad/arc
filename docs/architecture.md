# ARC Architecture

## Layers

- `app/cli.py` — Typer entry point and auth/config helper commands.
- `app/shell.py` — prompt-toolkit REPL, command dispatch, tab completion, docs-backed help.
- `app/commands/registry.py` — PAN-OS-like command registry and API/SSH mappings.
- `app/api/client.py` — SCM REST client.
- `app/ssh/manager.py` — Paramiko SSH connection pool.
- `app/utils/formatter.py` — Rich renderers for command output.
- `docs/` — user-facing Markdown rendered by `help <topic>` inside the shell.

## Dispatch model

1. Shell built-ins are handled first (`cd`, `remote`, `connect`, `folder`, `pwd`, `?`).
2. Registered commands are matched by longest command prefix.
3. API mode calls the command `api_handler`.
4. `--remote` or SSH mode calls the command/device over SSH.

## Documentation model

The agent instructions describe architecture and coding rules. The `docs/` folder is the user manual. ARC reads Markdown from `docs/` at runtime and renders it in the CLI.

## API coverage — generated and feature-gated

ARC's goal is broad coverage of the pulled SCM OpenAPI surface: generated command
metadata is created for `GET`, `POST`, `PUT`/`PATCH`, and `DELETE` operations.

- Curated commands (e.g. `show address`, `set address`, `show security policy`)
  have rich formatting/friendly argument parsing and live in `app/commands/*.py`.
- Generated commands cover the long tail from `app/commands/resource_catalog.py`.
  `GET` maps to `show`, `POST` maps to `set`, `PUT`/`PATCH` maps to `update`, and
  `DELETE` maps to `delete`.
- Generated commands are feature-gated through `settings/features/ (per-domain files)` and new
  flags default to `false`, so API surface stays hidden until intentionally
  enabled.
- When the API specs are refreshed (`docsupdate`), new endpoints become generated
  commands, command docs, API-index entries, and feature flags automatically.

So if Palo Alto adds a new API resource, ARC learns about it after the next docs
refresh. Enable the relevant feature flag when you are ready for operators to see
the generated command.

