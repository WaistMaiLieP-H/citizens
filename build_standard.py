#!/usr/bin/env python3
"""
build_standard.py — Vernen Standard Builder (Autopilot)

Codifies the standards-build pipeline that was developed manually for the
Field Act, Riley Act, and Contractors State License Law of 1929. Given a
standard's identifying inputs and a primary-source URL, this script does
the mechanical work:

  1. Creates the folder structure under the right Citizen
  2. Downloads the source PDF (with retry/resume)
  3. Hashes the PDF (sha256)
  4. Optionally renders specified PDF pages as PNG (via pdftoppm)
  5. Hashes each PNG
  6. Generates a stub manifest.json and provenance.json
  7. Prints a status report

It does NOT do the substantive work of reading the rendered pages, writing
the section outlines, resolving historical conflicts, or witnessing the
standard. Those steps still require a human or an LLM in the loop. The
script's job is to remove the mechanical labor so the verification step is
the only thing left.

Designed to be schedulable via cron / the Claude Code `schedule` skill.

Usage:
    python3 build_standard.py \\
        --id CA_RILEY_ACT_1933 \\
        --jurisdiction California \\
        --year 1933 \\
        --citizen CA_Building_Official \\
        --source-url https://clerk.assembly.ca.gov/sites/clerk.assembly.ca.gov/files/archive/Statutes/1933/33Vol1_Chapters.pdf \\
        --source-name "Statutes of California 1933 Volume 1 Chapters" \\
        --source-authority "California State Assembly, Office of the Chief Clerk" \\
        --pdf-pages 1532-1534 \\
        --chapter 601 \\
        --popular-name "Riley Act"

Required inputs:
    --id              Vernen standard ID (e.g. CA_RILEY_ACT_1933)
    --jurisdiction    Jurisdiction (e.g. California, Federal, Texas)
    --year            Year of original enactment
    --citizen         Citizen folder name under citizens/ that owns this standard
    --source-url      URL of the primary source PDF

Optional inputs:
    --source-name     Human-readable name of the source document
    --source-authority Name of the issuing authority for the source
    --pdf-pages       Page range to render (e.g. "352-355" or "352" for single)
    --chapter         Chapter or section number within the source
    --popular-name    Common name of the standard (e.g. "Field Act")
    --citizens-root   Override the default citizens root directory
    --no-render       Skip page rendering even if --pdf-pages is given
    --shared-source   If set, look for an existing PDF at this path before downloading
"""

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CITIZENS_ROOT_DEFAULT = Path("${citizens}")
USER_AGENT = "Vernen-Compliance-Provenance-Fetcher/1.0 (research; contact michael@vernenlegal.com)"


def now_utc_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def sha256_of_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, check=True, **kwargs)


def have(tool: str) -> bool:
    return shutil.which(tool) is not None


def check_tools() -> None:
    missing = [t for t in ("wget", "curl", "pdftoppm", "pdfinfo") if not have(t)]
    if missing:
        sys.exit(f"ERROR: missing required tools: {', '.join(missing)}. Install poppler-utils, wget, and curl.")


def setup_folder(citizens_root: Path, citizen: str, standard_id: str) -> Path:
    standard_folder_name = standard_id.lower().removeprefix("ca_").removeprefix("us_")
    base = citizens_root / citizen / "standards" / standard_folder_name
    for sub in ("origin", "origin/chapter_pages", "evolution", "current", "context"):
        (base / sub).mkdir(parents=True, exist_ok=True)
    return base


def download_pdf(url: str, dest: Path, shared_source: Path | None = None) -> Path:
    """Download a PDF to `dest` (with retry/resume), or use a pre-existing
    shared source file if given."""
    if shared_source and shared_source.exists():
        if not dest.exists() or dest.is_symlink():
            if dest.exists() or dest.is_symlink():
                dest.unlink()
            try:
                rel = os.path.relpath(shared_source, dest.parent)
                dest.symlink_to(rel)
            except Exception:
                shutil.copy2(shared_source, dest)
        return dest

    if dest.exists() and dest.stat().st_size > 0:
        return dest

    print(f"  downloading {url}")
    run([
        "wget", "--tries=20", "--timeout=60", "--continue",
        f"--user-agent={USER_AGENT}",
        "-O", str(dest),
        url,
    ])
    return dest


def pdf_metadata(pdf_path: Path) -> dict:
    out = subprocess.run(
        ["pdfinfo", str(pdf_path)], check=True, capture_output=True, text=True
    ).stdout
    meta = {}
    for line in out.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def parse_page_range(spec: str) -> tuple[int, int]:
    if "-" in spec:
        a, b = spec.split("-", 1)
        return int(a), int(b)
    return int(spec), int(spec)


