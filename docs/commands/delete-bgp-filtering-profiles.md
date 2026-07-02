---
command: "delete bgp-filtering-profiles"
description: "Delete a BGP filtering profile"
category: network
scope: global
---

# delete bgp-filtering-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a BGP filtering profile

## Usage

```
delete bgp-filtering-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete bgp-filtering-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete bgp-filtering-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete bgp-filtering-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
