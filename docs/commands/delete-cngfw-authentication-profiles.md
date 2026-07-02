---
command: "delete cngfw authentication-profiles"
description: "Delete an authentication profile"
category: cloudngfw
scope: global
---

# delete cngfw authentication-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an authentication profile

## Usage

```
delete cngfw authentication-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw authentication-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw authentication-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw authentication-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
