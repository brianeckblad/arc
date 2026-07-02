---
command: "update if-mgmt-profiles"
description: "Update an interface management profile"
category: network
scope: global
---

# update if-mgmt-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an interface management profile

## Usage

```
update if-mgmt-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > update if-mgmt-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > update if-mgmt-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update if-mgmt-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
