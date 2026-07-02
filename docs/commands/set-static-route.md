# set static-route

Create a **static-route** object in the active SCM folder.

## Feature flag

This command requires the **`show_routing`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_routing

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"show_routing\": true"}
```

## Syntax

```text
configure
set static-route <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/routing/static-routes
```

Resource notes: static routing table entries

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
arc:global # set static-route MyObject ...
  ✓ Static-Route MyObject created (id: ...)
```

## Related commands

- `show static-route` — list static-route objects in the active folder
- `delete static-route <name>` — remove a static-route object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
