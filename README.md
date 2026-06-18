# ARC — Assisted Remote Console

ARC is a PAN-OS-style interactive CLI shell for Palo Alto Networks SCM environments with SSH passthrough for managed devices.

## Run

```bash
uv pip install -e .
arc
```

Or from the repo root without installing:

```bash
python run.py
```

## Documentation

User-facing documentation lives in [`docs/`](docs/):

- [`docs/README.md`](docs/README.md) — help overview
- [`docs/usage.md`](docs/usage.md) — common workflows
- [`docs/configuration.md`](docs/configuration.md) — credentials and environment variables
- [`docs/architecture.md`](docs/architecture.md) — runtime architecture
- [`docs/commands/`](docs/commands/) — command details used by `help <command>` inside ARC

Inside ARC, run:

```text
help usage
help commands
help show system info
help remote
```

## Development

Developing ARC (or working on it with an AI agent)? Start with
[`README.dev.md`](README.dev.md) — the developer guide with tokenmaxing recipes,
a keyword dictionary, file ownership, and the smoke-test map. `AGENTS.md` holds
the full spec (architecture, security, SCM API gateway map).

