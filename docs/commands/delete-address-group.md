---
command: "delete address-group"
description: "Delete an address group — delete address-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/address-groups/{id}"
---

---
command: "delete address-group"
description: "Delete an address group — delete address-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/address-groups/{id}"
---

---
command: "delete address-group"
description: "Delete an address group — delete address-group <name>"
usage: "delete address-group <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/address-groups/{id}"
---

# delete address-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an address group — delete address-group <name>

## Usage

```
delete address-group [--remote]
```

## Examples

Run via SCM API:
```
arc > delete address-group
```

Run directly on device via SSH:
```
arc:fw-01 > delete address-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete address-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
