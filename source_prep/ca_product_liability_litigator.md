# SOURCE PREP: CA_Product_Liability_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** PARTIAL — CIV §1714 FETCHED; COM §2314 FETCHED this session; strict product liability is case-law-based (Greenman), not statutory
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- RedJag 2018 Jaguar XE — delivered stripped/stolen vehicle; stolen parts removed from vehicle; product delivered was fundamentally defective (not merely breach of warranty — defective product delivered)
- Toyota Camry XSE — separate vehicle fraud; product defect claims TBD at build time
- Spine surgery (L5-S1 fusion, Dr. Wiseman 4/20/22) — defective medical device or surgical product claims if implant failure established
- SIRVA (COVID vaccine Walgreens Brentwood ~11/2021) — vaccine product liability; manufacturer immunity question (VICP preemption) vs. administering party liability

**Boundary rule:**
- CA_Vehicle_Code_Specialist OWNS: VEH code dealer licensing violations; title fraud; CARFAX fraud
- CA_Consumer_Protection_Litigator OWNS: UCL §17200; CLRA; Rees-Levering yo-yo financing; warranty claims
- CA_Medical_Malpractice_Litigator OWNS: physician negligence in surgical care
- THIS CITIZEN OWNS: Strict product liability doctrine (Greenman); design defect; manufacturing defect; failure to warn; learned intermediary doctrine; component part manufacturer liability; successor liability

---

## ANCHOR STATUTES — FETCHED AND READY

### CIV CODE § 1714 — General negligence standard / basis for products negligence
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Everyone responsible for injury from "want of ordinary care or skill in the management of his or her property or person"
- Strict product liability is NOT grounded in §1714 — it is judge-made law from Greenman (below) — but §1714 is the negligence predicate that coexists with strict liability; plaintiff may plead BOTH
- §1714(b): Legislative abrogation of Vesely line re: alcohol furnishing (not relevant here)
**Standard ID:** `civ_1714_negligence_standard`

### CCP § 335.1 — 2-year statute of limitations (personal injury)
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** "Within two years: An action for assault, battery, or injury to, or for the death of, an individual caused by the wrongful act or neglect of another."
**Application:** Product liability personal injury claims: 2-year SOL from injury. SIRVA: injury date ~11/2021; Dr. Wiseman surgery: 4/20/22; discovery rule tolling may extend both.
**Standard ID:** `ccp_335_1_personal_injury_sol`

### CCP § 338 — 3-year statute of limitations (fraud / property injury)
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- §338(a): 3 years — action on liability created by statute
- §338(c): 3 years — action for taking/detaining/injuring goods or chattels (property damage from defective product)
- §338(d): 3 years — action on ground of fraud or mistake; accrues on DISCOVERY of fraud (discovery rule)
**Application:** RedJag property damage: 3-year from delivery (~2018) → EXPIRED unless discovery rule applies (wrong CARFAX discovered later; stripped vehicle discovered later). Fraud track: discovery rule preserves claims.
**Standard ID:** `ccp_338_property_fraud_sol`

---

## ANCHOR CASE LAW — FETCH/CONFIRM REQUIRED

### Greenman v. Yuba Power Products, Inc., 59 Cal.2d 57 (1963) — THE FOUNDATIONAL CASE
- **What it does:** Justice Traynor establishes strict product liability in California: "A manufacturer is strictly liable in tort when an article he places on the market, knowing that it is to be used without inspection for defects, proves to have a defect that causes injury to a human being."
- **Three theories:** (1) Manufacturing defect — product departs from intended design; (2) Design defect — entire product line unreasonably dangerous; (3) Failure to warn — product lacks adequate warnings
- **Standard ID:** `greenman_strict_products_liability`
- **Source:** Sargent Shriver National Center on Poverty Law; case text directly; or Westlaw/LexisNexis

### Barker v. Lull Engineering Co., 20 Cal.3d 413 (1978) — Design defect test
- **What it does:** Two alternative tests for design defect: (1) Consumer expectations test — product failed to perform as safely as an ordinary consumer would expect; (2) Risk-utility test — plaintiff shows design proximately caused injury, burden shifts to manufacturer to show benefits outweigh risks
- **Standard ID:** `barker_design_defect_test`

