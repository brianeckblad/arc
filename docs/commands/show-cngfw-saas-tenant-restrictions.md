---
command: "show cngfw saas-tenant-restrictions"
description: "Get Saas Tenant Restrictions"
category: cloudngfw
scope: global
---

# show cngfw saas-tenant-restrictions

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Saas Tenant Restrictions

## Usage

```
show cngfw saas-tenant-restrictions [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw saas-tenant-restrictions
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw saas-tenant-restrictions --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw saas-tenant-restrictions
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
