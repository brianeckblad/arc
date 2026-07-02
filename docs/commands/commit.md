---
command: "commit"
description: "Apply staged changes and push to devices"
usage: "commit [watch] [description <text>]"
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
commit watch                       same, then follow the push job until it finishes
commit description planned-change  attach a description to the push
commit watch description nightly   watch + description combined
```

## Related

- `show config` — review what is staged before committing
- `abandon` — discard all staged changes (SCM is never touched)
- `show jobs id <n>` — check a push job later
- `commit --remote` — run PAN-OS `commit` directly on the current device over SSH
