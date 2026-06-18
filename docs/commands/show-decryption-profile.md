# show decryption-profile

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** Not applicable (config read from SCM)

## Description

Show decryption profiles in the active folder

## Usage

```
show decryption-profile [--remote]
```

## Examples

Run via SCM API:
```
arc > show decryption-profile
```

Run directly on device via SSH:
```
arc:fw-01 > show decryption-profile --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show decryption-profile
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
