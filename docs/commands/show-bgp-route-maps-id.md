---
command: "show bgp-route-maps id"
description: "Get a BGP route map"
category: network
scope: global
---

# show bgp-route-maps id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a BGP route map

## Usage

```
show bgp-route-maps id [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-route-maps id
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-route-maps id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-route-maps id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
