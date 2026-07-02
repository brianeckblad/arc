#!/usr/bin/env python3
"""Generate app/commands/panos_catalog.py from the PAN-OS CLI mirrors.

Reads the committed mirrors under ``docs/panos-cli/`` (pulled by
``dev/panosupdate.py``) plus the hand-maintained knobs in
``dev/panos_curation.json`` and emits ``PANOS_CATALOG`` — one entry per command
*stem* with synthesized usage variants, platform/family tags and version
add/remove metadata.  ``app/commands/panos_generated.py`` turns each entry into
a feature-gated CommandDef.

Normalization pipeline (deterministic — running twice is byte-identical):

* pass 1 — normalize: NFKC, NBSP/dash/quote translation, dedupe, rejoin spaced
  angle brackets, join indented continuations; unbalanced brackets or residual
  non-ASCII are quarantined (reported, excluded).
* token classes — PARAM ``^<[^<>]*>$`` (tested before any ``|`` split so
  ``<yes|no>`` stays one param); CHOICE contains ``|`` and no ``<``; LITERAL is
  the rest (lowercased in keys, original case preserved in usage/ssh).  Tokens
  mixing ``<`` and ``|`` (``<value>|<all>``) or carrying list ellipses
  (``<x2>...``) are value slots and classify as PARAM.
* pass 2 — corpus-inferred VALUE_LIKE literals (plus curation overrides);
  every inference is printed in the report.
* pass 3 — enum collapse on a token trie, bottom-up: literal children that are
  ALL leaves collapse to one CHOICE at >=2 siblings; groups of >=4 literal
  children with an identical suffix shape collapse their heads to a CHOICE and
  merge suffixes.  Never below token position 2 (verbs and their first
  argument always stay distinct).
* pass 4 — stem cut at the first PARAM/CHOICE/VALUE_LIKE token; an all-literal
  line is its own stem.
* pass 5 — prefix folding of stems that re-cut to a shorter stem after
  collapse; a stem that exists as its own runnable line keeps both entries.
* pass 6 — usage synthesis: <=6 variants per stem, canonical first (most line
  coverage, then fewest tokens, then lexicographic).
* pass 7 — tagging: platforms via curated panorama markers on the first two
  stem tokens; families per verb / verb_secondtoken rules ("config_" prefixed
  for the configure hierarchy, curated recovery stems -> "config_recovery").
* deltas — kind=added/deleted pages applied per ascending version; deletions
  are tombstones (``version_removed``), never removals.
* collisions — curated registry keys drop the generated entry (reported);
  OpenAPI-generated keys are kept (merge order shadows, reported).

Usage::

    python dev/generate_panos_catalog.py            # regenerate + report
    python dev/generate_panos_catalog.py --check    # drift check, write nothing
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

DEV_DIR = Path(__file__).resolve().parent
REPO_ROOT = DEV_DIR.parent
sys.path.insert(0, str(REPO_ROOT))

MIRROR_DIR = REPO_ROOT / "docs" / "panos-cli"
SOURCES_FILE = REPO_ROOT / "settings" / "panos-sources.json"  # user-editable URL registry
CURATION_FILE = DEV_DIR / "panos_curation.json"
CATALOG_FILE = REPO_ROOT / "app" / "commands" / "panos_catalog.py"

PARAM_RE = re.compile(r"^<[^<>]*>$")
_ANGLE_SPAN_RE = re.compile(r"<\s*([^<>]*?)\s*>")

# NBSP / typographic dash / quote translation applied before NFKC.
_TRANSLATE = str.maketrans({
    " ": " ",   # NBSP
    "‐": "-", "‑": "-", "‒": "-", "–": "-",
    "—": "-", "―": "-", "−": "-",
    "‘": "'", "’": "'", "‚": "'",
    "“": '"', "”": '"', "„": '"',
})

USAGE_CAP = 6              # max usage variants per stem (canonical first)
VERB_FAMILY_MAX = 100      # verb stays the family below this many stems
SECOND_TOKEN_MIN = 5       # verb_secondtoken family needs this many members
LEAF_CHOICE_MIN = 2        # all-leaf literal siblings collapse at >= this
SHAPE_GROUP_MIN = 4        # identical-suffix-shape literal groups collapse at >= this
MIN_COLLAPSE_POS = 2       # never merge tokens at positions 0/1


# ── pass 1: normalize ────────────────────────────────────────────────────────


def _rejoin_angles(line: str) -> str:
    """Rejoin spaced angle-bracket params: ``< 1 - 65535 >`` -> ``<1-65535>``."""
    return _ANGLE_SPAN_RE.sub(lambda m: "<" + re.sub(r"\s*-\s*", "-", m.group(1)) + ">", line)


def _balanced(line: str) -> bool:
    return (
        line.count("<") == line.count(">")
        and line.count("[") == line.count("]")
        and line.count("{") == line.count("}")
    )


def tokenize(line: str) -> list[str]:
    """Whitespace-split with ``<...>`` spans kept atomic (they may hold spaces)."""
    protected = re.sub(r"<[^<>]*>", lambda m: m.group(0).replace(" ", "\x00"), line)
    return [tok.replace("\x00", " ") for tok in protected.split()]


def normalize_lines(raw_lines: list[str]) -> tuple[list[list[str]], list[str]]:
    """Return ``(deduped token lines, quarantined lines)`` for one mirror."""
    joined: list[str] = []
    for raw in raw_lines:
        if not raw.strip():
            continue
        if raw != raw.lstrip() and joined:
            joined[-1] = f"{joined[-1]} {raw.strip()}"  # indented continuation
        else:
            joined.append(raw.rstrip())

    token_lines: list[list[str]] = []
    quarantined: list[str] = []
    seen: set[str] = set()
    for line in joined:
        line = unicodedata.normalize("NFKC", line.translate(_TRANSLATE))
        line = _rejoin_angles(line)
        if not _balanced(line) or any(ord(ch) > 127 for ch in line):
            quarantined.append(line)
            continue
        tokens = tokenize(line)
        if not tokens:
            continue
        key = " ".join(tokens)
        if key in seen:
            continue
        seen.add(key)
        token_lines.append(tokens)
    return token_lines, quarantined


# ── token classes ────────────────────────────────────────────────────────────


def token_class(token: str, value_like: frozenset[str]) -> str:
    """Return P (param), C (choice), V (value-like literal) or L (literal)."""
    if PARAM_RE.fullmatch(token):
        return "P"
    if "<" in token or ">" in token:
        # Mixed alternations (<value>|<all>) and list ellipses (<x2>...) are
        # value slots, not keywords — keep angle brackets out of stems/keys.
        return "P"
    if "|" in token:
        return "C"
    if token.lower() in value_like:
        return "V"
    return "L"


# ── pass 2: VALUE_LIKE inference ─────────────────────────────────────────────


def infer_value_like(corpus: list[list[str]], curation: dict) -> tuple[frozenset[str], list[str]]:
    """Infer literals that behave like values (stem cut points).

    A literal L is value-like iff it never appears at token position 0/1 AND
    every occurrence is preceded by the same literal keyword AND that keyword
    slot has >=4 distinct literal successors whose suffix shapes are identical
    — OR L is in ``value_token_overrides``.  Never when L is in
    ``keyword_token_overrides``.
    """
    overrides = {t.lower() for t in curation.get("value_token_overrides", [])}
    keyword_overrides = {t.lower() for t in curation.get("keyword_token_overrides", [])}
    no_value = frozenset()

    early_position: set[str] = set()          # literals seen at position 0 or 1
    predecessors: dict[str, set] = defaultdict(set)
    successor_shapes: dict[str, dict[str, set]] = defaultdict(lambda: defaultdict(set))

    for tokens in corpus:
        classes = [token_class(t, no_value) for t in tokens]
        for i, (tok, cls) in enumerate(zip(tokens, classes)):
            if cls != "L":
                continue
            lit = tok.lower()
            if i < 2:
                early_position.add(lit)
            if i == 0:
                predecessors[lit].add(("start", ""))
            elif classes[i - 1] == "L":
                predecessors[lit].add(("lit", tokens[i - 1].lower()))
            else:
                predecessors[lit].add(("cls", classes[i - 1]))
        for i in range(len(tokens) - 1):
            if classes[i] == "L" and classes[i + 1] == "L":
                shape = tuple(classes[i + 2:])
                successor_shapes[tokens[i].lower()][tokens[i + 1].lower()].add(shape)

    inferred: list[str] = []
    for lit in sorted(predecessors):
        if lit in keyword_overrides or lit in overrides:
            continue
        if lit in early_position:
            continue
        if len(predecessors[lit]) != 1:
            continue
        (kind, keyword) = next(iter(predecessors[lit]))
        if kind != "lit":
            continue
        successors = successor_shapes.get(keyword, {})
        if len(successors) < SHAPE_GROUP_MIN:
            continue
        shape_sets = {frozenset(shapes) for shapes in successors.values()}
        if len(shape_sets) != 1:
            continue
        inferred.append(lit)

    value_like = frozenset((set(inferred) | overrides) - keyword_overrides)
    return value_like, inferred


# ── pass 3: trie + enum collapse ─────────────────────────────────────────────


def _new_node() -> dict:
    return {"children": {}, "end": 0}


def build_trie(token_lines: list[list[str]]) -> dict:
    root = _new_node()
    for tokens in token_lines:
        node = root
        for tok in tokens:
            node = node["children"].setdefault(tok, _new_node())
        node["end"] += 1
    return root


def _signature(node: dict):
    """Structural signature of a subtree (weights excluded) — merge test."""
    cached = node.get("_sig")
    if cached is not None:
        return cached
    sig = (
        node["end"] > 0,
        tuple(sorted((tok, _signature(child)) for tok, child in node["children"].items())),
    )
    node["_sig"] = sig
    return sig


def _merge_identical(target: dict, other: dict) -> None:
    """Merge two structurally identical subtrees by summing weights."""
    target["end"] += other["end"]
    for tok, child in other["children"].items():
        _merge_identical(target["children"][tok], child)


def _sorted_alts(tokens: list[str]) -> list[str]:
    return sorted(tokens, key=lambda t: (t.lower(), t))


def collapse(node: dict, pos: int, value_like: frozenset[str]) -> None:
    """Bottom-up enum collapse (pass 3).  ``pos`` = token position of children."""
    for child in node["children"].values():
        collapse(child, pos + 1, value_like)
    if pos < MIN_COLLAPSE_POS:
        return

    changed = True
    while changed:
        changed = False
        children = node["children"]
        literals = {
            tok: child for tok, child in children.items()
            if token_class(tok, value_like) == "L"
        }
        if not literals:
            break

        # Rule 1: literal children that are ALL leaves collapse at >=2 siblings.
        if (
            len(literals) >= LEAF_CHOICE_MIN
            and all(not c["children"] and c["end"] > 0 for c in literals.values())
        ):
            alts = _sorted_alts(list(literals))
            choice = "|".join(alts)
            total = sum(c["end"] for c in literals.values())
            for tok in alts:
                del children[tok]
            target = children.setdefault(choice, _new_node())
            target["end"] += total
            target.pop("_sig", None)
            node.pop("_sig", None)
            changed = True
            continue

        # Rule 2: >=4 literal children with an identical suffix shape collapse
        # their heads to a CHOICE and merge the (structurally equal) suffixes.
        groups: dict = defaultdict(list)
        for tok in _sorted_alts(list(literals)):
            groups[_signature(literals[tok])].append(tok)
        for _sig, toks in sorted(groups.items(), key=lambda kv: kv[1]):
            if len(toks) < SHAPE_GROUP_MIN:
                continue
            alts = _sorted_alts(toks)
            choice = "|".join(alts)
            existing = children.get(choice)
            if existing is not None and _signature(existing) != _sig:
                continue  # cannot merge safely; keep the originals distinct
            merged = children[alts[0]]
            for tok in alts[1:]:
                _merge_identical(merged, children[tok])
            for tok in alts:
                del children[tok]
            if existing is not None:
                _merge_identical(existing, merged)
            else:
                children[choice] = merged
            node.pop("_sig", None)
            changed = True
            break  # group map is stale after a merge — recompute


def trie_paths(node: dict) -> list[tuple[list[str], int]]:
    """Enumerate root-to-end paths as ``(tokens, weight)``, deterministically."""
    out: list[tuple[list[str], int]] = []

    def walk(current: dict, acc: list[str]) -> None:
        if current["end"]:
            out.append((list(acc), current["end"]))
        for tok in sorted(current["children"], key=lambda t: (t.lower(), t)):
            acc.append(tok)
            walk(current["children"][tok], acc)
            acc.pop()

    walk(node, [])
    return out


# ── pass 4: stem cut ─────────────────────────────────────────────────────────


def cut_stem(tokens: list[str], value_like: frozenset[str]) -> list[str]:
    """Leading literals until the first PARAM/CHOICE/VALUE_LIKE (or bracket)."""
    stem: list[str] = []
    for tok in tokens:
        if token_class(tok, value_like) != "L" or tok in ("[", "]"):
            break
        stem.append(tok)
    return stem


def group_stems(collapsed: list[tuple[list[str], int]], value_like: frozenset[str]) -> dict:
    """Group collapsed lines by stem key -> {tokens, variants, weight}."""
    stems: dict[str, dict] = {}
    for tokens, weight in collapsed:
        stem = cut_stem(tokens, value_like)
        if not stem:
            continue
        key = " ".join(t.lower() for t in stem)
        entry = stems.setdefault(key, {"tokens": stem, "variants": {}, "weight": 0})
        suffix = tuple(tokens[len(stem):])
        entry["variants"][suffix] = entry["variants"].get(suffix, 0) + weight
        entry["weight"] += weight
    return stems


# ── pass 5: prefix folding ───────────────────────────────────────────────────


def fold_prefixes(stems: dict, value_like: frozenset[str]) -> list[str]:
    """Fold stems that re-cut to a shorter stem after collapse.  Returns log."""
    log: list[str] = []
    # Group extension stems under their longest existing proper prefix stem.
    by_prefix: dict[str, list[str]] = defaultdict(list)
    for key in sorted(stems):
        key_tokens = key.split()
        for cut in range(len(key_tokens) - 1, 0, -1):
            prefix = " ".join(key_tokens[:cut])
            if prefix in stems:
                by_prefix[prefix].append(key)
                break

    for prefix in sorted(by_prefix):
        if prefix not in stems:
            continue  # already folded away
        extensions = [k for k in by_prefix[prefix] if k in stems]
        if not extensions:
            continue
        base = stems[prefix]
        cut = len(base["tokens"])

        local = _new_node()

        def insert(tokens: list[str], weight: int) -> None:
            node = local
            for tok in tokens:
                node = node["children"].setdefault(tok, _new_node())
            node["end"] += weight

        for suffix, weight in sorted(base["variants"].items()):
            insert(list(suffix), weight)
        for ext_key in extensions:
            ext = stems[ext_key]
            extra = ext["tokens"][cut:]
            for suffix, weight in sorted(ext["variants"].items()):
                insert(list(extra) + list(suffix), weight)

        collapse(local, cut, value_like)
        new_paths = trie_paths(local)
        foldable = all(
            not tokens or token_class(tokens[0], value_like) != "L"
            for tokens, _weight in new_paths
        )
        if foldable:
            base["variants"] = {tuple(tokens): weight for tokens, weight in new_paths}
            for ext_key in extensions:
                base["weight"] += stems[ext_key]["weight"]
                del stems[ext_key]
                log.append(f"{ext_key} -> {prefix}")
        # Not foldable: the prefix exists as its own runnable stem (or holds
        # its own param lines) — keep both entries.
    return log


# ── corpus -> stems (passes 1+3+4+5 for one mirror) ──────────────────────────


def stems_for_page(token_lines: list[list[str]], value_like: frozenset[str]) -> tuple[dict, list[str]]:
    trie = build_trie(token_lines)
    collapse(trie, 0, value_like)
    stems = group_stems(trie_paths(trie), value_like)
    fold_log = fold_prefixes(stems, value_like)
    return stems, fold_log


# ── pass 6: usage synthesis ──────────────────────────────────────────────────


def synthesize_usage(entry: dict) -> list[str]:
    """<=6 usage variants; canonical first (coverage, then brevity, then lex)."""
    stem_text = " ".join(entry["tokens"])
    ranked = sorted(
        entry["variants"].items(),
        key=lambda kv: (-kv[1], len(kv[0]), " ".join(kv[0])),
    )
    usage = []
    for suffix, _weight in ranked[:USAGE_CAP]:
        usage.append(f"{stem_text} {' '.join(suffix)}".strip())
    return usage


# ── pass 7: tagging ──────────────────────────────────────────────────────────


def _family_token(text: str) -> str:
    return text.replace("-", "_")


def assign_families(entries: dict) -> None:
    """Family per mode: verb if small, else verb_secondtoken (config_ prefixed)."""
    verb_counts: dict[tuple[str, str], int] = defaultdict(int)
    pair_counts: dict[tuple[str, str, str], int] = defaultdict(int)
    for key, entry in entries.items():
        tokens = key.split()
        verb_counts[(entry["mode"], tokens[0])] += 1
        if len(tokens) > 1:
            pair_counts[(entry["mode"], tokens[0], tokens[1])] += 1

    for key, entry in entries.items():
        tokens = key.split()
        verb, second = tokens[0], tokens[1] if len(tokens) > 1 else ""
        mode = entry["mode"]
        if verb_counts[(mode, verb)] < VERB_FAMILY_MAX:
            group = _family_token(verb)
        elif second and pair_counts[(mode, verb, second)] >= SECOND_TOKEN_MIN:
            # The configure tree drops the verb ("config_deviceconfig"); the
            # ops tree keeps it ("show_routing").
            group = _family_token(second) if mode == "config" else f"{_family_token(verb)}_{_family_token(second)}"
        else:
            group = f"{_family_token(verb)}_misc" if mode == "ops" else "misc"
        entry["family"] = f"config_{group}" if mode == "config" else group


def _variants_cover(entry: dict, remainder: tuple[str, ...]) -> bool:
    """True when some usage variant reaches *remainder* (CHOICE tokens expand)."""
    for suffix in entry["variants"]:
        if len(suffix) < len(remainder):
            continue
        for want, have in zip(remainder, suffix):
            if have != want and want not in have.split("|"):
                break
        else:
            return True
    return False


def apply_recovery_families(entries: dict, curation: dict) -> int:
    """Tag configure stems covering a curated recovery stem as config_recovery.

    Coverage is either direct (the entry stem starts with a recovery stem) or
    via enum collapse (the recovery stem's remaining tokens are reachable
    through a CHOICE token in one of the entry's usage variants, e.g.
    ``set deviceconfig system ip-address`` inside
    ``set deviceconfig system default-gateway|ip-address|... <ip/netmask>``).
    """
    recovery = [tuple(s.split()) for s in curation.get("recovery_stems", [])]
    tagged = 0
    for key, entry in entries.items():
        if entry["mode"] != "config":
            continue
        tokens = tuple(key.split())
        for stem in recovery:
            if tokens[:len(stem)] == stem or (
                stem[:len(tokens)] == tokens
                and _variants_cover(entry, stem[len(tokens):])
            ):
                entry["family"] = "config_recovery"
                tagged += 1
                break
    return tagged


def platforms_for(key: str, markers: set[str]) -> list[str]:
    tokens = key.split()
    return ["panorama"] if any(t in markers for t in tokens[:2]) else ["fw"]


# ── deltas ───────────────────────────────────────────────────────────────────


def _version_tuple(version: str) -> tuple[int, ...]:
    return tuple(int(part) for part in version.split("."))


# ── collisions ───────────────────────────────────────────────────────────────


def registry_keys() -> tuple[set[str], set[str]]:
    """Return ``(curated_keys, openapi_generated_keys)`` from the live registry."""
    from app.commands import identity, network, objects, operations, packet_tracer, security, setup

    curated: set[str] = set()
    for module in (setup, objects, security, network, identity, operations, packet_tracer):
        curated.update(module.COMMANDS)

    from app.commands.generated import COMMANDS as generated

    return curated, set(generated)


# ── build ────────────────────────────────────────────────────────────────────


def build_catalog() -> tuple[list[dict], dict]:
    sources = json.loads(SOURCES_FILE.read_text(encoding="utf-8"))
    curation = json.loads(CURATION_FILE.read_text(encoding="utf-8"))
    report: dict = {
        "pages": [],            # (key, mirror lines, normalized lines, quarantined)
        "quarantine": [],
        "inferred": [],
        "folds": [],
        "cross_merges": 0,
        "delta_merged": 0,
        "delta_created": 0,
        "tombstoned": 0,
        "unmatched_deletes": [],
        "scm_missing": [],
        "dropped_curated": [],
        "shadowed_generated": [],
        "curated_prefix": [],
    }

    # Read + normalize every registered mirror (union corpus feeds inference).
    page_tokens: dict[str, list[list[str]]] = {}
    union_corpus: list[list[str]] = []
    pages = [dict(p) for p in sources["pages"]]
    for page in pages:
        mirror = MIRROR_DIR / f"{page['key']}.txt"
        if not mirror.exists():
            print(f"  ⚠ mirror missing for {page['key']} — run dev/panosupdate.py first; skipping")
            report["pages"].append((page["key"], 0, 0, 0))
            continue
        raw_lines = mirror.read_text(encoding="utf-8").splitlines()
        token_lines, quarantined = normalize_lines(raw_lines)
        page_tokens[page["key"]] = token_lines
        union_corpus.extend(token_lines)
        report["pages"].append((page["key"], len(raw_lines), len(token_lines), len(quarantined)))
        report["quarantine"].extend(f"{page['key']}: {line}" for line in quarantined)

    # pass 2 — one global inference over the union corpus.
    value_like, inferred = infer_value_like(union_corpus, curation)
    report["inferred"] = inferred

    # Base hierarchy pages (in registry order), then version-ordered deltas.
    entries: dict[str, dict] = {}
    hierarchy = [p for p in pages if p["kind"] in ("ops-hierarchy", "config-hierarchy") and p["key"] in page_tokens]
    deltas = sorted(
        (p for p in pages if p["kind"] in ("added", "deleted") and p["key"] in page_tokens),
        key=lambda p: (_version_tuple(p["version"]), 0 if p["kind"] == "added" else 1, p["key"]),
    )

    for page in hierarchy:
        mode = "config" if page["kind"] == "config-hierarchy" else "ops"
        stems, fold_log = stems_for_page(page_tokens[page["key"]], value_like)
        report["folds"].extend(f"{page['key']}: {item}" for item in fold_log)
        for key in sorted(stems):
            stem = stems[key]
            if key in entries:
                existing = entries[key]
                for suffix, weight in stem["variants"].items():
                    existing["variants"][suffix] = existing["variants"].get(suffix, 0) + weight
                existing["weight"] += stem["weight"]
                report["cross_merges"] += 1
            else:
                entries[key] = {
                    "tokens": stem["tokens"],
                    "variants": dict(stem["variants"]),
                    "weight": stem["weight"],
                    "mode": mode,
                    "source": page["key"],
                    "version_added": page["version"],
                    "version_removed": None,
                }

    for page in deltas:
        stems, fold_log = stems_for_page(page_tokens[page["key"]], value_like)
        report["folds"].extend(f"{page['key']}: {item}" for item in fold_log)
        if page["kind"] == "added":
            for key in sorted(stems):
                stem = stems[key]
                if key in entries:
                    existing = entries[key]
                    for suffix, weight in stem["variants"].items():
                        existing["variants"][suffix] = existing["variants"].get(suffix, 0) + weight
                    existing["weight"] += stem["weight"]
                    report["delta_merged"] += 1  # version_added stays original
                else:
                    verb = key.split()[0]
                    entries[key] = {
                        "tokens": stem["tokens"],
                        "variants": dict(stem["variants"]),
                        "weight": stem["weight"],
                        "mode": "config" if verb == "set" else "ops",
                        "source": page["key"],
                        "version_added": page["version"],
                        "version_removed": None,
                    }
                    report["delta_created"] += 1
        else:  # deleted — tombstone, never remove
            for key in sorted(stems):
                if key in entries:
                    entries[key]["version_removed"] = page["version"]
                    report["tombstoned"] += 1
                else:
                    report["unmatched_deletes"].append(key)

    # pass 7 — families + platforms + curation extras.
    assign_families(entries)
    report["recovery_tagged"] = apply_recovery_families(entries, curation)
    markers = set(curation.get("panorama_markers", []))
    # scm_map: exact stem match preferred; when the parsed stem cut landed
    # deeper (a literal keyword followed the mapped stem), propagate the
    # mapping onto every entry extending it — they serve the same ops-job
    # data.  Longer mapped stems are applied last so the most specific wins.
    scm_map = dict(curation.get("scm_map", {}))
    scm_for_key: dict[str, dict] = {}
    report["scm_missing"] = []
    for mapped in sorted(scm_map, key=lambda s: (len(s.split()), s)):
        if mapped in entries:
            scm_for_key[mapped] = scm_map[mapped]
            continue
        extending = [k for k in sorted(entries) if k.startswith(mapped + " ")]
        for key in extending:
            scm_for_key[key] = scm_map[mapped]
        report["scm_missing"].append((mapped, extending))

    # Collisions against the live registry.
    curated_keys, generated_keys = registry_keys()
    for key in sorted(entries):
        if key in curated_keys:
            report["dropped_curated"].append(key)
            del entries[key]
        elif key in generated_keys:
            report["shadowed_generated"].append(key)
    for key in sorted(entries):
        tokens = key.split()
        for curated in curated_keys:
            curated_tokens = curated.split()
            if len(curated_tokens) < len(tokens) and tokens[:len(curated_tokens)] == curated_tokens:
                report["curated_prefix"].append(f"{key} (extends curated `{curated}`)")
                break

    # Final entry records (sorted by key).
    catalog: list[dict] = []
    for key in sorted(entries):
        entry = entries[key]
        record = {
            "key": key,
            "usage": synthesize_usage(entry),
            "ssh": " ".join(entry["tokens"]),
            "verb": key.split()[0],
            "family": entry["family"],
            "platforms": platforms_for(key, markers),
            "version_added": entry["version_added"],
            "version_removed": entry["version_removed"],
            "source": entry["source"],
            "merged_lines": entry["weight"],
        }
        if key in scm_for_key:
            record["scm"] = scm_for_key[key]
        catalog.append(record)

    return catalog, report


# ── report ───────────────────────────────────────────────────────────────────


def print_report(catalog: list[dict], report: dict) -> None:
    print("── PAN-OS catalog generation report ──")
    print("\nMirror line counts (raw -> normalized/deduped, quarantined):")
    for key, raw, norm, quarantined in report["pages"]:
        print(f"  {key:<18} {raw:>6} -> {norm:>6}   quarantined: {quarantined}")

    print(f"\nQuarantined lines: {len(report['quarantine'])}")
    for item in report["quarantine"][:20]:
        print(f"  ! {item}")
    if len(report["quarantine"]) > 20:
        print(f"  … and {len(report['quarantine']) - 20} more")

    print(f"\nInferred VALUE_LIKE tokens ({len(report['inferred'])}):")
    for token in report["inferred"]:
        print(f"  · {token}")
    if not report["inferred"]:
        print("  (none — only curated value_token_overrides apply)")

    fw = sum(1 for e in catalog if e["platforms"] == ["fw"])
    panorama = len(catalog) - fw
    print(f"\nStems emitted: {len(catalog)}  (fw: {fw}, panorama: {panorama})")
    print(f"Prefix folds: {len(report['folds'])}")
    for item in report["folds"][:10]:
        print(f"  ~ {item}")
    print(
        f"Cross-page merges: {report['cross_merges']}   "
        f"delta merged: {report['delta_merged']}   delta created: {report['delta_created']}   "
        f"tombstoned: {report['tombstoned']}   recovery-tagged: {report.get('recovery_tagged', 0)}"
    )

    families: dict[str, int] = defaultdict(int)
    for entry in catalog:
        families[entry["family"]] += 1
    print(f"\nFamily histogram ({len(families)} families):")
    for name in sorted(families):
        print(f"  {name:<28} {families[name]}")

    buckets = {"<=30": 0, "31-44": 0, "45-60": 0, ">60": 0}
    for entry in catalog:
        length = len(entry["key"])
        if length <= 30:
            buckets["<=30"] += 1
        elif length <= 44:
            buckets["31-44"] += 1
        elif length <= 60:
            buckets["45-60"] += 1
        else:
            buckets[">60"] += 1
    print("\nKey-length histogram:")
    for bucket, count in buckets.items():
        print(f"  {bucket:<6} {count}")

    print(f"\nCollisions — curated key match, entry DROPPED ({len(report['dropped_curated'])}):")
    for key in report["dropped_curated"]:
        print(f"  - {key}")
    print(f"Collisions — OpenAPI-generated key match, kept (merge order shadows) ({len(report['shadowed_generated'])}):")
    for key in report["shadowed_generated"]:
        print(f"  - {key}")
    print(f"Curated-prefix stems, kept ({len(report['curated_prefix'])}):")
    for item in report["curated_prefix"]:
        print(f"  - {item}")

    print(f"\nUnmatched deletions ({len(report['unmatched_deletes'])}) — expected for config refs:")
    for key in report["unmatched_deletes"][:15]:
        print(f"  - {key}")
    if len(report["unmatched_deletes"]) > 15:
        print(f"  … and {len(report['unmatched_deletes']) - 15} more")

    scm_count = sum(1 for e in catalog if "scm" in e)
    print(f"\nEntries carrying scm mappings: {scm_count}")
    if report["scm_missing"]:
        print(f"scm_map stems without an exact stem match ({len(report['scm_missing'])}) — "
              "mapping propagated to the extending stems:")
        for mapped, extending in report["scm_missing"]:
            print(f"  - {mapped}")
            for key in extending[:6]:
                print(f"      -> {key}")
            if not extending:
                print("      -> (no extending stems either — mapping unused)")


# ── render ───────────────────────────────────────────────────────────────────


def render(catalog: list[dict]) -> str:
    lines = [
        '"""AUTO-GENERATED PAN-OS CLI command catalog — DO NOT EDIT BY HAND.',
        "",
        "Generated by ``dev/generate_panos_catalog.py`` from the PAN-OS CLI mirrors",
        "under ``docs/panos-cli/`` (pulled by ``dev/panosupdate.py``).  Each entry is",
        "one command stem; ``app/commands/panos_generated.py`` turns entries into",
        "feature-gated CommandDefs.",
        "",
        "Regenerate with:",
        "    python dev/panosupdate.py               # refresh mirrors (network)",
        "    python dev/generate_panos_catalog.py    # rebuild this file",
        '"""',
        "",
        "from __future__ import annotations",
        "",
        "PANOS_CATALOG: list[dict] = [",
    ]
    for entry in catalog:
        lines.append(f"    {entry!r},")
    lines.append("]")
    lines.append("")
    return "\n".join(lines)


# ── CLI ──────────────────────────────────────────────────────────────────────


def main() -> int:
    check_only = "--check" in sys.argv[1:]
    catalog, report = build_catalog()
    rendered = render(catalog)
    print_report(catalog, report)

    current = CATALOG_FILE.read_text(encoding="utf-8") if CATALOG_FILE.exists() else ""
    if check_only:
        if rendered != current:
            print("\napp/commands/panos_catalog.py is STALE — mirrors or curation "
                  "changed. Run: python dev/generate_panos_catalog.py")
            return 1
        print(f"\npanos catalog current — {len(catalog)} entries")
        return 0

    CATALOG_FILE.write_text(rendered, encoding="utf-8")
    print(f"\nWrote app/commands/panos_catalog.py — {len(catalog)} entries")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
