---
command: "set ngts machines workflows"
description: "Initiate the workflow"
category: ngts
scope: global
---

# set ngts machines workflows

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate the workflow

## Usage

```
set ngts machines workflows [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts machines workflows
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts machines workflows --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts machines workflows
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
