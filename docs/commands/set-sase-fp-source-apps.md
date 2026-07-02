---
command: "set sase fp-source-apps"
description: "Create a GlobalProtect source application"
category: sase
scope: global
---

# set sase fp-source-apps

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a GlobalProtect source application

## Usage

```
set sase fp-source-apps [--remote]
```

## Examples

Run via SCM API:
```
arc > set sase fp-source-apps
```

Run directly on device via SSH:
```
arc:fw-01 > set sase fp-source-apps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set sase fp-source-apps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
