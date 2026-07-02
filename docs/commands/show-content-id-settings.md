---
command: "show content-id-settings"
description: "List Content-ID settings"
category: device-device-settings
scope: global
---

# show content-id-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List Content-ID settings

## Usage

```
show content-id-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show content-id-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show content-id-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show content-id-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
