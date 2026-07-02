---
command: "show cngfw local-user-groups"
description: "List local user groups"
category: cloudngfw
scope: global
---

# show cngfw local-user-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List local user groups

## Usage

```
show cngfw local-user-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw local-user-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw local-user-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw local-user-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
