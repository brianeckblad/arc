---
command: "set userid-match-list"
description: "Create a userid match list entry"
category: network
scope: global
---

# set userid-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a userid match list entry

## Usage

```
set userid-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > set userid-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > set userid-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set userid-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
