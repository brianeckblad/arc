---
command: "show ngts cert-requests approvalrequests id"
description: "Retrieve approval request for specific certificate"
category: ngts
scope: global
---

# show ngts cert-requests approvalrequests id

**Category:** ngts
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Retrieve approval request for specific certificate

## Usage

```
show ngts cert-requests approvalrequests id [--remote]
```

## Examples

Run via SCM API:
```
arc > show ngts cert-requests approvalrequests id
```

Run directly on device via SSH:
```
arc:fw-01 > show ngts cert-requests approvalrequests id --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show ngts cert-requests approvalrequests id
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
