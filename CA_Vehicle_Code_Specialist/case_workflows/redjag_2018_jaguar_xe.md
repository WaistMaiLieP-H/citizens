# Case Workflow — RedJag 2018 Jaguar XE

**Case:** #1 — RedJag 2018 Jaguar XE fraud
**Citizen:** CA_Vehicle_Code_Specialist (primary on vehicle side; CA_Consumer_Protection_Litigator primary on financing)
**Drafted:** 2026-04-15
**Status:** COUNTERSIGNED-BY-HERALD

## Facts (as currently documented)

- Dealer delivered a 2018 Jaguar XE on spot-delivery (contract contingent on financing)
- CARFAX provided was for a different vehicle (wrong CARFAX / vehicle-history fraud)
- Vehicle appears to have been stolen and/or stripped and reassembled
- Buyer paid $10,000 cash as down payment / out-of-pocket
- Third-party financing was not consummated on original terms
- Dealer did not return trade-in, did not return down payment, did not rescind
- $19,985 is asserted as active debt (debt collection currently live)
- 63 pages scanned under `${nonfamilylaw}/RedJag/`

## Applicable standards (pleading inventory)

### Vehicle Code (owned here)

1. **VEH § 11700** — Dealer licensing (confirm active licensure at time of sale)
2. **VEH § 11713(a), (u), (k)** — Untrue advertising, inaccurate history representation, no-downpayment misrepresentation
3. **VEH § 5900** — Title transfer / odometer disclosure (wrong CARFAX = false mileage/history if mileage falsified)
4. **VEH § 10751** — Altered/removed VIN (if VIN tampering evidence present on stripped vehicle)
5. **BPC § 9880 et seq.** — Automotive Repair Act (any "reconditioning" invoices without written estimates)

### Warranty (state + federal)

6. **CIV § 1793.2 (Song-Beverly)** — Repair or restitution; 2x civil penalty for willful; attorney's fees to prevailing buyer
7. **15 U.S.C. § 2301 (Magnuson-Moss)** — Implied-warranty-of-merchantability lock via § 2308; federal forum available if AIC > $50K; fees to prevailing consumer

### Financing (reference copy here; primary home Consumer_Protection)

8. **CIV § 2982 (Rees-Levering)** — Itemized-disclosure + § 2982.5 yo-yo unwind + § 2983 rescission + § 2984.4 willfulness penalty

## Theory of the case

**Three independent recovery paths, each sufficient alone:**

**Path A — Rescission via Rees-Levering § 2982.5:** Spot-delivered, financing never consummated on original terms → dealer must rescind, return $10K down + trade-in, discharge $19,985 asserted debt. Two-way attorney's fees under § 2983.4.

**Path B — Restitution via Song-Beverly § 1793.2(d)(2):** Vehicle nonconforming to express warranty (if any express warranty given — confirm). If nonconforming, manufacturer must replace or restitute; 2x civil penalty under § 1794(c) if willful; one-way fees under § 1794(d). Magnuson-Moss § 2308 locks implied warranty of merchantability; stripped/stolen vehicle is not merchantable.

**Path C — Vehicle Code civil/criminal remedies:** VEH § 11713 prohibited-act penalties; § 5900 intent-to-defraud criminal/civil; § 10751 VIN-tampering — these create independent recovery and are predicate facts for willfulness under Path A and Path B.

## Forum choice

- **State court (Superior Court, county of purchase):** Full state statutes; no AIC threshold.
- **Federal court (N.D. Cal.):** Available under Magnuson-Moss § 2310(d)(3) if AIC > $50K. Likely threshold met: $10K down + $19,985 debt + purchase-price restitution + consequential + 2x civil penalty = well over $50K.

## Pre-filing checklist

- [ ] Pull leginfo HTML + hash all referenced CA statutes (§§ 1793.2, 1793.22, 1794, 1795.5, 2981-2984.6, VEH 5900, 10751, 11700, 11713)
- [ ] Pull uscode.house.gov + hash 15 USC §§ 2301-2312
- [ ] Pull 16 CFR Parts 700-703
- [ ] HERALD authentication pass on the 63-page RedJag scan set
- [ ] Confirm dealer licensure status on date of sale (DMV OL database)
- [ ] Confirm CARFAX discrepancy with run-date VIN-specific pull
- [ ] Document each out-of-service / repair attempt (for § 1793.22(b) presumption)
- [ ] Confirm whether any written warranty was offered (triggers Magnuson-Moss § 2308)
- [ ] Verify whether $19,985 debt has been assigned / reported to credit bureaus (additional FCRA claim)

## Coordination

- **CA_Consumer_Protection_Litigator** — Rees-Levering primary home; draft § 2982 / § 2982.5 pleading
- **US_Federal_Financial_Fraud_Litigator** — FCRA / FDCPA if $19,985 reported to bureaus or collection activity ongoing
- **HERALD** — document authentication, contradictions log across 63-page scan set
- **CA_Insurance_Compliance_Litigator** — if forced GAP was included in financing (§ 790.03)

## Status signals

- **ADAM first witness:** APPROVE — 2026-04-15
- **HERALD countersign:** COUNTERSIGN — 2026-04-15
- **Publication:** PUBLISHED
