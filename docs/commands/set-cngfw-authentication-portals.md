---
command: "set cngfw authentication-portals"
description: "Create an authentication portal"
category: cloudngfw
scope: global
---

# set cngfw authentication-portals

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an authentication portal

## Usage

```
set cngfw authentication-portals [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw authentication-portals
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw authentication-portals --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw authentication-portals
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
