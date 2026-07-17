---
command: "show application-group"
description: "Show application groups in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-groups"
---

---
command: "show application-group"
description: "Show application groups in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-groups"
---

---
command: "show application-group"
description: "Show application groups in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-groups"
---

# show application-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** `show objects application-group`

## Description

Show application groups in the active folder

## Usage

```
show application-group [--remote]
```

## Examples

Run via SCM API:
```
arc > show application-group
```

Run directly on device via SSH:
```
arc:fw-01 > show application-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show application-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
