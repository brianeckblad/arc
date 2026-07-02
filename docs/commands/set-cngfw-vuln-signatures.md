---
command: "set cngfw vuln-signatures"
description: "Create a vulnerability protection signature"
category: cloudngfw
scope: global
---

# set cngfw vuln-signatures

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Create a vulnerability protection signature

## Usage

```
set cngfw vuln-signatures [--remote]
```

## Examples

Run via SCM API:
```
arc > set cngfw vuln-signatures
```

Run directly on device via SSH:
```
arc:fw-01 > set cngfw vuln-signatures --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > set cngfw vuln-signatures
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
