---
command: "set iptag-match-list"
description: "Create an iptag match list entry"
category: network
scope: global
---

# set iptag-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create an iptag match list entry

## Usage

```
set iptag-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > set iptag-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > set iptag-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set iptag-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
