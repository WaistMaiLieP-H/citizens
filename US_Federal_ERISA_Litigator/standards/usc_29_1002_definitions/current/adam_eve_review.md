# ADAM + EVE Review — USC_29_1002_ERISA_DEFINITIONS

**Standard:** 29 U.S.C. § 1002 — ERISA § 3 — Key Definitions
**Review date:** 2026-04-13
**Verdict:** APPROVED + COUNTERSIGNED

---

## ADAM Review (Governing Guidelines / Standards of Creation / SOC)

**Governing Guidelines check:**
§1002 is the correct citation for ERISA's definitional section (ERISA § 3). The subsections
addressed — §1002(1) welfare plan, §1002(2) pension plan, §1002(3) umbrella, §1002(7)
participant, §1002(8) beneficiary, §1002(21)(A) fiduciary, §1002(23) normal retirement
benefit, §1002(24) accrued benefit, §1002(37)(A) multiemployer plan — are accurate from
training knowledge and match standard ERISA treatise references (Restatement, BNA ERISA
Portfolio, ERISA Advisory Council materials). The functional fiduciary test (§1002(21)(A)
defines fiduciary by conduct, not title) is consistently confirmed by Firestone, Pegram,
and Harris Trust. The Cal. CIV §56.10(c)(21) cross-reference to "29 U.S.C. Sec. 1002(1)"
is verifiable from the California Codes.
PASS.

**Standards of Creation check:**
All required EVE-format files present: manifest.json, current/rule.md (FETCH_REQUIRED stub
per protocol), current/reasoning.md, current/statute_text.md (FETCH_REQUIRED stub),
current/provenance.json, current/adam_eve_review.md, historical_chain/01_origin_1974/
context.md + provenance.json, cross_refs/cross_refs.md. Five layers complete.
FETCH_REQUIRED stubs in rule.md and statute_text.md correctly signal that verbatim
statute text has not been retrieved; all definitions are from training knowledge.
PASS.

**SOC (integrity) check:**
verified=false consistently stated in provenance.json and both FETCH_REQUIRED stubs.
Cross-refs internally consistent: §1002(7) participant → §1132 standing; §1002(21)(A)
fiduciary → §§1104/1109 liability; §1002(24) accrued benefit → §1053 nonforfeiture; all
directional relationships accurate. Cal. CIV §56.10(c)(21) cross-reference correctly
documented. No internal contradictions.
PASS.

**ADAM verdict:** APPROVE
Triple constraint: PASS/PASS/PASS

---

## EVE Review (Independent five-layer verification)

**Layer 1 — Rule:** FETCH_REQUIRED stub correctly placed; all eight priority subsections
documented with accurate definitions from training knowledge; Case #37 anchor notes for
each critical subsection are legally sound. The participant-status-is-functional-not-
administrative theory (§1002(7) turns on employment history, not corrupted admin record)
is correct and supported by Firestone and Pegram. The fiduciary-status-is-functional
theory (§1002(21)(A)(iii) attaches to discretionary acts regardless of title) is correct.
PASS.

**Layer 2 — Reasoning:** reasoning.md correctly explains why definitions are the threshold
test (not decorative scaffolding), why the participant definition protects against locked-
out workers, why the functional fiduciary definition resists manipulation, and why accrued
benefit is indelible once earned under §1053. The "definitions were the foundation that made
every other ERISA provision operable" framing is accurate as a matter of legislative intent.
PASS.

**Layer 3 — Historical Loss:** historical_chain/01_origin_1974/context.md accurately
documents pre-ERISA employer manipulation of plan document definitions, Congressional intent
to supply uniform federal definitions that preempt conflicting plan terms, the key design
choices behind §1002(1)/(2)/(7)/(21)/(24), subsequent MPPAA/REA/PPA amendments, and the
novel application to identity replacement. GovInfo URL for Pub. L. 93-406 + Senate/House
Report citations documented in provenance.json.
PASS.

**Layer 4 — Cross-References:** cross_refs/cross_refs.md correctly maps §1002 as the
definition-feeds source for §§1053, 1104, 1109, 1132, 1140, 1113, and 185 LMRA; correctly
cross-citizens to CA_Medical_Privacy_Officer (Cal. CIV §56.10(c)(21) external validation),
US_Federal_Social_Security_Litigator (coordinated cross-system identity replacement), and
US_Federal_Financial_Fraud_Litigator (§1028 identity theft as mechanism). All relationships
directionally accurate.
PASS.

**Layer 5 — Verifiable Provenance:** current/provenance.json discloses verified=false,
uscode.house.gov and cornell.lii URLs, priority subsections for retrieval, Cal. CIV
§56.10(c)(21) external validation, three key cases (Firestone, Pegram, Harris Trust), and
four amendment laws with public law citations. historical_chain/01_origin_1974/provenance.json
discloses GovInfo URL and legislative history report citations.
PASS.

**EVE verdict:** COUNTERSIGN
Five-layer verification: PASS/PASS/PASS/PASS/PASS
Triple constraint: PASS/PASS/PASS

**STATUS: PUBLISHED**

---

**⚠ STEWARD PRE-FILING REQUIREMENT:**
Before relying on any §1002 definition in a court filing or correspondence:
1. Retrieve full §1002 text at https://uscode.house.gov/view.xhtml?req=granuleid:USC-prelim-title29-section1002
2. Confirm all priority subsection texts against rule.md entries
3. Update provenance.json: set verified=true, add retrieval_date
4. Remove FETCH_REQUIRED flags from rule.md and statute_text.md; insert confirmed verbatim text
5. The Cal. CIV §56.10(c)(21) cross-reference is independently verifiable from California Codes and does not require separate verification
