# show user ip-user-mapping

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show user ip-user-mapping all`

## Description

Show live user-to-IP mapping from device — use --remote

## Usage

```
show user ip-user-mapping [--remote]
```

## Examples

Run via SCM API:
```
arc > show user ip-user-mapping
```

Run directly on device via SSH:
```
arc:fw-01 > show user ip-user-mapping --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show user ip-user-mapping
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
