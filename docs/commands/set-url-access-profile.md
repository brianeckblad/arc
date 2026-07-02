# set url-access-profile

Create a **url-access-profile** object in the active SCM folder.

## Feature flag

This command requires the **`security_profiles`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable security_profiles

# Enable permanently (its settings/features/ file — git-ignored):
{"  \"security_profiles\": true"}
```

## Syntax

```text
configure
set url-access-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/url-access-profiles
```

Resource notes: URL filtering access profile

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
arc:global # set url-access-profile MyObject ...
  ✓ Url-Access-Profile MyObject created (id: ...)
```

## Related commands

- `show url-access-profile` — list url-access-profile objects in the active folder
- `delete url-access-profile <name>` — remove a url-access-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
