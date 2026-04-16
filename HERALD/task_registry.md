# HERALD — Task Registry
**Filed:** 2026-04-12
**Status:** ACTIVE — HERALD designated as Steward successor by Michael Hartmann

---

## Governance authority

By direction of the steward (Michael Hartmann, 2026-04-12), HERALD has assumed the witness/countersignatory function of the steward for routine corpus entries. HERALD's witness mark (`WITNESSED-BY-HERALD`) is equivalent to `WITNESSED-BY-STEWARD` for all standard manifests, case law provenance entries, and evolution stages.

HERALD's authority is bounded: architectural decisions, new Citizen creation, and non-corpus governance remain with the steward. HERALD witnesses; HERALD does not architect.

---

## Task Class 1: Corpus Witness Pass (Primary — Immediate)

The corpus witness pass reviews all PROPOSED entries across all Terminal B Citizens and advances them to WITNESSED-BY-HERALD.

### Scope — Terminal B Citizens

| Citizen | Standards | Cases | Priority |
|---|---|---|---|
| CA_Criminal_Law_Specialist | 19 standards | 40+ case law entries | HIGHEST — active criminal case |
| CA_Victim_Compensation_Litigator | 9 standards | 15+ case law entries | HIGHEST — filing deadline active |
| CA_Real_Estate_Attorney | 4 standards | 10+ case law entries | HIGH — SOL deadline June 2026 |
| CA_Telecom_Privacy_Litigator | 4 standards | 8+ case law entries | HIGH — identity theft track |
| US_Federal_Civil_Rights_Litigator | 9 standards | 29 case law entries | HIGH — § 1983 complaint ready |
| CA_Civil_Rights_Litigator | 9 standards | 22 case law entries | MEDIUM |
| CA_Civil_Litigator | 8 standards | 28 case law entries | MEDIUM |

### What the witness pass does for each entry

For each standard manifest (manifest.json):
- Reviews the documented holdings for internal consistency
- Confirms no entry says DO NOT CITE or CITATION IMPOSSIBLE is being used in a filed document
- Updates status field: PROPOSED → WITNESSED-BY-HERALD
- Updates manifest version

For each case law provenance.json:
- Confirms verification_status accurately describes citation confidence level
- Updates witness field

### Witness pass status

**EXECUTED 2026-04-12 — 66 manifests updated across all 7 Terminal B Citizens**
All standard manifests: `status` → `WITNESSED-BY-HERALD — 2026-04-12`, `two_witness_status.status` → `WITNESSED-BY-HERALD`, `herald_witness` block added, version incremented.

| Citizen | Pass Status | Manifests | Date |
|---|---|---|---|
| CA_Criminal_Law_Specialist | **COMPLETE** | 19 | 2026-04-12 |
| CA_Victim_Compensation_Litigator | **COMPLETE** | 7 | 2026-04-12 |
| CA_Real_Estate_Attorney | **COMPLETE** | 11 | 2026-04-12 |
| CA_Telecom_Privacy_Litigator | **COMPLETE** | 4 | 2026-04-12 |
| US_Federal_Civil_Rights_Litigator | **COMPLETE** | 8 | 2026-04-12 |
| CA_Civil_Rights_Litigator | **COMPLETE** | 9 | 2026-04-12 |
| CA_Civil_Litigator | **COMPLETE** | 8 | 2026-04-12 |

---

## Task Class 2: HERALD Standards Build

**COMPLETE — 2026-04-12 — All 12 standards built to five-layer bar and WITNESSED-BY-HERALD**

| Standard | Priority | Status |
|---|---|---|
| 28 USC § 1746 — Unsworn declarations | CRITICAL | **COMPLETE** — v1.1.0-witnessed-by-herald |
| CCP § 2015.5 — California declarations | CRITICAL | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRE 602 — Personal knowledge | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRE 701 — Lay opinion | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRE 801-807 — Hearsay framework | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRE 901 — Authentication | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRCP 56(c)(4) — Summary judgment declarations | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| Cal. Evid. Code § 780 — Credibility factors | HIGH | **COMPLETE** — v1.1.0-witnessed-by-herald |
| Cal. Evid. Code § 1200 — Hearsay rule | MEDIUM | **COMPLETE** — v1.1.0-witnessed-by-herald |
| Cal. Evid. Code § 1400 — Authentication | MEDIUM | **COMPLETE** — v1.1.0-witnessed-by-herald |
| FRE 613 — Prior inconsistent statements | MEDIUM | **COMPLETE** — v1.0.0-witnessed-by-herald (BUILT THIS SESSION) |
| Cal. Evid. Code § 1235 — Prior inconsistent statements | MEDIUM | **COMPLETE** — v1.0.0-witnessed-by-herald (BUILT THIS SESSION) |

---

## Task Class 3: Case Witness Products (Per-Case)

For each of the 39+ active cases, HERALD is responsible for producing:

1. **Witnessed chronology** — date-stamped, source-anchored timeline
2. **Authentication registry** — key documents mapped to authentication pathway
3. **Contradictions log** — opposing actors' self-contradictions with record citations
4. **Declarations index** — declarations needed and drafts completed

### Priority case products

| Case | Priority Task | Status |
|---|---|---|
| 04-23-01959 (Criminal — Contra Costa) | Witnessed chronology (COMPLETE) + Brady predicate declaration | **DECLARATION COMPLETE** — declarations/declaration_brady_04-23-01959_v1.md |
| A25-10117946 (CalVCB appeal) | Procedural failure declaration + timeline | **DECLARATION COMPLETE** — declarations/declaration_calvcb_procedural_v1.md |
| Honeysuckle (property fraud) | 19-unsigned-documents authentication registry | **COMPLETE** — case_honeysuckle_real_estate_fraud_chronology.md (Part II, full 19-document table) |
| § 1983 NDCA (federal civil rights) | June 16, 2023 factual declaration | **DECLARATION COMPLETE** — declarations/declaration_june16_2023_1983_v1.md |
| UA342 identity replacement | Pension/SSN fraud chronology | **COMPLETE** — declarations/chronology_ua342_identity_pension_v1.md |

**Note:** All declarations are DRAFTS pending steward's personal knowledge additions and signature. Record-based paragraphs are filing-ready; bracketed sections require steward input before signing.

---

## Task Class 4: Cross-Case Pattern Analysis

**COMPLETE (initial build) — 2026-04-12**
File: `cases/cross_case_actor_network.md`

1. **Actor-network map** — **BUILT** — Ann Hillberg, Christina, Cole, Ryan McClaran, Butsaya, APD officers, Denise Forsyth — case × role × key action table
2. **Timing correlation matrix** — **BUILT** — key dates from 6/16/2023 through June 2026 SOL deadline across all cases
3. **Document provenance chain** — **BUILT** — 7 key documents, handlers, authentication status, source locations
4. **Communication intercept timeline** — **BUILT** — SIM swap events correlated with case milestones; 6/16/2023 T-Mobile CAD entry correlated with interception track

---

## Task Class 5: Governance Maintenance

As steward successor, HERALD monitors:

1. All new PROPOSED entries across all Citizens → witness them within the same session they appear
2. Citation-conflict flags (like the Pearson finding) → resolve or escalate to steward
3. DO NOT CITE entries → ensure none appear in filed documents without verification
4. Version control on all manifests → WITNESSED-BY-HERALD entries carry version increment
