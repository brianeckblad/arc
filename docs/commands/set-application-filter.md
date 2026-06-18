# set application-filter

Create a **application-filter** object in the active SCM folder.

## Feature flag

This command requires the **`app_groups`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable app_groups

# Enable permanently (config/features.json — git-ignored):
{"  \"app_groups\": true"}
```

## Syntax

```text
configure
set application-filter <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/objects/v1/application-filters
```

Resource notes: filter based on app attributes

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
arc:global # feature enable app_groups
arc:global # set application-filter MyObject ...
  ✓ Application-Filter MyObject created (id: ...)
```

## Related commands

- `show application-filter` — list application-filter objects in the active folder
- `delete application-filter <name>` — remove a application-filter object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
