#!/usr/bin/env python3
"""ARC command scaffolder — generates boilerplate for a new registered command.

Usage:
    python app/scripts/scaffold.py "show bgp routes" network
    python app/scripts/scaffold.py "show address" objects
    python app/scripts/scaffold.py "show zone" network --scope folder

Arguments:
    command    Quoted command string as it will appear in COMMANDS dict
               e.g. "show bgp routes"
    module     Domain module that owns this command
               setup | objects | security | network | operations

Options:
    --scope    folder | device | remote | global  (default: folder)
    --render   Render key for ArcShell._render()  (default: list)
    --ssh      SSH command string  (default: same as command)
    --dry-run  Print output without writing files

What gets created:
    1. Handler stub + CommandDef snippet  (printed to stdout — paste into module)
    2. docs/commands/<slug>.md            (stub doc file)

Then run:
    python app/scripts/smoke_test.py --only 1,2,3
"""

from __future__ import annotations

import argparse
import re
import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
APP  = ROOT / "app"
DOCS = ROOT / "docs" / "commands"

# Map module name → SCM base URL
_MODULE_BASE_URL = {
    "setup":      "https://api.strata.paloaltonetworks.com/config/setup/v1",
    "objects":    "https://api.strata.paloaltonetworks.com/config/objects/v1",
    "security":   "https://api.strata.paloaltonetworks.com/config/security/v1",
    "network":    "https://api.strata.paloaltonetworks.com/config/network/v1",
    "operations": "https://api.strata.paloaltonetworks.com/config/setup/v1",
}

_MODULE_SPEC_FILE = {
    "setup":      "ngfw-setup.md",
    "objects":    "ngfw-objects.md",
    "security":   "ngfw-security.md",
    "network":    "ngfw-network.md",
    "operations": "ngfw-operations.md",
}

_VALID_MODULES = list(_MODULE_BASE_URL.keys())
_VALID_SCOPES  = ("folder", "device", "remote", "global")
_VALID_RENDERS = ("list", "raw", "panel", "table", "tree")


def _slugify(command: str) -> str:
    """Convert 'show bgp routes' → 'show-bgp-routes'."""
    return re.sub(r"\s+", "-", command.strip().lower())


def _fn_name(command: str) -> str:
    """Convert 'show bgp routes' → '_show_bgp_routes'."""
    return "_" + re.sub(r"\s+", "_", command.strip().lower())


def _endpoint_guess(command: str, module: str) -> str:
    """Guess the REST endpoint path from the command name.

    E.g. 'show bgp routes' in 'network' → GET /bgp-routes
    This is a starting point — verify against docs/scm-api/specs/<module>.md.
    """
    # Strip leading 'show' verb
    tokens = command.strip().lower().split()
    if tokens and tokens[0] in ("show", "get", "list"):
        tokens = tokens[1:]
    path = "-".join(tokens)
    base = _MODULE_BASE_URL.get(module, "/config/<module>/v1")
    return f"GET  {base}/{path}"


def _handler_code(command: str, module: str, scope: str, render: str) -> str:
    """Generate the Python handler stub + CommandDef entry."""
    fn   = _fn_name(command)
    ep   = _endpoint_guess(command, module)
    slug = _slugify(command)
    spec_file = _MODULE_SPEC_FILE[module]

    folder_param = "folder=ctx.folder" if scope == "folder" else ""
    device_guard = "    require_device(ctx)\n" if scope in ("device", "remote") else ""
    if scope not in ("device", "remote"):
        scm_lines = (
            f"    scm = require_scm(ctx)\n"
            f"    # TODO: verify endpoint in app/scripts/API_INDEX.md first; deep-dive {spec_file} if needed.\n"
            f"    # {ep}\n"
            f"    return scm.get_{slug.replace('-', '_')}({folder_param})\n"
        )
    else:
        scm_lines = f"    # TODO: SSH execution — ssh_command below handles this\n    pass\n"

    code = f'''\
def {fn}(ctx: ExecutionContext, args: dict) -> Any:
    """{command.title()} — fetched from SCM API.

    # TODO: implement handler body.
    # Endpoint: {ep}
    # Verify path and params in app/scripts/API_INDEX.md before coding.
    # Full spec: docs/scm-api/specs/{spec_file}
    """
{device_guard}{scm_lines}
COMMANDS: dict[str, CommandDef] = {{
    # ... existing entries ...
    {command!r}: CommandDef(
        description="{command.title()}",   # TODO: write a short one-liner
        category={module!r},
        scope={scope!r},
        api_handler={fn},
        ssh_command={command!r},           # TODO: verify PAN-OS SSH syntax
        render={render!r},                 # key in ArcShell._render()
    ),
}}
'''
    return code


