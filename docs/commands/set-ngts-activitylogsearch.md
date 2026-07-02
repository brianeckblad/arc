---
command: "set ngts activitylogsearch"
description: "Retrieve count and activity log entries"
category: ngts
scope: global
---

# set ngts activitylogsearch

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve count and activity log entries

## Usage

```
set ngts activitylogsearch [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts activitylogsearch
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts activitylogsearch --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts activitylogsearch
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
