---
command: "set ngts recoverycodes satellite"
description: "Create Recovery Code for Satellite Instance"
category: ngts
scope: global
---

# set ngts recoverycodes satellite

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Recovery Code for Satellite Instance

## Usage

```
set ngts recoverycodes satellite [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts recoverycodes satellite
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts recoverycodes satellite --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts recoverycodes satellite
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
