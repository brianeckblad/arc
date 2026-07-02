---
command: "update sase bgp-routing"
description: "Update BGP routing settings"
category: sase
scope: global
---

# update sase bgp-routing

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update BGP routing settings

## Usage

```
update sase bgp-routing [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase bgp-routing
```

Run directly on device via SSH:
```
arc:fw-01 > update sase bgp-routing --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase bgp-routing
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
