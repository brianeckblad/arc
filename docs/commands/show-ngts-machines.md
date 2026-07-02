---
command: "show ngts machines"
description: "Get the details of all machines"
category: ngts
scope: global
---

# show ngts machines

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of all machines

## Usage

```
show ngts machines [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts machines
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts machines --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts machines
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
