---
command: "update cngfw subscribed-tenants"
description: "Update a subscribed tenant"
category: cloudngfw
scope: global
---

# update cngfw subscribed-tenants

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a subscribed tenant

## Usage

```
update cngfw subscribed-tenants [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw subscribed-tenants
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw subscribed-tenants --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw subscribed-tenants
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
