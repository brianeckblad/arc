---
command: "set logical-routers"
description: "Create a logical router"
category: network
scope: global
---

# set logical-routers

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a logical router

## Usage

```
set logical-routers [--remote]
```

## Examples

Run via SCM API:
```
arc > set logical-routers
```

Run directly on device via SSH:
```
arc:fw-01 > set logical-routers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set logical-routers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
