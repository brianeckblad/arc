# set region

Create a **region** object in the active SCM folder.

## Feature flag

This command requires the **`regions`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable regions

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"regions\": true"}
```

## Syntax

```text
configure
set region <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/regions
```

Resource notes: geographic region definitions

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
arc:global # feature enable regions
arc:global # set region MyObject ...
  ✓ Region MyObject created (id: ...)
```

## Related commands

- `show region` — list region objects in the active folder
- `delete region <name>` — remove a region object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
