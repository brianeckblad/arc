---
command: "show cngfw authentication-portals"
description: "List authentication portals"
category: cloudngfw
scope: global
---

# show cngfw authentication-portals

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List authentication portals

## Usage

```
show cngfw authentication-portals [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-portals
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-portals --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-portals
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
