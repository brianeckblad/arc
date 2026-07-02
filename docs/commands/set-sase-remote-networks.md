---
command: "set sase remote-networks"
description: "Create a remote network"
category: sase
scope: global
---

# set sase remote-networks

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a remote network

## Usage

```
set sase remote-networks [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase remote-networks
```

Run directly on device via SSH:
```
arc:fw-01 > set sase remote-networks --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase remote-networks
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
