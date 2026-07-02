---
command: "show cngfw dynamic-user-groups"
description: "List Dynamic User Groups"
category: cloudngfw
scope: global
---

# show cngfw dynamic-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Dynamic User Groups

## Usage

```
show cngfw dynamic-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw dynamic-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw dynamic-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw dynamic-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
