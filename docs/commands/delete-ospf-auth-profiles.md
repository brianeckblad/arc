---
command: "delete ospf-auth-profiles"
description: "Delete an OSPF authentication profile"
category: network
scope: global
---

# delete ospf-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an OSPF authentication profile

## Usage

```
delete ospf-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ospf-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > delete ospf-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ospf-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
