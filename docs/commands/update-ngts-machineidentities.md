---
command: "update ngts machineidentities"
description: "Update a machine identity details"
category: ngts
scope: global
---

# update ngts machineidentities

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a machine identity details

## Usage

```
update ngts machineidentities [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts machineidentities
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts machineidentities --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts machineidentities
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
