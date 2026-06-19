# set schedule

Create a **schedule** object in the active SCM folder.

## Feature flag

This command requires the **`schedules`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable schedules

# Enable permanently (settings/features.json — git-ignored):
{"  \"schedules\": true"}
```

## Syntax

```text
configure
set schedule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/schedules
```

Resource notes: recurring or non-recurring time windows

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
arc:global # feature enable schedules
arc:global # set schedule MyObject ...
  ✓ Schedule MyObject created (id: ...)
```

## Related commands

- `show schedule` — list schedule objects in the active folder
- `delete schedule <name>` — remove a schedule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
