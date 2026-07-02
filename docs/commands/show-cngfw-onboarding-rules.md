---
command: "show cngfw onboarding-rules"
description: "List onboarding rules"
category: cloudngfw
scope: global
---

# show cngfw onboarding-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List onboarding rules

## Usage

```
show cngfw onboarding-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw onboarding-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw onboarding-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw onboarding-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
