# delete application-filter

Delete a **application-filter** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`app_groups`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete application-filter <name>
```

## API

```
DELETE /config/objects/v1/application-filters/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete application-filter MyObject
  ✓ Application-Filter MyObject deleted.
```

## Related commands

- `show application-filter` — list application-filter objects (to confirm name)
- `set application-filter <name>` — create a application-filter object

---
*Generated stub.*
