---
command: "delete ngts edgeworkers"
description: "Delete Satellite Worker"
category: ngts
scope: global
---

# delete ngts edgeworkers

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete Satellite Worker

## Usage

```
delete ngts edgeworkers [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts edgeworkers
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts edgeworkers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts edgeworkers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
