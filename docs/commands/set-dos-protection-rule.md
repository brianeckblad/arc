# set dos-protection-rule

Create a **dos-protection-rule** object in the active SCM folder.

## Feature flag

This command requires the **`dos_protection`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable dos_protection

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"dos_protection\": true"}
```

## Syntax

```text
configure
set dos-protection-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/dos-protection-rules
```

Resource notes: DoS protection policy rules

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
arc:global # feature enable dos_protection
arc:global # set dos-protection-rule MyObject ...
  ✓ Dos-Protection-Rule MyObject created (id: ...)
```

## Related commands

- `show dos-protection-rule` — list dos-protection-rule objects in the active folder
- `delete dos-protection-rule <name>` — remove a dos-protection-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
