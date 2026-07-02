---
command: "show cngfw http-header-profiles"
description: "List HTTP header profiles"
category: cloudngfw
scope: global
---

# show cngfw http-header-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List HTTP header profiles

## Usage

```
show cngfw http-header-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw http-header-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw http-header-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw http-header-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
