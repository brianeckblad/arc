# terminal

Per-user terminal preferences. Stored in `config/<user>/config.json`
(personal — not the shared `settings/` folder) and loaded at every launch.

```text
terminal                     show current settings
terminal length <n>          page long help/docs output after n lines
terminal length 0            disable paging (default — rely on scrollback)
terminal width <n>           force render width in columns
terminal width 0             auto-detect width from the terminal (default)
terminal spinner on|off      show/hide the "querying SCM…" spinner
```

There is no terminal-size auto-detection for paging: output is printed in
full unless you set a length, exactly like `terminal length 0` on a vendor CLI.

Changes apply immediately and persist across sessions.
