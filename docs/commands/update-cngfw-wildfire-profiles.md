---
command: "update cngfw wildfire-profiles"
description: "Update a wildfire and antivirus profile"
category: cloudngfw
scope: global
---

# update cngfw wildfire-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a wildfire and antivirus profile

## Usage

```
update cngfw wildfire-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw wildfire-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw wildfire-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw wildfire-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
