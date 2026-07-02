---
command: "set sase service-connections"
description: "Create a service connection"
category: sase
scope: global
---

# set sase service-connections

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a service connection

## Usage

```
set sase service-connections [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase service-connections
```

Run directly on device via SSH:
```
arc:fw-01 > set sase service-connections --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase service-connections
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
