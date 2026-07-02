---
command: "show cngfw dns-security-profiles"
description: "List DNS security profiles"
category: cloudngfw
scope: global
---

# show cngfw dns-security-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List DNS security profiles

## Usage

```
show cngfw dns-security-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw dns-security-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw dns-security-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw dns-security-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
