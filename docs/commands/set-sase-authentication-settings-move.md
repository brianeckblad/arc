---
command: "set sase authentication-settings move"
description: "Move a GlobalProtect authentication setting"
category: sase
scope: global
---

# set sase authentication-settings move

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Move a GlobalProtect authentication setting

## Usage

```
set sase authentication-settings move [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase authentication-settings move
```

Run directly on device via SSH:
```
arc:fw-01 > set sase authentication-settings move --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase authentication-settings move
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
