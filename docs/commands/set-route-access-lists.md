---
command: "set route-access-lists"
description: "Create a route access list"
category: network
scope: global
---

# set route-access-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a route access list

## Usage

```
set route-access-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > set route-access-lists
```

Run directly on device via SSH:
```
arc:fw-01 > set route-access-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set route-access-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
