---
command: "delete ngts credentials id"
description: "Delete shared credential by ID"
category: ngts
scope: global
---

# delete ngts credentials id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete shared credential by ID

## Usage

```
delete ngts credentials id [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts credentials id
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts credentials id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts credentials id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
