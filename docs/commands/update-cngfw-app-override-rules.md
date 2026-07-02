---
command: "update cngfw app-override-rules"
description: "Update an application override rule"
category: cloudngfw
scope: global
---

# update cngfw app-override-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an application override rule

## Usage

```
update cngfw app-override-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw app-override-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw app-override-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw app-override-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
