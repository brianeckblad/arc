---
command: "delete zones"
description: "Delete a security zone"
category: network
scope: global
---

# delete zones

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a security zone

## Usage

```
delete zones [--remote]
```

## Examples

Run via SCM API:
```
arc > delete zones
```

Run directly on device via SSH:
```
arc:fw-01 > delete zones --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete zones
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
