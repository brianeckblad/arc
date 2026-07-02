---
command: "show ngts credential-configs id"
description: "Retrieves a Credential Manager Service configurati"
category: ngts
scope: global
---

# show ngts credential-configs id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieves a Credential Manager Service configurati

## Usage

```
show ngts credential-configs id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts credential-configs id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts credential-configs id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts credential-configs id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
