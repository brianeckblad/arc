---
command: "delete ngts machineidentities"
description: "Remove a machine identity"
category: ngts
scope: global
---

# delete ngts machineidentities

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove a machine identity

## Usage

```
delete ngts machineidentities [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts machineidentities
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts machineidentities --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts machineidentities
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
