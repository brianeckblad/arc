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

