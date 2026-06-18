# set app-override-rule

Create a **app-override-rule** object in the active SCM folder.

## Feature flag

This command requires the **`app_override`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable app_override

# Enable permanently (config/features.json — git-ignored):
{"  \"app_override\": true"}
```

## Syntax

```text
configure
set app-override-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/app-override-rules
```

Resource notes: override application identification

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

> **Full schema:** See `docs/scm-api/specs/ngfw-security.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable app_override
arc:global # set app-override-rule MyObject ...
  ✓ App-Override-Rule MyObject created (id: ...)
```

## Related commands

- `show app-override-rule` — list app-override-rule objects in the active folder
- `delete app-override-rule <name>` — remove a app-override-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
