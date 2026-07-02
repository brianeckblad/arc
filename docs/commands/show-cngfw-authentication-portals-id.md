---
command: "show cngfw authentication-portals id"
description: "Get an authentication portal"
category: cloudngfw
scope: global
---

# show cngfw authentication-portals id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an authentication portal

## Usage

```
show cngfw authentication-portals id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-portals id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-portals id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-portals id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
