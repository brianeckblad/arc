---
command: "show route-path-acls id"
description: "Get a route path access list"
category: network
scope: global
---

# show route-path-acls id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a route path access list

## Usage

```
show route-path-acls id [--remote]
```

## Examples

Run via SCM API:
```
arc > show route-path-acls id
```

Run directly on device via SSH:
```
arc:fw-01 > show route-path-acls id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show route-path-acls id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
