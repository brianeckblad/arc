---
command: "show route-path-acls"
description: "List route path access lists"
category: network
scope: global
---

# show route-path-acls

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List route path access lists

## Usage

```
show route-path-acls [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-path-acls
```

Run directly on device via SSH:
```
arc:fw-01 > show route-path-acls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-path-acls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
