---
command: "delete if-mgmt-profiles"
description: "Delete an interface management profile"
category: network
scope: global
---

# delete if-mgmt-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an interface management profile

## Usage

```
delete if-mgmt-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete if-mgmt-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete if-mgmt-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete if-mgmt-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
