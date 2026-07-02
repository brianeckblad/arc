---
command: "show ngts autorenewal tenant-config"
description: "Retrieve the monitoring configuration"
category: ngts
scope: global
---

# show ngts autorenewal tenant-config

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve the monitoring configuration

## Usage

```
show ngts autorenewal tenant-config [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts autorenewal tenant-config
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts autorenewal tenant-config --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts autorenewal tenant-config
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
