---
command: "show sase service-connection-groups"
description: "List service connection groups"
category: sase
scope: global
---

# show sase service-connection-groups

**Category:** sase
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List service connection groups

## Usage

```
show sase service-connection-groups [--remote]
```

## Examples

Run via SCM API:
```
arc > show sase service-connection-groups
```

Run directly on device via SSH:
```
arc:fw-01 > show sase service-connection-groups --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show sase service-connection-groups
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
