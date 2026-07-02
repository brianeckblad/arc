---
command: "set bgp-af-profiles"
description: "Create a BGP address family profile"
category: network
scope: global
---

# set bgp-af-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a BGP address family profile

## Usage

```
set bgp-af-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set bgp-af-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set bgp-af-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set bgp-af-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
