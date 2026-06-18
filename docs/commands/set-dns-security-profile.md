# set dns-security-profile

Create a **dns-security-profile** object in the active SCM folder.

## Feature flag

This command requires the **`security_profiles`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable security_profiles

# Enable permanently (config/features.json — git-ignored):
{"  \"security_profiles\": true"}
```

## Syntax

```text
configure
set dns-security-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/dns-security-profiles
```

Resource notes: DNS sinkholing and threat prevention

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
arc:global # feature enable security_profiles
arc:global # set dns-security-profile MyObject ...
  ✓ Dns-Security-Profile MyObject created (id: ...)
```

## Related commands

- `show dns-security-profile` — list dns-security-profile objects in the active folder
- `delete dns-security-profile <name>` — remove a dns-security-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
