---
command: "show ngts cert-templates"
description: "Get the details of issuing templates"
category: ngts
scope: global
---

# show ngts cert-templates

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the details of issuing templates

## Usage

```
show ngts cert-templates [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-templates
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-templates --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-templates
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
