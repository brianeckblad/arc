---
command: "set posture root"
description: "Create Posture Check"
category: posture
scope: global
---

# set posture root

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Posture Check

## Usage

```
set posture root [--remote]
```

## Examples

Run via SCM API:
```
arc > set posture root
```

Run directly on device via SSH:
```
arc:fw-01 > set posture root --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set posture root
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
