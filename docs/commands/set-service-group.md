# set service-group

Create a **service-group** object in the active SCM folder.

## Feature flag

This command requires the **`create_service_group`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable create_service_group

# Enable permanently (config/features.json — git-ignored):
{"  \"create_service_group\": true"}
```

## Syntax

```text
configure
set service-group <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/service-groups
```

Resource notes: named list of service objects

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
arc:global # feature enable create_service_group
arc:global # set service-group MyObject ...
  ✓ Service-Group MyObject created (id: ...)
```

## Related commands

- `show service-group` — list service-group objects in the active folder
- `delete service-group <name>` — remove a service-group object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
