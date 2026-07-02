---
command: "update cngfw scep-profiles"
description: "Update a SCEP profile"
category: cloudngfw
scope: global
---

# update cngfw scep-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a SCEP profile

## Usage

```
update cngfw scep-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw scep-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw scep-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw scep-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
