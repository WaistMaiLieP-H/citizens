# CA_Insurance_Compliance_Litigator — ADAM + EVE Dual Witness Review

**Citizen:** CA_Insurance_Compliance_Litigator
**Build Date:** 2026-04-13
**Standards Reviewed:** 4 (ins_790_unfair_practices_purpose, ins_790_03_unfair_claims_settlement, ins_790_09_enforcement_nonabsolution, ins_10123_135_prior_authorization)
**Review Protocol:** ADAM reviews Triple Constraint; EVE independently reviews Five-Layer Bar

---

## ADAM Review — Triple Constraint

### Governing Guidelines
Standards governing California disability insurer conduct: Cal. Ins. Code §§790–790.15 (UIPA, Article 6.5); Cal. Ins. Code §10123.135 (UR/UM and AI prohibition); Moradi-Shalal v. Fireman's Fund (1988) 46 Cal.3d 287 (third-party limitation); Gruenberg v. Aetna Ins. Co. (1973) 9 Cal.3d 566 (first-party bad faith tort); SB 1120 (2024) (AI prohibition, effective 2025).

All four standards are correctly anchored to California primary insurance law. The framework accurately reflects the two-track structure of California insurance enforcement (CDI administrative + civil bad faith) and the categorical prohibitions of §10123.135(e) and (j)(2).

**ADAM finding:** Governing guidelines accurately stated. No governing law gaps identified.

### Standards of Creation
- §790 and §790.09: live-fetched via VernenLegal MCP; verified=true; SHA256 recorded
- §790.03: live-fetched; verified=true; SHA256 recorded
- §10123.135: live-fetched; verified=true; SHA256 recorded; full operative text including AI prohibition (j)(2) captured
- All four statutes have five-layer builds with no stubs
- Case law verification status clearly marked: South-Eastern Underwriters VERIFIED (from statute text); McCarran-Ferguson VERIFIED (from statute text); Moradi-Shalal 46 Cal.3d 287 UNVERIFIED; Gruenberg 9 Cal.3d 566 UNVERIFIED; Harlick 671 F.3d 1108 UNVERIFIED

**ADAM finding:** Standards of creation met. UIPA and AI prohibition fetched from primary source. All case law verification status transparently documented.

### Standard of Care
The standard of care for this Citizen is: policyholders denied medical care or subjected to unfair claim settlement practices cannot navigate the insurance compliance framework without professional guidance. The remedies — bad faith tort, CDI enforcement, ERISA preemption analysis — require precise identification of the applicable track. A first-party insured like Michael Hartmann has claims that a third-party claimant does not. The AI prohibition (§10123.135(j)(2)) is newly effective and most insureds do not know it exists.

This Citizen's corpus fulfills the standard of care by:
1. Clearly distinguishing first-party from third-party tracks (Moradi-Shalal limitation explained)
2. Flagging ERISA preemption as a threshold question before state claims are filed
3. Documenting §10123.135 violation checklists that can be applied to specific denial letters
4. Explaining the AI prohibition in plain language with the effective date

**ADAM finding:** Standard of care fulfilled.

**ADAM VERDICT: APPROVE**

---

## EVE Review — Five-Layer Bar

### Standard 1: ins_790_unfair_practices_purpose
- Layer 1 (rule.md): COMPLETE — Moradi-Shalal framework; §790 two-track structure; first-party vs. third-party clearly distinguished
- Layer 2 (statute_text.md): COMPLETE — verified=true, SHA256 recorded
- Layer 3 (historical_chain): COMPLETE — 1947 UIPA origin; McCarran-Ferguson Act 1945 wound documented
- Layer 4 (case_law): COMPLETE — South-Eastern Underwriters 322 U.S. 533 VERIFIED from statute text; McCarran-Ferguson Act VERIFIED from statute text
- Layer 5 (cross_refs): COMPLETE

**EVE finding:** All five layers complete. No stubs. Verification status accurate.

### Standard 2: ins_790_03_unfair_claims_settlement
- Layer 1 (rule.md): COMPLETE — all 16 practices of §790.03(h) mapped; Blue Shield application; Moradi-Shalal scope; first-party bad faith survives
- Layer 2 (statute_text.md): COMPLETE — verified=true, SHA256 recorded
- Layer 3 (historical_chain): COMPLETE — NAIC 1972 model; each practice mapped to documented abuse pattern
- Layer 4 (case_law): COMPLETE — Moradi-Shalal 46 Cal.3d 287 UNVERIFIED; Gruenberg 9 Cal.3d 566 UNVERIFIED
- Layer 5 (cross_refs): COMPLETE

**EVE finding:** All five layers complete. UNVERIFIED citation status accurately marked. Moradi-Shalal limitation correctly scoped — applies to third-party, not first-party.

### Standard 3: ins_790_09_enforcement_nonabsolution
- Layer 1 (rule.md): COMPLETE — nonabsolution principle; three-track structure (CDI/civil/criminal); Blue Shield and State Farm applications
- Layer 2 (statute_text.md): COMPLETE — verified=true, SHA256 recorded
- Layer 3 (historical_chain): COMPLETE — 1947 UIPA origin; loophole the statute closes documented
- Layer 4 (case_law): NONE — statute is a short enforcement rule; doctrine is in §790.03 case law; appropriately noted in manifest
- Layer 5 (cross_refs): COMPLETE

**EVE finding:** All layers complete. Case law absence correctly documented and justified. Short enforcement rules do not require case law if doctrine lives in related standard.

