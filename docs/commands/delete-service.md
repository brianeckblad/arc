---
command: "delete service"
description: "Delete a service object — delete service <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/services/{id}"
---

---
command: "delete service"
description: "Delete a service object — delete service <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/services/{id}"
---

---
command: "delete service"
description: "Delete a service object — delete service <name>"
usage: "delete service <name>"
feature_flag: delete_objects
category: objects
scope: folder
api: "DELETE /config/objects/v1/services/{id}"
---

# delete service

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service object — delete service <name>

## Usage

```
delete service [--remote]
```

## Examples

Run via SCM API:
```
arc > delete service
```

Run directly on device via SSH:
```
arc:fw-01 > delete service --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete service
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
