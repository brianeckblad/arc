---
command: "show iptag-match-list id"
description: "Get an iptag match list entry"
category: network
scope: global
---

# show iptag-match-list id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an iptag match list entry

## Usage

```
show iptag-match-list id [--remote]
```

## Examples

Run via SCM API:
```
arc > show iptag-match-list id
```

Run directly on device via SSH:
```
arc:fw-01 > show iptag-match-list id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show iptag-match-list id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
