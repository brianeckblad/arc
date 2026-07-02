---
command: "delete sase service-connections"
description: "Delete a service connection"
category: sase
scope: global
---

# delete sase service-connections

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a service connection

## Usage

```
delete sase service-connections [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase service-connections
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase service-connections --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase service-connections
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
