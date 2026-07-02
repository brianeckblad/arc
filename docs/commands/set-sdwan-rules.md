---
command: "set sdwan-rules"
description: "Create an SD-WAN rule"
category: network
scope: global
---

# set sdwan-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an SD-WAN rule

## Usage

```
set sdwan-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set sdwan-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set sdwan-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sdwan-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
