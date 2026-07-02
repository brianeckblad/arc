---
command: "set npb-rules"
description: "Create a new Network Packet Broker Rule"
category: network
scope: global
---

# set npb-rules

**Category:** network
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a new Network Packet Broker Rule

## Usage

```
set npb-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > set npb-rules
```

Run directly on device via SSH:
```
arc:fw-01 > set npb-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set npb-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
