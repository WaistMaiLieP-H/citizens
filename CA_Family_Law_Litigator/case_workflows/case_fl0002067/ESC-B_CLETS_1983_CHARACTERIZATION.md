# ESC-FL0002067-B — CLETS Face-of-Order § 1983 Injury Characterization

**Escalation ref:** ESC-FL0002067-B (ADAM NF-003 → EVE-DEPUTY)
**Scope:** 42 U.S.C. § 1983 characterization of CLETS footprint + 8 audit findings on DV-130 (2025-08-19)
**Resolution:** CHARACTERIZATION-ISSUED

---

## 1. Data-chain footprint (from ADAM NF-003, incorporated by reference)

- 11 `CLETS-OAH` header/footer references on DV-130 form face.
- 1 substantive line (OCR line 553): "Law Enforcement Telecommunications System (CLETS), or in an NCIC Protection Order File must enforce the orders."
- 8 `CLETS-001` rule findings in `AUDIT_2025-08-19.json` flagging: *"CLETS access must be logged with purpose and accessor ID — no access log documented."*

## 2. Governing § 1983 framework

42 U.S.C. § 1983 reaches any person who, "under color of" state law, subjects another to the deprivation of "rights, privileges, or immunities secured by the Constitution and laws." *Gomez v. Toledo*, 446 U.S. 635, 640 (1980). A judicially-issued DVRO entered into CLETS/NCIC is action "under color of state law" per se — the statewide telecommunications database is a state instrumentality operated by the California Department of Justice under Penal Code §§ 13100–13104 and Family Code § 6380(a). *West v. Atkins*, 487 U.S. 42, 49 (1988) (color-of-law is the use of power "possessed by virtue of state law and made possible only because the wrongdoer is clothed with the authority of state law," quoting *United States v. Classic*, 313 U.S. 299, 326 (1941)).

## 3. Finding-by-finding mapping

### CLETS-001 Finding #1 — No accessor-ID log on CLETS entry

| Element | Characterization |
|---|---|
| Right implicated | **Fourteenth Amendment procedural due process** (Fifth via incorporation for federal actors). |
| Color-of-state-law | CA DOJ operates CLETS under Penal Code § 13100 et seq.; Marin Superior Court clerk caused the entry; any downstream officer accessing without logging acts under state authority. |
| Injury element | **Stigma-plus.** Public/law-enforcement database entry labeling Michael Hartmann a domestic abuser, coupled with tangible legal disabilities (firearm prohibition under 18 U.S.C. § 922(g)(8); travel/encounter consequences), satisfies *Paul v. Davis*, 424 U.S. 693, 711–12 (1976), as refined by *Wisconsin v. Constantineau*, 400 U.S. 433, 437 (1971) (stigmatization + state-imposed disability = liberty-interest deprivation requiring notice and hearing). 9th Cir.: *Ulrich v. City & Cnty. of San Francisco*, 308 F.3d 968, 982 (9th Cir. 2002); *Humphries v. County of Los Angeles*, 554 F.3d 1170, 1185–88 (9th Cir. 2009) (CACI listing creates stigma-plus requiring meaningful procedures), *rev'd on other grounds*, 562 U.S. 29 (2010) — stigma-plus analysis remains good 9th Cir. law on remand, *Humphries v. County of Los Angeles*, 638 F.3d 1251 (9th Cir. 2011). |
| Available remedy | Damages under § 1983; injunctive expungement of the CLETS entry as violative of due process (*Humphries*, 554 F.3d at 1201–03, remedial framework). |
| Controlling authority | USSC: *Paul v. Davis*, 424 U.S. 693 (1976); *Wisconsin v. Constantineau*, 400 U.S. 433 (1971); *Mathews v. Eldridge*, 424 U.S. 319, 335 (1976) (balancing for process due). 9th Cir.: *Humphries*, 554 F.3d 1170, 1185–88 (9th Cir. 2009); *Ulrich*, 308 F.3d at 982. |

### CLETS-001 Findings #2–#8 — Recurring no-log, no-purpose-stated audit defects

Characterization identical to Finding #1. Each unlogged access is a **discrete** due-process event for accrual purposes (*see* ESC-D analysis) and compounds the *Mathews v. Eldridge* imbalance: the private interest is at maximum (liberty, reputation, firearm possession, encounter-with-LE risk); the government's marginal cost of logging is trivial; the risk of erroneous deprivation absent logging is high.

