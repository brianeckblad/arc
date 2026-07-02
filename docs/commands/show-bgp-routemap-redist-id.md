---
command: "show bgp-routemap-redist id"
description: "Get a BGP route map redistribution"
category: network
scope: global
---

# show bgp-routemap-redist id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a BGP route map redistribution

## Usage

```
show bgp-routemap-redist id [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-routemap-redist id
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-routemap-redist id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-routemap-redist id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
