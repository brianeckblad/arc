---
command: "set subscription instances"
description: "Create an instance"
category: subscription
scope: global
---

# set subscription instances

**Category:** subscription
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an instance

## Usage

```
set subscription instances [--remote]
```

## Examples

Run via SCM API:
```
arc > set subscription instances
```

Run directly on device via SSH:
```
arc:fw-01 > set subscription instances --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set subscription instances
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
