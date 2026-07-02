---
command: "set bgp-filtering-profiles"
description: "Create a BGP filtering profile"
category: network
scope: global
---

# set bgp-filtering-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a BGP filtering profile

## Usage

```
set bgp-filtering-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set bgp-filtering-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set bgp-filtering-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set bgp-filtering-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
