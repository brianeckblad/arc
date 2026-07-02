---
command: "set ospf-auth-profiles"
description: "Create an OSPF authentication profile"
category: network
scope: global
---

# set ospf-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an OSPF authentication profile

## Usage

```
set ospf-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > set ospf-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > set ospf-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ospf-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
