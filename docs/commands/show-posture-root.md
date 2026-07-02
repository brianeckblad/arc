---
command: "show posture root"
description: "List Posture Checks"
category: posture
scope: global
---

# show posture root

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Posture Checks

## Usage

```
show posture root [--remote]
```

## Examples

Run via SCM API:
```
arc > show posture root
```

Run directly on device via SSH:
```
arc:fw-01 > show posture root --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show posture root
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
