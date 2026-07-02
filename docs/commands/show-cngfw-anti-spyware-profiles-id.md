---
command: "show cngfw anti-spyware-profiles id"
description: "Get an anti-spyware profile"
category: cloudngfw
scope: global
---

# show cngfw anti-spyware-profiles id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an anti-spyware profile

## Usage

```
show cngfw anti-spyware-profiles id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw anti-spyware-profiles id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw anti-spyware-profiles id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw anti-spyware-profiles id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
