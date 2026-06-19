# set aggregate-interface

Create a **aggregate-interface** object in the active SCM folder.

## Feature flag

This command requires the **`show_interface`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_interface

# Enable permanently (settings/features.json — git-ignored):
{"  \"show_interface\": true"}
```

## Syntax

```text
configure
set aggregate-interface <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/aggregate-interfaces
```

Resource notes: aggregate (LACP/802.3ad) interface

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

> **Full schema:** See `docs/scm-api/specs/ngfw-network.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable show_interface
arc:global # set aggregate-interface MyObject ...
  ✓ Aggregate-Interface MyObject created (id: ...)
```

## Related commands

- `show aggregate-interface` — list aggregate-interface objects in the active folder
- `delete aggregate-interface <name>` — remove a aggregate-interface object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
