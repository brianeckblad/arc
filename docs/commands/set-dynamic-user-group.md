# set dynamic-user-group

Create a **dynamic-user-group** object in the active SCM folder.

## Feature flag

This command requires the **`local_users`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable local_users

# Enable permanently (settings/features.json — git-ignored):
{"  \"local_users\": true"}
```

## Syntax

```text
configure
set dynamic-user-group <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/dynamic-user-groups
```

Resource notes: dynamic group of users matching a filter

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
arc:global # feature enable local_users
arc:global # set dynamic-user-group MyObject ...
  ✓ Dynamic-User-Group MyObject created (id: ...)
```

## Related commands

- `show dynamic-user-group` — list dynamic-user-group objects in the active folder
- `delete dynamic-user-group <name>` — remove a dynamic-user-group object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
