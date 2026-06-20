---
command: "show sdwan-rules"
description: "Show SD-WAN rules in the active folder"
feature_flag: sdwan
category: network
scope: folder
api: "GET /config/network/v1/sdwan-rules"
---

# show sdwan-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show sdwan traffic`

## Description

Show SD-WAN rules in the active folder

## Usage

```
show sdwan-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show sdwan-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show sdwan-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sdwan-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
