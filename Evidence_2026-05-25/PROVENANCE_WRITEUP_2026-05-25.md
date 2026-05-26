# Vernen / CITIZEN™ / Agents — Four-Source Evidence Writeup (2026-05-25)

**Author / Steward:** Michael Vernen Thomas Hartmann
**Domains:** Vernen, Vernen Legal, Vernen Legal Compliance (VLC), CITIZEN™
**Document Created:** 2026-05-25
**Document Purpose:** Extend `PROVENANCE_TIMELINE_2026-04.md` (committed 2026-05-24 15:33 UTC) in two directions: **backward**, by recording the on-disk pre-suspension build state that did not make it to GitHub before 2026-04-16; and **forward**, by recording the 2026-05-24 forensic findings (Google MyActivity timestamp anomalies, the `_COMPLIANCE_STACK.md` un-attributed-Claude-draft discovery, the Proton rclone Code 2028 fallout). Anchored by SHA-256 manifest hashes that already exist on disk.

**Document Rule:** Full detail. Not a snapshot. Not a summary. Every count, date, filename, and hash is preserved verbatim. If something is uncertain or unverified, it is labeled as such — not omitted, not rounded, not paraphrased.

**Originating session:** `44b4f373-b5e2-4717-b7c1-b85513adddf5` (Claude Code, 2026-05-25 13:45:43Z → 18:36:03Z). The audit underlying this writeup was performed during that session against ProtonDrive (rclone mount, live), USB `/media/vernenlegal/USB/Vernen/`, and the 13 public `WaistMaiLieP-H` GitHub repos.

© 2024–2026 Michael Vernen Thomas Hartmann. All Rights Reserved.

---

## 1. Anchor: what `PROVENANCE_TIMELINE_2026-04.md` already establishes

The existing anchor document, committed to the public `WaistMaiLieP-H/citizens` repository on 2026-05-24 (commit pushed 15:33 UTC) and mirrored to `USB/Vernen/Evidence_2026-05-24/PROVENANCE_TIMELINE_2026-04.md`, establishes:

