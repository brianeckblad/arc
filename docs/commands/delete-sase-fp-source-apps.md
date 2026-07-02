---
command: "delete sase fp-source-apps"
description: "Delete a GlobalProtect source application"
category: sase
scope: global
---

# delete sase fp-source-apps

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Delete a GlobalProtect source application

## Usage

```
delete sase fp-source-apps [--remote]
```

## Examples

Run via SCM API:
```
arc > delete sase fp-source-apps
```

Run directly on device via SSH:
```
arc:fw-01 > delete sase fp-source-apps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete sase fp-source-apps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
