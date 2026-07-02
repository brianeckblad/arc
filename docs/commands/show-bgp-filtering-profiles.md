---
command: "show bgp-filtering-profiles"
description: "List BGP filtering profiles"
category: network
scope: global
---

# show bgp-filtering-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List BGP filtering profiles

## Usage

```
show bgp-filtering-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-filtering-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-filtering-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-filtering-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
