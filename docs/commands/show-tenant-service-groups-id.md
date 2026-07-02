---
command: "show tenant-service-groups id"
description: "Get a tenant service group"
category: tenancy
scope: global
---

# show tenant-service-groups id

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a tenant service group

## Usage

```
show tenant-service-groups id [--remote]
```

## Examples

Run via SCM API:
```
arc > show tenant-service-groups id
```

Run directly on device via SSH:
```
arc:fw-01 > show tenant-service-groups id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tenant-service-groups id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
