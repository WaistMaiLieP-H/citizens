# CA_Family_Law_Litigator — Outstanding Investigations

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
