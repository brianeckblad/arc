# set tls-service-profile

Create a **tls-service-profile** object in the active SCM folder.

## Feature flag

This command requires the **`certificates`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable certificates

# Enable permanently (settings/features.json — git-ignored):
{"  \"certificates\": true"}
```

## Syntax

```text
configure
set tls-service-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/identity/v1/tls-service-profiles
```

Resource notes: TLS protocol versions and cipher suites

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

> **Full schema:** See `docs/scm-api/specs/ngfw-identity.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable certificates
arc:global # set tls-service-profile MyObject ...
  ✓ Tls-Service-Profile MyObject created (id: ...)
```

## Related commands

- `show tls-service-profile` — list tls-service-profile objects in the active folder
- `delete tls-service-profile <name>` — remove a tls-service-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
