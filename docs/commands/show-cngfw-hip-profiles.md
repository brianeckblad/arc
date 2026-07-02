---
command: "show cngfw hip-profiles"
description: "List HIP profiles"
category: cloudngfw
scope: global
---

# show cngfw hip-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List HIP profiles

## Usage

```
show cngfw hip-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw hip-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw hip-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw hip-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
