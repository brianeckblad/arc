---
command: "show cngfw dos-protection-profiles id"
description: "Get a DoS protection profile"
category: cloudngfw
scope: global
---

# show cngfw dos-protection-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a DoS protection profile

## Usage

```
show cngfw dos-protection-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw dos-protection-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw dos-protection-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw dos-protection-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
