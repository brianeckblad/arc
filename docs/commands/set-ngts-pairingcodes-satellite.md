---
command: "set ngts pairingcodes satellite"
description: "Create Pairing Code for Satellite Instance"
category: ngts
scope: global
---

# set ngts pairingcodes satellite

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create Pairing Code for Satellite Instance

## Usage

```
set ngts pairingcodes satellite [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts pairingcodes satellite
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts pairingcodes satellite --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts pairingcodes satellite
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
