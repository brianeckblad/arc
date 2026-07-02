# dev — Development Mode (hidden command)

`dev` is a **hidden** command — it does not appear in `?` help or tab
completion. It toggles **development mode**, which reveals every command whose
feature flag is set to `"dev"` in `its settings/features/ file`.

This exists so a team can ship work-in-progress commands without confusing
normal users: a `"dev"` command stays invisible until someone deliberately
enters development mode.

## Usage

```text
dev            Toggle development mode on/off
dev on         Force development mode on
dev off        Force development mode off
dev status     Show the current state without changing it
```

When development mode is on, the prompt shows a magenta `dev` marker:

```text
arc:global:dev >
```

## How it fits with feature flags

Each flag in `its settings/features/ file` has three states:

| State | Visible to normal users | Visible in development mode |
|-------|:-----------------------:|:--------------------------:|
| `true`  | ✅ | ✅ |
| `"dev"` | ❌ | ✅ |
| `false` | ❌ | ❌ |

Typical lifecycle:

1. Build a command and mark its flag `"dev"` in `its settings/features/ file`.
2. Run ARC, type `dev`, and test the command in development mode.
3. When it is ready for everyone, set the flag to `true`.

## CI/CD

Start ARC already in development mode (no typing required):

```bash
ARC_DEV_MODE=1 arc
```

Session state is never written to disk — development mode resets to off on the
next start unless `ARC_DEV_MODE` is set.

## Related

- `help features` — the full feature-flag reference
- `settings/README.md` — overview of all user-editable files

