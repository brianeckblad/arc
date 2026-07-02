---
command: "show cngfw onboarding-rules id"
description: "Get an onboarding rule"
category: cloudngfw
scope: global
---

# show cngfw onboarding-rules id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an onboarding rule

## Usage

```
show cngfw onboarding-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw onboarding-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw onboarding-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw onboarding-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
