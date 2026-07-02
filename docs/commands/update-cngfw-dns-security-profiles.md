---
command: "update cngfw dns-security-profiles"
description: "Update a DNS security profile"
category: cloudngfw
scope: global
---

# update cngfw dns-security-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a DNS security profile

## Usage

```
update cngfw dns-security-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw dns-security-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw dns-security-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw dns-security-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
