---
command: "show iptag-match-list"
description: "List iptag match list entries"
category: network
scope: global
---

# show iptag-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List iptag match list entries

## Usage

```
show iptag-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show iptag-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > show iptag-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iptag-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
