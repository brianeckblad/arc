---
command: "update cngfw authentication-profiles"
description: "Update an authentication profile"
category: cloudngfw
scope: global
---

# update cngfw authentication-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an authentication profile

## Usage

```
update cngfw authentication-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw authentication-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw authentication-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw authentication-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
