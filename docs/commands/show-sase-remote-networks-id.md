---
command: "show sase remote-networks id"
description: "Get a remote network"
category: sase
scope: global
---

# show sase remote-networks id

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a remote network

## Usage

```
show sase remote-networks id [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase remote-networks id
```

Run directly on device via SSH:
```
arc:fw-01 > show sase remote-networks id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase remote-networks id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
