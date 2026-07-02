---
command: "update pbf-rules"
description: "Update a PBF rule"
category: network
scope: global
---

# update pbf-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a PBF rule

## Usage

```
update pbf-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update pbf-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update pbf-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update pbf-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
