---
command: "set cngfw http-header-profiles"
description: "Create an HTTP header profile"
category: cloudngfw
scope: global
---

# set cngfw http-header-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an HTTP header profile

## Usage

```
set cngfw http-header-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw http-header-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw http-header-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw http-header-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
