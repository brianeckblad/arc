---
command: "delete device-context-segment-association id"
description: "Delete a device context segment association"
category: device-device-settings
scope: global
---

# delete device-context-segment-association id

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a device context segment association

## Usage

```
delete device-context-segment-association id [--remote]
```

## Examples

Run via SCM API:
```
arc > delete device-context-segment-association id
```

Run directly on device via SSH:
```
arc:fw-01 > delete device-context-segment-association id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete device-context-segment-association id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
