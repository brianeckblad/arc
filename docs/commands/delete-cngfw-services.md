---
command: "delete cngfw services"
description: "Delete a service"
category: cloudngfw
scope: global
---

# delete cngfw services

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service

## Usage

```
delete cngfw services [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw services
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw services --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw services
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
