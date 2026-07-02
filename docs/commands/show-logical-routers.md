---
command: "show logical-routers"
description: "List logical routers"
category: network
scope: global
---

# show logical-routers

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List logical routers

## Usage

```
show logical-routers [--remote]
```

## Examples

Run via SCM API:
```
arc > show logical-routers
```

Run directly on device via SSH:
```
arc:fw-01 > show logical-routers --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show logical-routers
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
