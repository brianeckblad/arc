---
command: "delete cngfw dns-security-profiles"
description: "Delete a DNS security profile"
category: cloudngfw
scope: global
---

# delete cngfw dns-security-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a DNS security profile

## Usage

```
delete cngfw dns-security-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw dns-security-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw dns-security-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw dns-security-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
