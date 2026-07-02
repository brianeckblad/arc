---
command: "update bgp-route-maps"
description: "Update a BGP route map"
category: network
scope: global
---

# update bgp-route-maps

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a BGP route map

## Usage

```
update bgp-route-maps [--remote]
```

## Examples

Run via SCM API:
```
arc > update bgp-route-maps
```

Run directly on device via SSH:
```
arc:fw-01 > update bgp-route-maps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update bgp-route-maps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
