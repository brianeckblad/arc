---
command: "delete route-path-acls"
description: "Delete a route path access list"
category: network
scope: global
---

# delete route-path-acls

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a route path access list

## Usage

```
delete route-path-acls [--remote]
```

## Examples

Run via SCM API:
```
arc > delete route-path-acls
```

Run directly on device via SSH:
```
arc:fw-01 > delete route-path-acls --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete route-path-acls
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
