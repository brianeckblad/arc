---
command: "delete posture root"
description: "Delete Posture Check"
category: posture
scope: global
---

# delete posture root

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete Posture Check

## Usage

```
delete posture root [--remote]
```

## Examples

Run via SCM API:
```
arc > delete posture root
```

Run directly on device via SSH:
```
arc:fw-01 > delete posture root --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete posture root
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
