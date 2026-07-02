---
command: "delete cngfw application-groups"
description: "Delete an application group"
category: cloudngfw
scope: global
---

# delete cngfw application-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an application group

## Usage

```
delete cngfw application-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw application-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw application-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw application-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
