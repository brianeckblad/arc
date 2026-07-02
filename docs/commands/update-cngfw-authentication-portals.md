---
command: "update cngfw authentication-portals"
description: "Update an authentication portal"
category: cloudngfw
scope: global
---

# update cngfw authentication-portals

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an authentication portal

## Usage

```
update cngfw authentication-portals [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw authentication-portals
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw authentication-portals --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw authentication-portals
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
