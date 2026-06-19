# set vlan-interface

Create a **vlan-interface** object in the active SCM folder.

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
set vlan-interface <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/vlan-interfaces
```

Resource notes: VLAN (layer 3 sub-interface)

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
arc:global # set vlan-interface MyObject ...
  ✓ Vlan-Interface MyObject created (id: ...)
```

## Related commands

- `show vlan-interface` — list vlan-interface objects in the active folder
- `delete vlan-interface <name>` — remove a vlan-interface object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
