---
command: "update npb-rules"
description: "Update Network Packet Broker Rule by ID"
category: network
scope: global
---

# update npb-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update Network Packet Broker Rule by ID

## Usage

```
update npb-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > update npb-rules
```

Run directly on device via SSH:
```
arc:fw-01 > update npb-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update npb-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
