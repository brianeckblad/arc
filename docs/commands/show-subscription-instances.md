---
command: "show subscription instances"
description: "List instances"
category: subscription
scope: global
---

# show subscription instances

**Category:** subscription
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List instances

## Usage

```
show subscription instances [--remote]
```

## Examples

Run via SCM API:
```
arc > show subscription instances
```

Run directly on device via SSH:
```
arc:fw-01 > show subscription instances --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show subscription instances
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