### Additional 1A and 4A overlays on the CLETS footprint as a whole

- **First Amendment (retaliation / chilling).** If the DVRO issuance is shown (pending on working_theories and dossier.md) to have been procured on knowingly false declarations, the CLETS entry operates as state-authored reputational punishment that chills protected petitioning speech against the petitioner and her state-dispatcher co-actors. *Nieves v. Bartlett*, 587 U.S. 391, 404 (2019) (retaliation standard); *Hartman v. Moore*, 547 U.S. 250, 256 (2006) (causation in retaliation); 9th Cir.: *Capp v. County of San Diego*, 940 F.3d 1046, 1053 (9th Cir. 2019).
- **Fourth Amendment (informational privacy / seizure-adjacent).** An unaudited CLETS record can function as the justification for later stops and seizures. To the extent an unlogged entry is used as the sole predicate for a Terry stop or custodial arrest, the fruits doctrine reaches back to the database defect. *Herring v. United States*, 555 U.S. 135, 146–47 (2009) (systemic recordkeeping negligence can trigger exclusion); *Arizona v. Evans*, 514 U.S. 1, 14–16 (1995).
- **Fourteenth Amendment equal protection.** Selective enforcement — CLETS entries generated against respondents in DVROs while the *petitioner*'s parallel conduct (counter-filing playbook per project_christina_pattern.md) generates no database footprint — sounds in class-of-one EP under *Village of Willowbrook v. Olech*, 528 U.S. 562, 564 (2000), if a similarly-situated comparator is identified. 9th Cir.: *Gerhart v. Lake County*, 637 F.3d 1013, 1022 (9th Cir. 2011).

## 4. Injury taxonomy summary

| Injury | Doctrinal home | Key pinpoint |
|---|---|---|
| Stigma-plus (liberty + reputation) | 14A procedural DP | *Paul v. Davis*, 424 U.S. at 711–12; *Humphries*, 554 F.3d at 1185–88 |
| Deprivation-of-liberty-interest (firearm prohibition attaches on CLETS entry) | 14A DP / 2A overlay | 18 U.S.C. § 922(g)(8); *U.S. v. Rahimi*, 602 U.S. 680, 693–96 (2024) (2A framework; process still due on underlying order) |
| Chilling of protected speech | 1A | *Nieves*, 587 U.S. at 404; *Capp*, 940 F.3d at 1053 |
| Informational-privacy / unreliable-predicate seizures | 4A | *Herring*, 555 U.S. at 146; *Arizona v. Evans*, 514 U.S. at 14 |
| Class-of-one selective database enforcement | 14A EP | *Olech*, 528 U.S. at 564; *Gerhart*, 637 F.3d at 1022 |

## 5. Remedies

- § 1983 damages (compensatory for stigma-plus and collateral consequences; nominal if actual damages unquantified per *Carey v. Piphus*, 435 U.S. 247, 266 (1978); presumed damages unavailable without actual injury showing).
- Injunctive expungement of the CLETS/NCIC entry (*Humphries*, 554 F.3d at 1201–03).
- Declaratory judgment that unlogged CLETS access violates due process (framework from *Mathews*, 424 U.S. at 335).
- Attorney fees under 42 U.S.C. § 1988 upon prevailing-party status.

## 6. Residual verification flag (for EVE)

- Each pinpoint above was drawn from published decisions; EVE should confirm subsequent history on *Humphries* (Supreme Court reversal on *Monell* indemnity ground only; stigma-plus due-process holding survived on 9th Cir. remand) and on *Rahimi* as applied to 18 U.S.C. § 922(g)(8) procedural sufficiency.
- The 8 CLETS-001 audit findings are ADAM's count per `AUDIT_2025-08-19.json`; EVE should re-open the audit JSON and confirm each finding carries identical language before incorporating into a complaint paragraph.

## 7. Witness chain

```yaml
witness_chain:
  author: EVE-DEPUTY
  authored_at_utc: 2026-04-15T00:00:00Z
  signal: CHARACTERIZATION-ISSUED
  eve_countersign: PENDING
  custos_gate: PENDING
```
