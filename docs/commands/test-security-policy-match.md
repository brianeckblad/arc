# test security-policy-match

Test security policy match — test security-policy-match source <ip> destination <ip> application <app> protocol <n> destination-port <n>

## Category

tools

## Default path

API mode through SCM REST when a translation exists; otherwise use SSH for live device output.

## Remote behavior

Supported

## Examples

```text
test security-policy-match source 10.0.0.1 destination 8.8.8.8 application web-browsing protocol 6 destination-port 443
```

## Notes

Use `pwd` to confirm the current device and mode before running device-scoped commands.
