# SOURCE PREP: CA_Vehicle_Code_Specialist
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** ANCHORS_FETCHED (VEH §§11700/11713/5900/10751; BPC §§9880/9884/9884.7/9884.9)
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- RedJag 2018 Jaguar XE: yo-yo financing, wrong CARFAX (vehicle history fraud), stolen/stripped vehicle delivered, $10K cash lost, $19,985 debt collection active, 63 pages scanned
- Toyota Camry XSE: separate vehicle fraud; exact facts TBD at build time

---

## ANCHOR STATUTES — FETCH REQUIRED

### CAL. VEH. CODE § 11700 — Dealer licensing requirement
**Text:** FETCHED (full text — 2026-04-12)
**Key holding:** No person shall act as dealer, remanufacturer, manufacturer, or transporter without first being issued a license or temporary permit; when license canceled/suspended/revoked, inventory may only be sold wholesale to a licensed dealer; any consigned vehicle must be returned to consignor; non-consigned vehicles in possession returned to owner.
**Standard ID:** `veh_11700_dealer_licensing`

### CAL. VEH. CODE § 11713 — Prohibited dealer acts
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- **§11713(a):** No untrue or misleading statements in any advertising or public communication
- **§11713(b):** No advertising vehicle not actually for sale or available directly from manufacturer
- **§11713(d):** Cannot represent used vehicle as new
- **§11713(k):** Cannot advertise "no downpayment" unless genuinely no payment required
- **§11713(u):** Cannot advertise prior use or ownership history in an inaccurate manner
- **§11713(v)(1):** Cannot offer subscription service for features using hardware already installed that would function without ongoing cost — *directly applicable to yo-yo financing feature misrepresentation*
- **§11713(l):** Dealer must pay full tax due on transfer to DMV — failure to do so is prohibited act
**Standard ID:** `veh_11713_dealer_prohibited_acts`

### CAL. VEH. CODE § 5900 — Transfer of title / odometer disclosure
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- Within 5 calendar days of sale, owner must notify DMV: date, name/address of owner and transferee, vehicle description
- **§5900(b):** Owner must notify DMV of actual odometer mileage at time of transfer; if owner knows displayed mileage is incorrect, must indicate true mileage if known
- Providing false or inaccurate mileage = violation if done with INTENT TO DEFRAUD
- References 49 USC §32705 (federal odometer disclosure — cross-reference to federal fetch)
**Standard ID:** `veh_5900_title_transfer_odometer`

### CAL. BUS. & PROF. CODE §§ 9880 et seq. — Automotive Repair Act (BAR)
**Text:** FETCHED (§9880 = title citation; §§9884/9884.7/9884.9 operative provisions — 2026-04-12)
**Key holdings:**

**BPC §9884 (Registration):**
- Automotive repair dealer must pay fee and register with director; forms include: name, phone, email, location address, zoning compliance statement, seller's permit number, motor vehicle license plate if mobile repairs; fictitious name must be stated

**BPC §9884.7 (Grounds for discipline):**
- License may be denied/suspended/revoked for: untrue/misleading statements; failure to give customer copy of signed work order; any conduct constituting fraud; gross negligence; willful departure from accepted trade standards; making false promises to induce repair authorization; having work done by third party without customer knowledge/consent; fraud = misrepresentation of material fact, false promise, intentional failure to disclose

**BPC §9884.9 (Written estimate requirement):**
- MUST give written estimated price for labor and parts before any work begins — NO WORK shall proceed without authorization
- No charge in excess of estimate without oral OR written consent obtained after determining estimate is insufficient
- Oral consent: dealer must note on work order — date, time, name of authorizing person, phone number, additional parts/labor, total additional cost
- Body/collision repairs: itemized written estimate required; each part identified as new/used/rebuilt/reconditioned; OEM vs. aftermarket crash part identification
- Exception: preventative maintenance services displayed at posted price
**Standard ID:** `bpc_9880_automotive_repair_act`

### CAL. VEH. CODE § 10751 — Altered/removed VIN — FETCHED
**Text:** FETCHED (full text — 2026-04-12)
**Key holdings:**
- No person shall knowingly buy, sell, offer for sale, receive, or possess any vehicle or component part from which manufacturer's serial or identification number has been REMOVED, DEFACED, ALTERED, OR DESTROYED
- Exception: if replacement ID number assigned/approved by DMV
- When such vehicle seized: must be destroyed, sold, or disposed by court order UNLESS owner presents satisfactory evidence of ownership + new ID number assigned
- Court hearing required within 90 days of seizure; seizing agency bears burden of establishing VIN tampering
- Scrap metal processors exempt
**Standard ID:** `veh_10751_vin_tampering`
**NOTE:** This replaces the erroneous §4160 note in original prep. §4160 (address update on registration card) is NOT a stolen vehicle statute.

### CAL. VEH. CODE § 11615 — Conditional sale contracts (yo-yo financing)
- **What it does:** Conditional sales (financing contingent on third-party approval) — if dealer represents financing as final then "unwinds" it = Rees-Levering violation AND unfair practice
- **NOTE:** Yo-yo financing is primarily a Rees-Levering (CIV §2981 et seq.) violation ALREADY IN CA_Consumer_Protection_Litigator — this Citizen covers the VEHICLE CODE side; coordinate
- **Fetch:** leginfo → VEH § 11615

### ~~CAL. VEH. CODE § 4160~~ — CORRECTION
- **ORIGINAL NOTE WAS WRONG:** VEH §4160 is about updating the ADDRESS on a registration card after a registered owner moves — not stolen vehicle registration
- **REPLACE WITH:** VEH §10751 (above) — the actual VIN/stolen vehicle statute; FETCHED

### 49 USC § 32703 — Federal odometer fraud (Motor Vehicle Information and Cost Savings Act)
- **What it does:** Criminal and civil liability for odometer tampering; private right of action; $10,000 actual damages or three times actual damages, whichever is greater
- **Fetch:** uscode.house.gov → Title 49 → § 32703

---

## CROSS-REFERENCES

- `CA_Consumer_Protection_Litigator` → Rees-Levering (CIV §2981 — yo-yo financing already built); CLRA; UCL
- `CA_Insurance_Compliance_Litigator` → forced GAP insurance; unauthorized rate manipulation
- `HERALD` → Will witness RedJag documents (63 pages), wrong CARFAX report, debt collection records
