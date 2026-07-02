---
command: "show ngts machineidentities"
description: "Get the details of all machine"
category: ngts
scope: global
---

# show ngts machineidentities

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of all machine

## Usage

```
show ngts machineidentities [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts machineidentities
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts machineidentities --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts machineidentities
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
