---
command: "show cngfw security-rules"
description: "List security rules"
category: cloudngfw
scope: global
---

# show cngfw security-rules

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List security rules

## Usage

```
show cngfw security-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw security-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw security-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw security-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
