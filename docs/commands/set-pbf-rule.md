# set pbf-rule

Create a **pbf-rule** object in the active SCM folder.

## Feature flag

This command requires the **`pbf_rules`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable pbf_rules

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"pbf_rules\": true"}
```

## Syntax

```text
configure
set pbf-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/pbf-rules
```

Resource notes: policy-based forwarding rules

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
arc:global # feature enable pbf_rules
arc:global # set pbf-rule MyObject ...
  ✓ Pbf-Rule MyObject created (id: ...)
```

## Related commands

- `show pbf-rule` — list pbf-rule objects in the active folder
- `delete pbf-rule <name>` — remove a pbf-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
