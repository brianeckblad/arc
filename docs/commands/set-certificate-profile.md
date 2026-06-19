# set certificate-profile

Create a **certificate-profile** object in the active SCM folder.

## Feature flag

This command requires the **`certificates`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable certificates

# Enable permanently (settings/features.json — git-ignored):
{"  \"certificates\": true"}
```

## Syntax

```text
configure
set certificate-profile <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/identity/v1/certificate-profiles
```

Resource notes: certificate verification profile

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
arc:global # feature enable certificates
arc:global # set certificate-profile MyObject ...
  ✓ Certificate-Profile MyObject created (id: ...)
```

## Related commands

- `show certificate-profile` — list certificate-profile objects in the active folder
- `delete certificate-profile <name>` — remove a certificate-profile object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
