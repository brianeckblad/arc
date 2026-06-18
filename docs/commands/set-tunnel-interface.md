# set tunnel-interface

Create a **tunnel-interface** object in the active SCM folder.

## Feature flag

This command requires the **`ipsec_vpn`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable ipsec_vpn

# Enable permanently (config/features.json — git-ignored):
{"  \"ipsec_vpn\": true"}
```

## Syntax

```text
configure
set tunnel-interface <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/tunnel-interfaces
```

Resource notes: IPsec/GRE tunnel interface

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
arc:global # feature enable ipsec_vpn
arc:global # set tunnel-interface MyObject ...
  ✓ Tunnel-Interface MyObject created (id: ...)
```

## Related commands

- `show tunnel-interface` — list tunnel-interface objects in the active folder
- `delete tunnel-interface <name>` — remove a tunnel-interface object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
