---
command: "show bgp-redist-profiles id"
description: "Get a BGP redistribution profile"
category: network
scope: global
---

# show bgp-redist-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a BGP redistribution profile

## Usage

```
show bgp-redist-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-redist-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-redist-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-redist-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
