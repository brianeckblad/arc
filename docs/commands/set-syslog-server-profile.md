# set syslog-server-profile

Create a **syslog-server-profile** object in the active SCM folder.

## Feature flag

This command requires the **`log_profiles`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable log_profiles

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"log_profiles\": true"}
```

## Syntax

```text
configure
set syslog-server-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/syslog-server-profiles
```

Resource notes: syslog server configuration for log forwarding

## Supported methods

- GET (list)
- POST (create)
- PUT (update)
- DELETE

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `name` | Yes | Object name (must be unique in folder) |
| `folder` | Yes | Set automatically from active folder context |
| `description` | No | Human-readable description |
| `tag` | No | One or more tag names to associate |

> **Full schema:** See `docs/scm-api/specs/ngfw-objects.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable log_profiles
arc:global # set syslog-server-profile MyObject ...
  ✓ Syslog-Server-Profile MyObject created (id: ...)
```

## Related commands

- `show syslog-server-profile` — list syslog-server-profile objects in the active folder
- `delete syslog-server-profile <name>` — remove a syslog-server-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
