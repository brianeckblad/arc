---
command: "show cngfw dynamic-user-groups id"
description: "Get a Dynamic User Group"
category: cloudngfw
scope: global
---

# show cngfw dynamic-user-groups id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a Dynamic User Group

## Usage

```
show cngfw dynamic-user-groups id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw dynamic-user-groups id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw dynamic-user-groups id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw dynamic-user-groups id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
