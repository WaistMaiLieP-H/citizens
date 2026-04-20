# PROCEDURAL COMPLIANCE AUDIT
## OPD Incident Report 09-011438 | February 15, 2009
### Auditing Citizen: CA_Law_Enforcement_Procedures_Specialist

---

## PHASE 1: ENCOUNTER CLASSIFICATION MEMO

**Encounter Type:** Domestic Violence Response
**Incident Number:** 09-011438
**Date/Time:** February 15, 2009, 03:05–03:20
**Location:** [redacted] Marshall St., Oakland, CA 94608
**Agency:** Oakland Police Department

---

### Officers Identified

| Role | Emp# | Badge# | Name |
|---|---|---|---|
| Primary Assigned Officer | 8402 | — | HAZELWOOD, DAVID |
| Secondary Responding Officer | 8831 | — | LEE, MEGA |
| Primary Reporting Officer | 8775 | — | NGUYEN, MY |
| Primary Responding Officer | 8775 | — | NGUYEN, MY |
| Primary Reporting Officer / Reviewer | 8950 | — | RUSSELL, DEREK |
| Statement Officer (named in narrative) | 8923 | — | KATZ (first name not listed) |
| Admonishment Officer (named in narrative) | 8948 | — | VAN SCOY (first name not listed) |
| Approving Supervisor | — | — | CHAN, ROBERT |
| Supervising Sergeant (named in narrative) | — | 7552 | KIM (first name not listed) |

