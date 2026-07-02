---
command: "set route-prefix-lists"
description: "Create a route prefix list"
category: network
scope: global
---

# set route-prefix-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a route prefix list

## Usage

```
set route-prefix-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > set route-prefix-lists
```

Run directly on device via SSH:
```
arc:fw-01 > set route-prefix-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set route-prefix-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