### Soule v. General Motors Corp., 8 Cal.4th 548 (1994) — When consumer expectations test applies
- **What it does:** Consumer expectations test appropriate when product's performance is within common experience; risk-utility test appropriate for complex technical failures; court decides which test applies
- **Standard ID:** `soule_consumer_expectations_test_scope`

### Sindell v. Abbott Laboratories, 26 Cal.3d 588 (1980) — Market share liability
- **What it does:** When specific manufacturer cannot be identified (fungible product from multiple manufacturers), market share liability allocates liability by market share; each defendant liable for its proportionate share unless it can exculpate itself
- **Application:** SIRVA — if multiple vaccine lots from different manufacturers involved; OR if specific administering pharmacist/technician identified but manufacturer immune under VICP
- **Standard ID:** `sindell_market_share_liability`

---

## ANCHOR STATUTES — FETCH REQUIRED

### HEALTH & SAFETY CODE § 1797.196 — Vaccine liability (state law angle)
- **What it does:** State-level vaccine administration liability for non-VICP claims
- **Fetch:** leginfo → HSC § 1797.196

### 42 USC § 300aa-11 — VICP (National Childhood Vaccine Injury Act) — federal preemption
- **What it does:** Vaccine Injury Compensation Program; mandatory pre-suit filing for covered vaccines; manufacturer immunity from design defect claims for covered vaccines (Bruesewitz v. Wyeth)
- **NOTE:** Walgreens is the ADMINISTERING party, not manufacturer; Walgreens is NOT covered by VICP manufacturer immunity; negligent administration by Walgreens pharmacist = ordinary tort claim
- **Fetch:** uscode.house.gov → Title 42 → § 300aa-11
- **Standard ID:** `vicp_300aa_11_preemption`

### CAL. COM. CODE § 2314 — Implied warranty of merchantability
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§2314(1):** Unless excluded or modified (§2316), warranty that goods shall be MERCHANTABLE is implied in contract for sale if seller is a MERCHANT with respect to goods of that kind; food/drink served for value is a "sale"
- **§2314(2) — Merchantability standards (goods must be AT LEAST):**
  - **(a)** Pass without objection in trade under contract description
  - **(b)** Fungible goods: fair average quality within description
  - **(c)** Fit for the ORDINARY PURPOSES for which such goods are used
  - **(d)** Even kind, quality, and quantity within each unit and among all units
  - **(e)** Adequately contained, packaged, and labeled as agreement requires
  - **(f)** Conform to promises or affirmations of fact on container or label
- **§2314(3):** Other implied warranties may arise from course of dealing or usage of trade
**Application — RedJag:** A Jaguar dealer is a merchant with respect to vehicles. A stripped vehicle that fails to pass "without objection in trade" and is not "fit for ordinary purposes" (driving safely) fails every §2314(2) prong. The implied warranty runs regardless of whether the buyer reads or signs a disclaimer — §2316 exclusion of §2314 requires conspicuous language saying "AS IS" or "WITH ALL FAULTS." The CARFAX fraud = concealing the §2314 breach.
**Standard ID:** `com_2314_implied_warranty_merchantability`

### CAL. COM. CODE § 2315 — Implied warranty of fitness for particular purpose
- **What it does:** If seller knows buyer's particular purpose, warranty that goods are fit for that purpose
- **Fetch:** leginfo → COM § 2315

---

## CASE LAW SEEDS