- **2026-04-15 18:32:24 PDT** — initial commit `6ed17d7`: 45 Citizens, 5,163 files, FL Litigator 100% complete, CUSTOS/HERALD/ADAM/EVE all present.
- **2026-04-16** — Anthropic suspension notices (three same-day emails to `michetype78@gmail.com`) + $100 refund (Invoice #3293-5167) — one day after the public `citizens` initial commit.
- **2026-04-23** — Anthropic "Your account has been reinstated" email; user reports the account is not actually accessible.
- Commit-by-commit hash log 2026-04-08 → 2026-04-30 (verifiable by `git log` against the public repo).
- 2026-04-08 Anthropic "Managed Agents" public release predates `citizens` initial commit by 7 days and falls inside the 2026-04 build window.

This writeup does not restate that record. It **extends** it.

---

## 2. Backward extension: pre-2026-04-16 on-disk build state (Chunk1 inventory)

The `WaistMaiLieP-H/citizens` initial commit `6ed17d7` of 2026-04-15 18:32:24 PDT captured one snapshot of the build. The work in flight on the same machine in the days leading up to suspension was broader. ProtonDrive holds five archive ZIPs (`VernenDesktop_2026-04-14/Chunk{1..5}*.zip`, total **9.1 GB**) that were never extracted, never pushed to GitHub, and never indexed on USB until the 2026-05-25 audit.

### 2.1 Chunk inventory

| Chunk | Date | Size | Files | Contents | On GitHub? |
|---|---|---|---|---|---|
| **1** | **2026-04-11** | **1.7 GB** | **464** | Vernen build state (loose dirs + session logs) | **NO — gap** |
| 2 | 2026-04-14 | 3.5 MB | 313 | `CA_Family_Law_Litigator` snapshot | ✓ superset in `citizens` |
| **3** | **2026-04-11** | **3.25 GB** | **4,878** | Chunk1's loose dirs + `VernenBackup_2026-04-11/` (full citizens snapshot + statute work dirs) | Loose dirs **NO**; `VernenBackup` partially in `citizens` (current is newer) |
| 4 | 2026-04-12 | 1.63 GB | 3,690 | Full citizens snapshot 2026-04-12 | ✓ superset in `citizens` |
| 5 | — | 3.25 GB | — | **Byte-identical duplicate of Chunk3** (verified by file-listing match) | — |

**Verification performed 2026-05-25:** Chunk1's loose dirs are byte-for-byte present inside Chunk3 (same file counts for Action/Intelligence/Legal/Outreach/Reports/Standards). Chunk3 ⊃ Chunk1's loose dirs. Chunk5 was confirmed a duplicate of Chunk3 by central-directory listing comparison via `unzip -l`.

**Cross-check against GitHub:** A targeted `gh search code repo:WaistMaiLieP-H/*` against ten distinctive Chunk1 documents (named below in §2.2) returned **zero** matches across all 13 public repos. The Chunk1 distinctive material is not on GitHub as of 2026-05-25.

### 2.2 Chunk1 distinctive material — full inventory

This is the work product that existed on disk on **2026-04-11** (five days before the 2026-04-16 suspension), captured in the ZIP at that timestamp, and that has not been published.

**Top-level:**
- `SESSION_REVELATIONS_2026-04-11.md`
- `SESSION_WIRESHARK_BISQ_2026-04-11.md`
- `Father_Discovery_Institutions.md`
- `financial_advisor_tools.md`

**Action/** (2 files):
- `_BUILD_CLAIMS.md`

**CITIZEN/Catalog/** (3 files):
- `CATALOG-SUMMARY-2026-03-22.md`
- `CITIZEN_CATALOG.md`
- `CITIZEN_ROSTER_STATUS.md`

**Compliance/Platform/** (8 files):
- `Audio_Fork_Blueprint.md`
- `Communications_Fork_Blueprint.md`
- `Software_Fork_Blueprint.md`
- `Visual_Fork_Blueprint.md`
- `VERNEN_Technical_Spec_Sheet.md`
- `Vernen_ChromeAgent_Briefing.md`
- `Vernen_Deep_Forensic_Scan_OnePager.md`
- `Vernen_Forensic_Audit_Service_Agreement_TEMPLATE.md`

**Intelligence/** (8 files):
- `blackbox_results.md`
- `play_store_apps.csv`
- `play_store_apps.json`
- `play_store_audit_001-002.md`
- `play_store_suspicious_engagement.csv`
- `simulation_02_results.md`
- `simulation_03_black_swan_results.md`

**Legal/** (7 files):
- `Stockton_Corrective_Action_Plan.md`
- `Stockton_Follow_Up_Email.md`
- `Stockton_Triple_Constraint_Reaudit.md`
- `Vernen_Federal_Strategy.md`
- `Vernen_LLC_Formation_California_Quickstart.md`
- `Vernen_SAMgov_Prep_Checklist.md`

**Outreach/** (18 files):
- Anthropic pitches ×3 (`Anthropic_Pitch_2026-04-07_NEW.md`, `anthropic_email_phase2_cellular_attestation`, plus prior version)
- `BayLegal_Partnership_*`
- `Business_Loan_Application_*`
- `Vernen_AISIC_Letter_of_Interest.md`
- `Vernen_SBIR_Phase_I_Outline.md`
- `Federal_Grant_Landscape_*`
- `Vernen_Fork_Map_Overview.md`
- `Google_Introduction_*`
- Audio Fork (`*_deployment`, `*_savings`)
- `Competitive_Landscape_*`
- `Economic_Loss_*`
- `Persona_Population_Comparison_*`
- `Platform_Capabilities_Statistical_Profile_*`

**Reports/** (459 files):
- `VERNEN_CITIZENS_COMPLETE_BUILD_REPORT_2026-04-09.md`
- `vernen_evolution_build_2026-04-08/` tree — legal-historiography work on:
  - **California Contractors State License Law 1929** (CSLB origin)
  - **Riley Act 1933**
  - **Field Act 1933**
  - PDFs of 1931 / 1933 / 1935 California statute books, scanned chapter pages
  - leginfo HTML / TXT for current sections
  - `historical_chain.md`, `manifest.json`, `provenance.json`

**Standards/** (3 files):
- `NIST_AI_RMF_MAPPING_2026-04-07.md`
- `Vernen_SSP_NIST_800-53_DRAFT.md`

**Chunk3 adds** (`VernenBackup_2026-04-11/`):
- Statute working dirs: `bp_2234_medical_board`, `civ_1709_deceit`, `civ_1790_song_beverly`, `usc_18_1028a_aggravated_id_theft`, `usc_18_1961_rico`
- Session logs: `project_session_20260410_caselist_build`, `project_session_20260411_criminal_expansion`
- Inner `VernenLegal_Compliance/` snapshot
- 2026-04-11 citizens snapshot (subset of current `WaistMaiLieP-H/citizens`)

### 2.3 What §2 establishes

| Claim | Anchored by |
|---|---|
| The strategic / compliance / outreach build was substantially complete before suspension | Chunk1 timestamp (2026-04-11), 464-file content listing above |
| Anthropic-pitch material existed on disk 5–9 days before suspension | `Anthropic_Pitch_2026-04-07_NEW.md`, `anthropic_email_phase2_cellular_attestation` in Outreach/ |
| Federal-grant posture (SBIR / SAM.gov / AISIC) was in flight | `Vernen_SBIR_Phase_I_Outline.md`, `Vernen_SAMgov_Prep_Checklist.md`, `Vernen_AISIC_Letter_of_Interest.md` |
| NIST AI RMF + 800-53 compliance was being mapped, not adopted post hoc | `NIST_AI_RMF_MAPPING_2026-04-07.md`, `Vernen_SSP_NIST_800-53_DRAFT.md` |
| The Citizens architecture rests on a documented legal-historiography chain (not assertion-only) | 459-file `vernen_evolution_build_2026-04-08/` tree — CSLB 1929, Riley Act 1933, Field Act 1933 |
| Build cadence in early April 2026 was high-throughput, single-author | Session logs `project_session_20260410_caselist_build`, `project_session_20260411_criminal_expansion` |

---

## 3. Forward extension: 2026-05-24 forensic findings

The 2026-05-24 working sessions across two parallel Claude Code terminals produced three artifacts that are currently Desktop-only and are not yet on GitHub. Each is sha256-hashed in its own `MANIFEST.sha256`. This section indexes them and records the findings.

### 3.1 `Desktop/gemini-vernen-extract/` (11 MB)

**What it is:** Extraction of conversation history from both Google accounts (`1978mbc2020@gmail.com`, `michetype78@gmail.com`) — 68 conversations across the two accounts — plus an audit of Google MyActivity timestamps against the originating conversation records.

**Authority for:** Google MyActivity timestamp tampering forensics.

**Key files:**
- `ANOMALY.md` — narrative of the findings
- `EXHIBIT_timestamp_table.{md,csv,json}` — the 40-paradox table
- `MANIFEST.sha256` — hashes of every file in the export
- `MANIFEST.meta.txt`, `MANIFEST.detail.json` — extraction metadata
- `ACCOUNT1_SECURITY_AUDIT.txt`
- `matches.md`
- `_myactivity_sample.json`, `_myactivity_normalized.json`

**Findings recorded:**
- **40 timestamp paradoxes** in MyActivity across the two accounts (events with MyActivity timestamps inconsistent with the corresponding conversation record).
- **4-month gap January–April 2026** in both accounts simultaneously. Two independent accounts with the same 4-month void is not the user's gap; it is a platform-side gap.
- 2 of 4 user-stated architectural concepts (token, blockchain anchoring) are properly represented in GitHub repos; 2 (tether forking, parallelization / 7000 docs/sec) exist only in `verne-case-record` Claude JSONLs and not in any public repo.

### 3.2 `Desktop/Sunday_May_24_Terminal_1_Export/` (5.5 MB)

**What it is:** Full Claude Code session export of the May 24 anomaly investigation terminal (the terminal that produced the Gemini extraction and the MyActivity timestamp audit).

**Authority for:** Forensic record of the anomaly investigation itself — the steps taken, the queries run, the conclusions drawn, and the chain of reasoning.

**Files:**
- `conversation.jsonl` (4.1 MB) — authoritative raw transcript
- `conversation.md` (1.6 MB) — human-readable rendering
- `MANIFEST.sha256` — hashes of both above

### 3.3 `Desktop/Sunday_May_24_Terminal_2_Export/` (2.9 MB)

**What it is:** Full Claude Code session export of the May 24 evidence-cross-reference terminal (session `9044bd4c-9654-48d3-b8d2-fb32ee225614`).

**Authority for:** Gemini ↔ repo cross-reference, Proton rclone diagnosis, the drafting of `PROVENANCE_TIMELINE_2026-04.md`, and the `_COMPLIANCE_STACK.md` un-attributed-Claude-draft discovery.

**Files:**
- `session_9044bd4c.jsonl` (2.5 MB) — authoritative raw transcript
- `conversation_rendered.md` (146 KB) — human-readable rendering
- `tasks/`, `file-history/`, `image-cache/`, `session-env/`, `memory_snapshot/` — supporting state
- `MANIFEST.sha256` — hashes of the authoritative files
- `README.md` — index and integrity statement

**Findings recorded inside this export:**
- **`citizens/_COMPLIANCE_STACK.md`** was committed 2026-04-20 04:26 PDT bundled inside a Family Law Litigator gap-closing commit (`7505236`). Web search returned no public hits; Gemini conversation search returned no proposal; Claude JSONL search confirmed the file existed in the repo before the earliest preserved JSONL. The framing was not authored by the user — the originating session was not preserved.
- **Proton rclone Code 2028** restart-loop diagnosed: the per-address "Allow sign-in" toggle for `michael@vernenlegal.com` (custom-domain address attached to `Michetype78@proton.me`) was reset to OFF after the subscription lapsed and was repaid; cooldown extended on each retry. Distinct from the Anthropic suspension; not a ban.

### 3.4 `Desktop/Monday_May_25_Session_44b4f373_Export/` (this bundle)

**What it is:** Full Claude Code session export of the 2026-05-25 audit + IP-counsel session (this writeup is part of the export).

**Authority for:** The 2026-05-25 audit findings recorded in §2 above; the IP-counsel framing (binding ownership, liability locus, referral list) that closed the session; the conversation-level record of how the writeup was scoped at 17:04Z.

**Files (final once manifest is generated):**
- `session_44b4f373.jsonl` (966 KB) — authoritative raw transcript
- `conversation_rendered.md` (~369 KB) — human-readable rendering
- `PROVENANCE_WRITEUP_2026-05-25.md` (this file)
- `README.md` — index
- `MANIFEST.sha256` — hashes of all of the above

---

## 4. Distribution

Per user instruction at 2026-05-25 17:06:59Z (session 44b4f373, message 297 of the transcript): *"Github and For usb thumbdrive and 1 for email so I can send it to someone for keeping."*

| Channel | Destination | Rationale |
|---|---|---|
| **Public GitHub** | `WaistMaiLieP-H/citizens` (root) | Matches placement of `PROVENANCE_TIMELINE_2026-04.md`. Public is the chosen posture: "I seemingly need as many witnesses as possible, because someone is erasing parts of my [record]" (user, 17:08:29Z). |
| **USB** | `/media/vernenlegal/USB/Vernen/Evidence_2026-05-25/` | Local tamper-evident mirror. Pattern matches `Evidence_2026-05-24/`. |
| **Email** | `Michael@vernenlegal.com` | Portable archive, forward to third party for keeping. Bundle is a `.zip` of the export folder. |

The three copies are byte-identical; SHA-256s in `MANIFEST.sha256` permit independent verification by any recipient.

---

## 5. What the writeup does and does not claim

**Does claim, anchored above:**
- A 464-file pre-suspension build state existed on disk on 2026-04-11 that did not reach GitHub before 2026-04-16.
- The build included Anthropic-facing outreach material dated 2026-04-07 — nine days before the suspension event.
- Two independent Google accounts share a 4-month MyActivity gap January–April 2026 (40-paradox table on disk).
- `_COMPLIANCE_STACK.md` was committed to the public repo without a preserved authoring session.
- The full forensic chain (Gemini extraction, repo cross-reference, MyActivity audit, Proton diagnosis, this audit) is recorded in three Desktop exports, each sha256-hashed.

**Does not claim:**
- Causation between any single Anthropic action and any single state of the record.
- That any particular Anthropic employee, system, or policy is responsible for any specific anomaly.
- That the MyActivity gap is necessarily tampering rather than a platform issue. It is documented as paradox; explanation is open.
- That the suspension was retaliatory. The suspension is documented; its cause is documented as not specified by Anthropic.

The writeup's job is to fix the record in a form that survives later contestation. Interpretation is left to whoever holds the record.

---

## 6. Integrity

Recipients can verify integrity by:

1. Reading this file's SHA-256 from `MANIFEST.sha256` (in the same bundle).
2. Pulling the public commit from `WaistMaiLieP-H/citizens` and computing `sha256sum` locally.
3. Comparing against the USB copy's `MANIFEST.sha256`.
4. Comparing against the emailed `.zip`'s `MANIFEST.sha256` (the zip contains its own copy of the manifest plus the files).

Each of the three copies is independently verifiable. Editing one does not edit the others.

---

**End of writeup.**
