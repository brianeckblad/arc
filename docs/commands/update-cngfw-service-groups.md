---
command: "update cngfw service-groups"
description: "Update a service group"
category: cloudngfw
scope: global
---

# update cngfw service-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a service group

## Usage

```
update cngfw service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
