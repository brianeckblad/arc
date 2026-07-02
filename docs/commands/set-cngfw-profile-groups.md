---
command: "set cngfw profile-groups"
description: "Create a profile group"
category: cloudngfw
scope: global
---

# set cngfw profile-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a profile group

## Usage

```
set cngfw profile-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw profile-groups
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw profile-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw profile-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
