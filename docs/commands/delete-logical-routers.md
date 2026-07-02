---
command: "delete logical-routers"
description: "Delete a logical router"
category: network
scope: global
---

# delete logical-routers

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a logical router

## Usage

```
delete logical-routers [--remote]
```

## Examples

Run via SCM API:
```
arc > delete logical-routers
```

Run directly on device via SSH:
```
arc:fw-01 > delete logical-routers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete logical-routers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
