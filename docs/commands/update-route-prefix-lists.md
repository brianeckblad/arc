---
command: "update route-prefix-lists"
description: "Update a route prefix list"
category: network
scope: global
---

# update route-prefix-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a route prefix list

## Usage

```
update route-prefix-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > update route-prefix-lists
```

Run directly on device via SSH:
```
arc:fw-01 > update route-prefix-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update route-prefix-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
