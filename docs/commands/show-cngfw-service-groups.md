---
command: "show cngfw service-groups"
description: "List service groups"
category: cloudngfw
scope: global
---

# show cngfw service-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List service groups

## Usage

```
show cngfw service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
