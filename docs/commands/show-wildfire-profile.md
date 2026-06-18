# show wildfire-profile

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show WildFire anti-virus profiles in the active folder

## Usage

```
show wildfire-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show wildfire-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show wildfire-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show wildfire-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
