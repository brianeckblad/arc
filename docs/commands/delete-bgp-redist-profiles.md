---
command: "delete bgp-redist-profiles"
description: "Delete a BGP redistribution profile"
category: network
scope: global
---

# delete bgp-redist-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a BGP redistribution profile

## Usage

```
delete bgp-redist-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete bgp-redist-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete bgp-redist-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete bgp-redist-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
