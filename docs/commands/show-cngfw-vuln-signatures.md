---
command: "show cngfw vuln-signatures"
description: "List vulnerability protection signatures"
category: cloudngfw
scope: global
---

# show cngfw vuln-signatures

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

List vulnerability protection signatures

## Usage

```
show cngfw vuln-signatures [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw vuln-signatures
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw vuln-signatures --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw vuln-signatures
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
