---
command: "show ngts edgeinstances"
description: "Retrieve Satellite Instances"
category: ngts
scope: global
---

# show ngts edgeinstances

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Satellite Instances

## Usage

```
show ngts edgeinstances [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts edgeinstances
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts edgeinstances --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts edgeinstances
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
