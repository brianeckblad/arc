---
command: "set cngfw trust-validations"
description: "Validates Trust"
category: cloudngfw
scope: global
---

# set cngfw trust-validations

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Validates Trust

## Usage

```
set cngfw trust-validations [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw trust-validations
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw trust-validations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw trust-validations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
