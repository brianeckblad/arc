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
2. Writes a sectioned template `config.json` with `_note` fields that explain each section.
3. Sets the file permissions to `0600` (owner read/write only).
4. Prints the path to the file and next steps.

`config.json` holds **non-secret** settings only, in readable sections. All auth
information — credentials, storage mode, and the real token expiry — lives in a
separate `auth.json`. In the default `keychain` storage mode, secrets stay in the
OS keychain and `auth.json` carries only non-secret identifiers; in `file` mode
(opt-in, insecure) `auth.json` also holds the plaintext secrets.

## The generated file

```json
{
  "_note": "ARC config.json — NON-secret, sectioned. Auth values live in auth.json (run: setup scm  — or  arc auth configure). Secrets go to the OS keychain unless auth.storage is set to 'file'.",
  "preferences": {
    "_note": "Per-user shell prefs (terminal, aliases, GUI theme). Managed via the terminal/alias commands."
  },
  "auth": {
    "_note": "preferred_method: service|bearer · storage: keychain (secure) | file (plaintext auth.json)",
    "preferred_method": "service",
    "storage": "keychain",
    "active_profile": "default"
  },
  "gui": {
    "features": {"enabled": true, "port": 4445},
    "arc":      {"enabled": true, "port": 4444}
  },
  "profiles": {
    "default": {"default_folder": "Shared"}
  }
}
```

`_note` fields are ignored by ARC at runtime — they exist only as documentation
inside the file. Credentials are **not** entered here: run `setup scm` (in the
ARC shell) or `arc auth configure`, which write them to `auth.json` (secrets to
the OS keychain by default).

## Workflow

```bash
# Step 1 — generate the sectioned config.json
arc config generate

# Step 2 — enter credentials (writes auth.json; secrets → keychain by default)
#           inside the ARC shell:   setup scm
#           or from the CLI:        arc auth configure

# Step 3 — confirm everything is set
arc auth show
```

## See Also

- `help config`         — general configuration overview
- `setup osx`     — macOS keychain CLI commands
- `setup win`     — Windows Credential Manager CLI commands
- `setup linux`     — Linux secret-tool CLI commands
- `help configuration`  — full configuration reference

