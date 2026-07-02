---
command: "set cngfw services"
description: "Create a service"
category: cloudngfw
scope: global
---

# set cngfw services

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a service

## Usage

```
set cngfw services [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw services
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw services --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw services
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
