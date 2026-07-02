---
command: "show ngts machineidentities id"
description: "Get a machine identity details"
category: ngts
scope: global
---

# show ngts machineidentities id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a machine identity details

## Usage

```
show ngts machineidentities id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts machineidentities id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts machineidentities id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts machineidentities id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
