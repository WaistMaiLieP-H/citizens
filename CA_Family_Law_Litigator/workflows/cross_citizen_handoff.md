# Cross-Citizen Handoff

**Citizen:** CA_Family_Law_Litigator
**Created:** 2026-04-15
**Purpose:** Routing matrix for evidence that must be forwarded to sibling Citizens for analysis outside this Citizen's professional lane.

---

## Routing Principle

This Citizen audits family law compliance. When evidence surfaces issues in criminal law, insurance, probate/conservatorship, mental health, or telecom privacy, the evidence is forwarded to the specialist Citizen. The forwarding Citizen retains a copy and notes the handoff. The receiving Citizen processes the evidence under its own standards. Neither Citizen crosses into the other's domain.

---

## Routing Matrix by Investigation

### INV-01: OPD Records Pickup Audit

| Evidence Type | Forward To | Reason |
|---|---|---|
| OPD report with POST violations (POST-002B) | **CA_Criminal_Law_Specialist** | POST protocol violations are criminal law standards, not family law |
| Filing citing nonexistent OPD report (perjury) | **CA_Criminal_Law_Specialist** | Penal Code § 118 (perjury) audit; family law retains § 2015.5 and § 3027 angles |

### INV-02: Ajaniku PRA Request

| Evidence Type | Forward To | Reason |
|---|---|---|
| No records found (credential void confirmed) | No handoff — stays in family law | § 3164/1815/1816 is this Citizen's core domain |

### INV-03: Paredes License Verification

| Evidence Type | Forward To | Reason |
|---|---|---|
| No Board of Psychology license found | No handoff — stays in family law | § 3164/1815 is this Citizen's core domain |
| Confirmed unlicensed practice | **CA_Criminal_Law_Specialist** | Bus. & Prof. Code § 2903 criminal violation |

### INV-04: Conservatorship Existence Search

| Evidence Type | Forward To | Reason |
|---|---|---|
| Conservatorship docket found (any county) | **CA_Probate_Conservatorship_Litigator** | Root mechanism — Probate Code §§ 1800-1898 audit. This is THE critical handoff. |
| Conservatorship docket found + medical records access | **CA_Probate_Conservatorship_Litigator** + **CA_Mental_Health_Litigator** | Probate for the conservatorship itself; Mental Health for LPS/WIC § 5150/§ 5350 overlay |
| Sealed record found in probate court | **CA_Probate_Conservatorship_Litigator** | Unsealing strategy is probate domain |
| Florida guardianship found | **CA_Probate_Conservatorship_Litigator** | Interstate conservatorship under Uniform Adult Guardianship and Protective Proceedings Jurisdiction Act |

### INV-05: CMIA Disclosure Log Subpoenas

| Evidence Type | Forward To | Reason |
|---|---|---|
| § 56.10(c)(12) disclosure to probate court investigator | **CA_Probate_Conservatorship_Litigator** + **CA_Mental_Health_Litigator** | Probate for the conservatorship; Mental Health for the CMIA violation and medical privacy breach |
| § 56.10(c)(12) disclosure to domestic relations investigator | Stays in family law (+ copy to **CA_Probate_Conservatorship_Litigator**) | Domestic relations investigator is family law, but the (c)(12) mechanism may still indicate conservatorship |
| Provider's CMIA log shows unauthorized access (no (c)(12) basis) | **CA_Criminal_Law_Specialist** | Unauthorized medical records access — Penal Code § 502 / CMIA § 56.36 criminal penalties |

### INV-06: Mediator Switch Reason

| Evidence Type | Forward To | Reason |
|---|---|---|
| Any response | No handoff — stays in family law | Mediator assignment is § 3164 domain |

### INV-07: Marin August 2025 Hearing

| Evidence Type | Forward To | Reason |
|---|---|---|
| Transcript showing § 217 testimony right violation | No handoff — stays in family law | § 217 is family law; feeds to case_fl0002067 and federal complaint |
| Transcript showing UCCJEA jurisdictional defect | No handoff — stays in family law | § 3048 is family law |
| Evidence of CLETS misuse in the hearing | **CA_Criminal_Law_Specialist** | CLETS violations are criminal (Penal Code § 11142 et seq.) |

