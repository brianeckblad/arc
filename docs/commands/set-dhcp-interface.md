# set dhcp-interface

Create a **dhcp-interface** object in the active SCM folder.

## Feature flag

This command requires the **`dhcp`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable dhcp

# Enable permanently (config/features.json — git-ignored):
{"  \"dhcp\": true"}
```

## Syntax

```text
configure
set dhcp-interface <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/dhcp-interfaces
```

Resource notes: DHCP server or relay on an interface

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
arc:global # feature enable dhcp
arc:global # set dhcp-interface MyObject ...
  ✓ Dhcp-Interface MyObject created (id: ...)
```

## Related commands

- `show dhcp-interface` — list dhcp-interface objects in the active folder
- `delete dhcp-interface <name>` — remove a dhcp-interface object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
