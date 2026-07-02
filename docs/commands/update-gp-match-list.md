---
command: "update gp-match-list"
description: "Update a globalprotect match list entry"
category: network
scope: global
---

# update gp-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a globalprotect match list entry

## Usage

```
update gp-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > update gp-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > update gp-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update gp-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