1. **Greenman v. Yuba Power Products, Inc.**, 59 Cal.2d 57 (1963) — FOUNDATIONAL; strict liability in tort; no privity requirement
2. **Barker v. Lull Engineering Co.**, 20 Cal.3d 413 (1978) — Design defect: consumer expectations AND risk-utility; burden-shifting
3. **Soule v. General Motors Corp.**, 8 Cal.4th 548 (1994) — Consumer expectations test scope; complex product → risk-utility
4. **Cronin v. J.B.E. Olson Corp.**, 8 Cal.3d 121 (1972) — No "unreasonably dangerous" requirement for strict liability; Restatement §402A language rejected; California uses Greenman test
5. **Webb v. Special Electric Co., Inc.**, 63 Cal.4th 167 (2016) — Component parts manufacturer strict liability; component manufacturer liable if component substantially contributed to defect; no duty to warn about asbestos-containing products made by others
6. **Bruesewitz v. Wyeth LLC**, 562 U.S. 223 (2011) — VICP preempts ALL state law design defect claims for covered vaccines; but does NOT preempt manufacturing defect or negligent administration claims
7. **Kim v. Walls**, 107 Cal.App.4th 921 (2003) — Learned intermediary doctrine: manufacturer warns prescribing physician; physician is learned intermediary; but learned intermediary doctrine does NOT apply where manufacturer directly promotes product to consumer (direct-to-consumer advertising)

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **Product label / warning label** — Adequacy of warnings under "failure to warn" theory; must be in accessible language; must address known risks; must be conspicuous
- **Recall notice** — NHTSA/CPSC recall; timing relative to injury; was product recalled before injury? Did manufacturer have knowledge of defect before injury?
- **Manufacturer's design specifications** — Design defect; departure from spec = manufacturing defect; unreasonable design = design defect
- **Vehicle inspection report** — Expert assessment of stripped/stolen vehicle condition; VIN verification; component identification
- **Medical device 510(k) or PMA filing** — FDA premarket clearance; substantial equivalence; device performance standard

---

## SOC CONTROLS

- **NHTSA (National Highway Traffic Safety Administration)** — Vehicle recalls; Technical Service Bulletins; defect investigations
- **CPSC (Consumer Product Safety Commission)** — Non-vehicle consumer product defects; recall database
- **FDA MAUDE (Manufacturer and User Facility Device Experience)** — Medical device adverse events; implant failure reports
- **VICP (Health Resources & Services Administration)** — Vaccine Injury Compensation Program; covered vaccine list; VICP filing prerequisite before tort suit against manufacturer

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `greenman_strict_products_liability` | Greenman (1963) — strict liability | BUILD FIRST — foundational |
| `barker_design_defect_test` | Barker (1978) — design defect tests | BUILD SECOND |
| `ccp_338_property_fraud_sol` | CCP §338 — 3-year SOL | BUILD THIRD — timeliness gate |
| `com_2314_implied_warranty_merchantability` | COM §2314 — warranty (fetch needed) | BUILD FOURTH |
| `vicp_300aa_11_preemption` | 42 USC §300aa-11 — VICP (fetch needed) | BUILD FIFTH — SIRVA track |

---

## HISTORICAL CHAIN SEED

**The wound:** Before Greenman (1963), an injured consumer had to prove manufacturer negligence — a nearly impossible task when the manufacturing process was hidden inside the factory. Privity of contract further limited who could sue. Justice Traynor's Greenman opinion was a revolution: place a defective product in the stream of commerce, someone is injured, you pay — full stop. No negligence required. The wound that followed was not legislative — it was doctrinal erosion. By the time Barker (1978) created the risk-utility test, manufacturers gained a foothold: if the benefits of the design outweigh the risks, even a dangerous design is not actionable. Fifty years of product liability jurisprudence is essentially a tug-of-war over who bears the cost of industrialization's casualties. The Greenman principle — that manufacturers who profit from distribution bear the cost of defects — remains California law. But every plaintiff must still fight to keep it.

---

## CROSS-REFERENCES

- `CA_Vehicle_Code_Specialist` → RedJag stolen/stripped vehicle (VEH code violations are the regulatory track; product liability is the tort track)
- `CA_Consumer_Protection_Litigator` → CLRA; UCL §17200; warranty claims (parallel to strict liability)
- `CA_Medical_Malpractice_Litigator` → Spine surgery Dr. Wiseman; implant failure; learned intermediary doctrine intersection
- `US_Federal_Civil_Rights_Litigator` → VICP preemption (federal); if manufacturer fraud = false claims act angle
- `HERALD` → Will witness product recall notices, NHTSA complaints, medical device adverse event reports
