---
command: "update sase service-connections"
description: "Update a service connection"
category: sase
scope: global
---

# update sase service-connections

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a service connection

## Usage

```
update sase service-connections [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase service-connections
```

Run directly on device via SSH:
```
arc:fw-01 > update sase service-connections --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase service-connections
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
