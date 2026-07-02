---
command: "update bgp-redist-profiles"
description: "Update a BGP redistribution profile"
category: network
scope: global
---

# update bgp-redist-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a BGP redistribution profile

## Usage

```
update bgp-redist-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update bgp-redist-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update bgp-redist-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update bgp-redist-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
