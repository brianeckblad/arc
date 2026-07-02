# set hip-profile

Create a **hip-profile** object in the active SCM folder.

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
set hip-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/hip-profiles
```

Resource notes: GlobalProtect HIP profile (combines HIP objects)

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
arc:global # set hip-profile MyObject ...
  ✓ Hip-Profile MyObject created (id: ...)
```

## Related commands

- `show hip-profile` — list hip-profile objects in the active folder
- `delete hip-profile <name>` — remove a hip-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
