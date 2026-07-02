---
command: "update bgp-routemap-redist"
description: "Update a BGP route map redistribution"
category: network
scope: global
---

# update bgp-routemap-redist

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a BGP route map redistribution

## Usage

```
update bgp-routemap-redist [--remote]
```

## Examples

Run via SCM API:
```
arc > update bgp-routemap-redist
```

Run directly on device via SSH:
```
arc:fw-01 > update bgp-routemap-redist --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update bgp-routemap-redist
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
