---
command: "set posture clone"
description: "Clone Posture Check"
category: posture
scope: global
---

# set posture clone

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Clone Posture Check

## Usage

```
set posture clone [--remote]
```

## Examples

Run via SCM API:
```
arc > set posture clone
```

Run directly on device via SSH:
```
arc:fw-01 > set posture clone --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set posture clone
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
