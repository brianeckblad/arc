---
command: "show bgp-route-maps"
description: "List BGP route maps"
category: network
scope: global
---

# show bgp-route-maps

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List BGP route maps

## Usage

```
show bgp-route-maps [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-route-maps
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-route-maps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-route-maps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
