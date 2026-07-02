---
command: "update layer2-subinterfaces"
description: "Update a layer 2 subinterface"
category: network
scope: global
---

# update layer2-subinterfaces

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a layer 2 subinterface

## Usage

```
update layer2-subinterfaces [--remote]
```

## Examples

Run via SCM API:
```
arc > update layer2-subinterfaces
```

Run directly on device via SSH:
```
arc:fw-01 > update layer2-subinterfaces --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update layer2-subinterfaces
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
