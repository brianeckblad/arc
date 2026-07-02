---
command: "delete device-context-segment-association"
description: "Delete device context segment associations by name"
category: device-device-settings
scope: global
---

# delete device-context-segment-association

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete device context segment associations by name

## Usage

```
delete device-context-segment-association [--remote]
```

## Examples

Run via SCM API:
```
arc > delete device-context-segment-association
```

Run directly on device via SSH:
```
arc:fw-01 > delete device-context-segment-association --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete device-context-segment-association
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
