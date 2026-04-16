#!/usr/bin/env python3
"""
_populate_outstanding_investigations.py

Generates 11 individual investigation records for the
CA_Family_Law_Litigator Citizen, plus a README index. Each record is the
structured form of one open investigative item from tether.json.

Schema per record:
  - investigation_id
  - question — what we don't know
  - context — why it matters
  - unblock_path — what would resolve it
  - who_can_answer
  - related_actors
  - related_cases
  - related_standards
  - priority
  - status
  - filed_at_utc
"""

import json
from pathlib import Path

NOW = "2026-04-08T19:25:00Z"
BASE = Path("${citizens}/CA_Family_Law_Litigator/outstanding_investigations")


INVESTIGATIONS = [
    {
        "filename": "01_opd_records_pickup_audit.json",
        "data": {
            "investigation_id": "opd_records_pickup_audit",
            "title": "Re-audit each filing that relied on a 2009 OPD report against the actual OPD records system",
            "question": "For each filing in the case file that cited an Oakland Police Department report from 2009, does the cited report actually exist in OPD's records system as confirmed by the October 2025 OPD records pickup?",
            "context": "Per project_christina_pattern.md, the steward picked up OPD records in October 2025 and confirmed that only 2 reports exist for the entire 2009 situation. The 6/2/2009 5150 incident report (the actual event where Christina pulled a 10-inch kitchen knife) is NOT among them. The 6/11/2009 OPD report 09-040089 (which Christina has used to frame the TRO and 5150 evaluation as the steward 'calling police and saying I was suicidal') exists but has POST violations caught by the Vernen overlay rule POST-002B. Combined, this means: the events that hurt Christina's case are missing from OPD records; the events that help her narrative exist on paper but should not survive POST scrutiny. Every filing that cited a 2009 OPD report needs to be re-audited against the actual records.",
            "unblock_path": "Cross-reference the October 2025 OPD records pickup against every case-file filing that cites an OPD report. For each citation, confirm whether the cited report exists in the OPD records system. Document each finding.",
            "who_can_answer": "The steward (Michael Hartmann) — he holds the October 2025 OPD records pickup. Cross-reference is a manual desk audit.",
            "related_actors": ["cerretani_christina", "hillberg_ann"],
            "related_cases": ["RF09456481", "RF09459897", "RF09470833"],
            "related_standards": ["CA_FAMILY_CODE_3011_BEST_INTEREST", "CA_FAM_6203_DVPA_ABUSE_DEFINITION", "CA_EVIDENCE_1280_OFFICIAL_RECORDS"],
            "priority": "CRITICAL",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "02_ajaniku_pra_request.json",
        "data": {
            "investigation_id": "ajaniku_pra_request",
            "title": "Public Records Act request to Alameda County Superior Court for Sala Ajaniku employment, qualifications, and credential records",
            "question": "Does Alameda County Superior Court possess any documentary record of Sala Ajaniku's credentials, qualifications, employment status, hiring documentation, or training certificates?",
            "context": "Per the credential audit (CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md), Sala Ajaniku has zero verifiable credentials in any public database, professional directory, or licensing board. Her September 2010 mediator recommendation in RF09456481 reversed the prior protective DVRO and granted Christina unsupervised visitation. Family Code § 3164(b) requires every mediator to meet § 1815 minimum qualifications. § 1815(a)(7) requires DV training under § 1816. § 1816(g) requires court notification or certificate attachment. Without any documentary support, Ajaniku's appointment was statutorily defective.",
            "unblock_path": "File a California Public Records Act (Gov. Code § 7920.000 et seq.) request with Alameda County Superior Court Family Court Services seeking: (1) Sala Ajaniku's complete employment file; (2) any credential verification records on file at the time of her September 2010 mediator assignment; (3) any § 1816 DV training certificates filed by Ajaniku; (4) the original mediation report from 09/02/2010 with any credentials listed; (5) the institutional credential-verification process that should have applied to her appointment.",
            "who_can_answer": "Alameda County Superior Court — Public Records Act compliance officer",
            "related_actors": ["ajaniku_sala", "delucchi_paul_judge"],
            "related_cases": ["RF09456481"],
            "related_standards": ["CA_FAM_3164_MEDIATOR_QUALIFICATIONS", "CA_FAM_1815_COUNSELOR_QUALIFICATIONS", "CA_FAM_1816_MEDIATOR_DV_TRAINING"],
            "priority": "CRITICAL",
            "status": "OPEN — PRA REQUEST PENDING DRAFTING",
            "next_step": "Draft the PRA request as the next concrete pre-filing action; this is the highest-priority unblock for the Ajaniku audit",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "03_paredes_license_verification.json",
        "data": {
            "investigation_id": "paredes_license_verification",
            "title": "Direct DCA license search for Olga Paredes; California Board of Psychology contact for license verification",
            "question": "Did Olga Paredes hold a valid California Board of Psychology license in July 2009? What is her license number? What degree does she actually hold from the Wright Institute?",
            "context": "Per the credential audit, Paredes claims a Ph.D. from the Wright Institute, but the Wright Institute grants PsyD degrees, not Ph.D. The credential audit found no California Board of Psychology license number for her through web search. In California, one cannot use the title 'forensic psychologist' (which Paredes claims on LinkedIn) without a Board of Psychology license per Bus. & Prof. Code § 2903.",
            "unblock_path": "(1) Direct DCA License Search at search.dca.ca.gov for 'Olga Paredes'; (2) phone California Board of Psychology at 916-574-7720 for license verification; (3) contact Wright Institute Registrar's office for degree-type verification.",
            "who_can_answer": "California Board of Psychology; Wright Institute Registrar; California Department of Consumer Affairs",
            "related_actors": ["paredes_olga"],
            "related_cases": ["RF09456481"],
            "related_standards": ["CA_FAM_3164_MEDIATOR_QUALIFICATIONS", "CA_FAM_1815_COUNSELOR_QUALIFICATIONS", "CA_FAM_1816_MEDIATOR_DV_TRAINING"],
            "priority": "MEDIUM",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "04_conservatorship_existence_search.json",
        "data": {
            "investigation_id": "conservatorship_existence_search",
            "title": "Probate court docket searches across Contra Costa, Alameda, San Francisco, and adjacent counties for any conservatorship petition or order naming Michael Hartmann",
            "question": "Has any conservatorship been opened on the steward in any California county, at any time? If yes, what is the case number, court, petitioner, and date of order?",
            "context": "Per project_conservatorship_discovery.md and project_conservatorship_breakthrough.md, the steward has discovered evidence consistent with a long-standing conservatorship arrangement involving him. If such a conservatorship exists as a formal court order, it would be the root mechanism behind multiple harms documented in the case file (medical records access, financial control, surveillance). Probate Code § 1801(e) requires clear-and-convincing evidence for conservatorship appointment. CMIA § 56.10(c)(12) authorizes probate court investigators to obtain medical records without the patient's consent during a conservatorship investigation — which would explain how the steward's medical records were accessed without his knowledge.",
            "unblock_path": "Search the probate court dockets in: Contra Costa County Superior Court, Alameda County Superior Court, San Francisco County Superior Court, San Mateo County Superior Court, Solano County Superior Court, Marin County Superior Court, and any other adjacent county. California probate court records are public records and can be searched by name. Some counties offer online docket search; others require in-person visits to the clerk's office.",
            "who_can_answer": "California county Superior Court clerks (probate division)",
            "related_actors": ["hillberg_ann", "wiita_patrick"],
            "related_cases": [],
            "related_standards": ["CA_PROB_1801_CONSERVATORSHIP_APPOINTMENT", "CA_CIV_56_10_CMIA"],
            "priority": "CRITICAL",
            "status": "OPEN",
            "load_bearing_significance": "This is the root investigation. If a conservatorship exists, it explains the medical records access, the financial control, the surveillance, and possibly the family-court orchestration. Establishing existence/nonexistence is the foundation for everything downstream.",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "05_cmia_disclosure_log_subpoenas.json",
        "data": {
            "investigation_id": "cmia_disclosure_log_subpoenas",
            "title": "Subpoena CMIA § 56.10(c)(12) disclosure logs from every medical provider that has held the steward's records",
            "question": "Has any medical provider that held the steward's records ever made a § 56.10(c)(12) disclosure to a probate court investigator, probation officer, or domestic relations investigator? If yes, when, to whom, in connection with what proceeding?",
            "context": "CMIA § 56.10(c)(12) explicitly authorizes disclosure of medical information to a probate court investigator in a conservatorship proceeding under Probate Code § 1400, OR to a probate court investigator, probation officer, or domestic relations investigator engaged in determining initial or continuing guardianship. This is the lawful mechanism by which a covert conservatorship investigation could obtain the steward's medical records without his consent. Each (c)(12) disclosure should have generated a paper trail at the disclosing provider — a written request from the investigator and a logged disclosure entry. The steward's CMIA standard manifest (cross-tethered to this Citizen) flags this as a CRITICAL audit item.",
            "unblock_path": "Identify every medical provider, health plan, hospital, clinic, lab, and pharmacy that has held the steward's medical records since (approximately) 2009. For each, prepare and serve a subpoena duces tecum requesting CMIA disclosure logs and any (c)(12) disclosure records to a probate court investigator, probation officer, or domestic relations investigator.",
            "who_can_answer": "Each medical provider's privacy officer / records custodian",
            "related_actors": ["wiita_patrick"],
            "related_cases": [],
            "related_standards": ["CA_CIV_56_10_CMIA", "CA_PROB_1801_CONSERVATORSHIP_APPOINTMENT"],
            "priority": "CRITICAL",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "06_mediator_switch_reason.json",
        "data": {
            "investigation_id": "mediator_switch_reason",
            "title": "PRA request to Alameda Family Court Services for the documented reason for switching mediators between July 2009 (Paredes) and September 2010 (Ajaniku)",
            "question": "Why was Olga Paredes not re-assigned as the mediator for the September 2, 2010 hearing in RF09456481? Was she unavailable, recused, requested by a party, or simply not re-assigned? Was there a documented institutional reason?",
            "context": "Per the credential audit, San Francisco Superior Court's mediation guidelines reflect the widely recognized best practice that mediator continuity within the same case serves the interests of the children and parties — maintaining institutional knowledge, preventing inconsistent assessments, accountability for prior recommendations. The switch from Paredes (whose recommendation was protective) to Ajaniku (whose recommendation removed protection) is doctrinally anomalous, particularly because the new mediator had zero verifiable credentials.",
            "unblock_path": "Public Records Act request to Alameda County Family Court Services seeking: (1) any institutional record explaining the mediator change between 2009 and 2010 in RF09456481; (2) the assignment policy in effect at the time; (3) whether mediator continuity was the default and what the exceptions were; (4) any party request for a change of mediator.",
            "who_can_answer": "Alameda County Family Court Services / Alameda County Superior Court",
            "related_actors": ["paredes_olga", "ajaniku_sala", "thompson_trina_judge", "delucchi_paul_judge"],
            "related_cases": ["RF09456481"],
            "related_standards": ["CA_FAM_3164_MEDIATOR_QUALIFICATIONS"],
            "priority": "HIGH",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "07_marin_august_2025_hearing.json",
        "data": {
            "investigation_id": "marin_august_2025_hearing",
            "title": "Locate and obtain the Marin County 8/5/2025 hearing document in FL0002067",
            "question": "What does the Marin County 8/5/2025 hearing record show? Did the judge actually refuse to let the steward speak, as project_familylaw_orchestration.md states? What was the formal basis for Marin assuming jurisdiction over Cole?",
            "context": "Per project_familylaw_orchestration.md, Marin assumed jurisdiction over Cole at the 8/5/2025 hearing and the judge refused to let Michael speak. The hearing document is not yet in the case file per the existing memory. This is a load-bearing record for the UCCJEA jurisdictional challenge.",
            "unblock_path": "Request the hearing transcript and minute order from Marin County Superior Court FL0002067. Also obtain the audio recording if available.",
            "who_can_answer": "Marin County Superior Court clerk; court reporter",
            "related_actors": ["cerretani_christina", "hillberg_ann"],
            "related_cases": ["FL0002067"],
            "related_standards": ["CA_FAMILY_CODE_3011_BEST_INTEREST", "CA_FAM_3020_CUSTODY_POLICY"],
            "priority": "HIGH",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "08_alameda_solano_fee_waiver_filing_error.json",
        "data": {
            "investigation_id": "alameda_solano_fee_waiver_filing_error",
            "title": "Document and obtain the 2025 fee waiver 'filing error' that blocked the Alameda → Solano transfer",
            "question": "What was the specific 'filing error' on Michael's fee waiver in 2025 that prevented the transfer from Alameda to Solano? Was the error his, the court's, or the clerk's? What were the consequences?",
            "context": "Per project_familylaw_orchestration.md, the 2025 jurisdictional trap involved a fee waiver 'filing error' that blocked the transfer from Alameda to Solano. Alameda bounced Michael to Solano; Solano said no transfer received. Christina then took Cole and went to Marin. The fee waiver issue was structurally critical to the jurisdictional flip.",
            "unblock_path": "Request from Alameda County Superior Court: the fee waiver application Michael filed in 2025; any clerk-generated rejection or correction notice; any internal memo about the error. Cross-reference against the dates of the dismissal (6/25/2025) and the transfer.",
            "who_can_answer": "Alameda County Superior Court clerk's office",
            "related_actors": [],
            "related_cases": ["25FL122591", "RF10508853"],
            "related_standards": [],
            "priority": "HIGH",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "09_benicia_pd_call_recordings.json",
        "data": {
            "investigation_id": "benicia_pd_call_recordings",
            "title": "Obtain Benicia PD call recording for the 2025-07-14 to 2025-07-17 calls Michael made when Cole was missing",
            "question": "Are there preserved recordings of the Benicia PD calls Michael made between 7/14 and 7/17, 2025 trying to report Cole missing? What do the recordings show about how the calls were handled?",
            "context": "Per project_familylaw_audit.md and project_familylaw_orchestration.md, Michael called Benicia PD for 4 days starting 7/14/2025. No officers responded and no reports were taken. On 7/17/2025 Benicia PD finally arrived — to serve the Marin restraining order on Michael, not to take his missing-Cole report. Per project_familylaw_orchestration.md: 'Benicia PD recording: not yet scanned/uploaded.'",
            "unblock_path": "Public Records Act request to Benicia PD for: (1) all 911 and dispatch call recordings involving Michael Hartmann between 7/14/2025 and 7/17/2025; (2) all dispatch logs for those dates referencing him or Cole; (3) any officer notes or report drafts from the period. Note: 911 call recordings typically have 6-12 month retention; if not preserved by now, they may already be destroyed.",
            "who_can_answer": "Benicia Police Department records custodian",
            "related_actors": [],
            "related_cases": ["FL0002067"],
            "related_standards": ["CA_VEH_2800_OBEY_PEACE_OFFICER"],
            "priority": "HIGH",
            "status": "OPEN — TIME-SENSITIVE (recordings may have been destroyed by now)",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "10_michael_dual_filing_status.json",
        "data": {
            "investigation_id": "michael_dual_filing_status",
            "title": "Locate documents showing Michael as both petitioner AND respondent with fees charged both ways in the same proceeding",
            "question": "In which case(s) was Michael formally listed as both the petitioner and the respondent? Were filing fees charged to him in both capacities? What were the procedural consequences?",
            "context": "Per the existing memory entry list of critical missing documents (project_familylaw_orchestration.md): 'Documents showing Michael as both petitioner and respondent with fees charged both ways.' This is a structural irregularity that suggests either a clerical error, a deliberate misclassification, or a procedural manipulation. It may also explain the fee waiver issue investigation #08.",
            "unblock_path": "Search the case file for any filing in which Michael appears as both petitioner and respondent. Cross-reference against fee receipts. The 2025 sequence of cases (25FL122591 and 25FL125059) is the most likely location.",
            "who_can_answer": "The steward; the case file itself",
            "related_actors": [],
            "related_cases": ["25FL122591", "25FL125059", "RF10508853"],
            "related_standards": [],
            "priority": "MEDIUM",
            "status": "OPEN",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "11_carrier_communications_device_proximity.json",
        "data": {
            "investigation_id": "carrier_communications_device_proximity",
            "title": "Carrier communications about device access requiring physical proximity",
            "question": "What carrier communications exist documenting device access requiring physical proximity? Which devices? Which carriers? What was the technical nature of the access requirement?",
            "context": "Per the existing memory list of critical missing documents (project_familylaw_orchestration.md and project_communications_fraud.md), there are carrier communications about device access requiring physical proximity. This is structurally consistent with the Ryan McClaran IT investigation (project_ryan_mcclaran_it.md) on SIM swaps and proxy communication networks. The physical-proximity requirement may indicate a SIM-tied authentication mechanism.",
            "unblock_path": "Identify the specific carriers and devices involved. Request from each carrier: (1) account access logs for the relevant period; (2) any SIM swap, port-out, or device transfer records; (3) any technical notes about authentication requirements. PRA equivalents are limited for private carriers, but subpoena via litigation may be available.",
            "who_can_answer": "The carriers (AT&T, T-Mobile, Verizon, etc., depending on the steward's device history)",
            "related_actors": [],
            "related_cases": [],
            "related_standards": [],
            "priority": "MEDIUM",
            "status": "OPEN",
            "cross_reference": "Connects to project_communications_fraud.md and project_ryan_mcclaran_it.md",
            "filed_at_utc": NOW
        }
    },
]


README = """# CA_Family_Law_Litigator — Outstanding Investigations

**Purpose:** Open investigative items the Citizen needs answered to do its work. Each item is a discrete record with question, context, unblock path, who can answer, related actors/cases/standards, priority, and status.

**Filed:** 2026-04-08
**Citizen:** CA_Family_Law_Litigator
**Source:** Items enumerated in `tether.json` and surfaced by the deepened standards' steward audits

## Investigations currently open

| # | Title | Priority | Status |
|---|---|---|---|
| 01 | OPD records pickup audit (re-audit each filing against actual OPD records) | **CRITICAL** | OPEN |
| 02 | Sala Ajaniku PRA to Alameda County Superior Court | **CRITICAL** | OPEN — pending drafting |
| 03 | Olga Paredes DCA license verification | MEDIUM | OPEN |
| 04 | Conservatorship existence search across counties | **CRITICAL** | OPEN — load-bearing root |
| 05 | CMIA § 56.10(c)(12) disclosure log subpoenas | **CRITICAL** | OPEN |
| 06 | Mediator switch reason PRA | HIGH | OPEN |
| 07 | Marin County 8/5/2025 hearing document | HIGH | OPEN |
| 08 | Alameda → Solano fee waiver filing error | HIGH | OPEN |
| 09 | Benicia PD call recordings (7/14-17/2025) | HIGH | **OPEN — TIME-SENSITIVE** (911 recordings may have been destroyed) |
| 10 | Michael as both petitioner AND respondent | MEDIUM | OPEN |
| 11 | Carrier communications about device access | MEDIUM | OPEN |

## Critical investigations summary

The four CRITICAL investigations are the structural backbone of the case theory:

1. **OPD records pickup audit** (#01) — closes the gap between what Christina's filings claim and what OPD's records actually contain. The steward already has the October 2025 records pickup; the audit is a desk-review cross-reference.

2. **Sala Ajaniku PRA** (#02) — the unblock for the load-bearing Family Code § 3164 / § 1815 / § 1816 audit. Without the PRA results, the credential void argument rests on the absence of evidence. With the PRA results, it rests on the affirmative evidence that no credential records exist in the institution that would have created them.

3. **Conservatorship existence search** (#04) — the root mechanism investigation. If a conservatorship exists, it explains the medical-records access, the financial control, and possibly the family-court orchestration. Establishing existence/nonexistence is the foundation for everything downstream.

4. **CMIA § 56.10(c)(12) disclosure logs** (#05) — independent verification path for the conservatorship discovery. Even if the probate docket searches turn up nothing, a (c)(12) disclosure log entry at any medical provider would establish that a probate court investigator was active. The logs at each provider are a parallel investigation to the docket searches.

## Schema

Each investigation record contains:
- `investigation_id` — canonical identifier
- `title`, `question`, `context`
- `unblock_path` — what would resolve it
- `who_can_answer`
- `related_actors`, `related_cases`, `related_standards` (as lists)
- `priority` (CRITICAL / HIGH / MEDIUM / LOW)
- `status` (OPEN / IN PROGRESS / RESOLVED)
- `filed_at_utc`

## Updating an investigation

When new information arrives that resolves or advances an investigation, update the record's `status` field, add a `resolution_summary`, and link to the artifact that resolved it. Do not delete records — the historical state is part of the audit trail.
"""


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    written = []
    for entry in INVESTIGATIONS:
        path = BASE / entry["filename"]
        path.write_text(json.dumps(entry["data"], indent=2))
        json.loads(path.read_text())
        written.append(path)
    (BASE / "README.md").write_text(README)
    print(f"Wrote {len(written)} investigation records + README")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
