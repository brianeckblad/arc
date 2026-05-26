# arc config generate

Generate a starter `config.json` file with annotated placeholders and correct
file permissions (`0600`).

## Usage

```bash
arc config generate           # create config file (fails if file already exists)
arc config generate --force   # overwrite an existing config file
```

## What it does

1. Creates the ARC config directory if it does not exist.
2. Writes a template `config.json` with `_note` fields that explain each section.
3. Sets the file permissions to `0600` (owner read/write only).
4. Prints the path to the file and next steps.

## The generated file

```json
{
  "_note": "ARC config — fill in the REPLACE_WITH_* values, then run: arc auth login",
  "scm": {
    "_note": "Use bearer_token OR all three OAuth fields, not both",
    "bearer_token": "",
    "client_id":     "REPLACE_WITH_SCM_CLIENT_ID",
    "client_secret": "REPLACE_WITH_SCM_CLIENT_SECRET",
    "tsg_id":        "REPLACE_WITH_SCM_TSG_ID"
  },
  "ssh": {
    "_note": "SSH is used for --remote, remote <device>, and connect commands",
    "user":     "admin",
    "key_path": "",
    "password": "",
    "port":     22
  },
  "default_folder": "Shared"
}
```

`_note` fields are ignored by ARC at runtime — they exist only as documentation
inside the file.

## Workflow

```bash
# Step 1 — generate
arc config generate

# Step 2 — fill in non-sensitive values (client_id, tsg_id)
#           you can leave bearer_token / client_secret blank here;
#           arc auth login will prompt for them
$EDITOR ~/.config/arc/config.json     # Linux / macOS
notepad %APPDATA%\arc\config.json     # Windows

# Step 3 — migrate secrets to OS keychain
arc auth login

# Step 4 — confirm everything is set
arc auth show
```

## See Also

- `help config`         — general configuration overview
- `help config osx`     — macOS keychain CLI commands
- `help config win`     — Windows Credential Manager CLI commands
- `help config nix`     — Linux secret-tool CLI commands
- `help configuration`  — full configuration reference

