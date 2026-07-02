---
command: "set content-id-settings"
description: "Create Content-ID settings"
category: device-device-settings
scope: global
---

# set content-id-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Content-ID settings

## Usage

```
set content-id-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > set content-id-settings
```

Run directly on device via SSH:
```
arc:fw-01 > set content-id-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set content-id-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