def render_pages(pdf_path: Path, first: int, last: int, out_dir: Path) -> list[Path]:
    """Render PDF pages [first, last] inclusive to PNG, return list of paths."""
    out_dir.mkdir(parents=True, exist_ok=True)
    tmp_prefix = out_dir / "_tmp_page"
    print(f"  rendering pages {first}-{last} of {pdf_path.name}")
    run([
        "pdftoppm", "-f", str(first), "-l", str(last),
        "-r", "150", "-png",
        str(pdf_path), str(tmp_prefix),
    ])
    pngs = sorted(out_dir.glob("_tmp_page-*.png"))
    final = []
    for p in pngs:
        n = int(p.stem.split("-")[-1])
        target = out_dir / f"page_pdf{n:04d}.png"
        if target.exists():
            target.unlink()
        p.rename(target)
        final.append(target)
    return final


def write_manifest(args, base: Path, pdf_path: Path, pdf_hash: str, pdf_meta: dict, page_renders: list[tuple[Path, str]]) -> Path:
    """Write a stub manifest.json with the mechanical fields filled in.
    Substantive fields (section outlines, historical loss, citizen ownership
    detail) are placeholders for human/LLM verification."""
    manifest = {
        "standard_id": args.id,
        "version": "0.1.0-stub-autopilot",
        "filed_at_utc": now_utc_iso(),
        "filed_by": f"build_standard.py (autopilot) — operator: {os.environ.get('USER', 'unknown')}",
        "status": "STUB — mechanical scaffolding only; substantive verification still required",
        "primary_citation": {
            "jurisdiction": args.jurisdiction,
            "year": args.year,
            "chapter": args.chapter,
            "popular_name": args.popular_name,
            "official_title_verbatim_from_chaptered_text": "TO BE FILLED IN — read the rendered chapter pages and transcribe the title verbatim",
            "approval_date": "TO BE FILLED IN",
            "approval_governor": "TO BE FILLED IN",
            "in_effect_date": "TO BE FILLED IN",
            "primary_source_text_location": f"origin/{pdf_path.name}",
        },
        "structure_of_original_act": {
            "section_count": "TO BE FILLED IN",
            "section_outline": "TO BE FILLED IN — read the rendered chapter pages and outline each section",
        },
        "umbrellas": "TO BE FILLED IN — assign one or more of the 10 substantive umbrellas",
        "owner_citizen": {
            "primary": args.citizen,
            "ownership_note": "Owner assigned by autopilot based on --citizen argument; verify this is the correct owner for the standard",
        },
        "current_codification": {
            "status": "NOT YET DOCUMENTED",
            "note": "TO BE FILLED IN — locate the current codified form (if any) and its leginfo URL",
        },
        "triple_constraint_test_results": {
            "governing_guidelines": {"passes": "TO BE VERIFIED", "evidence": "TO BE FILLED IN"},
            "standards_of_creation": {"passes": "TO BE VERIFIED", "evidence": "TO BE FILLED IN"},
            "standard_of_care": {"passes": "PARTIAL", "origin_layer": "VERIFIED (autopilot)", "evolution_layer": "TO BE FILLED IN", "current_layer": "TO BE FILLED IN"},
        },
        "five_layer_bar_status": {
            "rule": "PRESENT (in rendered pages, but transcription/outline TO BE FILLED IN)",
            "reasoning": "TO BE FILLED IN",
            "historical_loss": "TO BE FILLED IN",
            "cross_references": "TO BE FILLED IN",
            "verifiable_provenance": "PRESENT (autopilot fetched, hashed, recorded)",
        },
        "two_witness_status": {
            "first_mouth_proposer": "build_standard.py autopilot (mechanical only — does not constitute first-mouth proposal)",
            "second_mouth_witness": "NONE",
            "publishable_to_corpus": False,
            "status": "STUB — autopilot scaffolding; first-mouth substantive proposal still required",
        },
        "files": {
            "origin": [f"origin/{pdf_path.name}"] + [f"origin/chapter_pages/{p.name}" for p, _ in page_renders],
            "evolution": [],
            "current": [],
            "context": [],
            "manifest": "manifest.json",
            "provenance": "provenance.json",
        },
        "outstanding_work": [
            "READ the rendered chapter pages and verify they contain the expected chapter",
            "TRANSCRIBE the chapter title verbatim into primary_citation.official_title_verbatim_from_chaptered_text",
            "OUTLINE each section in structure_of_original_act.section_outline",
            "ASSIGN umbrellas (from the 10 substantive umbrellas catalog)",
            "DOCUMENT the historical loss / triggering event",
            "FETCH the current codified form (if any)",
            "BUILD cross-references to other Vernen corpus standards",
            "OBTAIN second-mouth countersignature before publication",
        ],
    }
    p = base / "manifest.json"
    p.write_text(json.dumps(manifest, indent=2))
    return p


