---
command: "show incidents incidents details id"
description: "Incidents Details"
category: incidents
scope: global
---

# show incidents incidents details id

**Category:** incidents
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Incidents Details

## Usage

```
show incidents incidents details id [--remote]
```

## Examples

Run via SCM API:
```
arc > show incidents incidents details id
```

Run directly on device via SSH:
```
arc:fw-01 > show incidents incidents details id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show incidents incidents details id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
