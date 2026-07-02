---
command: "delete cngfw authentication-portals"
description: "Delete an authentication portal"
category: cloudngfw
scope: global
---

# delete cngfw authentication-portals

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an authentication portal

## Usage

```
delete cngfw authentication-portals [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw authentication-portals
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw authentication-portals --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw authentication-portals
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
