# set authentication-profile

Create a **authentication-profile** object in the active SCM folder.

## Feature flag

This command requires the **`authentication`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable authentication

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"authentication\": true"}
```

## Syntax

```text
configure
set authentication-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/identity/v1/authentication-profiles
```

Resource notes: LDAP, RADIUS, SAML, or local auth profile

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

> **Full schema:** See `docs/scm-api/specs/ngfw-identity.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable authentication
arc:global # set authentication-profile MyObject ...
  ✓ Authentication-Profile MyObject created (id: ...)
```

## Related commands

- `show authentication-profile` — list authentication-profile objects in the active folder
- `delete authentication-profile <name>` — remove a authentication-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
