# set application-group

Create a **application-group** object in the active SCM folder.

## Feature flag

This command requires the **`app_groups`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable app_groups

# Enable permanently (config/features.json — git-ignored):
{"  \"app_groups\": true"}
```

## Syntax

```text
configure
set application-group <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/application-groups
```

Resource notes: group of predefined applications

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
arc:global # feature enable app_groups
arc:global # set application-group MyObject ...
  ✓ Application-Group MyObject created (id: ...)
```

## Related commands

- `show application-group` — list application-group objects in the active folder
- `delete application-group <name>` — remove a application-group object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
