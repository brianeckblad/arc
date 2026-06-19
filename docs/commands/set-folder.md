# set folder

Create a **folder** object in the active SCM folder.

## Feature flag

This command requires the **`show_devices`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_devices

# Enable permanently (settings/features.json — git-ignored):
{"  \"show_devices\": true"}
```

## Syntax

```text
configure
set folder <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/setup/v1/folders
```

Resource notes: SCM folder — use 'set folder <name>' in configure mode

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

> **Full schema:** See `docs/scm-api/specs/ngfw-setup.md` for all fields.

## Example

```text
arc:global > configure
arc:global # feature enable show_devices
arc:global # set folder MyObject ...
  ✓ Folder MyObject created (id: ...)
```

## Related commands

- `show folder` — list folder objects in the active folder
- `delete folder <name>` — remove a folder object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
