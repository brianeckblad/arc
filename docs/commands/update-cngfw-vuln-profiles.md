---
command: "update cngfw vuln-profiles"
description: "Update an vulnerability protection profile"
category: cloudngfw
scope: global
---

# update cngfw vuln-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an vulnerability protection profile

## Usage

```
update cngfw vuln-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw vuln-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw vuln-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw vuln-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
