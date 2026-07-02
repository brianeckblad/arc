---
command: "delete hipmatch-match-list"
description: "Delete a hipmatch match list entry"
category: network
scope: global
---

# delete hipmatch-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a hipmatch match list entry

## Usage

```
delete hipmatch-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > delete hipmatch-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > delete hipmatch-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete hipmatch-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
