# set security-rule

Create a **security-rule** object in the active SCM folder.

## Feature flag

This command requires the **`create_security_rule`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable create_security_rule

# Enable permanently (settings/features.json — git-ignored):
{"  \"create_security_rule\": true"}
```

## Syntax

```text
configure
set security-rule <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/security-rules
```

Resource notes: allow|deny|drop with zone/address/app/service

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
arc:global # feature enable create_security_rule
arc:global # set security-rule MyObject ...
  ✓ Security-Rule MyObject created (id: ...)
```

## Related commands

- `show security-rule` — list security-rule objects in the active folder
- `delete security-rule <name>` — remove a security-rule object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
