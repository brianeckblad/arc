---
command: "update userid-match-list"
description: "Update a userid match list entry"
category: network
scope: global
---

# update userid-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a userid match list entry

## Usage

```
update userid-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > update userid-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > update userid-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update userid-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
