# delete sdwan-rule

Delete a **sdwan-rule** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`sdwan`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete sdwan-rule <name>
```

## API

```
DELETE /config/network/v1/sdwan-rules/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete sdwan-rule MyObject
  ✓ Sdwan-Rule MyObject deleted.
```

## Related commands

- `show sdwan-rule` — list sdwan-rule objects (to confirm name)
- `set sdwan-rule <name>` — create a sdwan-rule object

---
*Generated stub.*
