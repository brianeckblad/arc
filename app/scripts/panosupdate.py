#!/usr/bin/env python3
"""Update ARC's local PAN-OS CLI command mirrors from docs.paloaltonetworks.com.

This is the PAN-OS sibling of ``app/scripts/docsupdate.py``.  It pulls the pages listed
in **settings/panos-sources.json** (command-hierarchy pages plus per-version
new/deleted command lists), extracts the CLI command lines embedded as plain
text in each page's HTML, and writes one committed mirror per page under
``docs/panos-cli/<key>.txt`` — the diffable input consumed by
``app/scripts/generate_panos_catalog.py``.

Extraction pipeline (conservative — never guess):

1. Strip tags with a stdlib ``HTMLParser`` collecting text nodes (block-level
   tags emit line breaks; ``<script>``/``<style>`` bodies are skipped).
2. ``html.unescape`` happens implicitly via ``convert_charrefs``; the joined
   text is NFKC-normalized.
3. Keep lines that start (column 0) with a known PAN-OS CLI verb.  Indented
   lines directly following a kept command line that look like command syntax
   are joined to that line as continuations.  Indented verb-starting lines
   *not* following a command are ambiguous — they go to the quarantine report,
   never into the mirror.  Everything else (headings, nav, boilerplate) drops.

Also writes ``docs/panos-cli/CHANGES.md`` — lines added/removed vs the previous
mirror per key, plus quarantine counts.

Resilience: an unreachable URL is a warning; the existing mirror is kept.
Idempotent: pulling unchanged pages rewrites byte-identical mirrors.

Usage::

    python app/scripts/panosupdate.py            # refresh mirrors + CHANGES.md
    python app/scripts/panosupdate.py --check    # report drift, write nothing
"""

from __future__ import annotations

import argparse
import datetime as _dt
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parent
REPO_ROOT = DEV_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

SOURCES_FILE = REPO_ROOT / "settings" / "panos-sources.json"  # user-editable URL registry
OUTPUT_DIR = REPO_ROOT / "docs" / "panos-cli"
CHANGES_FILE = OUTPUT_DIR / "CHANGES.md"

HTTP_TIMEOUT = 30  # seconds — every network call is bounded

# Verbs that begin a PAN-OS CLI command line (ops + configure mode).
CLI_VERBS = (
    "show|set|clear|request|test|ping|traceroute|debug|schedule|delete|tail|"
    "less|grep|scp|tftp|ftp|ssh|telnet|exit|target|validate|commit|check|"
    "diff|copy|move|rename|load|save|replace"
)
_VERB_RE = re.compile(rf"^(?:{CLI_VERBS})(?:\s|$)")
# A continuation fragment looks like command syntax: lowercase keyword,
# parameter (<...>), optional-group bracket, or choice text — never prose.
_CONTINUATION_RE = re.compile(r"^[a-z0-9<\[|]")

# How many added/removed lines to list verbatim per key in CHANGES.md.
_CHANGES_LIST_CAP = 40
_QUARANTINE_LIST_CAP = 20


# ── Source registry ──────────────────────────────────────────────────────────


def load_sources() -> dict:
    """Return the page registry from settings/panos-sources.json."""
    try:
        data = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"  ✗ could not read {SOURCES_FILE.name}: {exc}", file=sys.stderr)
        raise SystemExit(1)
    pages = data.get("pages") or []
    if not pages:
        print(f"  ✗ {SOURCES_FILE.name} has no pages", file=sys.stderr)
        raise SystemExit(1)
    return data


# ── Network ──────────────────────────────────────────────────────────────────


def _fetch_bytes(url: str) -> bytes:
    """Download a URL and return its raw bytes, with an explicit timeout."""
    request = urllib.request.Request(url, headers={"User-Agent": "arc-panosupdate"})
    with urllib.request.urlopen(request, timeout=HTTP_TIMEOUT) as response:
        return response.read()


# ── HTML → text ──────────────────────────────────────────────────────────────


class _TextExtractor(HTMLParser):
    """Collect text nodes; block-level tags become line breaks."""

    _BREAK_TAGS = {"br", "p", "div", "li", "tr", "h1", "h2", "h3", "h4", "pre", "table", "section"}

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)  # entities unescaped in handle_data
        self.parts: list[str] = []
        self._skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list) -> None:
        if tag in ("script", "style"):
            self._skip_depth += 1
        if tag in self._BREAK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag: str) -> None:
        if tag in ("script", "style"):
            self._skip_depth = max(0, self._skip_depth - 1)
        if tag in self._BREAK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data: str) -> None:
        if not self._skip_depth:
            self.parts.append(data)


def html_to_lines(raw_html: str) -> list[str]:
    """Strip tags, NFKC-normalize, and return the page text as raw lines."""
    parser = _TextExtractor()
    parser.feed(raw_html)
    text = unicodedata.normalize("NFKC", "".join(parser.parts))
    return text.split("\n")


# ── Command-line isolation ───────────────────────────────────────────────────


def extract_command_lines(raw_lines: list[str]) -> tuple[list[str], list[str]]:
    """Return ``(command_lines, quarantined)`` from raw page text lines.

    Kept: column-0 lines starting with a known CLI verb; indented
    command-syntax fragments directly following a kept line join it as
    continuations.  Ambiguous indented verb lines are quarantined.  Everything
    else (headings/nav/boilerplate) is dropped.
    """
    commands: list[str] = []
    quarantined: list[str] = []
    prev_raw_was_command = False

    for raw in raw_lines:
        stripped = raw.strip()
        if not stripped:
            prev_raw_was_command = False
            continue

        indented = raw != raw.lstrip()
        if not indented and _VERB_RE.match(stripped):
            commands.append(re.sub(r"\s+$", "", raw))
            prev_raw_was_command = True
            continue

        if indented and _CONTINUATION_RE.match(stripped):
            if prev_raw_was_command and commands:
                # Continuation of the previous command line.
                commands[-1] = f"{commands[-1]} {stripped}"
                # prev_raw_was_command stays True — chained continuations join too.
                continue
            if _VERB_RE.match(stripped):
                # Indented verb line with no command to attach to: ambiguous.
                quarantined.append(stripped)
        prev_raw_was_command = False

    return commands, quarantined


