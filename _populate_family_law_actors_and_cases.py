#!/usr/bin/env python3
"""
_populate_family_law_actors_and_cases.py

Generates the structured actor records and case records for the
CA_Family_Law_Litigator Citizen, populating the actors/ and cases/
subdirectories enumerated in tether.json.

Each actor record is a JSON file with: identity, role, credentials,
case involvement, risk assessment, outstanding investigations, sources.

Each case record is a JSON file with: case number, court, parties,
dates, disposition, source folders, related actors, related standards,
known anomalies.

Run from ${citizens}/.
"""

import json
from pathlib import Path

NOW = "2026-04-08T18:05:00Z"
BASE = Path("${citizens}/CA_Family_Law_Litigator")
ACTORS = BASE / "actors"
CASES = BASE / "cases"


# ============================================================================
# ACTORS
# ============================================================================

ACTOR_RECORDS = [
    {
        "filename": "paredes_olga.json",
        "data": {
            "actor_id": "paredes_olga",
            "canonical_name": "Olga Paredes, Ph.D.",
            "aliases": ["Olga Paredes", "Olga Paredes, Ph.D.", "Olga Paredes (forensic psychologist, claimed)"],
            "role": "Child Custody Mediator (Court-connected, Alameda County)",
            "professional_identity": {
                "claimed_title": "Psychotherapist, Forensic Psychologist, Mediator (per LinkedIn)",
                "education_claimed": "Ph.D. — The Wright Institute, Berkeley, CA",
                "credential_concern": "The Wright Institute grants PsyD degrees, not Ph.D. The Ph.D. claim may be a credential misrepresentation (PsyD vs. Ph.D.)",
                "employer_at_time_of_service": "Alameda County Superior Court, Family Court Services",
                "current_location": "Richmond, CA",
                "external_listings": ["WebMD (Psychology, Richmond CA)", "courtlicensedabuse.com (cataloged by family court litigants)"],
                "linkedin": "https://www.linkedin.com/in/olga-paredes-ph-d-8402489b/"
            },
            "credential_verification": {
                "ca_board_of_psychology_license_number": "NOT FOUND through web-accessible public search",
                "dca_license_search_result": "No specific result returned for 'Olga Paredes' through web search queries",
                "board_of_behavioral_sciences": "Not found",
                "verification_status": "UNVERIFIED — direct DCA license search and Board of Psychology contact required",
                "ca_family_code_3164_compliance_assessment": "PsyD or Ph.D. from Wright Institute would satisfy educational requirement under § 3164 / § 1815. License-at-time-of-service is the unresolved question. In California one cannot use the title 'forensic psychologist' without a Board of Psychology license (Bus. & Prof. Code § 2903)."
            },
            "case_involvement": [
                {
                    "case_number": "RF09456481",
                    "date": "2009-07-02",
                    "action": "Issued mediation recommendation under California Family Code §§ 3164, 1815",
                    "outcome": "Sole legal/physical custody to Michael Hartmann; Christina Cerretani restricted to SUPERVISED visitation",
                    "outcome_classification": "FAVORABLE to the steward",
                    "judge_who_adopted": "Trina Thompson"
                }
            ],
            "risk_level": "MEDIUM",
            "risk_basis": "Credentials exist but are unverified; outcome was favorable; Ph.D./PsyD discrepancy needs resolution",
            "outstanding_investigations": [
                {
                    "id": "paredes_dca_search",
                    "question": "Does Olga Paredes hold a valid California Board of Psychology license? What is the license number? Was it valid in July 2009?",
                    "unblock": "Direct DCA License Search at search.dca.ca.gov for 'Olga Paredes'",
                    "alternate_unblock": "Phone California Board of Psychology at 916-574-7720 for license verification"
                },
                {
                    "id": "paredes_wright_institute",
                    "question": "What degree did Olga Paredes actually earn from the Wright Institute — Ph.D. or PsyD?",
                    "unblock": "Contact Wright Institute Registrar's office for degree verification"
                },
                {
                    "id": "paredes_employment_status",
                    "question": "Was Olga Paredes a court employee or independent contractor in July 2009?",
                    "unblock": "Public Records Act request to Alameda County Superior Court for her employment records and qualifications on file"
                },
                {
                    "id": "paredes_courtlicensedabuse",
                    "question": "What is the basis of her listing on courtlicensedabuse.com?",
                    "unblock": "Review the site listing"
                }
            ],
            "standards_governing_this_actor": [
                "Cal. Family Code § 3164 (custody mediator qualifications) — NOT YET BUILT in corpus",
                "Cal. Family Code § 1815 (counselor of conciliation qualifications) — NOT YET BUILT in corpus",
                "Cal. Family Code § 1816 (mediator DV training requirement) — NOT YET BUILT in corpus",
                "Cal. Rules of Court Rule 5.210 (court-connected mediation procedures) — NOT YET BUILT in corpus",
                "Cal. Bus. & Prof. Code § 2903 (psychologist title restriction) — NOT YET BUILT in corpus"
            ],
            "source_citations": [
                "${familylaw}/CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_audit.md"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "ajaniku_sala.json",
        "data": {
            "actor_id": "ajaniku_sala",
            "canonical_name": "Sala Ajaniku",
            "aliases": [],
            "role": "Child Custody Mediator (Court-connected, Alameda County, presumed)",
            "professional_identity": {
                "title_used_in_court": "Child Custody Mediator",
                "presumed_employer": "Alameda County Superior Court, Family Court Services",
                "credential_concern": "ZERO professional credentials found in ANY public database. No license, no degree confirmation, no LinkedIn, no professional directory presence."
            },
            "credential_verification": {
                "ca_board_of_psychology_license": "ZERO results",
                "ca_board_of_behavioral_sciences_license": "ZERO results (LCSW, LMFT, LPCC all checked)",
                "dca_license_search_result": "ZERO results",
                "linkedin": "ZERO results",
                "psychology_today_directory": "ZERO results",
                "webmd_provider_directory": "ZERO results",
                "goodtherapy_directory": "ZERO results",
                "google_scholar": "ZERO results",
                "court_mediator_panels_alameda_adr": "ZERO results",
                "any_professional_directory": "ZERO results",
                "verification_status": "CRITICAL — zero verifiable professional presence; cannot file licensing-board complaint because no licensing board exists for an unlicensed person",
                "ca_family_code_3164_compliance_assessment": "Without verifiable credentials, cannot determine whether Ajaniku met the master's-degree-and-two-years-experience baseline of § 3164 / § 1815. Without a license, cannot determine whether DV training under § 1816 was completed."
            },
            "case_involvement": [
                {
                    "case_number": "RF09456481",
                    "date": "2010-09-02",
                    "action": "Issued mediation recommendation that REVERSED the prior 2009-07-02 protective recommendation by Olga Paredes",
                    "outcome": "DVRO modified; Christina Cerretani granted UNSUPERVISED visitation (previously supervised)",
                    "outcome_classification": "ADVERSE to the steward — removed protective supervision",
                    "judge_who_adopted": "Paul A. Delucchi",
                    "anomaly": "A person with NO verifiable credentials made a recommendation that overturned a previous recommendation by a credentialed professional. The judge adopted it without apparent verification of the recommender's qualifications."
                }
            ],
            "risk_level": "CRITICAL",
            "risk_basis": "Zero verifiable credentials; adverse outcome (removed protective supervision); no accountability mechanism (no licensing board to complain to); resulted in modification of a protective DVRO",
            "outstanding_investigations": [
                {
                    "id": "ajaniku_pra",
                    "question": "What were Sala Ajaniku's actual credentials, employment status, and qualifications in September 2010?",
                    "unblock": "Public Records Act request to Alameda County Superior Court for: (a) all employment records, (b) qualifications and resume on file, (c) hiring documentation, (d) the original 09/02/2010 mediation report identifying any credentials listed",
                    "priority": "HIGHEST — load-bearing for the credential audit and for the steward's case theory"
                },
                {
                    "id": "ajaniku_alameda_hr",
                    "question": "Does Alameda County HR have any record of this individual?",
                    "unblock": "PRA to Alameda County HR"
                },
                {
                    "id": "ajaniku_name_variants",
                    "question": "Are there alternative spellings of the name that might surface credentials?",
                    "unblock": "Search variant spellings of first and last name"
                },
                {
                    "id": "ajaniku_current_employment",
                    "question": "Does this person still work for any California court?",
                    "unblock": "Court-system search across California county Superior Courts"
                }
            ],
            "standards_governing_this_actor": [
                "Cal. Family Code § 3164 (custody mediator qualifications)",
                "Cal. Family Code § 1815 (counselor of conciliation qualifications)",
                "Cal. Family Code § 1816 (mediator DV training requirement)",
                "Cal. Rules of Court Rule 5.210 (court-connected mediation procedures)",
                "Cal. Rules of Court Rule 5.215 (DV-related mediation requirements)"
            ],
            "source_citations": [
                "${familylaw}/CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_audit.md"
            ],
            "case_theory_significance": "The Ajaniku credential void, combined with the mediator switch (Paredes → Ajaniku) and the resulting protective-order modification, may constitute additional evidence of due process violations in the family court proceedings — relevant to both the federal § 1983 complaint and any state-court motion to vacate orders that flowed from the 2010-09-02 hearing.",
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "ditsworth_david.json",
        "data": {
            "actor_id": "ditsworth_david",
            "canonical_name": "David Alan Ditsworth, MD",
            "aliases": ["David Ditsworth", "David Ditsworth, MD"],
            "role": "SSA Disability Report Author (consultative or records-review)",
            "professional_identity": {
                "specialty": "Neurological Surgery (board-certified)",
                "npi_number": "1376685420 (registered since 2007-02-13)",
                "medical_school": "University of Utah School of Medicine, Class of 1972",
                "residency": "Yale-New Haven Medical Center (1973-1975, Neurological Surgery); UC Irvine (1976-1979, Neurological Surgery)",
                "primary_affiliation": "Cedars-Sinai Medical Center (on staff since 1983)",
                "practice": "Back Institute Surgery Center, Beverly Hills/Los Angeles",
                "office_address": "920 S Robertson Blvd, Los Angeles, CA 90035",
                "phone": "310-551-0690",
                "title": "Founder and Chief of Neurosurgery, Back Institute Surgery Center (Nano Back Institute)",
                "linkedin_title": "CEO, Back Surgery Institute",
                "approximate_age_in_2023": "~77 years",
                "years_in_practice": "51+",
                "publications": "40+ peer-reviewed abstracts, articles, book chapters",
                "innovation": "Developed 'Non-Traumatic Discectomy' for herniated/bulging discs"
            },
            "credential_verification": {
                "ca_medical_board_license": "License exists (verifiable at mbc.ca.gov; specific license number requires direct lookup)",
                "board_certification": "Neurosurgery (confirmed by multiple sources)",
                "npi_registry_status": "Active",
                "disciplinary_actions": "None found through web-accessible searches",
                "verification_status": "VERIFIED as a credentialed neurosurgeon; the question is not whether he has credentials but whether they are appropriate for the role he was used in"
            },
            "the_critical_problem": {
                "summary": "Specialty mismatch — board-certified neurosurgeon used as a medical source to DENY disability claim involving conditions outside neurosurgery",
                "details": [
                    "NOT A TREATING PHYSICIAN: Ditsworth does not appear in the steward's medical records as a treating physician",
                    "SPECIALTY MISMATCH: Per SSA POMS DI 24501.001, while SSA does not have strict rules about which specialist reviews which claim, a mismatch between examiner specialty and claimant conditions is a valid basis for appeal",
                    "CONFLICT OF INTEREST POTENTIAL: A surgeon whose career is built on performing spinal procedures has a professional bias toward viewing spine conditions as surgically treatable rather than disabling",
                    "AGE AND PRACTICE CONTEXT: At ~77 in 2023, with 51 years of practice focused on elective spine surgery at a Beverly Hills surgery center, his practice context is far removed from disability determination",
                    "TWO-REPORT DENIAL: SSA used only TWO medical reports to deny the claim. Having one of those two come from a neurosurgeon who never treated the claimant is a significant due process concern"
                ]
            },
            "case_involvement": [
                {
                    "case_number": "SSA Disability Claim",
                    "date": "2023-01-03 (report received by SSA)",
                    "action": "Issued medical opinion used to deny the steward's disability claim",
                    "outcome": "ADVERSE — disability claim denied; one of only two medical reports used in the denial",
                    "outcome_classification": "ADVERSE"
                }
            ],
            "risk_level": "HIGH",
            "risk_basis": "Fully credentialed but wrong specialty; one of only two reports used to deny disability; not a treating physician; practice context (Beverly Hills elective spine surgery) is incongruent with disability evaluation",
            "outstanding_investigations": [
                {
                    "id": "ditsworth_ssa_form_831",
                    "question": "What does SSA Form SSA-831 (Disability Determination and Transmittal) show as Ditsworth's specialty code?",
                    "unblock": "Obtain SSA Form SSA-831 from the disability claim file"
                },
                {
                    "id": "ditsworth_ce_vs_records_review",
                    "question": "Did Ditsworth perform a Consultative Examination or only a records review?",
                    "unblock": "Obtain the full Ditsworth report"
                },
                {
                    "id": "ditsworth_dds_selection",
                    "question": "How did the DDS select Ditsworth as an evaluator? Is he registered as a DDS CE provider?",
                    "unblock": "FOIA / SSA records request"
                },
                {
                    "id": "ditsworth_full_report",
                    "question": "What conditions did Ditsworth evaluate?",
                    "unblock": "Obtain the full Ditsworth report"
                },
                {
                    "id": "ditsworth_mbc_license",
                    "question": "What is the exact CA Medical Board license number and current status?",
                    "unblock": "Direct lookup at mbc.ca.gov"
                }
            ],
            "standards_governing_this_actor": [
                "SSA POMS DI 24501.001 (DDS Examiner Roles)",
                "SSA HALLEX II-4-1-2 (CE Standards)",
                "Bus. & Prof. Code § 2052 et seq. (Medical Practice Act)"
            ],
            "source_citations": [
                "${familylaw}/CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_medical_fraud_timeline.md"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "thompson_trina_judge.json",
        "data": {
            "actor_id": "thompson_trina_judge",
            "canonical_name": "Trina Thompson",
            "aliases": ["Hon. Trina Thompson", "Judge Trina Thompson"],
            "role": "Judge, Alameda County Superior Court",
            "professional_identity": {
                "judicial_office": "Alameda County Superior Court (verified)"
            },
            "credential_verification": {
                "verification_status": "VERIFIED as a sitting judge",
                "next_step": "Confirm dates of service in 2009 family-law assignment via California Courts judge directory or Alameda County Superior Court history"
            },
            "case_involvement": [
                {
                    "case_number": "RF09456481",
                    "date": "2009 (specifically the 7/2/2009 hearing)",
                    "action": "Adopted Olga Paredes' mediation recommendation",
                    "outcome": "Sole legal/physical custody to Michael Hartmann; Christina Cerretani restricted to supervised visitation",
                    "outcome_classification": "FAVORABLE to the steward"
                }
            ],
            "risk_level": "LOW (favorable rulings)",
            "outstanding_investigations": [
                {
                    "id": "thompson_dates_of_service",
                    "question": "What were Judge Thompson's dates of service in the Alameda County Family Court assignment?",
                    "unblock": "California Courts judge directory; Alameda County Superior Court history"
                },
                {
                    "id": "thompson_2010_assignment",
                    "question": "Why was Judge Thompson NOT the judge at the 2010-09-02 hearing where Sala Ajaniku's recommendation was adopted? Was she rotated off, retired, or recused?",
                    "unblock": "Alameda County Superior Court assignment records"
                }
            ],
            "source_citations": [
                "${familylaw}/CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_audit.md"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "delucchi_paul_judge.json",
        "data": {
            "actor_id": "delucchi_paul_judge",
            "canonical_name": "Paul A. Delucchi",
            "aliases": ["Hon. Paul A. Delucchi", "Judge Paul A. Delucchi", "Paul Delucchi"],
            "role": "Judge, Alameda County Superior Court",
            "professional_identity": {
                "judicial_office": "Alameda County Superior Court (verified)"
            },
            "credential_verification": {
                "verification_status": "VERIFIED as a sitting judge",
                "next_step": "Confirm dates of service and the specific assignment that placed him on RF09456481 in 2010"
            },
            "case_involvement": [
                {
                    "case_number": "RF09456481",
                    "date": "2010-09-02",
                    "action": "Adopted Sala Ajaniku's mediation recommendation",
                    "outcome": "DVRO modified; Christina Cerretani granted UNSUPERVISED visitation (previously supervised under Judge Thompson's 2009 ruling)",
                    "outcome_classification": "ADVERSE to the steward — reversed protective structure"
                }
            ],
            "risk_level": "HIGH",
            "risk_basis": "Adopted recommendation from a person with ZERO verifiable credentials (Sala Ajaniku); reversed protective DVRO without apparent verification of the recommender's qualifications; both judge and mediator changed simultaneously without documented reason",
            "outstanding_investigations": [
                {
                    "id": "delucchi_qualification_verification",
                    "question": "Did Judge Delucchi verify Sala Ajaniku's credentials before adopting her recommendation? Is there any record in the case file of credential review?",
                    "unblock": "Review the original 2010-09-02 hearing transcript and order"
                },
                {
                    "id": "delucchi_assignment_history",
                    "question": "Why was Judge Delucchi assigned to RF09456481 in 2010 when Judge Thompson had been the prior judge?",
                    "unblock": "Alameda County Superior Court assignment records"
                },
                {
                    "id": "delucchi_judicial_conduct",
                    "question": "Are there any judicial conduct complaints or appellate reversals associated with Judge Delucchi?",
                    "unblock": "California Commission on Judicial Performance records; appellate court records"
                }
            ],
            "source_citations": [
                "${familylaw}/CREDENTIAL-AUDIT-AJANIKU-PAREDES-DITSWORTH-2026-03-23.md"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "wiita_patrick.json",
        "data": {
            "actor_id": "wiita_patrick",
            "canonical_name": "Patrick Wiita, Dr.",
            "aliases": ["Dr. Wiita", "Dr. Patrick Wiita"],
            "role": "Competency Evaluator (Contra Costa County, criminal/competency case 04-23-01959)",
            "professional_identity": {
                "specialty": "TBD — to be confirmed",
                "case_involvement_summary": "Authored a competency evaluation for case 04-23-01959 that the case_audit_2026-03-17 describes as 'self-contradicting, template boilerplate, evaluated while high'"
            },
            "credential_verification": {
                "verification_status": "OUTSTANDING — needs MBC license lookup if MD; needs Board of Psychology lookup if Ph.D./PsyD",
                "next_step": "Direct license verification at mbc.ca.gov or psychology.ca.gov depending on specialty"
            },
            "case_involvement": [
                {
                    "case_number": "04-23-01959",
                    "date": "TBD",
                    "action": "Authored competency evaluation",
                    "outcome": "ADVERSE — evaluation was self-contradicting, template boilerplate, and per the steward, evaluated while the steward was under the influence",
                    "outcome_classification": "ADVERSE"
                }
            ],
            "risk_level": "HIGH",
            "risk_basis": "Per case_audit_2026-03-17: self-contradicting, template boilerplate, evaluated while high. Specialty appropriateness for competency evaluation TBD.",
            "outstanding_investigations": [
                {
                    "id": "wiita_specialty",
                    "question": "What is Dr. Wiita's actual specialty? Is competency evaluation within his scope of practice?",
                    "unblock": "License lookup at mbc.ca.gov"
                },
                {
                    "id": "wiita_evaluation_circumstances",
                    "question": "What were the circumstances of the evaluation? When was it performed? Was the steward under medical or substance influence at the time?",
                    "unblock": "Review the full Wiita evaluation report"
                },
                {
                    "id": "wiita_template_audit",
                    "question": "Is the template-boilerplate concern verifiable by comparing the Wiita report to other Wiita evaluations?",
                    "unblock": "Compare against other Wiita evaluations if available"
                }
            ],
            "source_citations": [
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_audit.md (forensic finding #10: 'Dr. Wiita competency evaluation audit (self-contradicting, template boilerplate, evaluated while high)')"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "cerretani_christina.json",
        "data": {
            "actor_id": "cerretani_christina",
            "canonical_name": "Christina Marie Cerretani",
            "aliases": [
                "Christina Marie Hartmann (during marriage 2009-2010)",
                "Christina Hartmann",
                "Christina Cerretani"
            ],
            "do_not_confuse_warning": "'Cappellini' appearing on the 2010 FL-100 is an OCR scan artifact, NOT a real prior name",
            "role": "Opposing party (former spouse, current opposing party in family-court matters)",
            "personal_identity": {
                "dob": "1984-08-23 (some filings show 1988)",
                "address_clusters": [
                    "San Francisco — 732 Divisadero, 428 Ellsworth",
                    "Benicia — 801 Southampton Rd #28"
                ]
            },
            "documented_pattern": {
                "summary": "16-year pattern of conduct as documented across 317 case-file documents in 3 review periods 2009-2025; the originally documented abuser per Alameda County Sheriff report 09-011438 (2/15/2009)",
                "origin_event": {
                    "date": "2009-02-15",
                    "report": "Alameda County Sheriff 09-011438",
                    "facts": "Christina slapped Michael in the face while he held their infant son Cole",
                    "her_status": "Suspect S-1",
                    "her_demeanor_recorded": "apologetic",
                    "outcome": "No charges filed despite SHE being the documented suspect"
                },
                "counter_filing_playbook": {
                    "description": "Every restraining order or criminal incident against her triggers a counter-DV filing within 2-3 weeks",
                    "instances": [
                        "2009-06-08 TRO against her → 2009-06-26 her counter DV-100 (18 days)",
                        "2025-05-15 Michael's DV-100 → 2025-06-04 her counter DV-100 in Alameda 25FL125059 (20 days)",
                        "2025-07-13 Ann Hillberg hands Cole to her → 2025-07-17 her DVRO in Marin FL0002067 (4 days, different jurisdiction)"
                    ]
                },
                "custody_history": {
                    "summary": "Has held lawful custody of Cole for less than 90 days out of his entire ~17-year life",
                    "details": "From 6/29/2009 court order through 7/17/2025 Marin DVRO, custody was Father's. The Marin DVRO is the only window in which she has it."
                },
                "statutory_failure_pattern_in_her_filings": [
                    "Civ. Code § 1633.7 — signatures not valid/attributable",
                    "Evidence Code § 1401 — exhibits and attachments fail authentication",
                    "CCP § 2015.5 — declarations missing penalty-of-perjury language",
                    "CCP § 1005(b) — motions filed without proper notice timing (15 failures in 2025 range alone)",
                    "Welfare & Institutions Code § 5150 — psychiatric hold standards referenced without basis",
                    "Penal Code § 11166 — child abuse allegations without mandatory cross-reporting",
                    "POST DV Response Guidelines — recurring violations",
                    "Penal Code §§ 836(c) / 13701 — felony DV alleged in reports she generated, no arrest documented (post-2026-04-07 overlay rule)"
                ],
                "narrative_escalation_by_year": {
                    "2009": "DV only, no drugs, no child abuse",
                    "2010": "Adds: bruises on Cole, nutritional neglect, flight risk, drug history (from age 18)",
                    "2025": "Adds: meth, stalking, firearms, kidnapping risk, animal abuse, technology abuse, DV shelter"
                },
                "the_2009_06_11_fabrication_finding": {
                    "date_added_to_pattern": "2026-04-07",
                    "summary": "The 2009-06-11 OPD report (09-040089) is the document where Christina frames the TRO and 5150 evaluation as Michael 'calling police and saying I was suicidal'",
                    "real_event": "The actual 5150 incident happened ~6/2/2009 after Christina pulled a 10-inch kitchen knife. Michael called 911 from down the street with factual details only. 1 officer + 2 EMTs responded. Officer gave Christina ultimatum: hand over Cole or it would be taken; either way 72-hour eval. She handed Cole over and went. Was out and messaging Michael within ~3 hours.",
                    "the_evidentiary_finding": "In October 2025 Michael picked up OPD records — only 2 reports exist for the entire situation. The 6/2/2009 5150 incident report is NOT among them. It is missing or was never written.",
                    "the_6_11_report_post_violations": [
                        "Walk-up civil standby intake (POST forbids) — POST-002A overlay rule",
                        "Single phone call attempt to Michael (primarily to confirm availability)",
                        "Felony abuse allegation forwarded to DA on single-party statement without arrest attempt — PC § 836(c) violation",
                        "POST-002B overlay rule (felony DV without arrest) catches this report",
                        "Real civil standby on a different unrecalled date had officer-segregation (Michael ordered to wait at curb, Christina stole property)"
                    ]
                },
                "she_does_not_act_alone": [
                    "2010-04-09: Her FL-100 filed same day as Ann Marie Packard's GC-220 grandparent visitation petition",
                    "2025-07-13 to 2025-07-17: Ann Hillberg handed Cole to her 4 days before Marin DVRO filed",
                    "Maternal-female-relative pairing is a recurring operational signature"
                ],
                "the_load_bearing_pattern": "This isn't a bitter ex-spouse using family court. This is a 16-year operation that uses fabricated or selectively-curated police records as the load-bearing beam under every custody and restraining-order action. The 14-year silence between 2010 and 2024 (no filings of her own during years she had no custody and no RO against Michael) confirms her court activity is reactive and instrumental, not chronic."
            },
            "case_involvement": [
                {"case_number": "RF09456481", "role": "Respondent", "date_range": "2009-2010+"},
                {"case_number": "RF09459897", "role": "Petitioner (counter-DV)", "date": "2009-06-26"},
                {"case_number": "RF09470833", "role": "Respondent", "date": "2009-08"},
                {"case_number": "RF10508853", "role": "Petitioner (ex parte dissolution)", "date": "2010-04-09"},
                {"case_number": "25FL125059", "role": "Petitioner (counter-DV 2025)", "date": "2025-06-04"},
                {"case_number": "FL0002067", "role": "Petitioner (Marin DVRO)", "date": "2025-07-17"}
            ],
            "risk_level": "OPPOSING PARTY",
            "outstanding_investigations": [
                {
                    "id": "christina_2009_06_02_incident",
                    "question": "Where is the 6/2/2009 5150 incident report? It is not in OPD records per October 2025 pickup.",
                    "unblock": "Cross-check Alameda County Sheriff records and Oakland Fire / EMS records (the 2 EMTs would have generated their own report)"
                },
                {
                    "id": "christina_dob_discrepancy",
                    "question": "Why do some filings show DOB 1988 instead of 1984?",
                    "unblock": "Compare birth certificate against filings"
                },
                {
                    "id": "christina_civil_capacity",
                    "question": "Does Christina herself have any conservatorship, capacity issue, or third-party-control structure that would explain the pattern?",
                    "unblock": "Probate court docket searches across counties"
                }
            ],
            "source_citations": [
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_christina_pattern.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_christina_custody_history.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_orchestration.md"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "hillberg_ann.json",
        "data": {
            "actor_id": "hillberg_ann",
            "canonical_name": "Ann Hillberg",
            "aliases": ["Ann Marie Packard (legal/maiden name on grandparent visitation petition)", "Ann Hillberg"],
            "role": "Mother of Christina Marie Cerretani; documented orchestrator (per project_familylaw_orchestration.md)",
            "professional_background": {
                "summary": "State police/emergency dispatcher 2008-2015 (SURCOMM, CENCOMM, NORCOM); transferred to Napa State Hospital 2015",
                "trained_for": "Dispatching CHP and local police; CAD language; police-report generation patterns",
                "doctrinal_significance": "Her dispatcher training explains the precision of 911 calls, knowledge of how to generate police reports without arrests, CAD language usage, and coordinated legal filings hitting every judicial trigger"
            },
            "documented_pattern": {
                "unsigned_police_reports": [
                    {
                        "date": "2009-02-15",
                        "report": "09-011438",
                        "fact": "Christina slaps Michael, SHE is arrested, report UNSIGNED by officer and supervisor; no charges filed"
                    },
                    {
                        "date": "2009-06-11",
                        "report": "OPD 09-040089",
                        "fact": "FELONY PC § 273.5(A) report against Michael; UNSIGNED; no arrest (mandatory arrest offense); no dispatch authorization for 'civil standby'; one phone call as entire investigation; Christina's mother staged the contact with officer"
                    }
                ],
                "coordinated_triple_filing_2010_04_09": [
                    "Christina's ex parte (FL-310/MC-020) — every trigger word for child abuse, neglect, flight risk, drugs",
                    "Ann Marie Packard's grandparent visitation petition (Family Code § 3104) — Christina as illegal co-filer despite 0% custody, restraining order, court-ordered psychiatric treatment",
                    "Duplicate dissolution filing (illegal — one already existed)",
                    "Grandparent visitation served by mail on the same day filed — likely mailed to Christina (co-filer), not Michael (custodial parent)"
                ],
                "repeated_pattern": [
                    {"date": "2009-06-11", "action": "Stages unauthorized civil standby", "result": "Unsigned felony report against Michael"},
                    {"date": "2010-04-09", "action": "Orchestrates triple filing", "result": "Custody/visitation challenge"},
                    {"date": "2023-06-16", "action": "911 call using dispatcher language: 'known to smoke meth'", "result": "Cole removed by APD without checking custody"},
                    {"date": "2023-06-22", "action": "Positions Cole in pre-furnished Benicia apartment with Christina", "result": "Cole gone 6 days"},
                    {"date": "2025-07-08", "action": "Hands Cole to Christina at night during transfer window", "result": "Cole taken to Marin County"}
                ]
            },
            "case_involvement": [
                {"case_number": "RF10508859", "role": "Petitioner (grandparent visitation)", "date": "2010-04-09", "anomaly": "Michael NEVER SERVED"}
            ],
            "risk_level": "ORCHESTRATOR — DOCUMENTED",
            "outstanding_investigations": [
                {
                    "id": "hillberg_dispatcher_records",
                    "question": "What were Ann Hillberg's specific duties and access at SURCOMM, CENCOMM, NORCOM 2008-2015?",
                    "unblock": "PRA requests to SURCOMM/CENCOMM/NORCOM"
                },
                {
                    "id": "hillberg_napa_state_hospital",
                    "question": "What is her role at Napa State Hospital from 2015 onward? Does it provide access to medical records?",
                    "unblock": "PRA to Napa State Hospital HR"
                },
                {
                    "id": "hillberg_911_call_recordings",
                    "question": "Are there preserved 911 call recordings from her interactions with APD/CHP/OPD across the 16-year pattern?",
                    "unblock": "PRA to each PD's 911 recording archive (typically 6-12 month retention; older recordings likely destroyed)"
                }
            ],
            "source_citations": [
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_familylaw_orchestration.md",
                "/home/vernenlegal/.claude/projects/-home-vernenlegal/memory/project_christina_pattern.md"
            ],
            "filed_at_utc": NOW,
        }
    },
]


# ============================================================================
# CASES
# ============================================================================

CASE_RECORDS = [
    {
        "filename": "RF09456481.json",
        "data": {
            "case_number": "RF09456481",
            "court": "Alameda County Superior Court",
            "jurisdiction": "Alameda County, California",
            "type": "Original DV / Custody",
            "petitioner": "Michael Hartmann",
            "respondent": "Christina Hartmann (Cerretani)",
            "filed_date": "2009-06-08",
            "current_status": "Michael protected. NO disposition on the case chart. The 7/2/2009 disposition (Paredes recommendation, sole custody to Michael, supervised visitation for Christina) is on the case chart for RF09459897 instead, which is anomalous.",
            "key_dates": [
                {"date": "2009-06-08", "event": "Michael files TRO"},
                {"date": "2009-06-11", "event": "OPD report 09-040089 filed (the contested fabricated report; basis for Christina's counter-narrative)"},
                {"date": "2009-06-26", "event": "Christina files counter DV-100 (becomes case RF09459897)"},
                {"date": "2009-06-29", "event": "Court order — Michael holds sole custody from this date forward"},
                {"date": "2009-07-02", "event": "Olga Paredes mediation hearing; Judge Trina Thompson adopts recommendation; sole custody confirmed"},
                {"date": "2010-09-02", "event": "Sala Ajaniku mediation hearing; Judge Paul A. Delucchi adopts recommendation; DVRO modified; Christina granted unsupervised visitation"}
            ],
            "source_folder": "${familylaw}/RO_DVRO_Custody-RF09456481/",
            "subfolders_by_date": [
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-02-15/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-06-08/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-06-10/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-06-11/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-06-26/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-06-26.1/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-6-08/",
                "${familylaw}/RO_DVRO_Custody-RF09456481/2009-07-02/"
            ],
            "related_actors": ["paredes_olga", "ajaniku_sala", "thompson_trina_judge", "delucchi_paul_judge", "cerretani_christina", "hillberg_ann"],
            "related_standards": [
                "CA_FAMILY_CODE_3011_BEST_INTEREST",
                "CA_FAM_3020_CUSTODY_POLICY",
                "CA_FAM_6203_DVPA_ABUSE_DEFINITION"
            ],
            "related_cases": ["RF09459897", "RF09470833", "RF10508853", "RF10508859"],
            "known_anomalies": [
                "Disposition for the 7/2/2009 Paredes hearing appears on RF09459897 (Christina's counter) instead of on RF09456481 (Michael's original) where it was actually issued",
                "Mediator switch between 2009 and 2010 (Paredes → Ajaniku) without documented reason",
                "Judge switch between 2009 and 2010 (Thompson → Delucchi) without documented reason",
                "Sala Ajaniku, who issued the 2010-09-02 recommendation that removed protective supervision, has zero verifiable credentials",
                "The 2009-06-11 OPD report (09-040089) that anchors Christina's counter-narrative has POST violations (POST-002B overlay rule) and the contemporaneous 6/2/2009 OPD report (the actual 5150 incident) does not exist in OPD records per October 2025 records pickup"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "RF09459897.json",
        "data": {
            "case_number": "RF09459897",
            "court": "Alameda County Superior Court",
            "type": "Counter-DV (Christina's)",
            "petitioner": "Christina Hartmann (Cerretani)",
            "respondent": "Michael Hartmann",
            "filed_date": "2009-06-26",
            "current_status": "ANOMALY — this case carries the 7/2/2009 disposition that should have been on RF09456481. The disposition includes the sole-custody-to-Michael / supervised-visitation-for-Christina ruling, which is structurally a ruling on Michael's TRO and Paredes mediation, not on Christina's counter.",
            "key_dates": [
                {"date": "2009-06-26", "event": "Christina files counter DV-100 (18 days after Michael's 6/8/2009 TRO; matches the counter-filing playbook pattern)"},
                {"date": "2009-07-02", "event": "Anomalous disposition entry — actually the disposition from RF09456481"}
            ],
            "source_folder": "FamilyLaw/2009-06-26/ (presumed)",
            "related_actors": ["cerretani_christina", "thompson_trina_judge", "paredes_olga"],
            "related_standards": ["CA_FAM_6203_DVPA_ABUSE_DEFINITION", "CA_FAMILY_CODE_3011_BEST_INTEREST"],
            "related_cases": ["RF09456481"],
            "known_anomalies": [
                "Carries the 7/2/2009 disposition that belongs on RF09456481 — this is a case-chart bookkeeping anomaly that may have substantive consequences for jurisdiction, finality, and res judicata",
                "Filed 18 days after Michael's TRO — matches the counter-filing playbook pattern documented across the 16-year case file"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "RF09470833.json",
        "data": {
            "case_number": "RF09470833",
            "court": "Alameda County Superior Court",
            "type": "Dissolution (Michael's)",
            "petitioner": "Michael Hartmann",
            "respondent": "Christina Hartmann",
            "filed_date": "2009-08",
            "current_status": "VOIDED 2010-11-22",
            "key_dates": [
                {"date": "2009-08", "event": "Michael files for dissolution"},
                {"date": "2010-11-22", "event": "Case VOIDED"}
            ],
            "source_folder": "${familylaw}/Dissolution-RF09470833/",
            "related_actors": ["cerretani_christina"],
            "related_standards": [],
            "related_cases": ["RF09456481", "RF10508853"],
            "known_anomalies": [
                "Case was voided in 2010-11-22 without explanation in the case file — the void event itself is an anomaly that should be investigated",
                "Christina's separate dissolution filing (RF10508853) was filed 2010-04-09 while Michael's RF09470833 was still active — duplicate dissolution filings are prohibited"
            ],
            "outstanding_investigations": [
                "Why was RF09470833 voided on 2010-11-22? What was the order or stipulation that led to the voiding?",
                "Did the voiding of RF09470833 have any procedural relationship to the 2010-09-02 Ajaniku/Delucchi hearing that removed protective supervision?"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "RF10508853.json",
        "data": {
            "case_number": "RF10508853",
            "court": "Alameda County Superior Court (transferred to Solano County 2025-06-25)",
            "type": "Dissolution Ex Parte (Christina's)",
            "petitioner": "Christina Hartmann (Cerretani)",
            "respondent": "Michael Hartmann",
            "filed_date": "2010-04-09",
            "current_status": "No disposition. Transferred to Solano County 2025-06-25 (the transfer was the same day as the dismissal of the 2025 Alameda DVROs and is part of the 2025 jurisdictional trap)",
            "key_dates": [
                {"date": "2010-04-09", "event": "Christina files ex parte dissolution as part of the coordinated triple filing (with Ann Marie Packard's grandparent visitation petition RF10508859 and a duplicate dissolution filing)"},
                {"date": "2025-06-25", "event": "Transferred to Solano County as part of jurisdictional trap"}
            ],
            "source_folder": "${familylaw}/Dissolution_ExParte-RF10508853/",
            "related_actors": ["cerretani_christina", "hillberg_ann"],
            "related_standards": ["CA_FAM_6203_DVPA_ABUSE_DEFINITION"],
            "related_cases": ["RF09470833", "RF10508859"],
            "known_anomalies": [
                "Filed 2010-04-09 as part of the coordinated triple filing orchestrated by Ann Hillberg/Packard",
                "Filed while Michael's dissolution RF09470833 was still active (duplicate dissolution filing — prohibited)",
                "Used FL-310/MC-020 form with 'every trigger word for child abuse, neglect, flight risk, drugs'",
                "No disposition for 15 years",
                "Transfer to Solano on 2025-06-25 was simultaneous with the dismissal of the 2025 Alameda DVROs and the Solano-says-no-transfer-received gap"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "RF10508859.json",
        "data": {
            "case_number": "RF10508859",
            "court": "Alameda County Superior Court",
            "type": "Grandparent Visitation (Family Code § 3104)",
            "petitioner": "Ann Marie Packard (Christina's mother)",
            "respondent": "Michael Hartmann",
            "co_filer_anomaly": "Christina is listed as a co-filer despite having 0% custody, an active restraining order against her, and being under court-ordered psychiatric treatment",
            "filed_date": "2010-04-09",
            "current_status": "Michael NEVER SERVED",
            "key_dates": [
                {"date": "2010-04-09", "event": "Filed as part of the coordinated triple filing"},
                {"date": "2010-04-09", "event": "Served by mail SAME DAY filed — likely mailed to Christina (co-filer), not Michael (custodial parent)"}
            ],
            "source_folder": "FamilyLaw/2010-04-09/ (presumed)",
            "related_actors": ["hillberg_ann", "cerretani_christina"],
            "related_standards": [],
            "related_cases": ["RF09456481", "RF10508853"],
            "known_anomalies": [
                "Petitioner is the grandmother (Ann Marie Packard) but Christina is listed as co-filer despite legal disqualifications",
                "Service by mail on the same day filed is procedurally suspect",
                "Service was NEVER actually effected on Michael per the case file",
                "Cross-references the same-day RF10508853 dissolution filing — coordinated by Ann Hillberg/Packard",
                "Family Code § 3104 grandparent visitation has elaborate procedural requirements (notice, service, parent objection rights) — if Michael was never served, the petition is structurally void"
            ],
            "outstanding_investigations": [
                "Was Family Code § 3104 procedural compliance ever established for this petition?",
                "What is the current status of the petition? Is it still pending? Was it dismissed? Defaulted?",
                "What was the disposition?"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "25FL122591.json",
        "data": {
            "case_number": "25FL122591",
            "court": "Alameda County Superior Court",
            "type": "DVRO (Michael's, 2025)",
            "petitioner": "Michael Hartmann",
            "respondent": "Christina Cerretani",
            "filed_date": "2025-05-15",
            "current_status": "Denied; dismissed 2025-06-25",
            "key_dates": [
                {"date": "2025-05-15", "event": "Michael files DV-100 in Alameda"},
                {"date": "2025-06-25", "event": "Denied and dismissed; case dismissed but Christina's response (25FL125059) survives the dismissal"}
            ],
            "source_folder": "FamilyLaw/2025-05-15/ and 2025-05-16/ (presumed)",
            "related_actors": ["cerretani_christina"],
            "related_standards": ["CA_FAM_6203_DVPA_ABUSE_DEFINITION"],
            "related_cases": ["25FL125059", "FL0002067"],
            "known_anomalies": [
                "Dismissal is part of the 2025 jurisdictional trap pattern",
                "Christina's counter-DVRO (25FL125059) was filed 20 days after Michael's filing — matches the counter-filing playbook pattern (18-20 day window)",
                "Both DVROs were dismissed the same day (2025-06-25), but Christina's response 'survives' Michael's dismissal — this is the structural mechanism by which she preserves her own filing while his goes away"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "25FL125059.json",
        "data": {
            "case_number": "25FL125059",
            "court": "Alameda County Superior Court",
            "type": "DVRO (Christina's counter, 2025)",
            "petitioner": "Christina Cerretani",
            "respondent": "Michael Hartmann",
            "filed_date": "2025-06-04",
            "current_status": "Denied; dismissed 2025-06-25",
            "key_dates": [
                {"date": "2025-06-04", "event": "Christina files counter DV-100 in Alameda (20 days after Michael's 5/15/2025 filing — matches counter-filing playbook)"},
                {"date": "2025-06-25", "event": "Denied and dismissed alongside Michael's 25FL122591"}
            ],
            "source_folder": "FamilyLaw/2025-06-04/ and 2025-06-05/ (presumed)",
            "related_actors": ["cerretani_christina"],
            "related_standards": ["CA_FAM_6203_DVPA_ABUSE_DEFINITION", "CA_FAMILY_CODE_3011_BEST_INTEREST"],
            "related_cases": ["25FL122591", "FL0002067"],
            "known_anomalies": [
                "Filed 20 days after Michael's TRO — matches the 16-year counter-filing playbook (18-20 day window)",
                "Dismissed same day as Michael's DVRO but Christina then files in Marin (FL0002067) approximately 22 days later — the same playbook pattern, this time crossing jurisdictional lines"
            ],
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "FL0002067.json",
        "data": {
            "case_number": "FL0002067",
            "court": "Marin County Superior Court",
            "type": "DVRO (Christina's, jurisdictional flip)",
            "petitioner": "Christina Cerretani",
            "respondent": "Michael Hartmann",
            "filed_date": "2025-07-17",
            "current_status": "ACTIVE — DV-130 granted 2025-10-17 with CLETS entry; expires 2026-08-19",
            "key_dates": [
                {"date": "2025-07-08", "event": "Ann Hillberg hands Cole to Christina at night during transfer window (per project_familylaw_orchestration.md)"},
                {"date": "2025-07-13", "event": "Christina takes Cole to Marin County (no court order at this point)"},
                {"date": "2025-07-14 to 2025-07-17", "event": "Michael calls Benicia PD for 4 days — no response, no reports taken"},
                {"date": "2025-07-17", "event": "Christina files DVRO in Marin (4 days AFTER Cole taken; 22 days after Alameda dismissal; jurisdictional flip)"},
                {"date": "2025-07-17", "event": "Benicia PD finally shows up — to serve Michael with the restraining order, NOT to take his missing-Cole report"},
                {"date": "2025-08-05", "event": "Marin assumes jurisdiction; judge refuses to let Michael speak"},
                {"date": "2025-10-17", "event": "DV-130 granted with CLETS entry"},
                {"date": "2026-08-19", "event": "Order expires"}
            ],
            "source_folder": "FamilyLaw/2025-07-17/, 2025-08-05/, 2025-10-17/ (presumed)",
            "related_actors": ["cerretani_christina", "hillberg_ann"],
            "related_standards": [
                "CA_FAM_6203_DVPA_ABUSE_DEFINITION",
                "CA_FAMILY_CODE_3011_BEST_INTEREST",
                "CA_FAM_3020_CUSTODY_POLICY"
            ],
            "related_cases": ["25FL122591", "25FL125059", "RF10508853"],
            "known_anomalies": [
                "Filed 4 days after Cole was taken (matches 4-day window of the counter-filing playbook for cross-jurisdictional flips)",
                "Marin assumed jurisdiction over a child whose habitual residence per UCCJEA was Solano County — UCCJEA challenge is the structural defense",
                "Benicia PD refused to act on Michael's reports for 4 days, then served the restraining order instead — pattern matches the broader orchestration finding",
                "Marin judge refused to let Michael speak at the 8/5/2025 hearing (per project_familylaw_orchestration.md)",
                "This is currently the ONLY active custody-affecting order against Michael; the steward's pending state action against Christina is presumably aimed at vacating or undermining FL0002067 OR is a separate civil action arising from the same conduct"
            ],
            "outstanding_investigations": [
                "Marin County 8/5/2025 hearing document — not yet in case file per memory",
                "Benicia PD call recording for the 7/14-17 calls — per memory: 'not yet scanned/uploaded'",
                "UCCJEA habitual residence analysis — was Cole's habitual residence Solano County under UCCJEA § 3402(g)? If yes, Marin lacked jurisdiction"
            ],
            "case_theory_significance": "FL0002067 is the active operational order against Michael. Vacating or limiting it is the most direct case objective. The combination of UCCJEA jurisdictional challenge + the documented orchestration pattern + the OPD records pickup audit + the credential audit on Paredes/Ajaniku may produce a viable motion to vacate or a fresh civil action.",
            "filed_at_utc": NOW,
        }
    },
    {
        "filename": "04-23-01959.json",
        "data": {
            "case_number": "04-23-01959",
            "court": "Contra Costa County Superior Court",
            "type": "Criminal / Competency",
            "current_status": "Active investigation per project_familylaw_audit.md",
            "key_dates": [],
            "source_folder": "TBD — to be located",
            "related_actors": ["wiita_patrick"],
            "related_standards": [],
            "related_cases": [],
            "known_anomalies": [
                "Dr. Patrick Wiita competency evaluation is described in the case audit as 'self-contradicting, template boilerplate, evaluated while high'",
                "Connection to family-court matters is via the criminal/competency overlay on the family-court actor's posture"
            ],
            "outstanding_investigations": [
                "Locate the source folder for this case",
                "Obtain the full Wiita evaluation",
                "Identify the underlying criminal charges and their disposition"
            ],
            "filed_at_utc": NOW,
        }
    },
]


# ============================================================================
# README INDICES
# ============================================================================

ACTORS_README = """# CA_Family_Law_Litigator — Actor Catalog

**Purpose:** Structured records for every named human actor in the family-law case file. Each actor has a JSON file with role, credentials, case involvement, risk assessment, outstanding investigations, and source citations.

**Filed:** 2026-04-08
**Citizen:** CA_Family_Law_Litigator
**Tether:** `../tether.json` (the binding manifest)

## Actors currently in catalog

| Actor | Role | Risk | File |
|---|---|---|---|
| Olga Paredes, Ph.D. | Child Custody Mediator (2009) | MEDIUM | [paredes_olga.json](paredes_olga.json) |
| Sala Ajaniku | Child Custody Mediator (2010) | **CRITICAL** | [ajaniku_sala.json](ajaniku_sala.json) |
| David Alan Ditsworth, MD | SSA Disability Report Author | HIGH | [ditsworth_david.json](ditsworth_david.json) |
| Trina Thompson | Judge (Alameda, 2009) | LOW | [thompson_trina_judge.json](thompson_trina_judge.json) |
| Paul A. Delucchi | Judge (Alameda, 2010) | HIGH | [delucchi_paul_judge.json](delucchi_paul_judge.json) |
| Patrick Wiita, Dr. | Competency Evaluator | HIGH | [wiita_patrick.json](wiita_patrick.json) |
| Christina Marie Cerretani | Opposing party (16-year pattern) | OPPOSING PARTY | [cerretani_christina.json](cerretani_christina.json) |
| Ann Hillberg / Ann Marie Packard | Mother of Christina; orchestrator | ORCHESTRATOR | [hillberg_ann.json](hillberg_ann.json) |

## Schema

Each actor record contains:
- `actor_id` — canonical identifier
- `canonical_name`, `aliases`
- `role`
- `professional_identity` — title, education, employer, credential claims
- `credential_verification` — what's verified, what's not, what's needed
- `case_involvement` — list of actions in specific cases with dates and outcomes
- `risk_level` and `risk_basis`
- `outstanding_investigations` — open questions about this actor with unblock paths
- `standards_governing_this_actor` — corpus standards that apply
- `source_citations` — where this information comes from
- `filed_at_utc`

## Outstanding catalog work

- Add records for additional actors as the case file is more deeply audited:
  - Other judges across the 16-year case
  - Other mediators
  - Public defenders / appointed counsel
  - CPS workers
  - Court-connected staff
  - Police officers named in specific reports
  - Process servers (relevant to the 2010 grandparent visitation never-served issue)
  - Witness names from the case file
- Verify the actor records against the source citations regularly
- When an outstanding investigation resolves, update the record and surface the resolution
"""

CASES_README = """# CA_Family_Law_Litigator — Case Index

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
"""


# ============================================================================
# MAIN
# ============================================================================

def main():
    actor_count = 0
    case_count = 0

    for entry in ACTOR_RECORDS:
        path = ACTORS / entry["filename"]
        path.write_text(json.dumps(entry["data"], indent=2))
        json.loads(path.read_text())
        actor_count += 1

    for entry in CASE_RECORDS:
        path = CASES / entry["filename"]
        path.write_text(json.dumps(entry["data"], indent=2))
        json.loads(path.read_text())
        case_count += 1

    (ACTORS / "README.md").write_text(ACTORS_README)
    (CASES / "README.md").write_text(CASES_README)

    print(f"Wrote {actor_count} actor records to {ACTORS}/")
    print(f"Wrote {case_count} case records to {CASES}/")
    print(f"Wrote README indices for actors and cases")
    print("All JSON validates")


if __name__ == "__main__":
    main()
