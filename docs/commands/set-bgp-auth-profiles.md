---
command: "set bgp-auth-profiles"
description: "Create a BGP authentication profile"
category: network
scope: global
---

# set bgp-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a BGP authentication profile

## Usage

```
set bgp-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set bgp-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set bgp-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set bgp-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
