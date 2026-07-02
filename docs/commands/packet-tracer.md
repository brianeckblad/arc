---
command: "packet-tracer"
description: "Trace a packet through the folder's security rule base"
usage: "packet-tracer from <zone> to <zone> source <ip> destination <ip> [application <app>] [destination-port <n>] [protocol <n>] [source-user <user>]"
feature_flag: packet_tracer
category: diagnostics
scope: folder
api: "(client-side simulation of the folder rule base)"
---

# packet-tracer

Trace a synthetic packet through the **active folder's** security rule base and
report which rule it matches and the resulting action — a Cisco-ASA
packet-tracer for Palo Alto / SCM policy.

It works **wherever you are in the tree**: the rules evaluated are those of the
folder you are currently in (`cd folder <name>`). No live device is required —
ARC reads the rule base from SCM and simulates the match locally.

`test security-policy-match` is an alias for the same behaviour (PAN-OS name).

## Feature flag

Gated by `packet_tracer` (ON in the MVP default `its settings/features/ file`).

## Syntax

```text
packet-tracer from <zone> to <zone> source <ip> destination <ip> \
              [application <app>] [destination-port <n>] [protocol <n>] [source-user <user>]
```

`source` and `destination` are required. Everything else is optional and
defaults to "any".

## Examples

```text
# Will DNS from the trust zone reach 8.8.8.8?
packet-tracer from trust to untrust source 10.0.0.5 destination 8.8.8.8 application dns destination-port 53 protocol 17

# Simplest form — just source and destination
packet-tracer source 10.0.0.5 destination 8.8.8.8

# PAN-OS alias
test security-policy-match source 10.0.0.5 destination 8.8.8.8 application web-browsing
```

## Output

```text
Packet Tracer  — folder: Shared
  Input: from=trust to=untrust src=10.0.0.5 dst=8.8.8.8 app=dns port=53/17
  Rules evaluated: 12
  ────────────────────────────────────────────────────────────
  Phase 1: SECURITY POLICY LOOKUP
    Matched rule : Allow-DNS  (#3 of 12)
    Action       : ALLOW
    From → To    : trust → untrust
    Application  : dns, any
    Service      : application-default
  ────────────────────────────────────────────────────────────
  RESULT: ALLOW — matched Allow-DNS
```

If no explicit rule matches, ARC reports the PAN-OS implicit default:
intrazone-allow when `from == to`, otherwise interzone-deny.

## Run it against a live device instead

Append `--remote` to run the real PAN-OS `test security-policy-match`
operational command over SSH on the selected device:

```text
cd device fw-01
packet-tracer source 10.0.0.5 destination 8.8.8.8 --remote
```

## Matching scope (current)

| Matched | How |
|---------|-----|
| from / to zone | value, `any`, or unset = any |
| source / destination | literal value, `any`, or unset = any (negation honoured) |
| application | value, `any`, or unset = any |
| disabled rules | skipped |

**Planned enhancement:** resolve address objects/groups to CIDRs (subnet
containment) and service objects to ports for strict 5-tuple matching. The
output labels its current literal-matching scope honestly.

## Related

- `show security policy` — list the rule base being evaluated
- `cd folder <name>` — switch which folder's rule base is tested

