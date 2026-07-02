---
command: "update cngfw services"
description: "Update a service"
category: cloudngfw
scope: global
---

# update cngfw services

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a service

## Usage

```
update cngfw services [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw services
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw services --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw services
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
