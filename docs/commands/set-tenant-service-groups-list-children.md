---
command: "set tenant-service-groups list-children"
description: "List tenant service group children"
category: tenancy
scope: global
---

# set tenant-service-groups list-children

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List tenant service group children

## Usage

```
set tenant-service-groups list-children [--remote]
```

## Examples

Run via SCM API:
```
arc > set tenant-service-groups list-children
```

Run directly on device via SSH:
```
arc:fw-01 > set tenant-service-groups list-children --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tenant-service-groups list-children
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
