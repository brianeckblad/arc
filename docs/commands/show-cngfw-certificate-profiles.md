---
command: "show cngfw certificate-profiles"
description: "List certificate profiles"
category: cloudngfw
scope: global
---

# show cngfw certificate-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List certificate profiles

## Usage

```
show cngfw certificate-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw certificate-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw certificate-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw certificate-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
