---
command: "set layer3-subinterfaces"
description: "Create a layer 3 subinterface"
category: network
scope: global
---

# set layer3-subinterfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a layer 3 subinterface

## Usage

```
set layer3-subinterfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > set layer3-subinterfaces
```

Run directly on device via SSH:
```
arc:fw-01 > set layer3-subinterfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set layer3-subinterfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
