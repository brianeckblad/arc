---
command: "show pbf-rules"
description: "Show policy-based forwarding rules in the active folder"
feature_flag: pbf_rules
category: network
scope: folder
api: "GET /config/network/v1/pbf-rules"
---

# show pbf-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** `show pbf rule all`

## Description

Show policy-based forwarding rules in the active folder

## Usage

```
show pbf-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show pbf-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show pbf-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show pbf-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
