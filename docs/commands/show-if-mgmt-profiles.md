---
command: "show if-mgmt-profiles"
description: "List interface management profiles"
category: network
scope: global
---

# show if-mgmt-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List interface management profiles

## Usage

```
show if-mgmt-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show if-mgmt-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show if-mgmt-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show if-mgmt-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
