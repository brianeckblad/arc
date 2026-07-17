---
command: "show service-group"
description: "Show service groups in the active folder"
feature_flag: service_groups
category: objects
scope: folder
api: "GET /config/objects/v1/service-groups"
---

---
command: "show service-group"
description: "Show service groups in the active folder"
feature_flag: service_groups
category: objects
scope: folder
api: "GET /config/objects/v1/service-groups"
---

---
command: "show service-group"
description: "Show service groups in the active folder"
feature_flag: service_groups
category: objects
scope: folder
api: "GET /config/objects/v1/service-groups"
---

# show service-group

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** `show objects service-group`

## Description

Show service groups in the active folder

## Usage

```
show service-group [--remote]
```

## Examples

Run via SCM API:
```
arc > show service-group
```

Run directly on device via SSH:
```
arc:fw-01 > show service-group --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show service-group
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
