---
command: "set cngfw hip-profiles"
description: "Create a HIP profile"
category: cloudngfw
scope: global
---

# set cngfw hip-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a HIP profile

## Usage

```
set cngfw hip-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw hip-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw hip-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw hip-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
