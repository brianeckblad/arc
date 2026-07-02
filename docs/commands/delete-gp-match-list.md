---
command: "delete gp-match-list"
description: "Delete a globalprotect match list entry"
category: network
scope: global
---

# delete gp-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a globalprotect match list entry

## Usage

```
delete gp-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > delete gp-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > delete gp-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete gp-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