**Note:** Badge numbers are not populated in the officer table for most entries. Badge numbers appear only in the narrative for Sgt. Kim (#7552), Ofc. Katz (#8923), and Ofc. Van Scoy (#8948). This is an administrative documentation gap.

---

### Persons Involved

| Role | Name | Age | Sex | Race |
|---|---|---|---|---|
| Arrestee / Suspect | CERRETANI, CHRISTINA MARIE | 24 | F | WHITE |
| Victim | HARTMANN, MICHAEL VERNON | 30 | M | WHITE |
| Other (minor child referenced) | [redacted] | — | — | — |

---

### Timeline Reconstruction

| Time | Event |
|---|---|
| 02/15/2009 03:05 | Incident occurred (per CAD start) |
| 02/15/2009 03:15 | Officer contact with victim HARTMANN |
| 02/15/2009 03:20 | Incident end / report taken / narrative entered |
| 02/15/2009 03:30 | Associated arrest event ARR09-004984 |
| 02/19/2009 06:30 | Disposition: CLEARED — Complainant Refused |
| 03/04/2009 11:08 | Report approved by CHAN, ROBERT |

---

### DV Classification Determination

The incident is coded **DOMESTIC VIOLENCE** in the Incident Type field. The offense charged is **PC 243(e)(1) — Battery: Spouse/Ex-Spouse/Date/Etc.** with the DOM enhancer applied. The narrative confirms a marital relationship, cohabitation, and the presence of a minor child. This encounter is unambiguously a domestic violence call.

**DV classification triggers mandatory § 13701 protocols in their entirety.**

---

### System Anomaly Flag — "Domestic: N"

The Incident Summary header field "Domestic:" is populated as **"N"** (No) despite:
- The Incident Type being coded as DOMESTIC VIOLENCE
- The offense carrying a DOM enhancer
- The narrative describing a spousal battery
- An arrest being made for a domestic violence statute

This is an internal data inconsistency within the report. The "Domestic: N" field directly contradicts every other field in the document. **This discrepancy is flagged for investigative follow-up.** It may reflect a data entry error, a system field definition that differs from the DV classification (e.g., the "Domestic" field may track something narrower than the incident type classification), or it may reflect an attempt to suppress the DV coding in one data field while retaining it in others. The discrepancy is noted; its cause cannot be determined from this document alone.

---

### Missing Documents Flagged at Intake

| Document | Status | Applicable Standard |
|---|---|---|
| CAD dispatch log | NOT PRESENT — timeline gaps cannot be fully audited | § 13701 |
| Arrest report ARR09-004984 | NOT PRESENT — referenced but not produced | § 836 |
| Written statement from HARTMANN taken by Ofc. Katz | NOT PRESENT — referenced but not produced | § 13701 |
| Body-worn camera footage | N/A — BWC programs were not standard OPD deployment in 2009 | § 832.18 |
| Emergency Protective Order documentation | Referenced as refused by victim — no EPO record present | § 836(b) |
| Victim information card copy | Referenced as given — no copy retained in report | § 13701 |

---

## PHASE 2: STANDARDS AUDIT — Chronological Application

---

### STANDARD: PEN_CODE_13701_DV_RESPONSE

**Applicable Subsections:** § 13701(a) (written policies), § 13701(b) (victim information), § 13701(c) (mandatory report and required contents)

---

#### Element 1: Written DV Response Policy

**Status: INDETERMINATE**

The existence of OPD's written § 13701 policy cannot be confirmed or denied from this document. The report references DV-specific documentation fields (FBR Narrative structure, DV resource card notation), suggesting OPD had an operational DV reporting protocol in place. However, the written policy itself is not part of this production. **Recommended action:** Obtain OPD's written § 13701 DV response policy via CPRA request, specifically the version in effect on February 15, 2009.

---

#### Element 2: Mandatory Written Report

**Status: COMPLIANT**

A written incident report was completed. The FBR (Family/Domestic Violence Boilerplate Report) narrative is present. The report documents the DV offense, the arrest, and the circumstances. The report was completed at 03:20 on the date of the incident. ✓

---

#### Element 3: Mandatory Report Contents — Six Required Fields

**Rule:** § 13701(c) requires documentation of: (1) physical symptoms of abuse or injury visible to the officer; (2) demeanor of both parties at time of officer arrival; (3) names and ages of minor children present; (4) description of any weapons on the premises; (5) any threats made by either party; (6) actions taken by responding officers.

**Field-by-field audit:**

**(1) Physical symptoms of abuse or injury:**
**Status: COMPLIANT (with qualification)**
The narrative states: *"V-1 did not have any visible injuries and refused medical attention."* The absence of visible injury is documented. The report does not document whether the suspect showed any physical condition. Qualified compliant — the victim's condition is documented; the suspect's physical condition at booking is absent from this report (may be in the arrest report).

**(2) Demeanor of both parties at time of officer arrival:**
**Status: PARTIALLY DEFICIENT**

The Characteristics section for suspect CERRETANI documents demeanor as **"APOLOGETIC."** However, this field appears in the person-record section, not in the narrative as an observed fact at arrival. No corresponding demeanor observation is documented for **victim HARTMANN** — the report contains no demeanor field or narrative statement describing HARTMANN's demeanor upon officer contact. The victim's demeanor at time of contact is a required § 13701(c) element and is absent.

**(3) Names and ages of minor children present:**
**Status: DEFICIENT**

The narrative states: *"They have 2 [redacted]"* — the presence of minor children is referenced but the names and ages of the children are redacted in this production. Whether they were documented in the original report cannot be confirmed from this document. If the children's names and ages were present in the original and redacted for this production, this may be an appropriate privacy redaction. If they were absent from the original, this is a § 13701(c) violation. **Status assessed as INDETERMINATE** pending review of unredacted original. **This is a material gap requiring resolution.**

**(4) Description of any weapons on the premises:**
**Status: NON-COMPLIANT**

The report contains no documentation of whether any weapons were present on the premises. The Modus Operandi section's "Weapon Type" fields are blank. The narrative contains no statement that officers checked for or found/did not find weapons. A residential DV call at 03:05 in a home with a marital dispute, a battery, and a minor child present — and no weapons check is documented. This is an omission of a mandatory § 13701(c) field.

**(5) Any threats made by either party:**
**Status: NON-COMPLIANT**

The narrative describes the battery incident in detail but documents no inquiry into whether threats were made before, during, or after the incident. The FBR boilerplate section does not include a threats field. No narrative statement addresses whether HARTMANN reported threats or whether officers asked. The absence of this required field is a documented § 13701(c) omission.

**(6) Actions taken by responding officers:**
**Status: COMPLIANT**

The narrative documents: arrival, contact with victim, Ofc. Katz taking written statement, arrest of suspect, double-locking of handcuffs, transport to North County Jail, Ofc. Van Scoy's admonishment of suspect, DV resource card provision, victim's refusal of EPO. Officer actions are documented with reasonable specificity. ✓

---

#### Element 4: Victim Information — § 13701(b)

**Status: COMPLIANT**

The FBR section states: *"Domestic Violence Resource Card Given: Yes."* The narrative confirms: *"A domestic violence resource card was given to the victim."* Two independent notations confirm compliance. ✓

---

#### Element 5: Citizen's Arrest Advisement — § 836(b)

**Status: COMPLIANT (documented)**

The FBR section states: *"If misdemeanor case, was the victim advised of citizen's arrest procedures? Yes."* An arrest was made, which under § 836(b) excuses the advisement requirement — but officers documented it as given regardless, which exceeds the minimum requirement. ✓

---

#### Element 6: Dominant Aggressor Identification

**Status: INDETERMINATE — Requires Evaluation**

Section 13701 and associated POST guidelines require officers responding to DV calls to identify the dominant aggressor rather than defaulting to the person the victim identifies or the person the caller names. The report reflects: HARTMANN called 911 reporting his wife slapped him; CERRETANI was arrested. The narrative documents a single physical act (slap). The report does not reflect whether officers conducted a dominant aggressor analysis — whether they considered relative sizes (HARTMANN 5'9"/180 lbs, CERRETANI 5'2"/127 lbs), history of violence (documented as "None"), injuries, or fear indicators before determining who was the dominant aggressor. The arrest appears facially consistent with the reported facts, but the analytical process is not documented. **Recommended action:** Confirm whether OPD's § 13701 policy in effect in 2009 required documented dominant aggressor analysis and whether the FBR form satisfied that requirement.

---

#### Element 7: Prior Incident Documentation

**Status: COMPLIANT**

The FBR section documents: *"Dates of Previous Incidents (Month/Year): None"* and *"Total Reported Incidents: None."* Prior history is affirmatively documented. ✓

---

#### Element 8: Restraining Order Status

**Status: COMPLIANT**

The FBR section documents: *"Restraining Order in Effect: No."* ✓

---

#### Element 9: Victim Relocation

**Status: COMPLIANT**

The FBR section documents: *"Victim Relocated to an Alternate Shelter: No."* ✓

---

#### Element 10: Investigator Notification Advisement

**Status: DEFICIENT**

The FBR section states: *"Victim advised to notify the investigator of any address or phone number changes: No."* This is documented as **not done**. Whether this is a required element of OPD's § 13701 policy cannot be confirmed from this document alone, but the negative notation reflects an acknowledged departure from a policy element that was significant enough to include on the form.

---

### STANDARD: PEN_CODE_836_ARREST_AUTHORITY

**Applicable Subsections:** § 836(a)(1) (in-presence misdemeanor), § 836(b) (victim citizen's arrest advisement), § 836(d) (DV warrantless arrest authority)

---

#### Element 1: Lawful Basis for Warrantless Arrest

**Status: COMPLIANT**

The arrest of CERRETANI for PC 243(e)(1) was supported by probable cause. The victim (HARTMANN) was present and provided a contemporaneous account of being slapped by his wife while holding their child. A written statement was taken by Ofc. Katz. The relationship (married, cohabitant) satisfies the spousal battery statutory relationship element. The arrest occurred at 03:30 — ten minutes after incident documentation began — within the temporal window where probable cause was fresh.

The applicable authority is § 836(a)(1) (offense committed in officers' presence) or § 836(d) (DV warrantless arrest on probable cause). The narrative does not specify whether officers directly witnessed any portion of the battery, but the victim's immediate contemporaneous account, combined with the call to 911, provides sufficient probable cause under § 836(a)(3) or § 836(d). **Facially compliant.**

---

#### Element 2: EPO — Victim's Refusal

**Status: DOCUMENTED — No Deficiency**

The narrative states: *"V-1 also refused a E.P.O in hopes that him and his wife could work this out when she gets out of jail."* The EPO was offered and refused. An officer cannot compel an EPO application from an unwilling victim. Documentation of the offer and refusal is appropriate practice. ✓

---

#### Element 3: Victim's Refusal to Prosecute

**Status: DOCUMENTED — No Deficiency**

The FBR section documents: *"If the victim refuses to prosecute, list reasons: Did not want wife to go to jail or lose custody of child."* The refusal reason is captured. Case disposition of "Complainant Refused / Cleared" on 02/19/2009 is consistent with the documented victim position. ✓

---

### STANDARD: PEN_CODE_835A_USE_OF_FORCE

**Applicable Subsections:** § 835a(b) (necessity standard), § 835a(d)(3) (totality of circumstances including pre-force conduct)

---

#### Analysis

The report documents one use of force: the arrest and handcuffing of CERRETANI. The narrative states: *"I double locked S-1's handcuffs and transported her to North County Jail."* The double-locking notation indicates compliance with handcuffing standards (preventing tightening).

No non-consensual physical force beyond arrest and restraint is described. The arrest was lawful under § 836(d). Restraint incident to a lawful arrest is authorized and necessary by definition under § 835a.

**Status: COMPLIANT** — No force beyond lawful arrest restraint is documented or suggested by the record.

---

### STANDARD: PEN_CODE_832_18_BODY_CAMERAS

**Status: NOT APPLICABLE**

This incident occurred on February 15, 2009. Body-worn camera programs were not standard OPD deployment at that time. Section 832.18 (AB 66) was enacted in 2015. No BWC analysis applies to this incident.

---

### STANDARD: PEN_CODE_832_7_PEACE_OFFICER_RECORDS

**Status: INDETERMINATE — Cross-Reference Flag Only**

This document is the incident report itself, not a personnel record. However, several officers named in this report are also involved in the steward's 2023 Antioch incident. Section 832.7(b) is relevant to any subsequent investigation of those officers.

**Cross-reference note:** RUSSELL, DEREK (Badge 8950) is both Primary Reporting Officer and Reviewer on this 2009 OPD report. Any sustained misconduct findings against Officer Russell — including dishonesty (§ 832.7(b)(1)(C)) or unlawful arrest/search (§ 832.7(b)(1)(E)) — from this or any other incident are now publicly disclosable under SB 1421. **Recommended action:** Submit CPRA requests to OPD for § 832.7(b) disclosable records for all officers named in this report who have subsequent involvement in the steward's case.

---

### STANDARD: GOV_CODE_12525_2