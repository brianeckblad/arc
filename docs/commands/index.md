# Command Reference

Use `help <command>` to open detailed docs for a command.

- `commit` — Push candidate config to managed devices — commit [description <text>]
- `ping host` — Ping a host from the device — ping host <ip>  (use --remote)
- `request system software check` — Check available software updates — use --remote for live data
- `show address` — Show address objects in the active folder
- `show address-group` — Show address groups in the active folder
- `show device` — Show detail for a device — show device <hostname>  (or 'show device' when cd'd in)
- `show device snippets` — Show snippets attached to a device — show device <hostname> snippets
- `show devices` — List all SCM-managed devices
- `show external-dynamic-list` — Show external dynamic lists (EDLs) in the active folder
- `show high-availability all` — Show full HA configuration from the active folder
- `show high-availability state` — Show HA state summary from the active folder
- `show interface` — Show a specific interface — show interface <name>
- `show interface all` — Show all interfaces in the active folder
- `show jobs all` — Show all SCM jobs (TSG-wide)
- `show jobs id` — Show a specific job by ID — show jobs id <n>
- `show log system` — Show live system log — use --remote for live device data
- `show log traffic` — Show live traffic log — use --remote for live device data
- `show routing route` — Show static routes in the active folder
- `show routing summary` — Show virtual routers / routing profiles in the active folder
- `show security policy` — Show security policy rules in the active folder
- `show service` — Show service objects in the active folder
- `show snippet` — Show full detail for a snippet — show snippet <name>
- `show snippets` — List snippets for the current context  [dim](device → device snippets | folder → folder snippets | Shared → all)[/dim]
- `show snippets global` — List ALL snippets regardless of device or folder context
- `show system disk-space` — Show live disk usage — use --remote for live device data
- `show system info` — Show device info from SCM (model, serial, SW version, IP, status…)
- `show system resources` — Show live CPU / memory — use --remote for live device data
- `show tag` — Show tags in the active folder
- `show url-categories` — Show custom URL categories in the active folder
- `show zone` — Show security zones in the active folder
- `test security-policy-match` — Test security policy match — test security-policy-match source <ip> destination <ip> application <app> protocol <n> destination-port <n>
