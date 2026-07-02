---
command: "show if-mgmt-profiles id"
description: "Get an interface management profile"
category: network
scope: global
---

# show if-mgmt-profiles id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an interface management profile

## Usage

```
show if-mgmt-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show if-mgmt-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show if-mgmt-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show if-mgmt-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
