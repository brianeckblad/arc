---
command: "delete route-access-lists"
description: "Delete a route access list"
category: network
scope: global
---

# delete route-access-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a route access list

## Usage

```
delete route-access-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > delete route-access-lists
```

Run directly on device via SSH:
```
arc:fw-01 > delete route-access-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete route-access-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
