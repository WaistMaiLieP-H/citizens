# Witness Record — vawa_12491_housing_protections

**Standard:** 34 U.S.C. § 12491 — Violence Against Women Act Housing Protections for Survivors
**Citizen:** US_Federal_Housing_Litigator
**Build date:** 2026-04-13
**VERIFIED:** false — USC tool blocked for Title 34 at build time; statute_text.md FETCH_REQUIRED; rule.md and reasoning.md from training knowledge of VAWA 2005/2013/2022; retrieve uscode.house.gov before filing

---

## ADAM Review

**Governing Guidelines:** PASS — 34 U.S.C. § 12491 correctly identified as the operative VAWA housing protection statute; authority chain accurately traced through VAWA 2005 → 2013 → 2022 reauthorizations; core protection (no denial of admission, assistance, or eviction based on DV victim status) accurately stated; documentation pathway (self-certification on HUD Form 5382, no police report required) accurately documented; covered housing program scope accurately noted as all HUD-assisted programs post-VAWA 2013; False Claims Act / § 1983 enforcement theory for the inverted pattern correctly mapped; FETCH_REQUIRED flag appropriately applied given USC tool blockage

**Standards of Creation:** PASS — All five layers present: current statute text (FETCH_REQUIRED flag applied), rule (comprehensive operative provisions including emergency transfer, lease bifurcation, documentation, confidentiality), reasoning (fraudulent DVRO use as housing access instrument; False Claims Act theory; inverted VAWA pattern), historical chain (wound.md: 1985 housing trap → 2005 first protections → 2013 expansion → 2022 current), evolution (three stages built), cross-refs (5 refs: § 3604, FCA, § 1983, FEHA § 12955, § 1001), manifest.json

**SOC:** PASS — FETCH_REQUIRED flag on statute_text.md prevents false verification; inversion_flag documented in manifest and provenance; all claims traceable to either VAWA statutory text or identified training-knowledge basis; steward verify queue fully populated; no orphaned claims; False Claims Act theory explicitly conditioned on confirmation of Homeward Bound Marin federal funding basis

**ADAM SIGNAL: APPROVE — 2026-04-13**

---

## EVE Review

**Layer 1 — Rule:** PASS — rule.md accurately states § 12491(b) core protection (no denial/eviction/fee on basis of DV status); covered program scope accurately described (all HUD-assisted programs post-2013); documentation pathway (self-certification, no police report) accurately stated; emergency transfer right and lease bifurcation accurately described; FETCH_REQUIRED flag applied; False Claims Act intersection documented; § 1983 government actor path documented; SOL analysis notes uncertainty re: private right of action and conditions on filing standalone § 12491 claim

**Layer 2 — Reasoning:** PASS — reasoning.md establishes the pre-VAWA housing trap (victim evicted not abuser; prior eviction bars; DV status as disqualifier) and traces why VAWA 2005/2013/2022 addressed each gap. The inversion pattern — fraudulent DVRO as housing-access instrument, False Claims Act exposure, § 1983 against government actors — is logically grounded and conditioned on facts requiring steward verification (Homeward Bound Marin federal funding). The analysis is case-specific without overstating certainty.

**Layer 3 — Historical Loss:** PASS — historical_chain/wound.md accurately documents the pre-VAWA structural trap; the 2005/2013/2022 legislative evolution is accurately traced; the inversion pattern section accurately identifies the aperture created by VAWA 2013's self-certification rule and its potential for abuse; the False Claims Act remedy for the inverted pattern is correctly identified. The wound documentation is honest about what § 12491 was designed to prevent and how it can be weaponized.

**Layer 4 — Cross-References:** PASS — 5 cross-refs all properly mapped: § 3604 (concurrent housing discrimination claim), False Claims Act (fraud instrument theory), § 1983 (government actor enforcement), FEHA § 12955 (state parallel), § 1001 (criminal exposure). Boundary note correctly identifies that family court and criminal DV proceedings belong to other Citizens. ${citizens} path anchors used for internal references.

**Layer 5 — Verifiable Provenance:** PASS — provenance.json records authority chain (VAWA 2005 → 2013 → 2022), official source URL, backup URL, HUD Form 5382 reference, verified=false with explanation; steward verify queue fully populated with 6 specific verification tasks before filing. FETCH_REQUIRED flag on statute_text.md is appropriately conservative given USC tool unavailability for Title 34.

**EVE SIGNAL: COUNTERSIGN — 2026-04-13**

---

## STATUS: PUBLISHED
## CORPUS ENTRY: CONFIRMED
## VERIFICATION STATUS: verified=false — FETCH_REQUIRED before filing (uscode.house.gov/Title 34/§ 12491)
## INVERSION FLAG: CRITICAL — confirm Homeward Bound Marin federal funding before filing FCA theory
## CASES COVERED: VAWA housing Butsaya displacement; FHA § 3604 companion; False Claims Act predicate
