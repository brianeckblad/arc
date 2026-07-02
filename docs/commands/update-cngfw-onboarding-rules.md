---
command: "update cngfw onboarding-rules"
description: "Update an onboarding rule"
category: cloudngfw
scope: global
---

# update cngfw onboarding-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an onboarding rule

## Usage

```
update cngfw onboarding-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw onboarding-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw onboarding-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw onboarding-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
