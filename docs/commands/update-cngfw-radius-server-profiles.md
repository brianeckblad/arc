---
command: "update cngfw radius-server-profiles"
description: "Update a RADIUS server profile"
category: cloudngfw
scope: global
---

# update cngfw radius-server-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a RADIUS server profile

## Usage

```
update cngfw radius-server-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw radius-server-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw radius-server-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw radius-server-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
