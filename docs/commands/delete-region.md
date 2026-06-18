# delete region

Delete a **region** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`regions`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete region <name>
```

## API

```
DELETE /config/objects/v1/regions/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete region MyObject
  ✓ Region MyObject deleted.
```

## Related commands

- `show region` — list region objects (to confirm name)
- `set region <name>` — create a region object

---
*Generated stub.*
