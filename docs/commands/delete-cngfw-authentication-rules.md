---
command: "delete cngfw authentication-rules"
description: "Delete an authentication rule"
category: cloudngfw
scope: global
---

# delete cngfw authentication-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an authentication rule

## Usage

```
delete cngfw authentication-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw authentication-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw authentication-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw authentication-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
