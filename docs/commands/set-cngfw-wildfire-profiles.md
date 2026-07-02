---
command: "set cngfw wildfire-profiles"
description: "Create a WildFire and anti-virus profile"
category: cloudngfw
scope: global
---

# set cngfw wildfire-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a WildFire and anti-virus profile

## Usage

```
set cngfw wildfire-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw wildfire-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw wildfire-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw wildfire-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
