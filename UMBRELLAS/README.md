# Vernen Substantive Umbrellas — Index

**Filed:** 2026-04-08
**Catalog source:** `citizens/UMBRELLAS.md` (the canonical narrative catalog)
**This file:** Folder index pointing to one README per umbrella

---

## What lives here

Each numbered subfolder represents one substantive umbrella in the Vernen corpus. The README in each subfolder contains:

- **Definition** — what the umbrella covers
- **Scope** — finer-grained sub-areas
- **Examples** — concrete standards that belong here
- **Canonical Citizen owners** — the professional roles/personas that work in this domain
- **Candidate seed standard** — the recommended first standard to build, with primary-source URL
- **Status** — which standards (if any) have already been built
- **Cross-cutting notes** — overlaps with other umbrellas

A standard belongs to one or more umbrellas. A standard *lives* in a Citizen folder (not in an umbrella folder). The umbrella folders are an *index* across Citizens, not a duplicate location for the standards themselves.

---

## The 18 umbrellas

| # | Umbrella | Status | Steward Relevance |
|---|---|---|---|
| 01 | [Authority / Governing Law](01_Authority/README.md) | seed identified | foundational to every other |
| 02 | [Procedure](02_Procedure/README.md) | seed identified | direct — § 1983 federal complaint |
| 03 | [Substance / Specification](03_Substance_Specification/README.md) | seed identified | trade — UA Local 342 |
| 04 | [Measurement / Metrology](04_Measurement_Metrology/README.md) | seed identified | indirect |
| 05 | [Safety](05_Safety/README.md) | **2 standards built** (Field Act witnessed; Riley Act proposed) | indirect |
| 06 | [Ethics / Conduct](06_Ethics_Conduct/README.md) | seed identified | direct — competence failures by appointed counsel |
| 07 | [Access / Inclusion](07_Access_Inclusion/README.md) | seed identified | indirect |
| 08 | [Environmental / External Impact](08_Environmental/README.md) | seed identified | indirect |
| 09 | [Integrity / Provenance / Records](09_Integrity_Provenance/README.md) | seed identified | **direct — chain-of-custody failures throughout case file** |
| 10 | [Privacy / Information Stewardship](10_Privacy_Information_Stewardship/README.md) | seed identified | **direct — medical fraud, HIPAA, CMIA** |
| 11 | **[Family / Personal Status](11_Family_Personal_Status/README.md)** | seed identified | **HIGHEST — the steward's entire case lives here** |
| 12 | [Property / Title / Ownership](12_Property_Title_Ownership/README.md) | seed identified | **direct — house sale fraud, recording acts** |
| 13 | [Finance / Money / Banking](13_Finance_Money_Banking/README.md) | seed identified | direct — Treasury fraud, Northern Trust |
| 14 | [Tax](14_Tax/README.md) | seed identified | indirect |
| 15 | [Communication / Speech / Press](15_Communication_Speech_Press/README.md) | seed identified | direct — anti-SLAPP relevant to retaliatory suits |
| 16 | [Travel / Movement / Immigration](16_Travel_Movement_Immigration/README.md) | seed identified | direct — Vehicle Code § 2800, June 16, 2023 incident |
| 17 | [Energy](17_Energy/README.md) | seed identified | indirect |
| 18 | [Agriculture / Food](18_Agriculture_Food/README.md) | seed identified | direct — peanut law example, school food safety |

---

## How to use this index when running the autopilot

For each umbrella, the README's "Candidate seed standard" section names a specific first standard to build with its primary-source URL. Feed those into `citizens/build_standard.py`:

```bash
python3 ${citizens}/build_standard.py \
  --id <STANDARD_ID> \
  --jurisdiction California \
  --year <YEAR> \
  --citizen <CITIZEN_FOLDER_NAME> \
  --source-url <PRIMARY_SOURCE_URL_FROM_README> \
  --pdf-pages <PAGE_RANGE> \
  --chapter <CHAPTER> \
  --popular-name "<NAME>"
```

Or queue them: put one per line in a text file, write a small wrapper that loops, schedule the wrapper via the `schedule` skill in the harness.

---

## Outstanding umbrella catalog work

Per `UMBRELLAS.md`, candidate umbrellas not yet promoted to first-class:

- **Religion / Conscience**
- **Education** — currently distributed across Authority, Access, and Privacy
- **Cyber / Information Security** — currently overlaps Integrity and Privacy
- **Defense / National Security**
- **Sports / Athletic Conduct**
- **Cultural Heritage / Antiquities**

Promotion of any of these requires (1) primary-source review of representative standards, (2) demonstration that the candidate is independent of every existing umbrella, and (3) steward concurrence on the addition.

---

**Filed:** 2026-04-08
**Status:** All 18 umbrellas have stub READMEs with candidate seed standards identified. Two standards (Field Act, Riley Act) are actually built under Umbrella 05 (Safety). One additional standard (Contractors State License Law 1929) is built under Umbrella 13 (Finance/Money/Banking) and Umbrella 06 (Ethics/Conduct) jointly. The remaining 17 umbrellas have seed standards identified but not yet built.
