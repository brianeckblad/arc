---
command: "show cngfw vuln-profiles"
description: "List vulnerability protection profiles"
category: cloudngfw
scope: global
---

# show cngfw vuln-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List vulnerability protection profiles

## Usage

```
show cngfw vuln-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw vuln-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw vuln-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw vuln-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
