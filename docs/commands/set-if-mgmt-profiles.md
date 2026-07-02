---
command: "set if-mgmt-profiles"
description: "Create a interface management profiles"
category: network
scope: global
---

# set if-mgmt-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a interface management profiles

## Usage

```
set if-mgmt-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set if-mgmt-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set if-mgmt-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set if-mgmt-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
