---
command: "show hipmatch-match-list"
description: "List hipmatch match list entries"
category: network
scope: global
---

# show hipmatch-match-list

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List hipmatch match list entries

## Usage

```
show hipmatch-match-list [--remote]
```

## Examples

Run via SCM API:
```
arc > show hipmatch-match-list
```

Run directly on device via SSH:
```
arc:fw-01 > show hipmatch-match-list --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show hipmatch-match-list
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
