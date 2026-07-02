---
command: "delete system-match-list"
description: "Delete a system match list entry"
category: network
scope: global
---

# delete system-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a system match list entry

## Usage

```
delete system-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > delete system-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > delete system-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete system-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
