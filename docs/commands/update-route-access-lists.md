---
command: "update route-access-lists"
description: "Update a route access list"
category: network
scope: global
---

# update route-access-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a route access list

## Usage

```
update route-access-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > update route-access-lists
```

Run directly on device via SSH:
```
arc:fw-01 > update route-access-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update route-access-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
