---
command: "update ngts edgeinstances"
description: "Update Satellite Instance"
category: ngts
scope: global
---

# update ngts edgeinstances

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Satellite Instance

## Usage

```
update ngts edgeinstances [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts edgeinstances
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts edgeinstances --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts edgeinstances
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
