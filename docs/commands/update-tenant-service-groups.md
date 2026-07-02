---
command: "update tenant-service-groups"
description: "Update a tenant service group"
category: tenancy
scope: global
---

# update tenant-service-groups

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a tenant service group

## Usage

```
update tenant-service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update tenant-service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update tenant-service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update tenant-service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
