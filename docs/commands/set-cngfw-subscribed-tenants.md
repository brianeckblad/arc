---
command: "set cngfw subscribed-tenants"
description: "Create Subscribed Tenant"
category: cloudngfw
scope: global
---

# set cngfw subscribed-tenants

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Subscribed Tenant

## Usage

```
set cngfw subscribed-tenants [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw subscribed-tenants
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw subscribed-tenants --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw subscribed-tenants
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
