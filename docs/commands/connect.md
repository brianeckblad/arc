# connect

Open an interactive SSH session on the current device (set with `cd <device>`).

ARC authenticates using stored credentials (OS keychain) and 2FA, then hands
the terminal over to the device. You are ON the device — every keystroke goes
directly to it, and ARC is a transparent byte pipe. Type `exit` on the device
to close the session and return to the ARC prompt.

**Category:** Shell built-in  
**API mode:** Not applicable (SSH only)  
**SSH mode:** Opens an interactive PTY session

## Usage

```
connect
```

## Examples

Set the device context, then open an SSH session:

```
arc > cd fw-dallas-01
arc:fw-dallas-01 > connect

✓ Authenticated — handing terminal to fw-dallas-01
ARC is now a transparent pipe. Every keystroke goes directly to the device.
Type 'exit' on the device to close the session and return to ARC.

admin@fw-dallas-01> show system info
...
admin@fw-dallas-01> exit

SSH session ended. Back in ARC — device context fw-dallas-01 preserved.
arc:fw-dallas-01 >
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

- `help remote` — SSH to a named device (also sets device context)
- `help config osx` / `help config win` / `help config nix` — credential storage
- `help cd` — change device context
