---
command: "show ngts edgeencryptionkeys"
description: "Retrieve Satellite Encryption Keys"
category: ngts
scope: global
---

# show ngts edgeencryptionkeys

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Satellite Encryption Keys

## Usage

```
show ngts edgeencryptionkeys [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts edgeencryptionkeys
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts edgeencryptionkeys --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts edgeencryptionkeys
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
