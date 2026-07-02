---
command: "update sase fp-source-apps"
description: "Update a GlobalProtect source application"
category: sase
scope: global
---

# update sase fp-source-apps

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Update a GlobalProtect source application

## Usage

```
update sase fp-source-apps [--remote]
```

## Examples

Run via SCM API:
```
arc > update sase fp-source-apps
```

Run directly on device via SSH:
```
arc:fw-01 > update sase fp-source-apps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update sase fp-source-apps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
