---
command: "update nat-rules"
description: "Update a NAT rule"
category: network
scope: global
---

# update nat-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a NAT rule

## Usage

```
update nat-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update nat-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update nat-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update nat-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
