---
command: "update cngfw profile-groups"
description: "Update a profile group"
category: cloudngfw
scope: global
---

# update cngfw profile-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a profile group

## Usage

```
update cngfw profile-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > update cngfw profile-groups
```

Run directly on device via SSH:
```
arc:fw-01 > update cngfw profile-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update cngfw profile-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
