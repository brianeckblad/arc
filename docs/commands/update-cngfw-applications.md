---
command: "update cngfw applications"
description: "Update an application"
category: cloudngfw
scope: global
---

# update cngfw applications

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an application

## Usage

```
update cngfw applications [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw applications
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw applications --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw applications
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
