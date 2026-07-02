---
command: "show cngfw authentication-profiles"
description: "List authentication profiles"
category: cloudngfw
scope: global
---

# show cngfw authentication-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List authentication profiles

## Usage

```
show cngfw authentication-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw authentication-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw authentication-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw authentication-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
