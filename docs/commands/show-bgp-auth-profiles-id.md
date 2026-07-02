---
command: "show bgp-auth-profiles id"
description: "Get a BGP authentication profile"
category: network
scope: global
---

# show bgp-auth-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a BGP authentication profile

## Usage

```
show bgp-auth-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-auth-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-auth-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-auth-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
