---
command: "show bgp-routemap-redist"
description: "List BGP route map redistributions"
category: network
scope: global
---

# show bgp-routemap-redist

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List BGP route map redistributions

## Usage

```
show bgp-routemap-redist [--remote]
```

## Examples

Run via SCM API:
```
arc > show bgp-routemap-redist
```

Run directly on device via SSH:
```
arc:fw-01 > show bgp-routemap-redist --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show bgp-routemap-redist
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
