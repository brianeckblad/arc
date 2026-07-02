---
command: "show ngts credentials id"
description: "Retrieves shared credential by ID"
category: ngts
scope: global
---

# show ngts credentials id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieves shared credential by ID

## Usage

```
show ngts credentials id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts credentials id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts credentials id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts credentials id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
