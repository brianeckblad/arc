---
command: "show subscription licenses"
description: "List license details"
category: subscription
scope: global
---

# show subscription licenses

**Category:** subscription
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List license details

## Usage

```
show subscription licenses [--remote]
```

## Examples

Run via SCM API:
```
arc > show subscription licenses
```

Run directly on device via SSH:
```
arc:fw-01 > show subscription licenses --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show subscription licenses
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
