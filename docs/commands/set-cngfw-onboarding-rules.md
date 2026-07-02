---
command: "set cngfw onboarding-rules"
description: "Create an onboarding rule"
category: cloudngfw
scope: global
---

# set cngfw onboarding-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an onboarding rule

## Usage

```
set cngfw onboarding-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw onboarding-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw onboarding-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw onboarding-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
