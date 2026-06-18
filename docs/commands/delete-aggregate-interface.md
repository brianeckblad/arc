# delete aggregate-interface

Delete a **aggregate-interface** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`show_interface`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete aggregate-interface <name>
```

## API

```
DELETE /config/network/v1/aggregate-interfaces/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete aggregate-interface MyObject
  ✓ Aggregate-Interface MyObject deleted.
```

## Related commands

- `show aggregate-interface` — list aggregate-interface objects (to confirm name)
- `set aggregate-interface <name>` — create a aggregate-interface object

---
*Generated stub.*
