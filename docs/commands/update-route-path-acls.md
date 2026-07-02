---
command: "update route-path-acls"
description: "Update a route path access list"
category: network
scope: global
---

# update route-path-acls

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a route path access list

## Usage

```
update route-path-acls [--remote]
```

## Examples

Run via SCM API:
```
arc > update route-path-acls
```

Run directly on device via SSH:
```
arc:fw-01 > update route-path-acls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update route-path-acls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
