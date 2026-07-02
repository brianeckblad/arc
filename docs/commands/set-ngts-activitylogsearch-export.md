---
command: "set ngts activitylogsearch export"
description: "Export filtered event log data to"
category: ngts
scope: global
---

# set ngts activitylogsearch export

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Export filtered event log data to

## Usage

```
set ngts activitylogsearch export [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts activitylogsearch export
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts activitylogsearch export --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts activitylogsearch export
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
