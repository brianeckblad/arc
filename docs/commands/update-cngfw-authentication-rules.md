---
command: "update cngfw authentication-rules"
description: "Update an authentication rule"
category: cloudngfw
scope: global
---

# update cngfw authentication-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an authentication rule

## Usage

```
update cngfw authentication-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw authentication-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw authentication-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw authentication-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
