---
command: "delete ngts cert-templates"
description: "Remove an issuing template"
category: ngts
scope: global
---

# delete ngts cert-templates

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Remove an issuing template

## Usage

```
delete ngts cert-templates [--remote]
```

## Examples

Run via SCM API:
```
arc > delete ngts cert-templates
```

Run directly on device via SSH:
```
arc:fw-01 > delete ngts cert-templates --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > delete ngts cert-templates
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
