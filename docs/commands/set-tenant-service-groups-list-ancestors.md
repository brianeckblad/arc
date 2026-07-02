---
command: "set tenant-service-groups list-ancestors"
description: "List tenant service group ancestors"
category: tenancy
scope: global
---

# set tenant-service-groups list-ancestors

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List tenant service group ancestors

## Usage

```
set tenant-service-groups list-ancestors [--remote]
```

## Examples

Run via SCM API:
```
arc > set tenant-service-groups list-ancestors
```

Run directly on device via SSH:
```
arc:fw-01 > set tenant-service-groups list-ancestors --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set tenant-service-groups list-ancestors
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
