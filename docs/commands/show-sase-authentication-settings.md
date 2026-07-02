---
command: "show sase authentication-settings"
description: "List GlobalProtect authentication settings"
category: sase
scope: global
---

# show sase authentication-settings

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect authentication settings

## Usage

```
show sase authentication-settings [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase authentication-settings
```

Run directly on device via SSH:
```
arc:fw-01 > show sase authentication-settings --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase authentication-settings
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
