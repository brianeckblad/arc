---
command: "show ngts tags id"
description: "Retrieve tag by name"
category: ngts
scope: global
---

# show ngts tags id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve tag by name

## Usage

```
show ngts tags id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts tags id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts tags id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts tags id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
