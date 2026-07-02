---
command: "show ngts activitytypes"
description: "Retrieve types of activities used for"
category: ngts
scope: global
---

# show ngts activitytypes

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve types of activities used for

## Usage

```
show ngts activitytypes [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts activitytypes
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts activitytypes --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts activitytypes
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
