# ARC Developer Keyword Dictionary

Use this file to ask for features/debugging in a way that minimizes AI context.
The goal is the "string theory" model: each feature request names the small
string/file that should be touched, not the whole CLI.

## Fast Start for AI Agents

Read these in order, stopping as soon as you have enough context:

1. `QUICK.md` — minimum agent map and recipes
2. `dev/API_INDEX.md` — compact SCM endpoint table (all specs in ~299 lines)
3. `dev/CODE_MAP.md` — exact line range of every method in large files
4. The one small file named by the keyword below
5. `AGENTS.md` only for full policy/security/architecture context

## Token-Saver Trigger Words

Say a trigger word and the agent jumps straight to the right small "string"
without scanning the whole codebase. One word can replace a paragraph of
explanation — that is the token saving.

| Trigger word | Means | Agent action (no full-repo read) |
|---|---|---|
| `map` | "use the code map" | Read `dev/CODE_MAP.md`, then read only the listed line range |
| `index` | "use the API index" | Read `dev/API_INDEX.md` for the endpoint, skip spec files |
| `string <file>` | "work only in this small file" | Edit only the named string file; do not open `shell.py` whole |
| `catalog` | builtin metadata | Open `app/shell_catalog.py` only |
| `flag <name>` | feature flag work | Open `app/features.py` + the one CommandDef |
| `scaffold <cmd> <module>` | generate boilerplate | Run `dev/scaffold.py`, then fill TODOs |
| `smoke <file>` | targeted validation | Run `python dev/smoke_test.py --file <file>` |
| `only <n>` | run smoke section n | Run `python dev/smoke_test.py --only <n>` |
| `endpoint <resource>` | API lookup | Find row in `dev/API_INDEX.md`, note methods + SSH column |
| `method <name>` | read one method | Look up name in `dev/CODE_MAP.md`, read just that range |
| `debug` | start the debug protocol | Use the debug template; read only files the error names |
| `ship <flag>` | enable a feature for all | Flip `app/features.py` default to `True`; run smoke |
| `docsupdate` | pull + self-heal docs | Run `dev/update_scm_docs.py`; read `docs/scm-api/CHANGES.md`; follow `dev/DOCS_AGENT.md` |
| `docs agent` | enter docs mode | Read `dev/DOCS_AGENT.md`; pull docs, report changes, update affected API calls only |

## Request Templates

Copy one of these and replace the angle-bracket values.

```text
add scm command: show <resource>
module: <objects|security|network|setup|operations>
feature_flag: <flag_name>
endpoint keyword: <resource from dev/API_INDEX.md>
```

```text
add device command: show <live-state>
ssh: <PAN-OS command>
scope: device
feature_flag: <flag_name>
```

```text
debug:
file: <file or command you were working on>
error: <paste traceback/output>
context: <device set? folder? configure mode? profile? SCM connected?>
```

```text
docs agent:
goal: <pull latest | check changes | update code for renamed endpoints>
notes: <anything you already know changed on pan.dev>
```

## Keyword Dictionary

| Say this | Agent reads first | Usually edits | Validation |
|---|---|---|---|
| `add scm command` | `dev/API_INDEX.md`, target `app/commands/<module>.py` | command module + `app/api/client.py` if method missing + docs page | `python dev/smoke_test.py --only 1,2,3` |
| `add feature-flagged command` | `app/features.py`, `dev/API_INDEX.md` | `app/features.py`, command module | `python dev/smoke_test.py --file app/features.py` then `--only 1,2,3` |
| `add device command` | `app/commands/operations.py`, `dev/API_INDEX.md` SSH column | `operations.py`, docs page | `python dev/smoke_test.py --only 1,2,3` |
| `add shell builtin` | `app/shell_catalog.py`, `dev/CODE_MAP.md` | `shell_catalog.py`, one `_cmd_*`, `_dispatch()` | `python dev/smoke_test.py --file app/shell_catalog.py` |
| `change help text` | `app/shell_catalog.py` for SHELL help, command module for registered commands | small catalog/module only | `python dev/smoke_test.py --only 8` |
| `change prompt/banner` | `dev/CODE_MAP.md` (`_print_banner`/`_prompt`), `app/banner.txt` | banner/theme files | `python dev/smoke_test.py --only 7,9` |
| `change renderer` | `app/utils/formatter.py`, `dev/CODE_MAP.md` (`_render`) | formatter + `_render` dispatch | `python dev/smoke_test.py --file app/utils/formatter.py` |
| `debug API 4xx` | `app/api/client.py`, `dev/API_INDEX.md` | client method or handler params | targeted smoke + reproduce command |
| `debug tab completion` | `dev/CODE_MAP.md` (`ArcCompleter.get_completions`) | completer only | `python dev/smoke_test.py --file app/shell.py` |
| `debug feature hidden` | `app/features.py`, command `feature_flag=` | feature flag default/local config | `python dev/smoke_test.py --file app/features.py` |
| `update docs` / `docs agent` | `dev/DOCS_AGENT.md`, then `docs/scm-api/CHANGES.md` | `dev/scm_sources.json` (auto), `app/api/client.py` for removed endpoints | `python dev/update_scm_docs.py --self-test` |

