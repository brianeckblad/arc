---
command: "show device-context-segment-association"
description: "List device context segment associations"
category: device-device-settings
scope: global
---

# show device-context-segment-association

**Category:** device-device-settings
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List device context segment associations

## Usage

```
show device-context-segment-association [--remote]
```

## Examples

Run via SCM API:
```
arc > show device-context-segment-association
```

Run directly on device via SSH:
```
arc:fw-01 > show device-context-segment-association --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show device-context-segment-association
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
