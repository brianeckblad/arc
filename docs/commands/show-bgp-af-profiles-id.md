---
command: "show bgp-af-profiles id"
description: "Get a BGP address family profile"
category: network
scope: global
---

# show bgp-af-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a BGP address family profile

## Usage

```
show bgp-af-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-af-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-af-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-af-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
