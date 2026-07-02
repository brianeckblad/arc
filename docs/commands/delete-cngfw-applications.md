---
command: "delete cngfw applications"
description: "Delete an application"
category: cloudngfw
scope: global
---

# delete cngfw applications

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an application

## Usage

```
delete cngfw applications [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw applications
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw applications --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw applications
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
