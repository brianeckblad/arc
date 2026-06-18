#!/usr/bin/env python3
"""Generate docs/commands/api-reference.md from gen_stub_commands.py data."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from dev.gen_stub_commands import RESOURCES, has_method  # noqa: E402

lines = [
    "# ARC Command API Reference",
    "",
    "Complete mapping of SCM REST API resources to ARC commands.",
    "",
    "| Symbol | Meaning |",
    "|--------|---------|",
    "| `yes`  | Implemented, enabled by default |",
    "| `stub` | Help doc exists; enable feature flag to use |",
    "| `-`    | Not yet in ARC |",
    "",
    "Methods: L=List  R=GetById  C=Create  U=Update  D=Delete",
    "",
    "---",
    "",
]

domains: dict = {}
for row in RESOURCES:
    resource, domain, url, methods, flag, arc_show, arc_set, arc_delete, notes = row
    domains.setdefault(domain, []).append(row)

for domain in ["objects", "security", "network", "identity", "setup"]:
    if domain not in domains:
        continue
    lines.extend([
        f"## {domain.title()}",
        "",
        "| Resource | Methods | show | set | delete | Feature Flag |",
        "|---|---|---|---|---|---|",
    ])
    for row in domains[domain]:
        resource, dom, url, methods, flag, arc_show, arc_set, arc_delete, notes = row
        s = "yes" if arc_show else "-"
        c = "yes" if arc_set else ("stub" if has_method(methods, "C") else "-")
        d = "yes" if arc_delete else ("stub" if has_method(methods, "D") else "-")
        lines.append(f"| `{resource}` | {methods} | {s} | {c} | {d} | `{flag}` |")
    lines.append("")

lines.extend([
    "---",
    "",
    "## Usage",
    "",
    "Inside ARC:",
    "```",
    "help api-reference          # view this table",
    "feature show                # see all feature flags and their status",
    "feature enable <flag>       # enable a command family",
    "help set-<resource>         # view usage for a specific set command",
    "help delete-<resource>      # view usage for a specific delete command",
    "```",
    "",
    "## Refresh API docs",
    "",
    "```bash",
    "python dev/update_scm_docs.py    # pull latest specs from pan.dev",
    "python dev/gen_stub_commands.py  # regenerate missing stub docs",
    "```",
    "",
])

out = ROOT / "docs" / "commands" / "api-reference.md"
out.write_text("\n".join(lines))
print(f"Written {out} ({len(lines)} lines, {len(domains)} domains, {len(RESOURCES)} resources)")

