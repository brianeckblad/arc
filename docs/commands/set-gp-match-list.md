---
command: "set gp-match-list"
description: "Create a globalprotect match list entry"
category: network
scope: global
---

# set gp-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a globalprotect match list entry

## Usage

```
set gp-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > set gp-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > set gp-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set gp-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
