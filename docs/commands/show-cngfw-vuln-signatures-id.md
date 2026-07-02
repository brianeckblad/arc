---
command: "show cngfw vuln-signatures id"
description: "Get a vulnerability protection signature"
category: cloudngfw
scope: global
---

# show cngfw vuln-signatures id

**Category:** cloudngfw
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Get a vulnerability protection signature

## Usage

```
show cngfw vuln-signatures id [--remote]
```

## Examples

Run via SCM API:
```
arc > show cngfw vuln-signatures id
```

Run directly on device via SSH:
```
arc:fw-01 > show cngfw vuln-signatures id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show cngfw vuln-signatures id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
