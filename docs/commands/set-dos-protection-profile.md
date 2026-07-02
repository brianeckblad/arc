# set dos-protection-profile

Create a **dos-protection-profile** object in the active SCM folder.

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
set dos-protection-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/dos-protection-profiles
```

Resource notes: DoS protection threshold settings

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
arc:global # set dos-protection-profile MyObject ...
  ✓ Dos-Protection-Profile MyObject created (id: ...)
```

## Related commands

- `show dos-protection-profile` — list dos-protection-profile objects in the active folder
- `delete dos-protection-profile <name>` — remove a dos-protection-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
