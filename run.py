#!/usr/bin/env python3
"""Root-level entry point for ARC — Assisted Remote Console.

Run this script directly from the project root without installing the package:

    python run.py
    python run.py --help
    python run.py auth login
    python run.py auth show
    python run.py scm get /sse/config/v1/addresses --folder Shared

If the package is installed in the active virtual environment (pip install -e .)
the 'arc' command is also available directly from the shell:

    arc
    arc --help
    arc auth configure
    arc auth show
    arc scm get /sse/config/v1/addresses --folder Shared
"""

import sys
from pathlib import Path

# Ensure the repo root is on sys.path so the app/ package resolves correctly
# when this script is run directly (i.e. without `pip install -e .`).
_ROOT = Path(__file__).parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from app.cli import run  # noqa: E402

if __name__ == "__main__":
    run()

