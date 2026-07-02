---
command: "delete layer3-subinterfaces"
description: "Delete a layer 3 subinterface"
category: network
scope: global
---

# delete layer3-subinterfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a layer 3 subinterface

## Usage

```
delete layer3-subinterfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > delete layer3-subinterfaces
```

Run directly on device via SSH:
```
arc:fw-01 > delete layer3-subinterfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete layer3-subinterfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
