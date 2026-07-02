---
command: "update sdwan-rules"
description: "Update an SD-WAN rule"
category: network
scope: global
---

# update sdwan-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update an SD-WAN rule

## Usage

```
update sdwan-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update sdwan-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update sdwan-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sdwan-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
