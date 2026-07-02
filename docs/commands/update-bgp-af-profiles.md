---
command: "update bgp-af-profiles"
description: "Update a BGP address family profile"
category: network
scope: global
---

# update bgp-af-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a BGP address family profile

## Usage

```
update bgp-af-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update bgp-af-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update bgp-af-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update bgp-af-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
