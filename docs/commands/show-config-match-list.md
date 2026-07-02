---
command: "show config-match-list"
description: "List config match list entries"
category: network
scope: global
---

# show config-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List config match list entries

## Usage

```
show config-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show config-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > show config-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show config-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
