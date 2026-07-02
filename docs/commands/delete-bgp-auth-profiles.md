---
command: "delete bgp-auth-profiles"
description: "Delete a BGP authentication profile"
category: network
scope: global
---

# delete bgp-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a BGP authentication profile

## Usage

```
delete bgp-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete bgp-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete bgp-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete bgp-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
