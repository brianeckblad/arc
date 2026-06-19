# set authentication-rule

Create a **authentication-rule** object in the active SCM folder.

## Feature flag

This command requires the **`authentication`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable authentication

# Enable permanently (settings/features.json — git-ignored):
{"  \"authentication\": true"}
```

## Syntax

```text
configure
set authentication-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/identity/v1/authentication-rules
```

Resource notes: authentication policy rules

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
arc:global # feature enable authentication
arc:global # set authentication-rule MyObject ...
  ✓ Authentication-Rule MyObject created (id: ...)
```

## Related commands

- `show authentication-rule` — list authentication-rule objects in the active folder
- `delete authentication-rule <name>` — remove a authentication-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
