---
command: "delete cngfw subscribed-tenants"
description: "Delete a subscribed tenant"
category: cloudngfw
scope: global
---

# delete cngfw subscribed-tenants

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a subscribed tenant

## Usage

```
delete cngfw subscribed-tenants [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw subscribed-tenants
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw subscribed-tenants --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw subscribed-tenants
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
