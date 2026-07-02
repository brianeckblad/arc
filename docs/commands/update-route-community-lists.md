---
command: "update route-community-lists"
description: "Update a route community list"
category: network
scope: global
---

# update route-community-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a route community list

## Usage

```
update route-community-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > update route-community-lists
```

Run directly on device via SSH:
```
arc:fw-01 > update route-community-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update route-community-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
