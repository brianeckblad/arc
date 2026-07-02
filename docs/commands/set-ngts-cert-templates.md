---
command: "set ngts cert-templates"
description: "Add an issuing template"
category: ngts
scope: global
---

# set ngts cert-templates

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Add an issuing template

## Usage

```
set ngts cert-templates [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts cert-templates
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts cert-templates --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts cert-templates
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
