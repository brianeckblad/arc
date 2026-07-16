# ARC Help — the `docs/` folder

ARC — Assisted Remote Console — is a PAN-OS-style shell for Palo Alto Networks
SCM environments with interactive SSH access to managed PAN-OS devices.
This folder is the **user manual**: ARC reads this Markdown at runtime and
renders it in the CLI (`help <topic>`), and `arc cliup` bundles it into an
offline browser site (`docs/index.html`, opened by the `docs` builtin).

## How help works inside ARC

- `?` — short, context-aware command reference (only what you can run now).
- `help <topic>` — renders a Markdown file from this folder (e.g. `help usage`).
- `help <command>` — the command's page from `docs/commands/`, or a page
  synthesized from the registry when no file exists.
- `setup osx|linux|win` — OS-specific credential setup.

## What lives here

| Path | One line |
|---|---|
| `usage.md` / `setup.md` / `setup-*.md` / `configuration.md` / `config-generate.md` / `architecture.md` / `dev-versioning.md` | Hand-written user/operator topics (`setup-*.md` render via the `setup osx\|linux\|win` shell subcommands) |
| `commands/` | Hand-written command pages with YAML front-matter (+ generated `index.md`, `api-reference.md`) |
| `scm-api/` | Mirrored pan.dev OpenAPI specs + guides (pulled by `app/scripts/docsupdate.py`; includes `CHANGES.md`, `MANIFEST.md`) |
| `panos-cli/` | Diffable PAN-OS CLI command mirrors (pulled by `app/scripts/panosupdate.py`) |
| `COMMAND_PATTERNS.md` / `RENDER_CATALOG.md` / `COMMANDDEF_REFERENCE.md` | Agent spoke files — minimal patterns, `render=` keys, CommandDef fields |
| `agent-patterns/` | Python/JS standards + security checklist for contributors |
| `index.html` / `docs-bundle.js` / `vendor/` / `static/` | The offline browser docs site, rebuilt by `arc cliup` |

## How to change things here

- Reword a command's `?` description or usage: edit the front-matter of
  `docs/commands/<slug>.md` — the single source of truth when the file exists.
  Validate: `python app/scripts/smoke_test.py --only 10`.
- New/changed topic pages: just edit the Markdown; `help <topic>` picks it up
  on next launch. Rebuild the browser bundle with `arc cliup` if you use `docs`.
- Refresh the mirrored API/PAN-OS references: `python app/scripts/docsupdate.py`
  (never edit `scm-api/` or `panos-cli/` by hand — they are overwritten).
- Rebuild `commands/index.md` + `api-reference.md`:
  `python app/scripts/generate_command_docs.py`.

## Do not

- Do not create doc stubs for generated commands — commands without a file get
  help synthesized from the registry at runtime (`app/docs.py`).
- Do not hand-edit `scm-api/**`, `panos-cli/**`, `commands/index.md`,
  `commands/api-reference.md`, or `docs-bundle.js` — all generated.
- Do not put developer/agent instructions here — that's `AGENTS.md` (the hub);
  this folder is user-facing content only.
