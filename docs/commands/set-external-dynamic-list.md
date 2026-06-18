# set external-dynamic-list

Create a **external-dynamic-list** object in the active SCM folder.

## Feature flag

This command requires the **`create_edl`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable create_edl

# Enable permanently (config/features.json — git-ignored):
{"  \"create_edl\": true"}
```

## Syntax

```text
configure
set external-dynamic-list <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/external-dynamic-lists
```

Resource notes: ip | domain | url | imsi | imei

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

> **Full schema:** See `docs/scm-api/specs/ngfw-objects.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable create_edl
arc:global # set external-dynamic-list MyObject ...
  ✓ External-Dynamic-List MyObject created (id: ...)
```

## Related commands

- `show external-dynamic-list` — list external-dynamic-list objects in the active folder
- `delete external-dynamic-list <name>` — remove a external-dynamic-list object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
