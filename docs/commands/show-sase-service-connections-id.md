---
command: "show sase service-connections id"
description: "Get a service connection"
category: sase
scope: global
---

# show sase service-connections id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a service connection

## Usage

```
show sase service-connections id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase service-connections id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase service-connections id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase service-connections id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
