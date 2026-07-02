---
command: "update device-context-segment-association"
description: "Update a device context segment association"
category: device-device-settings
scope: global
---

# update device-context-segment-association

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a device context segment association

## Usage

```
update device-context-segment-association [--remote]
```

## Examples

Run via SCM API:
```
arc > update device-context-segment-association
```

Run directly on device via SSH:
```
arc:fw-01 > update device-context-segment-association --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update device-context-segment-association
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
