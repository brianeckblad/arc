# show authentication-profile

**Category:** identity
**API mode:** ✓ Live SCM data
**SSH mode:** `show authentication-profile`

## Description

Show authentication profiles in the active folder

## Usage

```
show authentication-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show authentication-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show authentication-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show authentication-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
