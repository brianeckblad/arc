---
command: "show npb-rules"
description: "List all Network Packet Broker Rules"
category: network
scope: global
---

# show npb-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List all Network Packet Broker Rules

## Usage

```
show npb-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show npb-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show npb-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show npb-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
