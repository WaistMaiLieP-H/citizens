#!/usr/bin/env python3
"""
Path-anchor refactor.

Rewrites every known reference to /home/vernenlegal/{FamilyLaw,NonFamilyLaw,citizens}
into anchor form: ${familylaw}, ${nonfamilylaw}, ${citizens}.

For each tether.json, injects a `path_anchors` block immediately after the opening
brace so that future readers can resolve the anchors.

Usage:
    python3 _apply_path_anchors.py            # dry-run, prints planned changes
    python3 _apply_path_anchors.py --apply    # actually writes files

Safe to run while other terminals are active in dry-run mode (no disk writes).
"""

import sys
import re
import json
from pathlib import Path

REPO = Path("/home/vernenlegal")

# Substitution rules — applied in this order. Longest prefix first to avoid
# /home/vernenlegal/citizens being mangled by a shorter rule.
RULES = [
    ("/home/vernenlegal/NonFamilyLaw", "${nonfamilylaw}"),
    ("/home/vernenlegal/FamilyLaw",    "${familylaw}"),
    ("/home/vernenlegal/citizens",     "${citizens}"),
]

# Files to rewrite (text-level substitution preserves hand formatting).
TARGET_FILES = [
    # FamilyLaw/NonFamilyLaw + citizens — actor records
    "citizens/CA_Family_Law_Litigator/actors/ajaniku_sala.json",
    "citizens/CA_Family_Law_Litigator/actors/delucchi_paul_judge.json",
    "citizens/CA_Family_Law_Litigator/actors/ditsworth_david.json",
    "citizens/CA_Family_Law_Litigator/actors/paredes_olga.json",
    "citizens/CA_Family_Law_Litigator/actors/thompson_trina_judge.json",
    # case records
    "citizens/CA_Family_Law_Litigator/cases/RF09456481.json",
    "citizens/CA_Family_Law_Litigator/cases/RF09470833.json",
    "citizens/CA_Family_Law_Litigator/cases/RF10508853.json",
    # standard manifest
    "citizens/CA_Family_Law_Litigator/standards/cal_fam_3164_mediator_qualifications/manifest.json",
    # tether (also gets path_anchors injection)
    "citizens/CA_Family_Law_Litigator/tether.json",
    # historical chain
    "citizens/CA_Family_Law_Litigator/historical_chain/06_1993_family_code_recodification.json",
    "citizens/CA_Family_Law_Litigator/historical_chain/07_current.json",
    # dossier
    "citizens/CA_Family_Law_Litigator/dossier.md",
    # generator scripts
    "citizens/_deepen_mediator_qualifications_trio.py",
    "citizens/_deepen_remaining_manifests.py",
    "citizens/_deepen_umbrella11_second_seeds.py",
    "citizens/_generate_minimal_manifests.py",
    "citizens/_populate_family_law_actors_and_cases.py",
    "citizens/_populate_family_law_historical_chain.py",
    "citizens/_populate_outstanding_investigations.py",
    "citizens/build_standard.py",
    # supporting
    "citizens/_shared_statutes_archive/shared_hashes.txt",
    "citizens/UMBRELLAS/README.md",
]

# Files that get a path_anchors block injected (currently only the
# CA_Family_Law_Litigator tether — extend as more Citizens adopt anchors).
TETHER_INJECTION_TARGETS = [
    "citizens/CA_Family_Law_Litigator/tether.json",
]

PATH_ANCHORS_BLOCK = '''  "path_anchors": {
    "_comment": "Symbolic anchors. Any string in this Citizen's records of the form ${name}/... resolves to anchors[name] + '/...'. To relocate a bucket, edit one line here. Future readers (including future Claude sessions) MUST consult this block before assuming an absolute path.",
    "familylaw":    "/home/vernenlegal/FamilyLaw",
    "nonfamilylaw": "/home/vernenlegal/NonFamilyLaw",
    "citizens":     "/home/vernenlegal/citizens"
  },

'''


def count_substitutions(text):
    counts = {}
    for old, new in RULES:
        n = text.count(old)
        if n:
            counts[old] = n
    return counts


def apply_substitutions(text):
    for old, new in RULES:
        text = text.replace(old, new)
    return text


def inject_path_anchors(text):
    """Insert PATH_ANCHORS_BLOCK immediately after the opening `{\n` of a JSON file.
    Idempotent: if the block already exists, returns text unchanged.
    """
    if '"path_anchors"' in text:
        return text, False
    # Find the opening brace and the first newline after it
    m = re.match(r'^\s*\{\s*\n', text)
    if not m:
        return text, False
    insertion_point = m.end()
    new_text = text[:insertion_point] + PATH_ANCHORS_BLOCK + text[insertion_point:]
    return new_text, True


def validate_json(text, path):
    """For .json files, verify the result still parses."""
    if not str(path).endswith('.json'):
        return True, None
    # Strip the ${anchors} for the parse test — they're valid JSON strings as-is
    try:
        json.loads(text)
        return True, None
    except json.JSONDecodeError as e:
        return False, str(e)


def main():
    apply = "--apply" in sys.argv

    print("=" * 70)
    print(f"PATH ANCHOR REFACTOR  —  {'APPLY MODE' if apply else 'DRY RUN'}")
    print("=" * 70)
    print()

    total_subs = 0
    total_files_changed = 0
    errors = []

    for rel in TARGET_FILES:
        path = REPO / rel
        if not path.exists():
            print(f"  [MISS] {rel}")
            continue

        original = path.read_text()
        counts = count_substitutions(original)
        new_text = apply_substitutions(original)
        anchors_injected = False

        if str(rel) in TETHER_INJECTION_TARGETS:
            new_text, anchors_injected = inject_path_anchors(new_text)

        if not counts and not anchors_injected:
            continue

        # Validate JSON if applicable
        ok, err = validate_json(new_text, path)
        if not ok:
            errors.append((rel, err))
            print(f"  [JSON ERROR] {rel}: {err}")
            continue

        sub_count = sum(counts.values())
        total_subs += sub_count
        total_files_changed += 1

        markers = []
        for old, n in counts.items():
            short = old.replace("/home/vernenlegal/", "")
            markers.append(f"{short}×{n}")
        if anchors_injected:
            markers.append("INJECT path_anchors")

        print(f"  [{'WRITE' if apply else 'PLAN '}] {rel}")
        print(f"           {', '.join(markers)}")

        if apply:
            path.write_text(new_text)

    print()
    print("=" * 70)
    print(f"  Files changed: {total_files_changed}")
    print(f"  Substitutions: {total_subs}")
    if errors:
        print(f"  ERRORS: {len(errors)}")
        for r, e in errors:
            print(f"    {r}: {e}")
    print("=" * 70)
    if not apply:
        print()
        print("This was a DRY RUN. No files were modified.")
        print("Run with --apply to actually write changes.")


if __name__ == "__main__":
    main()
