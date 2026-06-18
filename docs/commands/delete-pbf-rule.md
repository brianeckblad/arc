# delete pbf-rule

Delete a **pbf-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`pbf_rules`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete pbf-rule <name>
```

## API

```
DELETE /config/network/v1/pbf-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete pbf-rule MyObject
  ✓ Pbf-Rule MyObject deleted.
```

## Related commands

- `show pbf-rule` — list pbf-rule objects (to confirm name)
- `set pbf-rule <name>` — create a pbf-rule object

---
*Generated stub.*
