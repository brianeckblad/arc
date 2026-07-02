---
command: "delete sdwan-rules"
description: "Delete an SD-WAN rule"
category: network
scope: global
---

# delete sdwan-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an SD-WAN rule

## Usage

```
delete sdwan-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sdwan-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete sdwan-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sdwan-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
