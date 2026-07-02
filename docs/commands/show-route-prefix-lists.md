---
command: "show route-prefix-lists"
description: "List route prefix lists"
category: network
scope: global
---

# show route-prefix-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List route prefix lists

## Usage

```
show route-prefix-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-prefix-lists
```

Run directly on device via SSH:
```
arc:fw-01 > show route-prefix-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-prefix-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
