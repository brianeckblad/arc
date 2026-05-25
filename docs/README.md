# ARC Help

ARC — Assisted Remote Console — is a PAN-OS-style shell for Palo Alto Networks SCM environments with SSH passthrough to managed PAN-OS devices.

## How help works inside ARC

- `?` prints the short command reference immediately.
- `help <topic>` reads Markdown from this `docs/` folder and renders it inside the ARC CLI.
- `help commands` lists documented command topics.
- `help show system info` opens the command detail page for `show system info`.
- `help remote` explains SSH passthrough mode.

## Core workflows

1. Set the SCM folder with `folder <name>`.
2. List managed devices with `ls` or `devices`.
3. Change API context with `cd <device>`.
4. Run supported commands through SCM/SCM APIs by default.
5. Use `--remote` for one remote SSH command, or `remote <device>` / `connect` for SSH passthrough mode.

See also: `help usage`, `help architecture`, and `help configuration`.

