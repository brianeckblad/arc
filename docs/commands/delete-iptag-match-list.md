---
command: "delete iptag-match-list"
description: "Delete an iptag match list entry"
category: network
scope: global
---

# delete iptag-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete an iptag match list entry

## Usage

```
delete iptag-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > delete iptag-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > delete iptag-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete iptag-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
