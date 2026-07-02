---
command: "set cngfw applications"
description: "Create an application"
category: cloudngfw
scope: global
---

# set cngfw applications

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an application

## Usage

```
set cngfw applications [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw applications
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw applications --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw applications
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
