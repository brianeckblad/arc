# show tls-service-profile

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show tls-service-profile`

## Description

Show TLS service profiles in the active folder

## Usage

```
show tls-service-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show tls-service-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show tls-service-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show tls-service-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
