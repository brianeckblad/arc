---
command: "set route-community-lists"
description: "Create a route community list"
category: network
scope: global
---

# set route-community-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a route community list

## Usage

```
set route-community-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > set route-community-lists
```

Run directly on device via SSH:
```
arc:fw-01 > set route-community-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set route-community-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
