# set decryption-exclusion

Create a **decryption-exclusion** object in the active SCM folder.

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
set decryption-exclusion <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/decryption-exclusions
```

Resource notes: hosts excluded from SSL decryption

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
arc:global # set decryption-exclusion MyObject ...
  ✓ Decryption-Exclusion MyObject created (id: ...)
```

## Related commands

- `show decryption-exclusion` — list decryption-exclusion objects in the active folder
- `delete decryption-exclusion <name>` — remove a decryption-exclusion object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
