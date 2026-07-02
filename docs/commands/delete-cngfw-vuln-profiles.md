---
command: "delete cngfw vuln-profiles"
description: "Delete a vulnerability protection profile"
category: cloudngfw
scope: global
---

# delete cngfw vuln-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a vulnerability protection profile

## Usage

```
delete cngfw vuln-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw vuln-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw vuln-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw vuln-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
