---
command: "show ngts autorenewal status"
description: "Get the current certificate auto-renewal monitorin"
category: ngts
scope: global
---

# show ngts autorenewal status

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get the current certificate auto-renewal monitorin

## Usage

```
show ngts autorenewal status [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts autorenewal status
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts autorenewal status --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts autorenewal status
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
