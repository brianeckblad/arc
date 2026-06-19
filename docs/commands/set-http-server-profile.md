# set http-server-profile

Create a **http-server-profile** object in the active SCM folder.

## Feature flag

This command requires the **`log_profiles`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable log_profiles

# Enable permanently (settings/features.json — git-ignored):
{"  \"log_profiles\": true"}
```

## Syntax

```text
configure
set http-server-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/http-server-profiles
```

Resource notes: HTTP server profile for log forwarding

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
arc:global # set http-server-profile MyObject ...
  ✓ Http-Server-Profile MyObject created (id: ...)
```

## Related commands

- `show http-server-profile` — list http-server-profile objects in the active folder
- `delete http-server-profile <name>` — remove a http-server-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
