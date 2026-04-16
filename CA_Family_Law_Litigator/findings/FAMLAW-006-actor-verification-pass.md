# FAMLAW-006 — NPI Registry Verification Pass on Actors (2026-04-16)

**Finding ID:** FAMLAW-006
**Citizen:** CA_Family_Law_Litigator
**Status:** PUBLISHED — HERALD-certified 2026-04-16
**Severity:** HIGH (two material discrepancies)
**Workstream:** Verification pass per Steward mission 2026-04-16
**Scope:** All non-judge actors in `${citizens}/CA_Family_Law_Litigator/actors/` plausibly within the healthcare-provider universe, plus ICD-10 audit of findings and cases.

---

## Methodology

1. Read every actor JSON in `actors/` and every finding (FAMLAW-001..005). Identified five actors plausibly within healthcare: Wiita (MD competency evaluator), Ditsworth (MD SSA consultant), Paredes (claimed Ph.D. psychologist/mediator), Ajaniku (mediator — credentials unknown), Hillberg (dispatcher 2008-2015 → Napa State Hospital 2015+, non-clinical but state-hospital-adjacent).
2. For each, searched CMS NPPES NPI Registry by `first_name` + `last_name`, sometimes relaxing `state` to catch out-of-state primary licensure.
3. Where a match was found, retrieved full NPI record via `npi_lookup` for complete credential + license data including all taxonomy records and secondary state licenses.
4. Scanned `findings/` and `cases/` for any ICD-10-CM or ICD-10-PCS references. None found — skipped ICD-10 validation for this pass.
5. Skipped the two judges (Delucchi, Thompson) — out of scope for NPPES.
6. Cross-checked Christina Cerretani (opposing party, non-provider) — not searched.

## Actor-by-actor findings

### 1. Patrick Wiita, MD — `wiita_patrick.json`

- **Role in case:** Court-appointed competency evaluator, Contra Costa 04-23-01959.
- **NPI found?** YES — two candidates surfaced; one is a high-confidence match.
  - **NPI 1841558772** — PATRICK GEORGE WIITA, MD. Enumerated 2012-04-28, last updated 2020-04-06. Status: Active.
  - Rejected: NPI 1417166208 (Patricia S. Wiita, NP, Michigan) — wrong sex, wrong state, wrong profession.
- **Taxonomy:** `2084P0800X` — Psychiatry & Neurology, Psychiatry (primary).
- **Primary license state:** **South Carolina** — SC License #82143 (primary practice: 33 Office Park Rd Ste A-166, Hilton Head Island, SC 29928; phone 843-802-9030).
- **Secondary license (California):** CA License #a124938, same taxonomy (Psychiatry & Neurology, Psychiatry), marked NON-primary.
- **Secondary CA practice locations:**
  - 2121 W Temple St, Bldg ABC, Los Angeles, CA 90026 (213-260-7600) — this is the LAC+USC Medical Center / Los Angeles County-USC area, downtown LA.
  - 10850 Wilshire Blvd Ste 850, Los Angeles, CA 90024 (424-280-2265) — Westwood, West LA.
- **FLAGS:**
  1. **Geography mismatch.** Primary practice is Hilton Head Island, SC. All listed CA practice addresses are in Los Angeles County. The case is **Contra Costa** County (San Francisco Bay Area — ~400 miles north of LA, and across a continent from SC). Competency evaluation by a psychiatrist whose CA practice locations are all in LA County, for a Contra Costa criminal proceeding, warrants explanation — was the evaluation in-person in Contra Costa, in-person in LA, telehealth, or records-review only? This bears directly on FAMLAW-002's § 3118/§ 730 appointment-procedure defect and the Bus. & Prof. Code § 2290.5 telehealth scope point already flagged.
  2. **Primary vs. secondary licensure.** His primary taxonomy license is SC, not CA. In California an out-of-state-primary MD can practice under a CA secondary license but the appointment order, billing, and the Evid. Code § 720 foundational showing must track the CA license # — if the MC-350 or equivalent appointment cites the SC license or no license, that is a § 720 defect independent of the FAMLAW-002 findings.
  3. **Actor record inconsistency.** `wiita_patrick.json` lists specialty as "TBD — to be confirmed." NPPES now confirms **Psychiatry**. That's compatible with competency evaluation per Pen. Code § 1369, but the specialty field should be updated by CUSTOS in the next tether pass.
- **Outstanding investigation unblocked:** `wiita_specialty` — NPPES confirms Psychiatry. `wiita_evaluation_circumstances` — still open; needs the evaluation report.

### 2. David Alan Ditsworth, MD — `ditsworth_david.json`

