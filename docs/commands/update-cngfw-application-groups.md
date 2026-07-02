---
command: "update cngfw application-groups"
description: "Update an application group"
category: cloudngfw
scope: global
---

# update cngfw application-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an application group

## Usage

```
update cngfw application-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw application-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw application-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw application-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
