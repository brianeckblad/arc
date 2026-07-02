---
command: "set sase enable"
description: "Create application defaults"
category: sase
scope: global
---

# set sase enable

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create application defaults

## Usage

```
set sase enable [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase enable
```

Run directly on device via SSH:
```
arc:fw-01 > set sase enable --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase enable
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
