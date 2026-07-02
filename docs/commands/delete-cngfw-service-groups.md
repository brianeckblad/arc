---
command: "delete cngfw service-groups"
description: "Delete a service group"
category: cloudngfw
scope: global
---

# delete cngfw service-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service group

## Usage

```
delete cngfw service-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw service-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw service-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw service-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