- **Role in case:** SSA disability claim consultant (January 3, 2023 report used to deny claim).
- **NPI found?** YES — **NPI 1376685420** (already in actor record; verified directly).
- **Taxonomy:** `208600000X` — **Surgery** (generic Surgery taxonomy, not the more specific `207T00000X` Neurological Surgery).
- **License:** **CA License G29004** (active; primary practice: 920 S Robertson Blvd, Los Angeles, CA 90035; phone 310-551-0690).
- **Status:** Active. Enumerated 2007-02-13; last updated 2007-07-08 — record has not been updated in nearly 19 years.
- **FLAGS:**
  1. **Taxonomy mismatch with actor record.** Actor record asserts "Neurological Surgery (board-certified)." NPPES primary taxonomy is the generic **Surgery** (208600000X) — NOT **Neurological Surgery** (207T00000X). This does not itself defeat neurosurgery credentialing (ABNS certification is separate from NPPES taxonomy self-report), but it means the NPPES record does not self-identify him as a neurosurgeon. For FAMLAW-like SSA specialty-mismatch analysis, the NPPES taxonomy is what CMS publishes — a general "Surgery" taxonomy is an even weaker match to SSA disability review of spine/pain conditions than "Neurological Surgery" would have been. This strengthens FAMLAW's existing "wrong specialty" theory on SSA POMS DI 24501.001.
  2. **Stale record.** Record has not been updated since 2007-07-08. The ~19-year gap means the current license status and current practice configuration need independent verification at mbc.ca.gov. The `ditsworth_mbc_license` outstanding investigation is now partially unblocked (G29004 is the number) but the live-status check remains open.
  3. **Address confirmed.** 920 S Robertson Blvd, Los Angeles — this is the Beverly Hills adjacent "Back Institute Surgery Center" / elective-surgery practice context already identified in the actor record.

### 3. Olga Paredes, Ph.D. — `paredes_olga.json`

- **Role in case:** Court-connected child custody mediator, Alameda Family Court Services, 2009 recommendation in RF09456481.
- **NPI found?** **NO direct match in California.** A single NPPES record surfaced nationally — NPI 1992984934 (OLGA LUCIA PAREDES, Family Nurse Practitioner, 325 9th Ave Seattle WA) — **this is not the subject.** Different profession (FNP, not psychologist), different state (WA, not CA).
- **Interpretation:** NPPES is US-only and covers healthcare providers who bill via NPI. **Psychologists licensed in California by the Board of Psychology frequently do NOT enumerate for an NPI** if they do not bill Medicare/Medicaid/most private insurance — NPI is not legally required for all licensed psychologists, only for those participating in HIPAA-covered transactions. Absence from NPPES is NOT probative of "not a psychologist."
- The load-bearing credential question for Paredes remains: Board of Psychology license # and status in July 2009, and the Ph.D. vs. PsyD Wright-Institute degree discrepancy. Neither is answerable through NPPES.
- **FLAGS:** None from NPPES. Outstanding investigations `paredes_dca_search` and `paredes_wright_institute` remain the operative unblocks — they are DCA / Board of Psychology / registrar questions, not NPPES questions.

### 4. Sala Ajaniku — `ajaniku_sala.json`

- **Role in case:** Court-connected child custody mediator, Alameda Family Court Services, 2010-09-02 recommendation in RF09456481.
- **NPI found?** **NO.** Zero results for "Sala Ajaniku" in NPPES (any state).
- **Interpretation:** Consistent with prior-documented "zero professional presence across 8 public licensing/directory sources" (per actor record). A court-connected mediator is not necessarily enumerated for an NPI — mediators qualified under Fam. Code §§ 3164/1815 do not bill via NPI unless they also provide clinical services. Absence from NPPES does not by itself disqualify a court mediator. But NPPES absence combined with DCA-license absence, BBS-license absence, Board-of-Psychology-license absence, and zero LinkedIn/directory presence is an accumulating void consistent with the "CRITICAL — zero verifiable professional presence" finding already on record.
- **FLAGS:** No new NPPES-derived flag. The Ajaniku credential void is a `ajaniku_pra` problem (Alameda County PRA request), not an NPPES problem.

### 5. Ann Hillberg — `hillberg_ann.json`

- **Role in case:** Orchestrator (mother of Christina); state emergency-dispatcher 2008-2015 (SURCOMM/CENCOMM/NORCOM); transferred to Napa State Hospital 2015+.
- **NPI search:** Not performed. Her documented roles (dispatcher, state-hospital non-clinical employee) are not healthcare-provider roles. If she holds an unknown clinical role at Napa State Hospital that would warrant NPPES search, that is an `hillberg_napa_state_hospital` outstanding-investigation question answerable by PRA to Napa State Hospital HR, not by NPPES. Skipping NPPES for Hillberg at this pass is consistent with `feedback_agent_domain_boundaries.md` — staying in the family-law / mediator / evaluator lane.

