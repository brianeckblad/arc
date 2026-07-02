---
command: "set ngts edgeinstances update"
description: "Trigger manual update of Satellite Instance"
category: ngts
scope: global
---

# set ngts edgeinstances update

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Trigger manual update of Satellite Instance

## Usage

```
set ngts edgeinstances update [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts edgeinstances update
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts edgeinstances update --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts edgeinstances update
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
