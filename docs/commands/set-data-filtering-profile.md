# set data-filtering-profile

Create a **data-filtering-profile** object in the active SCM folder.

## Feature flag

This command requires the **`security_profiles`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable security_profiles

# Enable permanently (settings/features.json — git-ignored):
{"  \"security_profiles\": true"}
```

## Syntax

```text
configure
set data-filtering-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/security/v1/data-filtering-profiles
```

Resource notes: data loss prevention (DLP) profile

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
arc:global # set data-filtering-profile MyObject ...
  ✓ Data-Filtering-Profile MyObject created (id: ...)
```

## Related commands

- `show data-filtering-profile` — list data-filtering-profile objects in the active folder
- `delete data-filtering-profile <name>` — remove a data-filtering-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