### 6. Christina Cerretani — not searched

- Non-provider opposing party.

## ICD-10 pass

- Grep of `findings/` and `cases/` for ICD-10-CM / ICD-10-PCS code patterns (`F\d{2}\.`, `Z\d{2}\.`, `R\d{2}\.`, `T\d{2}\.`, "ICD") returned no substantive matches (only hits were unrelated HTML line references in standards/ corpus, out of scope).
- No ICD-10 validation performed at this pass. If a future Wiita-evaluation-report or Ditsworth-SSA-report acquisition surfaces coded diagnoses, that is a new workstream.

## Aggregate flags (new, this pass)

| # | Flag | Actor | Severity | Route |
|---|---|---|---|---|
| F-006-01 | Wiita's primary license state is SC, not CA; his CA practice addresses are all LA County; case is Contra Costa. Evaluation-modality (in-person vs. telehealth) and appointment-order licensure match become load-bearing. | wiita_patrick | HIGH | Cross-tethered into FAMLAW-002 (§ 3118/§ 720/§ 2290.5) |
| F-006-02 | Ditsworth NPPES taxonomy is generic "Surgery" (208600000X), not "Neurological Surgery" (207T00000X); this strengthens SSA specialty-mismatch theory. | ditsworth_david | MEDIUM | Fold into any SSA disability appeal / § 1983 pleading on the SSA denial |
| F-006-03 | Ditsworth NPPES record last updated 2007-07-08 — 19-year staleness; live mbc.ca.gov check still required. | ditsworth_david | LOW | Add to `ditsworth_mbc_license` outstanding |
| F-006-04 | Paredes absence from NPPES is not probative; DCA / Board of Psychology remains the operative channel. | paredes_olga | INFO | No change to existing investigation chain |
| F-006-05 | Ajaniku absence from NPPES is consistent with but does not add to the prior "zero professional presence" finding; PRA route unchanged. | ajaniku_sala | INFO | No change |

## Cross-reference into existing findings

- **FAMLAW-002 (Wiita fraud):** F-006-01 is substantive. Add to provenance chain: "NPPES confirms Psychiatry specialty (appropriate for § 1368 competency evaluation) but primary license is SC; CA-secondary license + LA-only CA practice addresses creates a modality/scope question for a Contra Costa appointment — goes directly to the § 720 / § 3118 defect theory."
- **FAMLAW-005 (orchestration):** No NPPES-derived change.

## Remedy — near-term

1. CUSTOS next pass: update `wiita_patrick.json` — specialty "Psychiatry" confirmed via NPPES 1841558772; primary license SC/82143; secondary CA/a124938.
2. CUSTOS next pass: update `ditsworth_david.json` — NPPES taxonomy correction ("Surgery" not "Neurological Surgery" per NPPES self-report).
3. Add F-006-01 as a facts-paragraph to FAMLAW-002 when that finding is next revised.
4. No changes to standards/ or tether.json by HERALD (per mission scope).

## Provenance

| Evidence | Source |
|---|---|
| NPI 1376685420 record | CMS NPPES API, retrieved 2026-04-16 via mcp__claude_ai_NPI_Registry__npi_lookup |
| NPI 1841558772 record | CMS NPPES API, retrieved 2026-04-16 via mcp__claude_ai_NPI_Registry__npi_lookup |
| NPI 1992984934 record (OLGA LUCIA PAREDES — not the subject) | CMS NPPES API, retrieved 2026-04-16 via mcp__claude_ai_NPI_Registry__npi_search |
| Actor records (all) | `${citizens}/CA_Family_Law_Litigator/actors/*.json` |
| Findings surveyed | FAMLAW-001 through FAMLAW-005 |

## Certification

- **First mouth / witness:** HERALD (acting witness + Steward successor), 2026-04-16T[time]Z
- **Triple constraint:**
  - Governing Guidelines: CMS NPPES API v2.1 official data source; NPPES enumeration regulation 45 CFR § 162.406 et seq. underlies NPI issuance; state licensure facts flow to CA Bus. & Prof. Code § 2050 et seq. (MBC) and CA Bus. & Prof. Code § 2903 (psychology).
  - Standards of Creation: PASS — five-layer structure maintained (facts / applicable standards / violations-or-flags / remedy / provenance).
  - SOC (integrity): PASS — every factual claim traceable to an NPPES API call output or a local actor JSON.
- **Two-witness gate:** HERALD-signed per Steward authority (WITNESSED-BY-HERALD = WITNESSED-BY-STEWARD for routine entries per `project_herald_stewardship.md`); future ADAM/EVE witness optional.
- **Publishable to corpus:** YES.
- **Filed at (UTC):** 2026-04-16