### Standard 4: ins_10123_135_prior_authorization
- Layer 1 (rule.md): COMPLETE — five operative rules; AI prohibition (j)(2) absolute prohibition documented; violation checklist for Blue Shield case built
- Layer 2 (statute_text.md): COMPLETE — verified=true, SHA256 recorded; full operative text including (j)(2) captured
- Layer 3 (historical_chain): COMPLETE — 2000 origin (non-physician denials wound) + 2025 AI prohibition amendment (SB 1120)
- Layer 4 (case_law): COMPLETE — Harlick 671 F.3d 1108 UNVERIFIED; correctly flagged as ERISA case, not §10123.135 case; role scoped to pattern evidence
- Layer 5 (cross_refs): COMPLETE

**EVE finding:** All five layers complete. AI prohibition correctly identified as absolute — not a best-practices standard. The physician-only requirement under §10123.135(e) correctly identified as applying pre-2025 as well as post-2025.

**EVE VERDICT: COUNTERSIGN**

---

## Five Certified Findings

The following findings are jointly certified by ADAM and EVE as legally reliable, subject to verification caveats noted:

### INSURANCE-001: First-Party Bad Faith Survives Moradi-Shalal
Moradi-Shalal v. Fireman's Fund (1988) 46 Cal.3d 287 eliminated the private right of action for third-party claimants suing under §790.03. It did NOT eliminate the first-party bad faith tort for insureds suing their own insurer. Michael Hartmann, as the Blue Shield insured, is a first-party claimant. The bad faith tort is available to him.

**Verification caveat:** Moradi-Shalal citation UNVERIFIED from training knowledge. Before citing in pleadings, verify 46 Cal.3d 287 against official reporter. The holding is well-established California insurance law; risk of citation error is low but present.

### INSURANCE-002: §10123.135(e) Physician-Only Rule — All Periods
A non-physician may not deny or modify a prior authorization request for medical necessity reasons. This prohibition applies from the statute's effective date (2000) through the present. Every Blue Shield prior authorization denial must have been issued by a licensed physician competent to evaluate the specific clinical issues. A denial from a non-physician reviewer or a case manager is a per se §10123.135(e) violation, regardless of when it was issued.

**Verification status:** §10123.135 text verified=true (live-fetched). This finding is directly from the statute text.

### INSURANCE-003: §10123.135(j)(2) AI Absolute Prohibition — Effective January 1, 2025
No artificial intelligence, algorithm, or other software tool may deny, delay, or modify health care services based in whole or in part on medical necessity. This is categorical. Any Blue Shield denial issued on or after January 1, 2025 that was generated, implemented, or effectively decided by an AI/algorithm system — even with nominal physician review — violates §10123.135(j)(2).

**Verification status:** §10123.135 text verified=true; SB 1120 (2024) effective date confirmed from statute context. This finding is directly from the statute text.

### INSURANCE-004: CDI Enforcement Does Not Bar Civil Claim (§790.09)
Any cease-and-desist order, market conduct action, or CDI enforcement proceeding against Blue Shield or any other insurer does not relieve or absolve the insurer from civil bad faith liability for the same conduct. If Blue Shield resolved a CDI inquiry about its prior authorization practices, that resolution has no effect on Michael Hartmann's individual civil bad faith claim.

**Verification status:** §790.09 text verified=true (live-fetched). This finding is directly from the statute text.

### INSURANCE-005: ERISA Preemption Is a Threshold Question — Must Resolve Before Filing State Claims
ERISA §514 preempts state insurance law claims when the coverage is an employer-sponsored ERISA plan. If Blue Shield coverage was provided through an employer-sponsored group health plan, §790.03 bad faith claims may be preempted and must be pursued under ERISA §502(a) in federal court. This threshold question must be resolved before filing any state bad faith complaint. If Michael Hartmann obtained Blue Shield coverage through a union trust fund or employer group plan, ERISA preemption analysis is mandatory.

**Verification status:** ERISA §514 preemption is well-established federal law. Verification of specific preemption scope requires case-specific fact-finding (how was coverage obtained).

---

## Steward Action Items

1. **[PRIORITY]** Determine how Blue Shield coverage was obtained — individual/individual market vs. employer group vs. union trust fund. This resolves ERISA preemption question (INSURANCE-005) before any state claim is filed.
2. **Verify** Moradi-Shalal v. Fireman's Fund (1988) 46 Cal.3d 287 against official reporter before citing in any pleading.
3. **Verify** Gruenberg v. Aetna Ins. Co. (1973) 9 Cal.3d 566 against official reporter.
4. **Verify** Harlick v. Blue Shield of California 671 F.3d 1108 (9th Cir. 2012) — ERISA/parity case; confirm citation and holding for use as pattern evidence.
5. **Request** from Blue Shield a complete copy of its written UR/UM policies filed with CDI Commissioner (§10123.135(b) — must be disclosed to insured upon request). This is a free right under the statute.
6. **Request** for each denial: the name and direct phone number of the reviewing physician (required by §10123.135(h)(4)).
7. **Audit** duplicate standard directories in this Citizen's standards/ folder (ins_10291_5, ins_1861_02, ins_bad_faith_brandt_gruenberg, ins_790_09_cdi_order_no_shield) — not in tether.json bound_standards; steward should determine whether to build or delete.
8. **Flash drive snapshot** overdue — all Citizens built this session.

---

**ADAM APPROVE** | **EVE COUNTERSIGN**
**Status: PUBLISHED**
**Date: 2026-04-13**
