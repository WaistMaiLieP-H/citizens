# CA_Family_Law_Litigator — Actor Catalog

**Purpose:** Structured records for every named human actor in the family-law case file. Each actor has a JSON file with role, credentials, case involvement, risk assessment, outstanding investigations, and source citations.

**Filed:** 2026-04-08
**Citizen:** CA_Family_Law_Litigator
**Tether:** `../tether.json` (the binding manifest)

## Actors currently in catalog

| Actor | Role | Risk | File |
|---|---|---|---|
| Olga Paredes, Ph.D. | Child Custody Mediator (2009) | MEDIUM | [paredes_olga.json](paredes_olga.json) |
| Sala Ajaniku | Child Custody Mediator (2010) | **CRITICAL** | [ajaniku_sala.json](ajaniku_sala.json) |
| David Alan Ditsworth, MD | SSA Disability Report Author | HIGH | [ditsworth_david.json](ditsworth_david.json) |
| Trina Thompson | Judge (Alameda, 2009) | LOW | [thompson_trina_judge.json](thompson_trina_judge.json) |
| Paul A. Delucchi | Judge (Alameda, 2010) | HIGH | [delucchi_paul_judge.json](delucchi_paul_judge.json) |
| Patrick Wiita, Dr. | Competency Evaluator | HIGH | [wiita_patrick.json](wiita_patrick.json) |
| Christina Marie Cerretani | Opposing party (16-year pattern) | OPPOSING PARTY | [cerretani_christina.json](cerretani_christina.json) |
| Ann Hillberg / Ann Marie Packard | Mother of Christina; orchestrator | ORCHESTRATOR | [hillberg_ann.json](hillberg_ann.json) |

## Schema

Each actor record contains:
- `actor_id` — canonical identifier
- `canonical_name`, `aliases`
- `role`
- `professional_identity` — title, education, employer, credential claims
- `credential_verification` — what's verified, what's not, what's needed
- `case_involvement` — list of actions in specific cases with dates and outcomes
- `risk_level` and `risk_basis`
- `outstanding_investigations` — open questions about this actor with unblock paths
- `standards_governing_this_actor` — corpus standards that apply
- `source_citations` — where this information comes from
- `filed_at_utc`

## Outstanding catalog work

- Add records for additional actors as the case file is more deeply audited:
  - Other judges across the 16-year case
  - Other mediators
  - Public defenders / appointed counsel
  - CPS workers
  - Court-connected staff
  - Police officers named in specific reports
  - Process servers (relevant to the 2010 grandparent visitation never-served issue)
  - Witness names from the case file
- Verify the actor records against the source citations regularly
- When an outstanding investigation resolves, update the record and surface the resolution
