---
command: "show ngts serviceaccounts id"
description: "Gets a Service Account"
category: ngts
scope: global
---

# show ngts serviceaccounts id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Gets a Service Account

## Usage

```
show ngts serviceaccounts id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts serviceaccounts id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts serviceaccounts id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts serviceaccounts id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
