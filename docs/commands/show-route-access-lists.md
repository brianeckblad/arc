---
command: "show route-access-lists"
description: "List route access lists"
category: network
scope: global
---

# show route-access-lists

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List route access lists

## Usage

```
show route-access-lists [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-access-lists
```

Run directly on device via SSH:
```
arc:fw-01 > show route-access-lists --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-access-lists
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
