# set ike-gateway

Create a **ike-gateway** object in the active SCM folder.

## Feature flag

This command requires the **`ipsec_vpn`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable ipsec_vpn

# Enable permanently (settings/features.json — git-ignored):
{"  \"ipsec_vpn\": true"}
```

## Syntax

```text
configure
set ike-gateway <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/ike-gateways
```

Resource notes: IKE phase-1 gateway configuration

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
arc:global # set ike-gateway MyObject ...
  ✓ Ike-Gateway MyObject created (id: ...)
```

## Related commands

- `show ike-gateway` — list ike-gateway objects in the active folder
- `delete ike-gateway <name>` — remove a ike-gateway object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
