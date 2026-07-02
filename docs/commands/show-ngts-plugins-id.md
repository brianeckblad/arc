---
command: "show ngts plugins id"
description: "Retrieve plugin by ID"
category: ngts
scope: global
---

# show ngts plugins id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve plugin by ID

## Usage

```
show ngts plugins id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts plugins id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts plugins id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts plugins id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
