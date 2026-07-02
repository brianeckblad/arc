---
command: "delete cngfw onboarding-rules"
description: "Delete an onboarding rule"
category: cloudngfw
scope: global
---

# delete cngfw onboarding-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an onboarding rule

## Usage

```
delete cngfw onboarding-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw onboarding-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw onboarding-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw onboarding-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
