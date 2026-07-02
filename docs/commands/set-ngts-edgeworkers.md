---
command: "set ngts edgeworkers"
description: "Create Satellite Worker"
category: ngts
scope: global
---

# set ngts edgeworkers

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Satellite Worker

## Usage

```
set ngts edgeworkers [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts edgeworkers
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts edgeworkers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts edgeworkers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
