---
command: "delete pbf-rules"
description: "Delete a PBF rule"
category: network
scope: global
---

# delete pbf-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a PBF rule

## Usage

```
delete pbf-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > delete pbf-rules
```

Run directly on device via SSH:
```
arc:fw-01 > delete pbf-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete pbf-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
