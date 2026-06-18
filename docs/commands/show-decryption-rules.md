# show decryption-rules

**Category:** security
**API mode:** ✓ Live SCM data
**SSH mode:** `show running decryption-policy`

## Description

Show decryption rules in the active folder

## Usage

```
show decryption-rules [--remote]
```

## Examples

Run via SCM API:
```
arc > show decryption-rules
```

Run directly on device via SSH:
```
arc:fw-01 > show decryption-rules --remote

# Or enter SSH passthrough mode:
arc > remote fw-01
arc:fw-01[ssh] > show decryption-rules
```

## See Also

- `help remote` — SSH passthrough mode
- `help connect` — SSH to the current device
- `help commands` — Full command reference
