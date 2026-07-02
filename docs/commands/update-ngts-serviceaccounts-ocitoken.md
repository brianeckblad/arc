---
command: "update ngts serviceaccounts ocitoken"
description: "Regenerate the OCI registry token for"
category: ngts
scope: global
---

# update ngts serviceaccounts ocitoken

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Regenerate the OCI registry token for

## Usage

```
update ngts serviceaccounts ocitoken [--remote]
```

## Examples

Run via SCM API:
```
arc > update ngts serviceaccounts ocitoken
```

Run directly on device via SSH:
```
arc:fw-01 > update ngts serviceaccounts ocitoken --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > update ngts serviceaccounts ocitoken
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
