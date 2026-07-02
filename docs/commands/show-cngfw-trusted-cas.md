---
command: "show cngfw trusted-cas"
description: "List trusted certificate authorities"
category: cloudngfw
scope: global
---

# show cngfw trusted-cas

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List trusted certificate authorities

## Usage

```
show cngfw trusted-cas [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw trusted-cas
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw trusted-cas --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw trusted-cas
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
