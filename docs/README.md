# ARC Help

ARC — Assisted Remote Console — is a PAN-OS-style shell for Palo Alto Networks
SCM environments with interactive SSH access to managed PAN-OS devices.

## How help works inside ARC

- `?` prints the short command reference immediately.
- `help <topic>` reads Markdown from this `docs/` folder and renders it inside the ARC CLI.
- `help commands` lists documented command topics.
- `help show system info` opens the command detail page for `show system info`.
- `help remote` explains the interactive SSH session model.

## Configuration help

- `help config` — general configuration overview
- `help config osx` — macOS-specific setup (Keychain, Touch ID)
- `help config win` — Windows setup (Credential Manager)
- `help config nix` — Linux setup (Secret Service, headless/CI)

## Core workflows

1. Set the SCM folder with `folder <name>`.
2. List managed devices with `show devices`.
3. Change API context with `cd <device>`.
4. Run supported commands through SCM APIs by default.
5. Use `connect` or `remote <device>` to open an interactive SSH session on a device.

See also: `help usage`, `help architecture`, and `help configuration`.

