---
command: "show pbf-rules id"
description: "Get a PBF rule"
category: network
scope: global
---

# show pbf-rules id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a PBF rule

## Usage

```
show pbf-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show pbf-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show pbf-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show pbf-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
