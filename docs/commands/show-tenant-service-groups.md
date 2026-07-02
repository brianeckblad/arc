---
command: "show tenant-service-groups"
description: "List all tenant service groups"
category: tenancy
scope: global
---

# show tenant-service-groups

**Category:** tenancy
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all tenant service groups

## Usage

```
show tenant-service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show tenant-service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show tenant-service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tenant-service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
