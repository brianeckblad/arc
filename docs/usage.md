# Using ARC

## Launch

```bash
arc
# or
python run.py
```

## Navigation

```text
folder Shared          Set the active SCM folder
ls                     List managed devices in the active folder
cd fw-dallas-01        Change Device in SCM/API context
pwd                    Show device, mode, and folder
```

## API-first command execution

Commands run through SCM/SCM APIs unless you explicitly choose SSH.

```text
show system info
show routing route
show security policy
```

## One-command SSH override

Append `--remote` while typing a registered command.

```text
show system info --remote
ping host 8.8.8.8 --remote
```

This runs only that command through SSH, then returns to API mode.

## SSH passthrough

```text
remote fw-dallas-01
show system info
show counter global filter severity drop
exit
```

Or use the current `cd` device:

```text
cd fw-dallas-01
connect
show system info
exit
```

