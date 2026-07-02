---
command: "delete content-id-settings"
description: "Delete Content-ID settings"
category: device-device-settings
scope: global
---

# delete content-id-settings

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete Content-ID settings

## Usage

```
delete content-id-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > delete content-id-settings
```

Run directly on device via SSH:
```
arc:fw-01 > delete content-id-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete content-id-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
