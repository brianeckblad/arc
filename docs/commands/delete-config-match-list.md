---
command: "delete config-match-list"
description: "Delete a config match list entry"
category: network
scope: global
---

# delete config-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a config match list entry

## Usage

```
delete config-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > delete config-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > delete config-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete config-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
