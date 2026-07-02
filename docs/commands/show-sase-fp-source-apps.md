---
command: "show sase fp-source-apps"
description: "List GlobalProtect source applications"
category: sase
scope: global
---

# show sase fp-source-apps

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List GlobalProtect source applications

## Usage

```
show sase fp-source-apps [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase fp-source-apps
```

Run directly on device via SSH:
```
arc:fw-01 > show sase fp-source-apps --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase fp-source-apps
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
