---
command: "show application-filter"
description: "Show application filters in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-filters"
---

---
command: "show application-filter"
description: "Show application filters in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-filters"
---

---
command: "show application-filter"
description: "Show application filters in the active folder"
feature_flag: app_groups
category: objects
scope: folder
api: "GET /config/objects/v1/application-filters"
---

# show application-filter

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show application filters in the active folder

## Usage

```
show application-filter [--remote]
```

## Examples

Run via SCM API:
```
arc > show application-filter
```

Run directly on device via SSH:
```
arc:fw-01 > show application-filter --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show application-filter
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
