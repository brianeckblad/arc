---
command: "show gp-match-list"
description: "List globalprotect match list entries"
category: network
scope: global
---

# show gp-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List globalprotect match list entries

## Usage

```
show gp-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show gp-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > show gp-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show gp-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
