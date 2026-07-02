---
command: "set cngfw config-versions candidate push"
description: "Push the candidate configuration"
category: cloudngfw
scope: global
---

# set cngfw config-versions candidate push

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Push the candidate configuration

## Usage

```
set cngfw config-versions candidate push [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw config-versions candidate push
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw config-versions candidate push --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw config-versions candidate push
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
