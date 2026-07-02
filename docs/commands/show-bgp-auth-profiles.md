---
command: "show bgp-auth-profiles"
description: "List BGP authentication profiles"
category: network
scope: global
---

# show bgp-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List BGP authentication profiles

## Usage

```
show bgp-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
