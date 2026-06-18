# set snippet

Create a **snippet** object in the active SCM folder.

## Feature flag

This command requires the **`show_snippets`** feature flag to be enabled:

```bash
# Enable for this session:
arc> feature enable show_snippets

# Enable permanently (config/features.json — git-ignored):
{"  \"show_snippets\": true"}
```

## Syntax

```text
configure
set snippet <name> [<type-or-field> <value>] [description <text>] [tag <name>]
```

## API

```
POST /config/setup/v1/snippets
```

Resource notes: configuration snippet (reusable config block)

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
arc:global # feature enable show_snippets
arc:global # set snippet MyObject ...
  ✓ Snippet MyObject created (id: ...)
```

## Related commands

- `show snippet` — list snippet objects in the active folder
- `delete snippet <name>` — remove a snippet object
- `help features` — manage feature flags

---
*Generated stub — update this file when the command is fully implemented.*
