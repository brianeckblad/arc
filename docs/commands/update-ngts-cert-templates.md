---
command: "update ngts cert-templates"
description: "Overwrite an issuing template details"
category: ngts
scope: global
---

# update ngts cert-templates

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Overwrite an issuing template details

## Usage

```
update ngts cert-templates [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts cert-templates
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts cert-templates --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts cert-templates
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
