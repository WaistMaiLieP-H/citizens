# CA_Family_Law_Litigator — Case Index

**Purpose:** Structured records for every case number in the steward's documented family-law case file. Each case has a JSON file with court, type, parties, dates, source folder, related actors, related standards, anomalies, and outstanding investigations.

**Filed:** 2026-04-08
**Citizen:** CA_Family_Law_Litigator
**Tether:** `../tether.json` (the binding manifest)

## Cases currently in index

| Case Number | Court | Type | Status | File |
|---|---|---|---|---|
| RF09456481 | Alameda Superior | Original DV / Custody | Anomalous disposition placement | [RF09456481.json](RF09456481.json) |
| RF09459897 | Alameda Superior | Counter-DV (Christina's) | Carries the 7/2/2009 disposition that belongs on RF09456481 | [RF09459897.json](RF09459897.json) |
| RF09470833 | Alameda Superior | Dissolution (Michael's) | VOIDED 2010-11-22 | [RF09470833.json](RF09470833.json) |
| RF10508853 | Alameda → Solano | Dissolution Ex Parte (Christina's) | Transferred to Solano 2025-06-25 | [RF10508853.json](RF10508853.json) |
| RF10508859 | Alameda Superior | Grandparent Visitation (Packard) | Michael NEVER SERVED | [RF10508859.json](RF10508859.json) |
| 25FL122591 | Alameda Superior | DVRO (Michael's, 2025) | Denied, dismissed 2025-06-25 | [25FL122591.json](25FL122591.json) |
| 25FL125059 | Alameda Superior | DVRO (Christina's counter, 2025) | Denied, dismissed 2025-06-25 | [25FL125059.json](25FL125059.json) |
| **FL0002067** | **Marin Superior** | **Active DVRO (Christina's, jurisdictional flip)** | **ACTIVE — expires 2026-08-19** | [FL0002067.json](FL0002067.json) |
| 04-23-01959 | Contra Costa Superior | Criminal / Competency | Active investigation | [04-23-01959.json](04-23-01959.json) |

## The case theory at a glance

1. **Origin (2009-02-15):** Christina is documented as Suspect S-1 in a slap incident involving the steward and their infant son. SHE is the originally documented abuser. No charges filed.
2. **Original DVRO (RF09456481, 2009-06-08):** Michael files. Paredes mediation 7/2/2009 produces favorable result (sole custody, supervised visitation for Christina). Judge Thompson adopts.
3. **Counter-filing (RF09459897, 2009-06-26):** Christina files counter-DV 18 days later. The 7/2/2009 disposition that belongs on RF09456481 is anomalously placed on RF09459897.
4. **2010-09-02 reversal (RF09456481):** Sala Ajaniku (zero verifiable credentials) issues a recommendation that REMOVES protective supervision. Judge Delucchi adopts.
5. **Coordinated triple filing (2010-04-09):** Christina's ex parte dissolution (RF10508853), Ann Marie Packard's grandparent visitation (RF10508859, Michael never served), and a duplicate dissolution all filed the same day.
6. **Michael's dissolution voided (RF09470833, 2010-11-22):** No documented reason.
7. **14-year silence (2010-2024):** No filings by Christina during the years she had no custody and no RO against Michael.
8. **2025 jurisdictional trap:** Michael files Alameda DVRO (25FL122591). Christina counter-files (25FL125059) 20 days later. Both dismissed 6/25/2025 but Christina's response survives. Christina then takes Cole to Marin and files FL0002067 22 days later — jurisdictional flip across counties.
9. **Currently active:** FL0002067 (Marin DVRO, expires 2026-08-19) is the ONLY active custody-affecting order against Michael.

The pending state action against Christina is presumably aimed at vacating or undermining FL0002067, OR is a separate civil action arising from the same 16-year course of conduct.

## Schema

Each case record contains:
- `case_number`, `court`, `jurisdiction`, `type`
- `petitioner`, `respondent`
- `filed_date`, `current_status`
- `key_dates` — chronological events
- `source_folder` — path on disk to the case file artifacts
- `related_actors` — list of actor_ids
- `related_standards` — list of standard_ids from the corpus
- `related_cases` — cross-references to other cases
- `known_anomalies` — structural irregularities flagged for litigation
- `outstanding_investigations` — open questions about this case
- `filed_at_utc`

## Outstanding case index work

- Locate source folders for cases not yet matched (RF09459897, RF10508859, 25FL122591, 25FL125059, FL0002067, 04-23-01959)
- Add detailed key-dates for cases that currently have only partial timelines
- Connect each case to specific document paths within its source folder
- Build a unified timeline across all cases (next pass)
