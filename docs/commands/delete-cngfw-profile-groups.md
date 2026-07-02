---
command: "delete cngfw profile-groups"
description: "Delete a profile group"
category: cloudngfw
scope: global
---

# delete cngfw profile-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a profile group

## Usage

```
delete cngfw profile-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > delete cngfw profile-groups
```

Run directly on device via SSH:
```
arc:fw-01 > delete cngfw profile-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete cngfw profile-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
