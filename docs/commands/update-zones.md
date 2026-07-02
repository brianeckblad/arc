---
command: "update zones"
description: "Update a security zone"
category: network
scope: global
---

# update zones

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a security zone

## Usage

```
update zones [--remote]
```

## Examples

Run via SCM API:
```
arc > update zones
```

Run directly on device via SSH:
```
arc:fw-01 > update zones --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update zones
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
