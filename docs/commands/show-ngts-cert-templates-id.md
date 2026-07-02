---
command: "show ngts cert-templates id"
description: "Get an issuing template details"
category: ngts
scope: global
---

# show ngts cert-templates id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get an issuing template details

## Usage

```
show ngts cert-templates id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-templates id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-templates id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-templates id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
