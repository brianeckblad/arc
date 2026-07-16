# cd <device>

Change Device in SCM/API context. This does not start SSH.

## Examples

```text
cd fw-dallas-01
```

```text
cd 10.0.0.10
```

## Navigation contexts

`cd` moves between three kinds of context:

```text
cd device <name>    # enter a device context (operational commands)
cd folder <name>    # set the active SCM folder (config scope)
cd snippet <name>   # enter a snippet container — set/show/clone target it
cd ..               # step back: snippet → device → folder → global
```

### Snippet editing

A **snippet** is a reusable config container that is mutually exclusive with a
folder. While a snippet context is active, object reads and writes target it via
`?snippet=` instead of the active folder, and the prompt shows the snippet
segment (e.g. `arc:snippet:dmz-baseline >`).

```text
cd snippet dmz-baseline
set address web-1 ip-netmask 10.1.2.3/32
clone address web-1 web-2
cd ..                 # leave the snippet, back to the folder
```

To attach a snippet to a folder, use `folder attach-snippet <snippet>` (in
configure mode, from within the target folder).

