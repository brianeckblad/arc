---
command: "set posture reports config-file-upload"
description: "Initiate a Configuration Upload"
category: posture
scope: global
---

# set posture reports config-file-upload

**Category:** posture
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Initiate a Configuration Upload

## Usage

```
set posture reports config-file-upload [--remote]
```

## Examples

Run via SCM API:
```
arc > set posture reports config-file-upload
```

Run directly on device via SSH:
```
arc:fw-01 > set posture reports config-file-upload --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set posture reports config-file-upload
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
