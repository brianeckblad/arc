# set sdwan-rule

Create a **sdwan-rule** object in the active SCM folder.

## Feature flag

This command requires the **`sdwan`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable sdwan

# Enable permanently (config/features.json — git-ignored):
{"  \"sdwan\": true"}
```

## Syntax

```text
configure
set sdwan-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/sdwan-rules
```

Resource notes: SD-WAN path selection rules

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
arc:global # feature enable sdwan
arc:global # set sdwan-rule MyObject ...
  ✓ Sdwan-Rule MyObject created (id: ...)
```

## Related commands

- `show sdwan-rule` — list sdwan-rule objects in the active folder
- `delete sdwan-rule <name>` — remove a sdwan-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
