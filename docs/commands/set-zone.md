# set zone

Create a **zone** object in the active SCM folder.

## Feature flag

This command requires the **`create_zone`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable create_zone

# Enable permanently (settings/features.json — git-ignored):
{"  \"create_zone\": true"}
```

## Syntax

```text
configure
set zone <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/network/v1/zones
```

Resource notes: layer3 | layer2 | virtual-wire | tap | tunnel

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

> **Full schema:** See `docs/scm-api/specs/ngfw-network.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable create_zone
arc:global # set zone MyObject ...
  ✓ Zone MyObject created (id: ...)
```

## Related commands

- `show zone` — list zone objects in the active folder
- `delete zone <name>` — remove a zone object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
