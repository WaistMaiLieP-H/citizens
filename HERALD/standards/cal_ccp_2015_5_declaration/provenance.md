# Layer 5 — Verifiable Provenance
## CAL_CCP_2015_5 | Primary Sources and Verification Chain

**Standard ID:** CAL_CCP_2015_5
**Filed:** 2026-04-12
**Witness:** PROPOSED — requires steward review

---

## Primary Source

| Field | Value |
|---|---|
| Statute | California Code of Civil Procedure § 2015.5 |
| Official text source | California Legislative Information — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=2015.5 |
| Fetched | 2026-04-12 (this session, via VernenLegal MCP — leginfo.legislature.ca.gov) |
| Text verified | Yes — full verbatim text retrieved and reproduced in rule.md |
| Current law | Active — no pending repeal or amendment noted |

---

## Legislative History Note

CCP § 2015.5 is California's parallel to 28 U.S.C. § 1746. The California provision predates the federal statute — it was enacted to address the same access-to-justice concerns. No major amendments to the substantive perjury-phrase and signature requirements have been documented in recent decades; the form has been stable.

---

## Case Law — California Courts

### The place-of-execution requirement

**[STEWARD: California case law specifically addressing the place-of-execution defect under § 2015.5(a) has not been retrieved this session. HERALD notes the requirement is explicit in the statute — "states the date and place of execution" — and recommends using Form (b) universally to eliminate this risk. Primary-source case citation is pending.]**

Flag: No specific case citation retrieved for the place-of-execution defect. The requirement is textual, not case-law-derived. Risk mitigation = use Form (b).

---

### CalVCB-specific authority

**Government Code § 13959** (CalVCB hearing procedure):

**[STEWARD: HERALD has not retrieved § 13959 directly this session. The CalVCB standard is owned by CA_Victim_Compensation_Litigator (CAL_GOV_13959). HERALD flags: the § 13959 appeal declaration should be reviewed in conjunction with the CA_Victim_Compensation_Litigator's CAL_GOV_13959 standard to confirm the applicable form. This is a cross-citizen dependency.]**

---

### Penal Code § 118 (Perjury — California)

| Field | Value |
|---|---|
| Authority | California Penal Code § 118 |
| Source | California Legislative Information — https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=PEN&sectionNum=118 |
| Status | Active |
| Relevance | The criminal enforcement mechanism for § 2015.5 declarations — a false declaration is perjury under § 118 |
| Verification | Text not retrieved this session; widely known, stable statute; retrieve before citing in any filing |

---

## Offensive Use — Unsigned Reports in the Steward's Cases

The three unsigned police reports identified in HERALD's family law chronology (case_familylaw_defective_reports_chronology.md) cannot satisfy § 2015.5 because they are unsigned — they fail element 6 (signature). Under California law, an unsigned report is not a sworn declaration and cannot carry the evidentiary weight of a sworn statement. HERALD has flagged these reports as defective sworn evidence throughout the case record.

**Primary source for the signature requirement:** CCP § 2015.5 text — "is subscribed by him or her." An unsigned document is not subscribed.

---

## Verification Checklist

| Item | Status |
|---|---|
| Statutory text retrieved from leginfo.legislature.ca.gov | DONE — 2026-04-12 |
| Verbatim text reproduced in rule.md | DONE |
| Penal Code § 118 text retrieved | PENDING — flagged for retrieval before first use in filing |
| CalVCB § 13959 form requirement confirmed | PENDING — cross-citizen dependency (CA_Victim_Compensation_Litigator) |
| California case law on place-of-execution defect | PENDING — not retrieved; Form (b) mitigates |
| Opposing declarations audit (unsigned reports) | COMPLETE in historical_loss.md — textual basis confirmed |

---

## Manifest

```json
{
  "standard_id": "CAL_CCP_2015_5",
  "popular_name": "California declarations under penalty of perjury",
  "citizen_owner": "HERALD",
  "filed": "2026-04-12",
  "status": "PROPOSED",
  "two_witness_status": {
    "status": "PROPOSED",
    "witness_1": null,
    "witness_2": null
  },
  "herald_witness": {
    "status": "SELF — HERALD is the owner; external witness required",
    "note": "HERALD cannot self-witness its own standards. Requires steward review."
  },
  "layers_complete": {
    "rule": true,
    "reasoning": true,
    "historical_loss": true,
    "cross_refs": true,
    "provenance": true
  },
  "primary_source": "CCP § 2015.5 — California Code of Civil Procedure",
  "source_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CCP&sectionNum=2015.5",
  "priority": "CRITICAL",
  "use_in_cases": [
    "CalVCB_A25-10117946",
    "criminal_04-23-01959",
    "FamilyLaw_RF09456481",
    "Honeysuckle_CA_fraud_track",
    "DVRO_challenge"
  ],
  "flags": [
    "Penal Code § 118 text not yet retrieved — retrieve before citing in any filing",
    "CalVCB § 13959 form requirement — cross-citizen dependency with CA_Victim_Compensation_Litigator",
    "California case law on place-of-execution defect not retrieved — use Form (b) universally as mitigation"
  ],
  "version": "1.0.0"
}
```
