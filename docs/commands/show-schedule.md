---
command: "show schedule"
description: "Show schedules in the active folder"
feature_flag: schedules
category: objects
scope: folder
api: "GET /config/objects/v1/schedules"
---

---
command: "show schedule"
description: "Show schedules in the active folder"
feature_flag: schedules
category: objects
scope: folder
api: "GET /config/objects/v1/schedules"
---

---
command: "show schedule"
description: "Show schedules in the active folder"
feature_flag: schedules
category: objects
scope: folder
api: "GET /config/objects/v1/schedules"
---

# show schedule

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show schedules in the active folder

## Usage

```
show schedule [--remote]
```

## Examples

Run via SCM API:
```
arc > show schedule
```

Run directly on device via SSH:
```
arc:fw-01 > show schedule --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show schedule
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
