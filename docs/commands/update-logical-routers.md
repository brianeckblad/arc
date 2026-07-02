---
command: "update logical-routers"
description: "Update a logical router"
category: network
scope: global
---

# update logical-routers

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a logical router

## Usage

```
update logical-routers [--remote]
```

## Examples

Run via SCM API:
```
arc > update logical-routers
```

Run directly on device via SSH:
```
arc:fw-01 > update logical-routers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update logical-routers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
