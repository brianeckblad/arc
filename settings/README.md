# ARC Settings — User-Editable Files

Everything in this folder customizes ARC **without touching code**.
Edit a file, save, restart ARC. That's it.

| File | What it controls | How to edit |
|------|------------------|-------------|
| `features.json` | Which commands are turned **on/off** | Set a flag to `true` or `false` |
| `banner.txt` | The startup logo / banner | Plain text + Rich colour tags like `[bold cyan]…[/bold cyan]` |
| `goodbye.txt` | Random exit messages (one per line) | Add/remove lines |
| `theme.json` | Colours used in `?` help and prompts | Rich style strings: `"cyan"`, `"bold yellow"`, `"dim"` |
| `cli-structure.yaml` | Verb descriptions, section headers, help footer, configure banner | YAML key/values |

---

## features.json — turn features on/off

This is the most important file. Each entry is a **feature flag**:

```json
{
  "show_address": true,      // command is visible and runnable
  "show_zone": false         // command is hidden until you flip it to true
}
```

- `true`  → the command(s) the flag gates appear in `?` help and run.
- `false` → those commands are hidden and blocked.
- A flag **missing** from this file defaults to **off** (safe).

Keys starting with `_` (like `_README`, `_section_*`) are comments — ignored.

**Inside ARC** you can also toggle for one session (not saved):

```
feature show                list every flag and its on/off state
feature enable show_zone    turn one on for this session
feature disable show_zone   turn one off for this session
```

To make a change permanent, edit `features.json` here and restart.

---

## Where secrets live (NOT here)

Credentials (API tokens, SSH passwords) are **never** stored in this folder.
They live in the OS keychain + `config/<your-username>/config.json`.
Run `arc auth configure` to set them.