def _docs_stub(command: str, module: str, scope: str) -> str:
    """Generate a minimal docs/commands/<slug>.md stub."""
    ep   = _endpoint_guess(command, module)
    spec_file = _MODULE_SPEC_FILE[module]
    return textwrap.dedent(f"""\
        # {command}

        **Category:** {module}  |  **Scope:** {scope}

        > TODO: one paragraph describing what this command shows/does.

        ## Usage

        ```
        {command}
        {command} --remote
        ```

        ## Example Output

        ```
        TODO: paste example output here
        ```

        ## Notes

        - Endpoint: `{ep}`
        - Start with `app/scripts/API_INDEX.md`; deep-dive `docs/scm-api/specs/{spec_file}`
          only if the compact index is not enough.

        ## See Also

        - [`help {command.split()[0]}`]({command.split()[0]}-{command.split()[1] if len(command.split()) > 1 else "index"}.md)
    """)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Scaffold a new ARC registered command.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument("command", help='Command string, e.g. "show bgp routes"')
    parser.add_argument(
        "module",
        choices=_VALID_MODULES,
        help=f"Domain module: {' | '.join(_VALID_MODULES)}",
    )
    parser.add_argument("--scope",        default="folder", choices=_VALID_SCOPES)
    parser.add_argument("--render",       default="list",   choices=_VALID_RENDERS)
    parser.add_argument("--ssh",          default=None, help="SSH command string override")
    parser.add_argument("--feature-flag", default="", dest="feature_flag",
                        help="Feature flag name to gate this command (e.g. nat_rules); add it to settings/features.json")
    parser.add_argument("--dry-run",      action="store_true", help="Print without writing files")
    args = parser.parse_args()

    command      = args.command.strip().lower()
    module       = args.module
    scope        = args.scope
    render       = args.render
    feature_flag = args.feature_flag
    slug         = _slugify(command)
    dry_run      = args.dry_run

    # ------------------------------------------------------------------ #
    # 1. Handler + CommandDef snippet (always printed to stdout)
    # ------------------------------------------------------------------ #
    handler = _handler_code(command, module, scope, render)
    # Inject feature_flag into CommandDef if specified
    if feature_flag:
        handler = handler.replace(
            f"        render={render!r},",
            f"        render={render!r},\n        feature_flag={feature_flag!r},",
        )

    print("\n" + "=" * 60)
    print(f"PASTE INTO  app/commands/{module}.py")
    print("=" * 60)
    print(handler)

    # ------------------------------------------------------------------ #
    # 2. Docs stub
    # ------------------------------------------------------------------ #
    docs_content = _docs_stub(command, module, scope)
    docs_path = DOCS / f"{slug}.md"

    print("=" * 60)
    print(f"DOCS FILE   docs/commands/{slug}.md")
    print("=" * 60)
    print(docs_content)

    if not dry_run:
        if docs_path.exists():
            print(f"[skip] docs/commands/{slug}.md already exists — not overwritten.")
        else:
            docs_path.write_text(docs_content, encoding="utf-8")
            print(f"[created] docs/commands/{slug}.md")
    else:
        print("[dry-run] No files written.")

    # ------------------------------------------------------------------ #
    # 3. Remind which smoke sections to run
    # ------------------------------------------------------------------ #
    print("=" * 60)
    print("NEXT STEPS")
    print("=" * 60)
    print(f"  1. Paste the handler + CommandDef above into app/commands/{module}.py")
    print(f"  2. Fill in the TODO: items (handler body, endpoint, description)")
    if feature_flag:
        print(f"  3. Add to settings/features.json: \"{feature_flag}\": false")
        print(f"     (enable for a session: ARC_FEATURE_{feature_flag.upper()}=1 arc)")
        print(f"     When ready to ship: set \"{feature_flag}\": true in settings/features.json")
        next_step = 4
    else:
        next_step = 3
    if render not in ("list", "raw"):
        print(f"  {next_step}. Add render={render!r} case to app/utils/formatter.py + ArcShell._render()")
        print(f"  {next_step+1}. Add formatter call to smoke_test.py section 6")
        print(f"  {next_step+2}. python app/scripts/smoke_test.py --only 1,2,3,6")
    else:
        print(f"  {next_step}. python app/scripts/smoke_test.py --only 1,2,3")
    print(f"\n  Compact index:      app/scripts/API_INDEX.md")
    print(f"  Full API reference: docs/scm-api/specs/{_MODULE_SPEC_FILE[module]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
