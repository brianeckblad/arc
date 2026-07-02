---
command: "show cngfw anti-spyware-profiles"
description: "List anti-spyware profiles"
category: cloudngfw
scope: global
---

# show cngfw anti-spyware-profiles

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List anti-spyware profiles

## Usage

```
show cngfw anti-spyware-profiles [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw anti-spyware-profiles
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw anti-spyware-profiles --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw anti-spyware-profiles
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
