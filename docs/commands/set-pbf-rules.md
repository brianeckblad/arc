---
command: "set pbf-rules"
description: "Create a PBF rule"
category: network
scope: global
---

# set pbf-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a PBF rule

## Usage

```
set pbf-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set pbf-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set pbf-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set pbf-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
