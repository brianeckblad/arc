---
command: "show cngfw scep-profiles"
description: "List SCEP profiles"
category: cloudngfw
scope: global
---

# show cngfw scep-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List SCEP profiles

## Usage

```
show cngfw scep-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw scep-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw scep-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw scep-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
