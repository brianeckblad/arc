---
command: "set bgp-route-maps"
description: "Create a BGP route map"
category: network
scope: global
---

# set bgp-route-maps

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a BGP route map

## Usage

```
set bgp-route-maps [--remote]
```

## Examples

Run via SCM API:
```
arc > set bgp-route-maps
```

Run directly on device via SSH:
```
arc:fw-01 > set bgp-route-maps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set bgp-route-maps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
