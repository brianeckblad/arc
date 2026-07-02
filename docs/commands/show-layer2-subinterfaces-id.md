---
command: "show layer2-subinterfaces id"
description: "Get a layer 2 subinterface"
category: network
scope: global
---

# show layer2-subinterfaces id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a layer 2 subinterface

## Usage

```
show layer2-subinterfaces id [--remote]
```

## Examples

Run via SCM API:
```
arc > show layer2-subinterfaces id
```

Run directly on device via SSH:
```
arc:fw-01 > show layer2-subinterfaces id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show layer2-subinterfaces id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
