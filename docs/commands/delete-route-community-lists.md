---
command: "delete route-community-lists"
description: "Delete a route community list"
category: network
scope: global
---

# delete route-community-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a route community list

## Usage

```
delete route-community-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > delete route-community-lists
```

Run directly on device via SSH:
```
arc:fw-01 > delete route-community-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete route-community-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
