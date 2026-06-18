# set decryption-rule

Create a **decryption-rule** object in the active SCM folder.

## Feature flag

This command requires the **`decryption_policy`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable decryption_policy

# Enable permanently (config/features.json — git-ignored):
{"  \"decryption_policy\": true"}
```

## Syntax

```text
configure
set decryption-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/decryption-rules
```

Resource notes: SSL/TLS decryption policy rules

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

> **Full schema:** See `docs/scm-api/specs/ngfw-security.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable decryption_policy
arc:global # set decryption-rule MyObject ...
  ✓ Decryption-Rule MyObject created (id: ...)
```

## Related commands

- `show decryption-rule` — list decryption-rule objects in the active folder
- `delete decryption-rule <name>` — remove a decryption-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
