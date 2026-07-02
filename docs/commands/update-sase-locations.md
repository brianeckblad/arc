---
command: "update sase locations"
description: "Select a GlobalProtect location"
category: sase
scope: global
---

# update sase locations

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Select a GlobalProtect location

## Usage

```
update sase locations [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase locations
```

Run directly on device via SSH:
```
arc:fw-01 > update sase locations --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase locations
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
