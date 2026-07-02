---
command: "show cngfw profile-groups id"
description: "Get a profile group"
category: cloudngfw
scope: global
---

# show cngfw profile-groups id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a profile group

## Usage

```
show cngfw profile-groups id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw profile-groups id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw profile-groups id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw profile-groups id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
