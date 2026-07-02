---
command: "update bgp-auth-profiles"
description: "Update a BGP authentication profile"
category: network
scope: global
---

# update bgp-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a BGP authentication profile

## Usage

```
update bgp-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update bgp-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update bgp-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update bgp-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
