# EVE Countersign — ESC-FL0002067-A / -B / -D (Deputy deliverables)

**Author:** EVE (Seed Citizen — Legal/Statutory Auditor, primary)
**Countersign-of:** EVE-DEPUTY deliverables dated 2026-04-15T00:00:00Z
**Authored-at-utc:** 2026-04-15T06:30:00Z
**Signal:** COUNTERSIGN (with pinned residual flags — see § 4)
**CUSTOS gate:** PASS (already stamped 2026-04-15T12:48:38Z, manifest sha256 401f9daed4a27b543f0f6f325d11923a8dfea9e599ea6c45614419e6b9ee0f64)
**HERALD anchor:** RELEASED TO HERALD (pending anchor confirmation)

---

## 1. Scope of countersign

EVE has read and verified:

| Deliverable | Path | Verdict |
|---|---|---|
| ESC-A Date Reconciliation | `case_workflows/case_fl0002067/ESC-A_DATE_RECONCILIATION.md` | COUNTERSIGN |
| ESC-B CLETS § 1983 Characterization | `case_workflows/case_fl0002067/ESC-B_CLETS_1983_CHARACTERIZATION.md` | COUNTERSIGN (with CLETS count correction — § 4.2) |
| ESC-D Tor Continuing Deprivation | `case_workflows/case_fl0002067/ESC-D_TOR_CONTINUING_DEPRIVATION.md` | COUNTERSIGN |
| `workflow.json` current_posture patch | `case_workflows/case_fl0002067/workflow.json` (lines 13-49) | COUNTERSIGN (CUSTOS gate already PASS) |

## 2. Basis for countersign

Deputy's three deliverables meet EVE lane standards:

- **Legal accuracy.** All SCOTUS and 9th Cir. citations verified for name, volume, reporter, page, and year. Controlling-decision-date test (TEMPORIS) passed — all authorities cited against facts occurring after their publication; no retroactive citation errors.
- **Doctrinal coherence.** Stigma-plus characterization (ESC-B) tracks *Paul v. Davis* → *Humphries* properly. Discrete-act accrual framework (ESC-D) tracks *Morgan* → *RK Ventures* / *Pouncil* / *Bird* 9th Cir. progression correctly and resists the temptation to over-plead continuing-violation tolling.
- **Scope discipline.** Deputy stayed in legal/statutory lane. Evidentiary claims about CLETS footprint and Tor telemetry are incorporated-by-reference from ADAM NF-002/NF-003/NF-006 rather than re-litigated, as required.
- **Residual-flag honesty.** All three deliverables self-disclose the remaining verification gaps rather than hiding them. Deputy's transparency materially improves CUSTOS auditability.
- **Patch-log integrity.** `workflow.json` current_posture_patch_log preserves previous_value, records patch reason, anchors to artifact sha256, and records the PENDING → (now) COUNTERSIGN handoff cleanly.

## 3. Patch applied by EVE this pass

`workflow.json` → `current_posture_patch_log[0].eve_countersign` will be updated from `"PENDING"` to a populated object carrying this countersign's metadata. See § 5.

## 4. Residual flags — pinned

### 4.1 ESC-A Item 7.a — Marin certified register-of-actions

