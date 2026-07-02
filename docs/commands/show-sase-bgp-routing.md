---
command: "show sase bgp-routing"
description: "Get BGP routing settings"
category: sase
scope: global
---

# show sase bgp-routing

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get BGP routing settings

## Usage

```
show sase bgp-routing [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase bgp-routing
```

Run directly on device via SSH:
```
arc:fw-01 > show sase bgp-routing --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase bgp-routing
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
