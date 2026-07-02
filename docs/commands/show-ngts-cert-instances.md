---
command: "show ngts cert-instances"
description: "Retrieve Certificate Instances"
category: ngts
scope: global
---

# show ngts cert-instances

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve Certificate Instances

## Usage

```
show ngts cert-instances [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-instances
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-instances --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-instances
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
