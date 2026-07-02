---
command: "show route-access-lists id"
description: "Get a route access list"
category: network
scope: global
---

# show route-access-lists id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a route access list

## Usage

```
show route-access-lists id [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-access-lists id
```

Run directly on device via SSH:
```
arc:fw-01 > show route-access-lists id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-access-lists id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
