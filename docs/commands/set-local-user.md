# set local-user

Create a **local-user** object in the active SCM folder.

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
set local-user <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/identity/v1/local-users
```

Resource notes: local firewall user account

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
arc:global # feature enable local_users
arc:global # set local-user MyObject ...
  ✓ Local-User MyObject created (id: ...)
```

## Related commands

- `show local-user` — list local-user objects in the active folder
- `delete local-user <name>` — remove a local-user object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
