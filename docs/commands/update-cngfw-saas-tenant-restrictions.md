---
command: "update cngfw saas-tenant-restrictions"
description: "Update Saas Tenant Restrictions"
category: cloudngfw
scope: global
---

# update cngfw saas-tenant-restrictions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Saas Tenant Restrictions

## Usage

```
update cngfw saas-tenant-restrictions [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw saas-tenant-restrictions
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw saas-tenant-restrictions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw saas-tenant-restrictions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
