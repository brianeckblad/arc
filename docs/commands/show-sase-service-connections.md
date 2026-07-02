---
command: "show sase service-connections"
description: "List service connections"
category: sase
scope: global
---

# show sase service-connections

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List service connections

## Usage

```
show sase service-connections [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase service-connections
```

Run directly on device via SSH:
```
arc:fw-01 > show sase service-connections --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase service-connections
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
