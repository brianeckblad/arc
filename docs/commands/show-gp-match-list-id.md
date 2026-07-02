---
command: "show gp-match-list id"
description: "Get a globalprotect match list entry"
category: network
scope: global
---

# show gp-match-list id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a globalprotect match list entry

## Usage

```
show gp-match-list id [--remote]
```

## Examples

Run via SCM API:
```
arc > show gp-match-list id
```

Run directly on device via SSH:
```
arc:fw-01 > show gp-match-list id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show gp-match-list id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
