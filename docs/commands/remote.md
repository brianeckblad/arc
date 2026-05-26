# remote <device>

Open an interactive SSH session on a named device. Sets the device context and
immediately opens an SSH session.

This is a shortcut for `cd <device>` + `connect`. ARC authenticates using
stored credentials (OS keychain) and 2FA, then hands the terminal over to the
device. You are ON the device — every keystroke goes directly to it, and ARC is
a transparent byte pipe. Type `exit` on the device to close the session and
return to the ARC prompt.

**Category:** Shell built-in  
**API mode:** Not applicable (SSH only)  
**SSH mode:** Opens an interactive PTY session

## Usage

```
remote <device-name | hostname | ip | serial>
```

Tab after `remote ` to see available devices from the SCM cache.

## Examples

SSH directly to a device by name:

```
arc > remote fw-dallas-01

✓ Authenticated — handing terminal to fw-dallas-01
ARC is now a transparent pipe. Every keystroke goes directly to the device.
Type 'exit' on the device to close the session and return to ARC.

admin@fw-dallas-01> show system info
...
admin@fw-dallas-01> exit

SSH session ended. Back in ARC — device context fw-dallas-01 preserved.
arc:fw-dallas-01 >
```

SSH to a device by IP address (creates a stub device context):

```
arc > remote 192.168.1.10

Device '192.168.1.10' not found in cache — using as hostname/IP directly.

✓ Authenticated — handing terminal to 192.168.1.10
...
```

## Authentication

ARC tries authentication methods in this order:
1. SSH agent keys
2. Configured key file (`arc auth login --ssh-key`)
3. Default key files (`~/.ssh/id_ed25519`, `id_rsa`, `id_ecdsa`)
4. Keyboard-interactive (auto-fills stored password from keychain, surfaces 2FA prompts)
5. Plain password fallback

If you have no stored credentials, you'll be prompted during the keyboard-interactive exchange.

## See Also

- `help connect` — SSH to the current `cd` device
- `help config osx` / `help config win` / `help config nix` — credential storage
- `help cd` — change device context without connecting
