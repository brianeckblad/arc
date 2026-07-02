---
command: "show ngts edgeencryptionkeys id"
description: "Retrieve SatelliteEncryption Key By Id"
category: ngts
scope: global
---

# show ngts edgeencryptionkeys id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve SatelliteEncryption Key By Id

## Usage

```
show ngts edgeencryptionkeys id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts edgeencryptionkeys id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts edgeencryptionkeys id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts edgeencryptionkeys id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
