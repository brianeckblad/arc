#!/usr/bin/env python3
"""Generate app/scripts/CODE_MAP.md — an accurate method→line-range map of large files.

WHY THIS EXISTS (string-theory model):
  Agents should read only the lines they need, not whole 900–2500 line files.
  Hand-maintained "TOC" comments drift the moment code is edited and become
  actively misleading. This tool AST-parses each large file and emits an
  always-accurate map of every class, method, and function with exact line
  ranges, so an agent can `read_file(path, offset=N, limit=M)` precisely.

Usage:
    python app/scripts/generate_code_map.py           # writes app/scripts/CODE_MAP.md
    python app/scripts/generate_code_map.py --check   # exit 1 if app/scripts/CODE_MAP.md is stale
    python app/scripts/generate_code_map.py --print    # print to stdout, don't write

Threshold: files with >= _MIN_LINES lines under app/ are mapped.
The smoke test (section 10) runs --check so the map can never silently rot.
"""

from __future__ import annotations

import argparse
import ast
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
APP  = ROOT / "app"
OUT_FILE = ROOT / "app" / "scripts" / "CODE_MAP.md"

# Only map files large enough that targeted reading actually saves tokens.
_MIN_LINES = 300


def _iter_large_files() -> list[Path]:
    """Return app/ Python files with >= _MIN_LINES lines, sorted largest first."""
    files: list[tuple[int, Path]] = []
    for path in APP.rglob("*.py"):
        if path.name == "__init__.py":
            continue
        line_count = sum(1 for _ in path.open(encoding="utf-8"))
        if line_count >= _MIN_LINES:
            files.append((line_count, path))
    files.sort(reverse=True)
    return [p for _, p in files]


def _node_span(node: ast.AST) -> tuple[int, int]:
    """Return (start_line, end_line) for an AST node."""
    start = getattr(node, "lineno", 0)
    end = getattr(node, "end_lineno", start)
    return start, end


def _first_doc_line(node: ast.AST) -> str:
    """Return the first line of a node's docstring, or '' when absent."""
    doc = ast.get_docstring(node)
    if not doc:
        return ""
    return doc.strip().splitlines()[0][:70]


def _map_one_file(path: Path) -> list[str]:
    """Return markdown lines mapping one file's classes/methods/functions/key dicts."""
    rel = path.relative_to(ROOT)
    src = path.read_text(encoding="utf-8")
    total = src.count("\n") + 1
    tree = ast.parse(src)

    rows: list[tuple[str, int, int, str]] = []  # (qualified_name, start, end, doc)

    # Track module-level dicts/assignments agents commonly need to locate
    # (COMMANDS, _WRITE_COMMANDS, _UPDATE_COMMANDS, _EXTRA_COMMANDS, etc.)
    _DICT_PATTERNS = ("COMMANDS", "_WRITE_COMMANDS", "_UPDATE_COMMANDS",
                      "_READ_COMMANDS", "_EXTRA_COMMANDS", "_FORMAT_SET_SPECS",
                      "_DEFAULT_VERB_GROUPS")

    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
            start, end = _node_span(node)
            rows.append((f"{node.name}()", start, end, _first_doc_line(node)))
        elif isinstance(node, ast.ClassDef):
            cstart, cend = _node_span(node)
            rows.append((f"class {node.name}", cstart, cend, _first_doc_line(node)))
            for child in node.body:
                if isinstance(child, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    mstart, mend = _node_span(child)
                    rows.append((f"  .{child.name}()", mstart, mend, _first_doc_line(child)))
        elif isinstance(node, (ast.Assign, ast.AnnAssign)):
            # Capture key module-level dict/constant assignments by name
            targets = []
            if isinstance(node, ast.Assign):
                targets = [t for t in node.targets if isinstance(t, ast.Name)]
            elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
                targets = [node.target]
            for t in targets:
                if t.id in _DICT_PATTERNS:
                    start, end = _node_span(node)
                    rows.append((f"{t.id}", start, end, "command registry dict"))
        elif isinstance(node, ast.Expr) and isinstance(node.value, ast.Call):
            # Capture COMMANDS.update(...) calls so agents know where dicts are merged
            call = node.value
            if (isinstance(call.func, ast.Attribute) and
                    call.func.attr == "update" and
                    isinstance(call.func.value, ast.Name) and
                    call.func.value.id == "COMMANDS"):
                start, end = _node_span(node)
                rows.append(("COMMANDS.update(…)", start, end, "merge additional commands into registry"))

    out: list[str] = []
    out.append(f"## `{rel}`  ({total} lines)")
    out.append("")
    out.append(f"{'Symbol':<40} {'Lines':<14} Purpose")
    out.append(f"{'─'*40} {'─'*14} {'─'*40}")
    for name, start, end, doc in rows:
        span = f"{start}-{end}"
        out.append(f"{name:<40} {span:<14} {doc}")
    out.append("")
    return out


def _build_map() -> str:
    """Build the full CODE_MAP.md content."""
    lines: list[str] = [
        "# ARC Code Map — Method Line Ranges for Large Files",
        "<!--",
        "  Generated by app/scripts/generate_code_map.py — do NOT edit by hand.",
        "  Refresh with: python app/scripts/generate_code_map.py",
        "  Drift-checked by smoke_test.py section 10 (--check).",
        "",
        "  TOKEN-SAVER: To edit one method, read ONLY its line range here, then",
        "  read_file(path, offset=START, limit=END-START+1). Avoid loading whole",
        f"  files. Files under app/ with >= {_MIN_LINES} lines are mapped.",
        "-->",
        "",
    ]
    for path in _iter_large_files():
        lines.extend(_map_one_file(path))
    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if app/scripts/CODE_MAP.md is stale (used by smoke test).")
    parser.add_argument("--print", dest="to_stdout", action="store_true",
                        help="Print to stdout instead of writing the file.")
    args = parser.parse_args()

    content = _build_map()

    if args.to_stdout:
        print(content)
        return 0

    if args.check:
        if not OUT_FILE.exists():
            print("app/scripts/CODE_MAP.md is missing — run: python app/scripts/generate_code_map.py", file=sys.stderr)
            return 1
        current = OUT_FILE.read_text(encoding="utf-8")
        if current != content:
            print("app/scripts/CODE_MAP.md is STALE — run: python app/scripts/generate_code_map.py", file=sys.stderr)
            return 1
        print("app/scripts/CODE_MAP.md is current.")
        return 0

    OUT_FILE.write_text(content, encoding="utf-8")
    mapped = len(_iter_large_files())
    print(f"Wrote {OUT_FILE.relative_to(ROOT)}  ({mapped} files mapped)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
