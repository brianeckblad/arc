---
command: "commit"
description: "Apply staged changes and push to devices — commit [watch] [description <text>]"
category: operations
scope: folder
api: "POST /config/setup/v1/config-versions/candidate:push"
---

---
command: "commit"
description: "Apply staged changes and push to devices — commit [watch] [description <text>]"
category: operations
scope: folder
api: "POST /config/setup/v1/config-versions/candidate:push"
---

---
command: "commit"
description: "Apply staged changes and push to devices"
usage: "commit [check|watch|confirmed <min>|confirm] [description <text>]"
category: operations
scope: folder
api: "POST /config/setup/v1/config-versions/candidate:push"
---

# commit

Apply every locally staged configure-mode change to SCM, then push the
candidate configuration to managed devices as one SCM job.

Configure-mode writes (`set` / `update` / `delete`) do **not** touch SCM when
you run them — they are validated and staged locally. `commit` is the moment
they become real:

1. Each staged change's API call is replayed against SCM, in order.
   A failure stops the replay; the failing change and everything after it
   stay staged so you can fix or `abandon` and commit again.
2. The candidate configuration is pushed to devices (scoped to the active
   folder when one is set).

## Variants

```text
commit                             apply + push, print the job ID
commit check                       re-validate staged changes against current
                                   SCM state without applying anything
commit watch                       apply + push, then follow the job until done
commit description planned-change  attach a description to the push
commit watch description nightly   watch + description combined
```

`commit check` is the Junos-style dry run: each staged change's validation
re-runs against SCM as it is *now*, catching objects someone else deleted or
renamed since you staged. Valid entries get their lookups refreshed; failures
are reported and stay staged for you to fix or `abandon`.

## Related

- `show config` — review what is staged before committing
- `abandon` — discard all staged changes (SCM is never touched)
- `show jobs id <n>` — check a push job later
- `commit --remote` — run PAN-OS `commit` directly on the current device over SSH