## Feature Flags

Feature flags let unfinished API work live in the registry without appearing to
normal users.

```python
# app/features.py
nat_rules: bool = False

# app/commands/network.py
'show nat-rules': CommandDef(..., feature_flag='nat_rules')
```

Enable locally without committing:

```json
{
  "nat_rules": true
}
```

Or for one shell session:

```bash
ARC_FEATURE_NAT_RULES=1 python run.py
```

## Shell String Theory Map

`app/shell.py` remains the shell spine, but small strings are now split out:

| String file | Owns | Edit when |
|---|---|---|
| `app/shell_catalog.py` | builtin command names + SHELL `?` help rows | adding/renaming builtin metadata |
| `app/features.py` | feature flags + local/env override loader | gating unfinished commands |
| `app/commands/<module>.py` | registered command handlers + `CommandDef`s | adding SCM/device commands |
| `app/api/client.py` | SCM HTTP methods | endpoint path/query changes |
| `app/utils/formatter.py` | output renderers | display changes |
| `app/theme.py` + `app/cli_theme.json` | color roles | theme changes |

To read one method inside any large file, look up its exact line range in
`dev/CODE_MAP.md` (auto-generated, never drifts) and read only that range.

Future extraction order if `shell.py` keeps growing:

1. `app/shell_help.py` — `_cmd_help*`, collapsed prefix/tier helpers
2. `app/shell_nav.py` — `cd`, `folder`, `ls`, `pwd`, cache refresh
3. `app/shell_sessions.py` — `connect`, `remote`, `tsg`, `account`
4. `app/shell_execution.py` — `_execute_api`, `_execute_remote`, `_render`
5. `app/shell_prompt.py` — banner, prompt, goodbye, lifecycle

Extract one string at a time and run:

```bash
python dev/smoke_test.py --file app/shell.py
python dev/smoke_test.py
```

## Endpoint Lookup Without Reading Specs

Use `dev/API_INDEX.md` first. It has:

- Resource path
- Methods: `L` list, `R` get-by-id, `C` create, `U` update, `D` delete
- Existing ARC command if implemented
- PAN-OS SSH equivalent for `--remote`

Only read `docs/scm-api/specs/<category>.md` when the compact index is not enough.

## Scaffold Examples

```bash
python dev/scaffold.py "show nat-rules" network --feature-flag nat_rules
python dev/scaffold.py "show ipsec-tunnels" network --feature-flag ipsec_vpn
python dev/scaffold.py "show decryption-rules" security --feature-flag decryption_policy --dry-run
```

## Minimal Validation Matrix

| Changed | Run |
|---|---|
| `app/commands/*.py` | `python dev/smoke_test.py --only 1,2,3` |
| `app/shell_catalog.py` | `python dev/smoke_test.py --file app/shell_catalog.py` |
| `app/shell.py` (or any 300+ line file) | `python dev/gen_code_map.py && python dev/smoke_test.py --file app/shell.py` |
| `app/features.py` | `python dev/smoke_test.py --file app/features.py` |
| `app/utils/formatter.py` | `python dev/smoke_test.py --file app/utils/formatter.py` |
| before commit | `python dev/smoke_test.py` (pre-commit auto-refreshes `dev/CODE_MAP.md`) |

