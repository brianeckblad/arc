---
command: "delete bgp-routemap-redist"
description: "Delete a BGP route map redistribution"
category: network
scope: global
---

# delete bgp-routemap-redist

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a BGP route map redistribution

## Usage

```
delete bgp-routemap-redist [--remote]
```

## Examples

Run via SCM API:
```
arc > delete bgp-routemap-redist
```

Run directly on device via SSH:
```
arc:fw-01 > delete bgp-routemap-redist --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete bgp-routemap-redist
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
