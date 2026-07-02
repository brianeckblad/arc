---
command: "show cngfw services id"
description: "Get a service"
category: cloudngfw
scope: global
---

# show cngfw services id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a service

## Usage

```
show cngfw services id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw services id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw services id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw services id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