### INV-08: Fee Waiver Filing Error

| Evidence Type | Forward To | Reason |
|---|---|---|
| Any response | No handoff — stays in family law | Procedural; feeds to case_25fl122591 and case_rf10508853 |

### INV-09: Benicia PD Call Recordings

| Evidence Type | Forward To | Reason |
|---|---|---|
| Recordings showing law enforcement non-response | **CA_Criminal_Law_Specialist** | Penal Code § 13701 DV response protocol violations; feeds to federal § 1983 complaint |
| Recordings showing coordination with another party | **CA_Criminal_Law_Specialist** | Possible conspiracy / obstruction |
| Recordings destroyed despite litigation hold | **CA_Criminal_Law_Specialist** | Spoliation; Penal Code § 135 (destroying evidence) |

### INV-10: Dual Filing Status

| Evidence Type | Forward To | Reason |
|---|---|---|
| Any response | No handoff — stays in family law | Procedural anomaly |

### INV-11: Carrier Communications / Device Proximity

| Evidence Type | Forward To | Reason |
|---|---|---|
| SIM swap records | **CA_Telecom_Privacy_Litigator** | SCA § 2703 / CPNI § 222 / Pen. Code § 502 — telecom privacy domain |
| CSLI data showing device co-location (6/16/2023) | **CA_Telecom_Privacy_Litigator** + **CA_Criminal_Law_Specialist** | Telecom for SCA analysis; Criminal for potential stalking / conspiracy evidence |
| Account recovery logs showing unauthorized access | **CA_Telecom_Privacy_Litigator** | CFAA / Pen. Code § 502 analysis |
| Any carrier record implicating Ryan McClaran | **CA_Telecom_Privacy_Litigator** + **CA_Criminal_Law_Specialist** | Telecom for the mechanism; Criminal for the actor |

---

## Routing Matrix by Receiving Citizen

### CA_Criminal_Law_Specialist
Receives evidence involving: POST violations, perjury (Pen. § 118), unlicensed practice (B&P § 2903), unauthorized medical records access (Pen. § 502), CLETS misuse, law enforcement protocol violations (Pen. § 13701), spoliation (Pen. § 135), stalking, conspiracy, obstruction.

### CA_Probate_Conservatorship_Litigator
Receives evidence involving: any conservatorship docket, any § 56.10(c)(12) disclosure to a probate court investigator, sealed probate records, interstate guardianship.

### CA_Mental_Health_Litigator
Receives evidence involving: LPS/WIC § 5150/§ 5350 overlay on conservatorship, CMIA violations with medical privacy component, any 5150 hold documentation.

### CA_Insurance_Compliance_Litigator
Receives evidence involving: insurance coverage denials connected to conservatorship, any State Farm / Northern Trust records discovered through family law investigations.

### CA_Telecom_Privacy_Litigator
Receives evidence involving: SIM swaps, CSLI data, account recovery logs, carrier records, SCA/CPNI/CFAA violations, any records implicating Ryan McClaran's digital operations.

---

## Handoff Protocol

1. **Create handoff record:** File `handoff_<timestamp>_<receiving_citizen>.json` in this Citizen's `junctions/` directory.
2. **Contents of handoff record:**
   - `source_citizen`: CA_Family_Law_Litigator
   - `receiving_citizen`: [name]
   - `investigation_id`: [source investigation]
   - `evidence_description`: [what is being forwarded]
   - `evidence_path`: [file path to the evidence]
   - `routing_reason`: [why this goes to the receiving Citizen]
   - `handoff_at_utc`: [timestamp]
3. **Copy evidence** to the receiving Citizen's intake path (or reference by path if co-located).
4. **Do not interpret** the evidence under the receiving Citizen's standards. The forwarding Citizen describes what was received; the receiving Citizen applies its own analysis.
