---
command: "show cngfw wildfire-profiles"
description: "List Wildfire and anti-virus profiles"
category: cloudngfw
scope: global
---

# show cngfw wildfire-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Wildfire and anti-virus profiles

## Usage

```
show cngfw wildfire-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw wildfire-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw wildfire-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw wildfire-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
