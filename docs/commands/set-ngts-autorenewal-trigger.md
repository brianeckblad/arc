---
command: "set ngts autorenewal trigger"
description: "Attempt to initiate the certificate renewal"
category: ngts
scope: global
---

# set ngts autorenewal trigger

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Attempt to initiate the certificate renewal

## Usage

```
set ngts autorenewal trigger [--remote]
```

## Examples

Run via SCM API:
```
arc > set ngts autorenewal trigger
```

Run directly on device via SSH:
```
arc:fw-01 > set ngts autorenewal trigger --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set ngts autorenewal trigger
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
