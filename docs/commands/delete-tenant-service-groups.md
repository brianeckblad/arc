---
command: "delete tenant-service-groups"
description: "Delete a tenant service group"
category: tenancy
scope: global
---

# delete tenant-service-groups

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a tenant service group

## Usage

```
delete tenant-service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete tenant-service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete tenant-service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete tenant-service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
