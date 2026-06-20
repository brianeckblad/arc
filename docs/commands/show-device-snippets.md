---
command: "show device snippets"
description: "Show snippets attached to a device"
usage: "show device <hostname> snippets"
feature_flag: show_devices
category: setup
scope: global
api: "GET /config/setup/v1/devices/{id}"
---

# show device snippets

**Category:** setup
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show snippets attached to a device — show device <hostname> snippets

## Usage

```
show device snippets [--remote]
```

## Examples

Run via SCM API:
```
arc > show device snippets
```

Run directly on device via SSH:
```
arc:fw-01 > show device snippets --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show device snippets
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
