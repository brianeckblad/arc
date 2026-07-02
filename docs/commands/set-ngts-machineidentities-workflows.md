---
command: "set ngts machineidentities workflows"
description: "Initiate a machine workflow"
category: ngts
scope: global
---

# set ngts machineidentities workflows

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a machine workflow

## Usage

```
set ngts machineidentities workflows [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machineidentities workflows
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machineidentities workflows --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machineidentities workflows
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
