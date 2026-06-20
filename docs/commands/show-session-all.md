---
command: "show session all"
description: "Show live session table from device — use --remote"
feature_flag: show_sessions
category: network
scope: device
api: "(live device state — SSH via --remote)"
---

# show session all

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show session all`

## Description

Show live session table from device — use --remote

## Usage

```
show session all [--remote]
```

## Examples

Run via SCM API:
```
arc > show session all
```

Run directly on device via SSH:
```
arc:fw-01 > show session all --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show session all
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
