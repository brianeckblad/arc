---
command: "update posture root"
description: "Update Posture Check"
category: posture
scope: global
---

# update posture root

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Posture Check

## Usage

```
update posture root [--remote]
```

## Examples

Run via SCM API:
```
arc > update posture root
```

Run directly on device via SSH:
```
arc:fw-01 > update posture root --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update posture root
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
