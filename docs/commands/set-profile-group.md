# set profile-group

Create a **profile-group** object in the active SCM folder.

## Feature flag

This command requires the **`profile_groups`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable profile_groups

# Enable permanently (config/features.json — git-ignored):
{"  \"profile_groups\": true"}
```

## Syntax

```text
configure
set profile-group <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/profile-groups
```

Resource notes: bundle security profiles into one group

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
arc:global # feature enable profile_groups
arc:global # set profile-group MyObject ...
  ✓ Profile-Group MyObject created (id: ...)
```

## Related commands

- `show profile-group` — list profile-group objects in the active folder
- `delete profile-group <name>` — remove a profile-group object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
