# set virtual-router

Create a **virtual-router** object in the active SCM folder.

## Feature flag

This command requires the **`show_routing`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_routing

# Enable permanently (config/features.json — git-ignored):
{"  \"show_routing\": true"}
```

## Syntax

```text
configure
set virtual-router <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/virtual-routers
```

Resource notes: virtual router (routing domain)

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
arc:global # feature enable show_routing
arc:global # set virtual-router MyObject ...
  ✓ Virtual-Router MyObject created (id: ...)
```

## Related commands

- `show virtual-router` — list virtual-router objects in the active folder
- `delete virtual-router <name>` — remove a virtual-router object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
