---
command: "delete nat-rules"
description: "Delete a NAT rule"
category: network
scope: global
---

# delete nat-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a NAT rule

## Usage

```
delete nat-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete nat-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete nat-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete nat-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
