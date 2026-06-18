# set nat-rule

Create a **nat-rule** object in the active SCM folder.

## Feature flag

This command requires the **`create_nat_rule`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable create_nat_rule

# Enable permanently (config/features.json — git-ignored):
{"  \"create_nat_rule\": true"}
```

## Syntax

```text
configure
set nat-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/nat-rules
```

Resource notes: source/destination NAT translations

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
arc:global # feature enable create_nat_rule
arc:global # set nat-rule MyObject ...
  ✓ Nat-Rule MyObject created (id: ...)
```

## Related commands

- `show nat-rule` — list nat-rule objects in the active folder
- `delete nat-rule <name>` — remove a nat-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
