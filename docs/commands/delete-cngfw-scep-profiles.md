---
command: "delete cngfw scep-profiles"
description: "Delete a SCEP profile"
category: cloudngfw
scope: global
---

# delete cngfw scep-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a SCEP profile

## Usage

```
delete cngfw scep-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw scep-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw scep-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw scep-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
