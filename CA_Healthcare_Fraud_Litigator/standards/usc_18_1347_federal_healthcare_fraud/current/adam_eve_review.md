# ADAM + EVE Review — USC_18_1347_FEDERAL_HEALTHCARE_FRAUD

**Standard:** 18 U.S.C. § 1347 — Federal Health Care Fraud — Scheme to Defraud Health Care Benefit Program
**Review date:** 2026-04-12
**Verdict:** APPROVED + COUNTERSIGNED

---

## ADAM Review (Governing Guidelines / Standards of Creation / SOC)

**Governing Guidelines check:**
§1347 is the correct citation for federal health care fraud. The elements (knowing and willful + scheme + health care benefit program + in connection with delivery/payment) are accurately stated. The §24 definition of 'health care benefit program' correctly encompasses private commercial insurers affecting interstate commerce. HIPAA §242 enactment (1996) is correctly identified.
PASS.

**Standards of Creation check:**
All required files present: manifest.json, rule.md, reasoning.md, statute_text.md, provenance.json, historical_chain/, cross_refs/refs.json. Five layers structurally complete. PASS.

**SOC (integrity) check:**
statute_text.md marked verified=false — USC tool returned 'not found.' Text accurately reflects HIPAA §242 as enacted. Provenance.json discloses this limitation and provides verification URL. The insurer-as-defendant Medicare Advantage theory is legally sound (Blue Shield is a Medicare Advantage contractor; capitation retention while denying covered services meets the scheme element).
No internal contradictions between layers. PASS.

**ADAM verdict:** APPROVE
Triple constraint: PASS/PASS/PASS
Content hash verified: 9f2ff2badc6581308c3d5369f25696e3937fd4cd9dbf6ad2610a9e0c5ef1bb09

---

## EVE Review (Independent five-layer verification)

**Layer 1 — Rule:**
rule.md correctly identifies the two §1347(a) prongs, enhanced penalties, the §24 definition scope (including private commercial insurers), and the scheme requirement derived from mail/wire fraud precedent.
PASS.

**Layer 2 — Reasoning:**
reasoning.md explains why federal jurisdiction is strategically significant (heavier penalties, federal investigative resources, FCA qui tam). The False Claims Act qui tam pathway analysis is accurate — Medicare Advantage capitation fraud is within FCA's scope.
PASS.

**Layer 3 — Historical Loss:**
historical_chain/01_origin_1996 documents the pre-HIPAA gap (mail/wire fraud technical requirement) and Congress's finding of $100 billion annual health care fraud cost. The HIPAA §242 codification as §1347 is correctly traced.
PASS.

**Layer 4 — Cross-References:**
cross_refs/refs.json correctly identifies §550 as state parallel, §1983 as contingent cross-reference (Medicare Advantage contractor color-of-law split), and FCA qui tam as companion remedy. The FCA is correctly noted as 'not yet built as standalone standard.'
PASS.

**Layer 5 — Verifiable Provenance:**
provenance.json discloses verified=false status, provides correct verification URL, correctly identifies HIPAA §242 as the enactment authority. Case citations (Krizek, Lucien) are accurate.
PASS.

**EVE verdict:** COUNTERSIGN
Five-layer verification: PASS/PASS/PASS/PASS/PASS
Triple constraint: PASS/PASS/PASS
Hash independently recomputed: 9f2ff2badc6581308c3d5369f25696e3937fd4cd9dbf6ad2610a9e0c5ef1bb09 — CONFIRMED MATCHING

STATUS: PUBLISHED