def write_provenance(args, base: Path, pdf_path: Path, pdf_hash: str, pdf_meta: dict, page_renders: list[tuple[Path, str]], first: int | None, last: int | None) -> Path:
    fetches = [
        {
            "artifact_local_path": f"origin/{pdf_path.name}",
            "source_url": args.source_url,
            "source_authority": args.source_authority or "TO BE FILLED IN",
            "source_authority_type": "primary",
            "fetched_at_utc": now_utc_iso(),
            "fetch_method": "wget --tries=20 --timeout=60 --continue (via build_standard.py autopilot)",
            "file_size_bytes": pdf_path.stat().st_size,
            "sha256": pdf_hash,
            "pdf_metadata": pdf_meta,
            "content_description": args.source_name or f"{args.year} {args.jurisdiction} primary source PDF",
        }
    ]
    for png_path, png_hash in page_renders:
        n = int(png_path.stem.replace("page_pdf", ""))
        fetches.append({
            "artifact_local_path": f"origin/chapter_pages/{png_path.name}",
            "derived_from_artifact": f"origin/{pdf_path.name}",
            "derived_from_artifact_sha256": pdf_hash,
            "derivation_method": f"pdftoppm -f {n} -l {n} -r 150 -png",
            "derivation_at_utc": now_utc_iso(),
            "sha256": png_hash,
            "file_size_bytes": png_path.stat().st_size,
            "content_description": f"Rendered page {n} of source PDF (TO BE VERIFIED for chapter contents)",
        })
    prov = {
        "standard_id": args.id,
        "provenance_record_filed_at_utc": now_utc_iso(),
        "fetcher_software": "build_standard.py autopilot (curl/wget/pdftoppm/sha256sum)",
        "fetcher_operator": os.environ.get("USER", "unknown"),
        "verification_principle": "Mechanical fetches are recorded with URL, timestamp, hash, and source authority. Autopilot does not verify substantive content; that remains the human/LLM step.",
        "fetches": fetches,
    }
    p = base / "provenance.json"
    p.write_text(json.dumps(prov, indent=2))
    return p


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--id", required=True, help="Vernen standard ID (e.g. CA_RILEY_ACT_1933)")
    p.add_argument("--jurisdiction", required=True)
    p.add_argument("--year", required=True, type=int)
    p.add_argument("--citizen", required=True, help="Citizen folder name under citizens/")
    p.add_argument("--source-url", required=True)
    p.add_argument("--source-name", default=None)
    p.add_argument("--source-authority", default=None)
    p.add_argument("--pdf-pages", default=None, help="Page range to render, e.g. 352-355 or 352")
    p.add_argument("--chapter", default=None)
    p.add_argument("--popular-name", default=None)
    p.add_argument("--citizens-root", default=str(CITIZENS_ROOT_DEFAULT))
    p.add_argument("--no-render", action="store_true")
    p.add_argument("--shared-source", default=None, help="Path to existing shared PDF; if present, symlink instead of downloading")
    args = p.parse_args()

    check_tools()

    print(f"[autopilot] standard_id = {args.id}")
    citizens_root = Path(args.citizens_root)
    base = setup_folder(citizens_root, args.citizen, args.id)
    print(f"[autopilot] folder = {base}")

    pdf_filename = args.source_url.rsplit("/", 1)[-1]
    pdf_path = base / "origin" / pdf_filename
    shared = Path(args.shared_source) if args.shared_source else None
    download_pdf(args.source_url, pdf_path, shared)
    pdf_hash = sha256_of_file(pdf_path) if not pdf_path.is_symlink() else sha256_of_file(pdf_path.resolve())
    print(f"[autopilot] pdf sha256 = {pdf_hash}")
    meta = pdf_metadata(pdf_path.resolve() if pdf_path.is_symlink() else pdf_path)
    print(f"[autopilot] pdf pages = {meta.get('Pages', '?')}")

    page_renders: list[tuple[Path, str]] = []
    if args.pdf_pages and not args.no_render:
        first, last = parse_page_range(args.pdf_pages)
        rendered = render_pages(
            pdf_path.resolve() if pdf_path.is_symlink() else pdf_path,
            first, last,
            base / "origin" / "chapter_pages",
        )
        for p_ in rendered:
            h = sha256_of_file(p_)
            page_renders.append((p_, h))
            print(f"[autopilot] rendered {p_.name} sha256={h[:16]}...")

    first, last = (parse_page_range(args.pdf_pages) if args.pdf_pages else (None, None))
    write_manifest(args, base, pdf_path, pdf_hash, meta, page_renders)
    write_provenance(args, base, pdf_path, pdf_hash, meta, page_renders, first, last)

    print()
    print(f"[autopilot] DONE — folder ready at {base}")
    print(f"[autopilot] Outstanding: a human or LLM must now read the rendered pages,")
    print(f"[autopilot]   verify the chapter contents, fill in the substantive fields")
    print(f"[autopilot]   in manifest.json, and obtain a second-mouth countersignature")
    print(f"[autopilot]   before this standard can be published to the corpus.")


if __name__ == "__main__":
    main()
