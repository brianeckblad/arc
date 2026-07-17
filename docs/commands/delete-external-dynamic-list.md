---
command: "delete external-dynamic-list"
description: "Delete an EDL — delete external-dynamic-list <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/external-dynamic-lists/{id}"
---

---
command: "delete external-dynamic-list"
description: "Delete an EDL — delete external-dynamic-list <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/external-dynamic-lists/{id}"
---

---
command: "delete external-dynamic-list"
description: "Delete an EDL — delete external-dynamic-list <name>"
usage: "delete external-dynamic-list <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/external-dynamic-lists/{id}"
---

# delete external-dynamic-list

Delete a **external-dynamic-list** object by name from the active SCM folder.

## Feature flag

This command requires **`delete_objects`** or **`create_edl`** to be enabled:

```bash
arc> feature enable delete_objects
```

## Syntax

```text
configure
delete external-dynamic-list <name>
```

## API

```
DELETE /config/objects/v1/external-dynamic-lists/{id}
```

ARC looks up the object by name in the active folder, then sends the DELETE request.

## Example

```text
arc:global > configure
arc:global # delete external-dynamic-list MyObject
  ✓ External-Dynamic-List MyObject deleted.
```

## Related commands

- `show external-dynamic-list` — list external-dynamic-list objects (to confirm name)
- `set external-dynamic-list <name>` — create a external-dynamic-list object

---
*Generated stub.*
