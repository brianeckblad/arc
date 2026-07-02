---
command: "show route-prefix-lists id"
description: "Get a route prefix list"
category: network
scope: global
---

# show route-prefix-lists id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a route prefix list

## Usage

```
show route-prefix-lists id [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-prefix-lists id
```

Run directly on device via SSH:
```
arc:fw-01 > show route-prefix-lists id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-prefix-lists id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
