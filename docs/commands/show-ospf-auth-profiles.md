---
command: "show ospf-auth-profiles"
description: "List OSPF authentication profiles"
category: network
scope: global
---

# show ospf-auth-profiles

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List OSPF authentication profiles

## Usage

```
show ospf-auth-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show ospf-auth-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show ospf-auth-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ospf-auth-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
