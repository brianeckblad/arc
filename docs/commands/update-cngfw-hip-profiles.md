---
command: "update cngfw hip-profiles"
description: "Update a HIP profile"
category: cloudngfw
scope: global
---

# update cngfw hip-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a HIP profile

## Usage

```
update cngfw hip-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw hip-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw hip-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw hip-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
