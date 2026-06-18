# set loopback-interface

Create a **loopback-interface** object in the active SCM folder.

## Feature flag

This command requires the **`show_interface`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_interface

# Enable permanently (config/features.json — git-ignored):
{"  \"show_interface\": true"}
```

## Syntax

```text
configure
set loopback-interface <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/loopback-interfaces
```

Resource notes: loopback interface

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
arc:global # set loopback-interface MyObject ...
  ✓ Loopback-Interface MyObject created (id: ...)
```

## Related commands

- `show loopback-interface` — list loopback-interface objects in the active folder
- `delete loopback-interface <name>` — remove a loopback-interface object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
