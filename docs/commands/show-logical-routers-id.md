---
command: "show logical-routers id"
description: "Get a logical router"
category: network
scope: global
---

# show logical-routers id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a logical router

## Usage

```
show logical-routers id [--remote]
```

## Examples

Run via SCM API:
```
arc > show logical-routers id
```

Run directly on device via SSH:
```
arc:fw-01 > show logical-routers id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show logical-routers id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
