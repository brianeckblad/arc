---
command: "set ngts machineidentities"
description: "Add a machine identity to a"
category: ngts
scope: global
---

# set ngts machineidentities

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add a machine identity to a

## Usage

```
set ngts machineidentities [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machineidentities
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machineidentities --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machineidentities
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
