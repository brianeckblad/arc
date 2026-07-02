---
command: "show npb-rules id"
description: "Get Network Packet Broker Rule by ID"
category: network
scope: global
---

# show npb-rules id

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get Network Packet Broker Rule by ID

## Usage

```
show npb-rules id [--remote]
```

## Examples

Run via SCM API:
```
arc > show npb-rules id
```

Run directly on device via SSH:
```
arc:fw-01 > show npb-rules id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show npb-rules id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
