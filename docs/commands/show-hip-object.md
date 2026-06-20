---
command: "show hip-object"
description: "Show GlobalProtect HIP objects in the active folder"
feature_flag: hip
category: objects
scope: folder
api: "GET /config/objects/v1/hip-objects"
---

# show hip-object

**Category:** objects
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show GlobalProtect HIP objects in the active folder

## Usage

```
show hip-object [--remote]
```

## Examples

Run via SCM API:
```
arc > show hip-object
```

Run directly on device via SSH:
```
arc:fw-01 > show hip-object --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show hip-object
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
