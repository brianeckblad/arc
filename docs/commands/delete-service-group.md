---
command: "delete service-group"
description: "Delete a service group — delete service-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/service-groups/{id}"
---

---
command: "delete service-group"
description: "Delete a service group — delete service-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/service-groups/{id}"
---

---
command: "delete service-group"
description: "Delete a service group — delete service-group <name>"
usage: "delete service-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/service-groups/{id}"
---

# delete service-group

Delete a **service-group** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`create_service_group`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete service-group <name>
```

## API

```
DELETE /config/objects/v1/service-groups/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete service-group MyObject
  ✓ Service-Group MyObject deleted.
```

## Related commands

- `show service-group` — list service-group objects (to confirm name)
- `set service-group <name>` — create a service-group object

---
*Generated stub.*
