---
command: "show hipmatch-match-list id"
description: "Get a hipmatch match list entry"
category: network
scope: global
---

# show hipmatch-match-list id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a hipmatch match list entry

## Usage

```
show hipmatch-match-list id [--remote]
```

## Examples

Run via SCM API:
```
arc > show hipmatch-match-list id
```

Run directly on device via SSH:
```
arc:fw-01 > show hipmatch-match-list id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show hipmatch-match-list id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
