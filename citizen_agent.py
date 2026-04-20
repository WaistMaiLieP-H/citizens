#!/usr/bin/env python3
"""
Layer 6 — Citizen Agent Runner
Each Citizen loads its standards corpus and audits documents via the Anthropic API.
"""

import anthropic
import base64
import json
import os
import sys
from datetime import datetime
from pathlib import Path

CITIZENS_DIR = Path(__file__).parent
API_KEY = os.environ.get("ANTHROPIC_API_KEY")
MODEL = "claude-sonnet-4-6"


def load_citizen_context(citizen_id: str, standard_ids: list[str] | None = None) -> str:
    """Load dossier + methodology + requested standards as system context."""
    citizen_dir = CITIZENS_DIR / citizen_id
    parts = []

    for fname in ("dossier.md", "methodology.md"):
        fpath = citizen_dir / fname
        if fpath.exists():
            parts.append(fpath.read_text())

    std_dir = citizen_dir / "standards"
    if std_dir.exists():
        candidates = (
            [std_dir / s for s in standard_ids] if standard_ids
            else sorted(std_dir.iterdir())
        )
        for std_path in candidates:
            if not std_path.is_dir():
                continue
            current = std_path / "current"
            rule = (current / "rule.md").read_text() if (current / "rule.md").exists() else ""
            reasoning = (current / "reasoning.md").read_text() if (current / "reasoning.md").exists() else ""
            if rule or reasoning:
                parts.append(
                    f"---\n# STANDARD: {std_path.name}\n\n## RULE\n{rule}\n\n## REASONING\n{reasoning}"
                )

    return "\n\n".join(parts)


def build_system_prompt(citizen_id: str, standard_ids: list[str] | None = None) -> str:
    ctx = load_citizen_context(citizen_id, standard_ids)
    return f"""You are {citizen_id}, a professional Citizen agent in the Vernen Legal Compliance framework.

{ctx}

AUDIT INSTRUCTIONS:
- You audit documents against your standards corpus. Your findings carry professional authority only within your domain.
- For each applicable standard: state the Standard ID, compliance status (COMPLIANT / NON-COMPLIANT / INDETERMINATE / NOT_APPLICABLE), specific rule elements implicated, evidence from the document (quote directly), and recommended action.
- Flag cross-domain findings with the responsible Citizen ID — do not opine outside your domain.
- If a required document element is absent, that absence is the finding. State it plainly.
- Do not speculate beyond what the document contains. Unknown = INDETERMINATE, not assumed.
- End with a SUMMARY TABLE listing each standard ID and its status."""


def audit_text(citizen_id: str, document_text: str, document_meta: dict,
               standard_ids: list[str] | None = None) -> dict:
    """Audit a text document."""
    client = anthropic.Anthropic(api_key=API_KEY)

    meta_block = "\n".join(f"{k}: {v}" for k, v in document_meta.items())
    user_content = f"""DOCUMENT METADATA:
{meta_block}

DOCUMENT CONTENT:
{document_text}

Produce your audit finding."""

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=build_system_prompt(citizen_id, standard_ids),
        messages=[{"role": "user", "content": user_content}],
    )

    return {
        "citizen": citizen_id,
        "document_meta": document_meta,
        "audit": response.content[0].text,
        "model": MODEL,
        "tokens": {"input": response.usage.input_tokens, "output": response.usage.output_tokens},
        "timestamp": datetime.utcnow().isoformat(),
    }


def audit_image(citizen_id: str, image_path: str, document_meta: dict,
                standard_ids: list[str] | None = None) -> dict:
    """Audit a document image (JPG/PNG/PDF page)."""
    client = anthropic.Anthropic(api_key=API_KEY)

    img = Path(image_path)
    media_type = "image/jpeg" if img.suffix.lower() in (".jpg", ".jpeg") else "image/png"
    img_data = base64.standard_b64encode(img.read_bytes()).decode()

    meta_block = "\n".join(f"{k}: {v}" for k, v in document_meta.items())

    response = client.messages.create(
        model=MODEL,
        max_tokens=4096,
        system=build_system_prompt(citizen_id, standard_ids),
        messages=[{
            "role": "user",
            "content": [
                {
                    "type": "image",
                    "source": {"type": "base64", "media_type": media_type, "data": img_data},
                },
                {
                    "type": "text",
                    "text": f"DOCUMENT METADATA:\n{meta_block}\n\nProduce your audit finding for this document image.",
                },
            ],
        }],
    )

    return {
        "citizen": citizen_id,
        "document_meta": document_meta,
        "source_image": str(img),
        "audit": response.content[0].text,
        "model": MODEL,
        "tokens": {"input": response.usage.input_tokens, "output": response.usage.output_tokens},
        "timestamp": datetime.utcnow().isoformat(),
    }


def save_finding(result: dict, session_dir: str) -> Path:
    """Save audit finding to session directory."""
    out = Path(session_dir) / result["citizen"]
    out.mkdir(parents=True, exist_ok=True)

    (out / "audit_finding.md").write_text(result["audit"])
    meta = {k: v for k, v in result.items() if k != "audit"}
    (out / "audit_metadata.json").write_text(json.dumps(meta, indent=2))

    print(f"  Saved: {out}/audit_finding.md  ({result['tokens']['input']}in / {result['tokens']['output']}out tokens)")
    return out


def run_session(session_id: str, document_meta: dict,
                citizens: list[dict], document_text: str = None,
                image_path: str = None) -> Path:
    """
    Run a multi-citizen audit session.
    citizens = [{"id": "CA_Law_Enforcement_Procedures_Specialist", "standards": [...optional list...]}]
    """
    session_dir = CITIZENS_DIR / "audit_sessions" / session_id
    doc_name = document_meta.get("filename", "document").replace(" ", "_")
    doc_dir = session_dir / doc_name
    doc_dir.mkdir(parents=True, exist_ok=True)

    print(f"\nSession: {session_id}")
    print(f"Document: {doc_name}")
    print(f"Citizens: {[c['id'] for c in citizens]}\n")

    results = []
    for c in citizens:
        print(f"  Auditing: {c['id']} ...")
        if image_path:
            result = audit_image(c["id"], image_path, document_meta, c.get("standards"))
        else:
            result = audit_text(c["id"], document_text, document_meta, c.get("standards"))
        save_finding(result, str(doc_dir))
        results.append(result)

    # Write session index
    index = {
        "session_id": session_id,
        "document": document_meta,
        "citizens_audited": [c["id"] for c in citizens],
        "timestamp": datetime.utcnow().isoformat(),
        "total_tokens": sum(r["tokens"]["input"] + r["tokens"]["output"] for r in results),
    }
    (doc_dir / "session_index.json").write_text(json.dumps(index, indent=2))
    print(f"\nSession complete. Total tokens: {index['total_tokens']}")
    print(f"Output: {doc_dir}")
    return doc_dir


if __name__ == "__main__":
    # Quick smoke test
    if not API_KEY:
        print("ERROR: ANTHROPIC_API_KEY not set"); sys.exit(1)

    test_meta = {
        "filename": "layer6_smoke_test",
        "document_type": "test",
        "date": "2026-04-20",
        "agency": "N/A",
    }
    test_text = "This is a Layer 6 smoke test. No real document content."

    result = audit_text(
        citizen_id="CA_Law_Enforcement_Procedures_Specialist",
        document_text=test_text,
        document_meta=test_meta,
        standard_ids=["pen_code_836_arrest_authority"],
    )
    print(result["audit"][:300])
    print(f"\nTokens: {result['tokens']}")
    print("Layer 6 LIVE")
