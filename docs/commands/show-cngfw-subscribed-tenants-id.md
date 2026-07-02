---
command: "show cngfw subscribed-tenants id"
description: "Get Subscribed Tenants"
category: cloudngfw
scope: global
---

# show cngfw subscribed-tenants id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Subscribed Tenants

## Usage

```
show cngfw subscribed-tenants id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw subscribed-tenants id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw subscribed-tenants id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw subscribed-tenants id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
