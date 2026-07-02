---
command: "show system-match-list"
description: "List system match list entries"
category: network
scope: global
---

# show system-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List system match list entries

## Usage

```
show system-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show system-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > show system-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show system-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
