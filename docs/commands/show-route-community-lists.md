---
command: "show route-community-lists"
description: "List route community lists"
category: network
scope: global
---

# show route-community-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List route community lists

## Usage

```
show route-community-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-community-lists
```

Run directly on device via SSH:
```
arc:fw-01 > show route-community-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-community-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
