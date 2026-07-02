---
command: "set tenant-service-groups"
description: "Create a tenant service group"
category: tenancy
scope: global
---

# set tenant-service-groups

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a tenant service group

## Usage

```
set tenant-service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set tenant-service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set tenant-service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tenant-service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
