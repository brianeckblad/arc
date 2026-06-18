# delete folder

Delete a **folder** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_devices`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete folder <name>
```

## API

```
DELETE /config/setup/v1/folders/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete folder MyObject
  ✓ Folder MyObject deleted.
```

## Related commands

- `show folder` — list folder objects (to confirm name)
- `set folder <name>` — create a folder object

---
*Generated stub.*
