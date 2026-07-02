---
command: "set cngfw dynamic-user-groups"
description: "Create a Dynamic User Group"
category: cloudngfw
scope: global
---

# set cngfw dynamic-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a Dynamic User Group

## Usage

```
set cngfw dynamic-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw dynamic-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw dynamic-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw dynamic-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
