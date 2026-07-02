---
command: "delete cngfw app-override-rules"
description: "Delete an application override rule"
category: cloudngfw
scope: global
---

# delete cngfw app-override-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an application override rule

## Usage

```
delete cngfw app-override-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw app-override-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw app-override-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw app-override-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
