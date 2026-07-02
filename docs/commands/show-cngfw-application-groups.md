---
command: "show cngfw application-groups"
description: "List application groups"
category: cloudngfw
scope: global
---

# show cngfw application-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List application groups

## Usage

```
show cngfw application-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw application-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw application-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw application-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