# ── Change report ────────────────────────────────────────────────────────────


def _diff_section(lines: list[str], title: str, out: list[str]) -> None:
    out.append(f"**{title} ({len(lines)}):**")
    out.append("")
    for line in lines[:_CHANGES_LIST_CAP]:
        out.append(f"- `{line}`")
    if len(lines) > _CHANGES_LIST_CAP:
        out.append(f"- … and {len(lines) - _CHANGES_LIST_CAP} more")
    out.append("")


def build_changes_markdown(
    results: list[dict],
    pulled_on: str,
) -> str:
    """Render CHANGES.md from per-page pull results."""
    lines = [
        "# PAN-OS CLI Mirror Change Report",
        "",
        f"> Generated by `app/scripts/panosupdate.py` on {pulled_on}.",
        "> Mirrors live in `docs/panos-cli/<key>.txt`; the catalog generator is",
        "> `app/scripts/generate_panos_catalog.py`.",
        "",
    ]

    had_changes = False
    for res in results:
        added, removed = res["added"], res["removed"]
        quarantined = res["quarantined"]
        if not (added or removed or quarantined):
            continue
        had_changes = True
        lines.append(f"## `{res['key']}` — {res['line_count']} command lines")
        lines.append("")
        if added:
            _diff_section(added, "Added", lines)
        if removed:
            _diff_section(removed, "Removed", lines)
        if quarantined:
            lines.append(f"**Quarantined ({len(quarantined)})** — ambiguous lines excluded from the mirror:")
            lines.append("")
            for item in quarantined[:_QUARANTINE_LIST_CAP]:
                lines.append(f"- `{item}`")
            if len(quarantined) > _QUARANTINE_LIST_CAP:
                lines.append(f"- … and {len(quarantined) - _QUARANTINE_LIST_CAP} more")
            lines.append("")

    if not had_changes:
        lines.append("No mirror changes since the last pull; no quarantined lines.")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n"


# ── Orchestration ────────────────────────────────────────────────────────────


def update(check_only: bool = False) -> int:
    """Pull every registered page and refresh mirrors.  Returns exit code."""
    sources = load_sources()
    pulled_on = _dt.date.today().isoformat()
    if not check_only:
        OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    results: list[dict] = []
    hard_failures: list[str] = []

    for page in sources["pages"]:
        key, url = page["key"], page["url"]
        mirror = OUTPUT_DIR / f"{key}.txt"
        print(f"  ↓ {key:<18} {url}")

        try:
            raw = _fetch_bytes(url)
        except (urllib.error.URLError, urllib.error.HTTPError, OSError, TimeoutError) as exc:
            if mirror.exists():
                print(f"    ⚠ unreachable ({exc}) — keeping existing mirror")
            else:
                print(f"    ✗ unreachable ({exc}) and no existing mirror")
                hard_failures.append(f"{key}: {exc}")
            continue

        commands, quarantined = extract_command_lines(
            html_to_lines(raw.decode("utf-8", errors="replace"))
        )
        if not commands:
            # A page with zero command lines means the layout changed — do not
            # clobber a good mirror with an empty one.
            print("    ✗ no command lines extracted — page layout changed? mirror untouched")
            hard_failures.append(f"{key}: extracted 0 command lines")
            continue

        old_lines = mirror.read_text(encoding="utf-8").splitlines() if mirror.exists() else []
        old_set, new_set = set(old_lines), set(commands)
        added = sorted(new_set - old_set)
        removed = sorted(old_set - new_set)

        results.append({
            "key": key,
            "line_count": len(commands),
            "added": added,
            "removed": removed,
            "quarantined": quarantined,
        })

        status = "current" if not (added or removed) else f"+{len(added)} / -{len(removed)}"
        quarantine_note = f", {len(quarantined)} quarantined" if quarantined else ""
        print(f"    ✓ {len(commands)} command lines ({status}{quarantine_note})")

        if not check_only:
            mirror.write_text("\n".join(commands) + "\n", encoding="utf-8")

    if check_only:
        print("\n  ── check summary ──")
        drift = [r for r in results if r["added"] or r["removed"]]
        if drift:
            for res in drift:
                print(f"  {res['key']}: +{len(res['added'])} / -{len(res['removed'])} lines")
            print("  Drift detected — run without --check to refresh mirrors.")
        else:
            print("  Mirrors current.")
        return 1 if hard_failures else 0

    CHANGES_FILE.write_text(build_changes_markdown(results, pulled_on), encoding="utf-8")
    print(f"\n  ✓ mirrors + CHANGES.md written under {OUTPUT_DIR} ({pulled_on})")

    if hard_failures:
        print("\n  Some pages failed:")
        for item in hard_failures:
            print(f"    - {item}")
        return 1
    return 0


# ── CLI ──────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Update ARC's PAN-OS CLI command mirrors from docs.paloaltonetworks.com."
    )
    parser.add_argument(
        "--check",
        action="store_true",
        help="Report drift against the committed mirrors without writing files.",
    )
    args = parser.parse_args(argv)

    print("Updating PAN-OS CLI mirrors from docs.paloaltonetworks.com…\n")
    return update(check_only=args.check)


if __name__ == "__main__":
    raise SystemExit(main())
