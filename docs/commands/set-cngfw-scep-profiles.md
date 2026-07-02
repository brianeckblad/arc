---
command: "set cngfw scep-profiles"
description: "Create a SCEP profile"
category: cloudngfw
scope: global
---

# set cngfw scep-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a SCEP profile

## Usage

```
set cngfw scep-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw scep-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw scep-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw scep-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
