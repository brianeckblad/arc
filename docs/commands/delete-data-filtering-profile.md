# delete data-filtering-profile

Delete a **data-filtering-profile** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`security_profiles`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete data-filtering-profile <name>
```

## API

```
DELETE /config/security/v1/data-filtering-profiles/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete data-filtering-profile MyObject
  ✓ Data-Filtering-Profile MyObject deleted.
```

## Related commands

- `show data-filtering-profile` — list data-filtering-profile objects (to confirm name)
- `set data-filtering-profile <name>` — create a data-filtering-profile object

---
*Generated stub.*
