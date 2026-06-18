# delete zone

Delete a **zone** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`create_zone`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete zone <name>
```

## API

```
DELETE /config/network/v1/zones/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete zone MyObject
  ✓ Zone MyObject deleted.
```

## Related commands

- `show zone` — list zone objects (to confirm name)
- `set zone <name>` — create a zone object

---
*Generated stub.*