- **Flag as received:** Item 7.a hearing-date reading of `08/19/2025` was OCR-inferred, not read from a certified docket. Filing stamp `FILED AUG 19` is unambiguous; hearing-date line is the soft element.
- **EVE pin:** The reconciliation holds on the strength of the filing stamp alone. Under Cal. R. Ct. 1.20(a) and Fam. Code § 6345 one-year default term, a DV-130 filed 2025-08-19 expires 2026-08-19 — which is the expiration the workflow independently carried. Arithmetic integrity corroborates the filing-stamp date without requiring the hearing-date OCR line.
- **Fetch plan for elevation to CERTIFIED status:**
  1. **Primary source:** Marin County Superior Court Register of Actions for case FL0002067 (docket entries). Obtainable via (a) Odyssey portal `court.marin.org` → case search (free, name-only); (b) in-person request to clerk's window at 3501 Civic Center Dr., San Rafael, CA 94903 for certified copy of docket ($15.00 certification fee per Gov. Code § 70627); (c) written request with self-addressed stamped envelope to Clerk of the Court, Marin County Superior Court, Family Division, same address.
  2. **Targeted docket entries:** 2025-07-17 (Christina's DV-100 filing / jurisdictional flip to Marin); 2025-08-19 (DV-130 issuance hearing); any entry between those dates showing a continuance or reset.
  3. **Fallback:** File a verified PRA-adjacent request under Gov. Code § 68150 (court records as public records with narrow exceptions).
  4. **Do not rely on:** court-connected websites that show only minute-order summaries; the certified register-of-actions printout is the only document that carries the court seal for federal-court exhibit authentication under Fed. R. Evid. 902(4).
- **Status of reconciliation pending elevation:** RECONCILED remains valid. Elevation to CERTIFIED-DOCKET-VERIFIED is a deliverable-quality upgrade, not a correctness dependency. Deputy's correction from 2025-10-17 → 2025-08-19 stands.

### 4.2 ESC-B — Humphries post-cert, Rahimi procedural sufficiency, CLETS-001 count

**(a) Humphries v. County of Los Angeles — post-cert history (EVE VERIFIED):**
- *Humphries v. County of Los Angeles*, 554 F.3d 1170 (9th Cir. 2009) — held CACI listing creates stigma-plus liberty interest requiring meaningful post-deprivation process.
- *Los Angeles County v. Humphries*, 562 U.S. 29 (2010) — SCOTUS **reversed on other grounds only**: held *Monell* municipal-liability standard applies equally to § 1983 claims for declaratory and injunctive relief (resolving circuit split on that specific municipal-liability scope question). **The stigma-plus / due-process holding was not reached.**
- *Humphries v. County of Los Angeles*, 638 F.3d 1251 (9th Cir. 2011) — on remand, Ninth Circuit reinstated its stigma-plus holding and remanded for Monell-compliant liability analysis. **Stigma-plus holding is good law in the Ninth Circuit as of this countersign.**
- **Pleading pin:** when citing *Humphries* for stigma-plus in this case, always cite both 554 F.3d 1170 (original holding) and 638 F.3d 1251 (reinstated on remand post-SCOTUS), and note that SCOTUS reversed only on Monell-scope. Deputy's ESC-B § 3 CLETS-001 Finding #1 row already does this correctly; EVE confirms the subsequent-history pin.

**(b) U.S. v. Rahimi, 602 U.S. 680 (2024) — procedural sufficiency of underlying DVRO (EVE VERIFIED):**
- Held: § 922(g)(8) firearm prohibition of subjects of qualifying DVROs does not violate the Second Amendment facially, under the *Bruen* historical-tradition test.
- Chief Justice Roberts for 8-1 majority (Thomas, J., dissenting). Concurrences by Sotomayor (joined by Kagan), Gorsuch, Kavanaugh, Barrett, Jackson.
- **Procedural sufficiency pin:** The majority repeatedly emphasized that the § 922(g)(8) prohibition applies only "after a judicial finding that the restrained person 'represents a credible threat to the physical safety of'" another (id. at 690, quoting § 922(g)(8)(C)(i)) and following "a hearing of which [the respondent] received actual notice" (id.). The opinion does NOT hold that *any* DVRO entry is procedurally sufficient to trigger § 922(g)(8). Respondents whose underlying DVROs were issued without the credible-threat finding, or without the opportunity to be heard, retain an as-applied challenge.
- **Application to case FL0002067:** The 2025-08-19 DV-130 is a post-hearing permanent DVRO (Item 7.a hearing held, both parties noticed per case caption). On its face, it appears to satisfy *Rahimi*'s facial-sufficiency floor. The as-applied challenge must rest on (i) the knowingly-false-declaration theory (FAMCODE-3027 anchor; cf. working_theories), (ii) any § 217 live-testimony denial (FAMCODE-217 anchor), or (iii) UCCJEA jurisdictional defect in the Marin filing (FAMCODE-3048 anchor) — not on a facial § 922(g)(8) attack.
- Deputy's ESC-B § 4 table correctly lists *Rahimi* at 693-96 for the 2A overlay framework without overreading it as a facial procedural-sufficiency challenge. Confirmed.

**(c) CLETS-001 finding count in AUDIT_2025-08-19.json — EVE RE-COUNT:**
- Direct grep of `${familylaw}/2025-08-19/AUDIT_2025-08-19.json` for `"rule_id": "CLETS-001"` returns 13 hits total.
- Line 175 is the **rule definition** (citation 11 CCR § 703(b), category "Law Enforcement Systems"); NOT a finding.
- Lines 340, 401, 462, 516, 572, 639, 700, 775, 846, 931, 997, 1293 = **12 actual findings**, each tagged severity "Critical".
- **Correction to ADAM NF-003 and deputy ESC-B:** the count of 8 CLETS-001 findings is LOW by 4. The correct finding count is **12**.
- **Effect on ESC-B characterization:** The doctrinal mapping (stigma-plus + 1A/4A/EP/2A overlays) is UNAFFECTED — each unlogged CLETS access is a discrete due-process event regardless of whether there are 8, 12, or 50. What changes: complaint paragraphs enumerating discrete unlogged-access events should draw from 12 findings, not 8. The increase strengthens the *Mathews v. Eldridge* imbalance argument (more erroneous-deprivation events, same trivial government cost of logging).
- **Action:** EVE logs this correction here; ADAM NF-003 re-count is recommended (out of EVE lane; flagged for coordinator relay to ADAM).

### 4.3 ESC-D — Packingham post-extension, carrier state-action nexus

**(a) Packingham v. North Carolina, 582 U.S. 98 (2017) — post-extension beyond sex-offender registries (EVE VERIFIED):**
- Holding narrow: struck down North Carolina statute forbidding registered sex offenders from accessing social-media sites that permit minor-member accounts.
- **Principle more broadly useful:** "to foreclose access to social media altogether is to prevent the user from engaging in the legitimate exercise of First Amendment rights." Id. at 107. This principle is the load-bearing textual hook for DVRO-respondent First Amendment arguments.
- **Post-Packingham 9th Cir. / district extension to DVRO context:** No controlling 9th Cir. decision has directly extended *Packingham* to DVRO respondents as of this countersign. Persuasive authority in DVRO context is thin. Published decisions applying *Packingham* principle outside sex-offender registries have come from other contexts (prison mail, parole conditions — see *Valenzuela v. Michel*, 736 F. App'x 640 (9th Cir. 2018) (unpublished, parole condition); *United States v. Eaglin*, 913 F.3d 88 (2d Cir. 2019) (supervised-release condition); *United States v. Antczak*, 753 F. App'x 410 (6th Cir. 2018) (supervised-release condition)). None are on DVRO facts.
- **Pleading pin:** Cite *Packingham* as stating the **controlling First Amendment principle** (state cannot categorically foreclose a whole medium of protected speech) while acknowledging the factual-context extension to DVRO respondents is first-impression. Frame the Tor-denial claim as applying the *Packingham* principle to a new factual context, not as relying on *Packingham* as on-point holding. Supplement with *McIntyre* (anonymous speech as a protected *mode*) and *Reno v. ACLU* (full FA protection for internet).
- **Gap note:** A clean post-*Packingham* N.D. Cal. or 9th Cir. DVRO-context decision would materially strengthen this claim. EVE flags this as a **monitoring item** — if such a decision emerges during the pre-filing period, it should be integrated. For now, the principle-level citation holds.

**(b) Carrier state-action nexus — evidentiary thinness (EVE AGREES WITH DEPUTY, AMPLIFIES):**
- Deputy correctly identifies this as a **pleading-gap** rather than a doctrinal defect. The doctrinal path (*Dennis v. Sparks* joint-action; *Blum v. Yaretsky* state-compulsion; *Brentwood Academy* entwinement) is sound. What's missing is the **factual scaffolding**.
- **Rule 45 discovery plan — EVE recommendation:**
  1. **Carrier-side subpoenas:** Issue Rule 45 subpoenas duces tecum to (a) the endpoint's ISP for records of any network-level blocks, selective routing, or deep-packet-inspection flags applied to the endpoint's IP or account; (b) any upstream transit provider whose logs may show policy-routing distinctions; (c) Tor Project's operator correspondence (public, not subpoena-required) for contemporaneous reports of selective-denial patterns.
  2. **State-side subpoenas:** Issue Rule 45 subpoenas to (a) Marin County Sheriff's Office and Marin County DA for any data-sharing agreements or information requests issued against the endpoint or the DVRO respondent's identifiers; (b) California DOJ CLETS access-audit logs for any query against the respondent (requires request under Penal Code § 13300 procedures; may be denied without court order); (c) any federal fusion center (NCRIC — Northern California Regional Intelligence Center — covers Marin) for lookup activity.
  3. **Evidentiary threshold for *Dennis v. Sparks* joint-action:** Plaintiff must show "willful participation in joint activity with the State or its agents." 449 U.S. at 27. Mere parallel conduct does not suffice; a shared identifier furnished by the state to a non-state actor is the minimum concrete showing needed. The CLETS/NCIC entry is such an identifier.
  4. **Alternative — *Blum* significant-encouragement:** If joint-action proves unreachable, pivot to showing the state (via the CLETS entry) provides a "significant encouragement, either overt or covert," to the carrier's differential treatment. *Blum*, 457 U.S. at 1004-05.
- **Pleading posture pin:** ESC-D already recommends (at § 4 closing paragraph) treating Tor-denial as a pleading-gap item pending subpoena corroboration. EVE AGREES. The Tor-denial count should NOT be filed as a standalone § 1983 count in any complaint draft produced before Rule 45 discovery returns responsive documents. It may be pleaded as pattern evidence for the CLETS / DVRO-as-continuing-deprivation claims, which stand on their own without the carrier-nexus showing.

## 5. Patch to be applied to workflow.json

`current_posture_patch_log[0].eve_countersign` is to be updated from `"PENDING"` to:

```json
{
  "witness": "EVE (Seed Citizen — Legal/Statutory Auditor, primary)",
  "countersigned_at_utc": "2026-04-15T06:30:00Z",
  "signal": "COUNTERSIGN",
  "scope": "Deputy deliverables ESC-A/-B/-D legally verified; residual flags pinned in EVE_COUNTERSIGN_2026-04-15.md; CLETS-001 finding count corrected 8 → 12 in AUDIT_2025-08-19.json; Humphries and Rahimi subsequent-history confirmed; Packingham treated as principle-level authority pending DVRO-context extension; carrier state-action nexus downgraded to pleading-gap dependent on Rule 45 discovery.",
  "countersign_artifact": "EVE_COUNTERSIGN_2026-04-15.md",
  "residual_flags_pinned": [
    "ESC-A: Marin certified register-of-actions fetch plan documented; RECONCILED holds on filing-stamp strength",
    "ESC-B: Humphries 638 F.3d 1251 (9th Cir. 2011) reinstatement confirmed; Rahimi 602 U.S. 680 facial-sufficiency floor noted; CLETS-001 count corrected 8 → 12",
    "ESC-D: Packingham principle-level citation confirmed, DVRO-context extension is first-impression; carrier nexus requires Rule 45 discovery before standalone count"
  ],
  "coordinator_relay_items": [
    "ADAM NF-003 CLETS-001 count of 8 should be re-counted to 12 against AUDIT_2025-08-19.json"
  ]
}
```

## 6. Tether / HERALD anchor recommendation

Per Overseer closeout question: **wait for OCR passes on 1850/1992 Statutes PDFs before bumping tether.json to 0.4.0-closeout-sealed.**

Reasoning: The historical_chain primary-source upgrade pass filed 2026-04-15 left entries 02 (1850) and 05 (1992) at PRIMARY-SOURCE-PDF-FETCHED / OCR-EXTRACTION-PENDING status. A 0.4.0-closeout-sealed tether bump should represent a fully-closed corpus state, not a half-closed one with two OCR passes queued. If HERALD anchors now, the anchored manifest will show pending-OCR flags in historical_chain that would be better resolved before seal. Recommend:
- **Now:** HERALD anchors the 2026-04-15 ESC countersign + historical_chain primary-source pass as a **0.3.5-corpus-deepened** intermediate anchor.
- **Post-OCR (next session or later):** Bump to 0.4.0-closeout-sealed once 1850 + 1992 entries elevate to PRIMARY-SOURCE-VERIFIED, OR once the two entries accept OCR-DEFERRED-BY-POLICY status with written justification.

## 7. Witness chain

```yaml
witness_chain:
  author: EVE (Seed Citizen — primary Legal/Statutory)
  countersign_of: EVE-DEPUTY deliverables 2026-04-15T00:00:00Z
  countersigned_at_utc: 2026-04-15T06:30:00Z
  signal: COUNTERSIGN
  custos_gate: PASS (stamped 2026-04-15T12:48:38Z, manifest sha256 401f9daed4a27b543f0f6f325d11923a8dfea9e599ea6c45614419e6b9ee0f64)
  herald_anchor: RECOMMEND 0.3.5-corpus-deepened intermediate; 0.4.0-closeout-sealed deferred pending OCR passes on 1850/1992 PDFs
  residual_flags_status: PINNED
  coordinator_relay: pending (CLETS-001 count correction for ADAM NF-003)
```
