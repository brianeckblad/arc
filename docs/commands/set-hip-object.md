# set hip-object

Create a **hip-object** object in the active SCM folder.

## Feature flag

This command requires the **`hip`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable hip

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"hip\": true"}
```

## Syntax

```text
configure
set hip-object <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/hip-objects
```

Resource notes: GlobalProtect host information profile object

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
arc:global # feature enable hip
arc:global # set hip-object MyObject ...
  ✓ Hip-Object MyObject created (id: ...)
```

## Related commands

- `show hip-object` — list hip-object objects in the active folder
- `delete hip-object <name>` — remove a hip-object object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
