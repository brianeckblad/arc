# set bgp-profile

Create a **bgp-profile** object in the active SCM folder.

## Feature flag

This command requires the **`bgp_routing`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable bgp_routing

# Enable permanently (config/features.json — git-ignored):
{"  \"bgp_routing\": true"}
```

## Syntax

```text
configure
set bgp-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/bgp-address-family-profiles
```

Resource notes: BGP address-family profile (SCM config)

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
arc:global # feature enable bgp_routing
arc:global # set bgp-profile MyObject ...
  ✓ Bgp-Profile MyObject created (id: ...)
```

## Related commands

- `show bgp-profile` — list bgp-profile objects in the active folder
- `delete bgp-profile <name>` — remove a bgp-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
