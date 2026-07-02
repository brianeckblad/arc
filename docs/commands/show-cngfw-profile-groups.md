---
command: "show cngfw profile-groups"
description: "List profile groups"
category: cloudngfw
scope: global
---

# show cngfw profile-groups

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List profile groups

## Usage

```
show cngfw profile-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw profile-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw profile-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw profile-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
