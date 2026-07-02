---
command: "show ospf-auth-profiles id"
description: "Get an OSPF authentication profile"
category: network
scope: global
---

# show ospf-auth-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an OSPF authentication profile

## Usage

```
show ospf-auth-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ospf-auth-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show ospf-auth-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ospf-auth-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
