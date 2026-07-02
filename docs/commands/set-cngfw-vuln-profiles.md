---
command: "set cngfw vuln-profiles"
description: "Create a vulnerability protection profile"
category: cloudngfw
scope: global
---

# set cngfw vuln-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a vulnerability protection profile

## Usage

```
set cngfw vuln-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw vuln-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw vuln-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw vuln-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
