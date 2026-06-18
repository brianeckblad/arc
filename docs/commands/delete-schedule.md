# delete schedule

Delete a **schedule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`schedules`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete schedule <name>
```

## API

```
DELETE /config/objects/v1/schedules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete schedule MyObject
  ✓ Schedule MyObject deleted.
```

## Related commands

- `show schedule` — list schedule objects (to confirm name)
- `set schedule <name>` — create a schedule object

---
*Generated stub.*
