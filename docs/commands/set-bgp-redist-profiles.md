---
command: "set bgp-redist-profiles"
description: "Create a BGP redistribution profile"
category: network
scope: global
---

# set bgp-redist-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a BGP redistribution profile

## Usage

```
set bgp-redist-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set bgp-redist-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set bgp-redist-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set bgp-redist-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
