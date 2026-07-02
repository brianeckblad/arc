---
command: "set ngts edgeworkers pair"
description: "Pair Satellite Worker with Satellite Instance"
category: ngts
scope: global
---

# set ngts edgeworkers pair

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Pair Satellite Worker with Satellite Instance

## Usage

```
set ngts edgeworkers pair [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts edgeworkers pair
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts edgeworkers pair --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts edgeworkers pair
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
