---
command: "show hip-profile"
description: "Show GlobalProtect HIP profiles in the active folder"
feature_flag: hip
category: objects
scope: folder
api: "GET /config/objects/v1/hip-profiles"
---

---
command: "show hip-profile"
description: "Show GlobalProtect HIP profiles in the active folder"
feature_flag: hip
category: objects
scope: folder
api: "GET /config/objects/v1/hip-profiles"
---

---
command: "show hip-profile"
description: "Show GlobalProtect HIP profiles in the active folder"
feature_flag: hip
category: objects
scope: folder
api: "GET /config/objects/v1/hip-profiles"
---

# show hip-profile

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show GlobalProtect HIP profiles in the active folder

## Usage

```
show hip-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show hip-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show hip-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show hip-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
