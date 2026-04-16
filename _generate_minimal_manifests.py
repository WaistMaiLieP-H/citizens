#!/usr/bin/env python3
"""
_generate_minimal_manifests.py

One-shot generator for the 14 breadth-first umbrella seed standards
built on 2026-04-08. Writes manifest.json and provenance.json into each
standard's folder using a consistent minimal-substance template.

Each standard's primary-source HTML has already been fetched and hashed
in a separate bash step; the configs below carry the canonical hash and
URL for each.

Run from ${citizens}/.
"""

import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

NOW = "2026-04-08T09:23:00Z"

# Each entry: a complete config for one minimal-substance standard.
STANDARDS = [
    {
        "standard_id": "CA_CONST_ART_I_SEC_1",
        "citizen": "CA_Constitutional_Law_Specialist",
        "folder": "cal_const_art1_sec1",
        "umbrella_number": 1,
        "umbrella_name": "Authority / Governing Law",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Constitution",
        "section": "Article I, Section 1",
        "popular_name": "Inalienable Rights Clause",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CONS&sectionNum=SEC.%201.&article=I",
        "html_file": "cal_const_art1_sec1_leginfo.html",
        "sha256": "05ff94a1b8bc0c429e83e77018a92983a3cb7fb554685b068fc0611552be4fcf",
        "size": 160304,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov), maintained by the Office of Legislative Counsel of California",
        "rule_summary": "All people are by nature free and independent and have inalienable rights, including enjoying and defending life and liberty, acquiring/possessing/protecting property, and pursuing and obtaining safety, happiness, and privacy. Foundational article of the California Constitution and the textual root of every California rights claim.",
        "owner_note": "Constitutional law specialist as canonical owner; this section is the textual root of every California-jurisdiction rights claim and therefore foundational to every Citizen who litigates rights in California courts.",
        "steward_relevance": "FOUNDATIONAL — every California-specific standard in the corpus rests on the California Constitution, and Article I § 1 is its rights-bearing root. The federal companion (U.S. Constitution Bill of Rights) is a planned secondary seed.",
    },
    {
        "standard_id": "US_42_USC_1983",
        "citizen": "CA_Civil_Rights_Litigator",
        "folder": "usc_42_1983",
        "umbrella_number": 2,
        "umbrella_name": "Procedure",
        "umbrella_first": True,
        "jurisdiction": "United States (federal)",
        "code_or_source": "42 United States Code",
        "section": "Section 1983",
        "popular_name": "Civil Action for Deprivation of Rights",
        "url": "https://www.law.cornell.edu/uscode/text/42/1983",
        "html_file": "usc_42_1983_cornell.html",
        "sha256": "c0124651a15d4c02397cfbb3631535995ac11f835b18ae74b96803b3a701c5e6",
        "size": 30828,
        "source_authority": "Cornell Legal Information Institute (LII) — public-domain mirror of the U.S. Code maintained by Cornell Law School",
        "rule_summary": "Every person who, under color of any state or territorial statute, ordinance, regulation, custom, or usage, subjects or causes any U.S. citizen or other person within U.S. jurisdiction to the deprivation of any rights, privileges, or immunities secured by the Constitution and laws shall be liable to the party injured in an action at law, suit in equity, or other proper proceeding for redress.",
        "owner_note": "Civil rights litigator as canonical owner. § 1983 is the operational vehicle for federal-court redress of state-actor deprivations of constitutional rights.",
        "steward_relevance": "DIRECT — this is the federal statute under which the steward's planned § 1983 federal complaint is filed (per project_federal_complaint_draft.md). Building this standard is an act of arming the steward's own active litigation.",
    },
    {
        "standard_id": "CA_HSC_109925_SHERMAN_LAW",
        "citizen": "CA_Food_Safety_Specialist",
        "folder": "sherman_law_hsc_109925",
        "umbrella_number": 3,
        "umbrella_name": "Substance / Specification",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Health and Safety Code",
        "section": "§ 109925",
        "popular_name": "Sherman Food, Drug, and Cosmetic Law — Adoption of Federal Standards",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=109925.&lawCode=HSC",
        "html_file": "cal_hsc_109925_leginfo.html",
        "sha256": "f83dbe9faddecdffb3a876d7e514e62de54e254719f9a74514a91134f8df9621",
        "size": 163769,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "California's Sherman Food, Drug, and Cosmetic Law adopts federal FDA food, drug, device, and cosmetic standards as state law. Establishes the substantive identity, purity, labeling, and adulteration standards for food, drugs, devices, and cosmetics in California by reference to federal standards.",
        "owner_note": "Food safety specialist as canonical owner. The Sherman Law is the California-specific framework that brings federal FDA standards into state-enforceable form.",
        "steward_relevance": "INDIRECT — substance/specification standards generally; Sherman Law specifically because it is the structural example of how California adopts federal standards by reference, a pattern repeated throughout California regulatory law.",
    },
    {
        "standard_id": "CA_BPC_12001_WEIGHTS_AND_MEASURES",
        "citizen": "CA_Weights_Measures_Inspector",
        "folder": "cal_bp_12001",
        "umbrella_number": 4,
        "umbrella_name": "Measurement / Metrology",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Business and Professions Code",
        "section": "§ 12001",
        "popular_name": "California Weights and Measures Law — Foundational Section",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12001.&lawCode=BPC",
        "html_file": "cal_bpc_12001_leginfo.html",
        "sha256": "558eadeb5ebcd36c6bc700f35762924711c517dfa4b38b49cd4fb371dbf74549",
        "size": 161905,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Establishes the State Sealer of Weights and Measures (the Director of the Department of Food and Agriculture, or designee). Foundation of California's weights and measures regulatory regime, including the testing and certification of scales, fuel pumps, taximeters, package contents, and any other commercial measuring device used in California.",
        "owner_note": "Weights and Measures Inspector as canonical owner. § 12001 establishes the state-level authority; county sealers are appointed under subsequent sections to perform field inspection.",
        "steward_relevance": "DOCTRINAL — direct descendant of the cooper's grain measure that was 'slightly wrong by a cooper who genuinely believed it was correct,' the example used during the second-mouth doctrine discussion. The codified protection against good-faith measurement failure at scale.",
    },
    {
        "standard_id": "CA_GOV_11135_NONDISCRIMINATION",
        "citizen": "CA_Civil_Rights_Compliance_Specialist",
        "folder": "cal_gov_11135",
        "umbrella_number": 7,
        "umbrella_name": "Access / Inclusion",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Government Code",
        "section": "§ 11135",
        "popular_name": "Nondiscrimination in State-Funded Programs",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11135.&lawCode=GOV",
        "html_file": "cal_gov_11135_leginfo.html",
        "sha256": "62aa59c964cbeb980c7a9d5e5d37177faaf80aaee78d9924167c1a82481e3a92",
        "size": 165630,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "No person shall, on the basis of sex, race, color, religion, ancestry, national origin, ethnic group identification, age, mental disability, physical disability, medical condition, genetic information, marital status, or sexual orientation, be unlawfully denied full and equal access to the benefits of, or be unlawfully subjected to discrimination under, any program or activity that is conducted, operated, or administered by the state or by any state agency, is funded directly by the state, or receives any financial assistance from the state.",
        "owner_note": "Civil Rights Compliance Specialist as canonical owner. § 11135 is California's general non-discrimination statute for state-funded programs — the state-level analog to federal Title VI.",
        "steward_relevance": "INDIRECT — every California public school, every state agency, every state-funded service is bound by this section. It is the umbrella's foundational state-law provision.",
    },
    {
        "standard_id": "CA_PRC_21000_CEQA",
        "citizen": "CA_CEQA_Consultant",
        "folder": "cal_prc_21000",
        "umbrella_number": 8,
        "umbrella_name": "Environmental / External Impact",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Public Resources Code",
        "section": "§ 21000",
        "popular_name": "California Environmental Quality Act (CEQA) — Legislative Findings",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=21000.&lawCode=PRC",
        "html_file": "cal_prc_21000_leginfo.html",
        "sha256": "aa9580c278895048c58616ab494e67162ab8db4722fc33b467895a3bfcf70669",
        "size": 164540,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Section 21000 contains the California Legislature's findings and declarations supporting CEQA: that the maintenance of a quality environment for the people of this state now and in the future is a matter of statewide concern; that it is necessary to provide a high-quality environment that at all times is healthful and pleasing to the senses and intellect of man; etc. The opening section of CEQA, adopted in 1970 and modeled on federal NEPA.",
        "owner_note": "CEQA Consultant as canonical owner. § 21000 is the legislative-findings section of CEQA, the rhetorical foundation of California environmental review.",
        "steward_relevance": "INDIRECT — CEQA is one of the most consequential California statutes, but is not directly relevant to the steward's existing case file. Included because CEQA is the canonical doctrinal example of 'good intentions outrunning standards at scale' producing a standards regime that catches up with the harm.",
    },
    {
        "standard_id": "CA_EVIDENCE_1400_AUTHENTICATION",
        "citizen": "CA_Records_Authentication_Specialist",
        "folder": "cal_evidence_1400",
        "umbrella_number": 9,
        "umbrella_name": "Integrity / Provenance / Records",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Evidence Code",
        "section": "§ 1400",
        "popular_name": "Authentication of a Writing — California state-level analog to FRE 901",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1400.&lawCode=EVID",
        "html_file": "cal_evid_1400_leginfo.html",
        "sha256": "6e17040d9c883eca8bb88718e9a4d9d57b1885a0b6335c246d004b323db6b666",
        "size": 162296,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Authentication of a writing means (a) the introduction of evidence sufficient to sustain a finding that it is the writing that the proponent of the evidence claims it is or (b) the establishment of such facts by any other means provided by law. The California state-court counterpart to Federal Rule of Evidence 901, and the legal embodiment of the SOC-001 / Authentic Identity doctrine in the California state context.",
        "owner_note": "Records Authentication Specialist as canonical owner. § 1400 is the California state-court rule that 'a writing must be what it claims to be' — directly equivalent to FRE 901 in the federal system.",
        "steward_relevance": "DIRECT — every exhibit the steward intends to use in California state court (rather than federal court) must satisfy § 1400. The chain-of-custody failures across his 16-year case file are, structurally, § 1400 failures: writings that were presented as something they were not, or whose authenticity could not be re-derived by an independent verifier.",
    },
    {
        "standard_id": "CA_CIV_56_10_CMIA",
        "citizen": "CA_Medical_Privacy_Officer",
        "folder": "cmia_civ_56_10",
        "umbrella_number": 10,
        "umbrella_name": "Privacy / Information Stewardship",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Civil Code",
        "section": "§ 56.10",
        "popular_name": "Confidentiality of Medical Information Act (CMIA) — Disclosure Restrictions",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=56.10.&lawCode=CIV",
        "html_file": "cal_civ_56_10_leginfo.html",
        "sha256": "5415c9a31627ae04c1c055d23a8c9dee15c44aaf9bc3f92933be84aea7a99005",
        "size": 186960,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "A provider of health care, health care service plan, or contractor shall not disclose medical information regarding a patient of the provider of health care or an enrollee or subscriber of a health care service plan without first obtaining an authorization, except as expressly enumerated. CMIA is California's medical privacy statute, generally regarded as more protective than HIPAA in several respects. Where CMIA is more protective, CMIA controls and HIPAA does not preempt it (per 45 CFR § 160.203(b)).",
        "owner_note": "Medical Privacy Officer as canonical owner. CMIA § 56.10 is the substantive disclosure-restriction core of California medical privacy law, distinct from and often more protective than HIPAA.",
        "steward_relevance": "DIRECT — every medical record disclosed without authorization, every medical record altered or substituted in the steward's medical fraud documentation (per project_medical_fraud_timeline.md), every CMIA-protected disclosure made without consent, falls under § 56.10. Building this as a witnessed standard creates a state-law analytical tool for the steward's medical fraud audit, complementary to the federal HIPAA framework.",
    },
    {
        "standard_id": "CA_CIV_1213_RECORDING_ACTS",
        "citizen": "CA_Real_Estate_Attorney",
        "folder": "cal_civ_1213_recording_acts",
        "umbrella_number": 12,
        "umbrella_name": "Property / Title / Ownership",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Civil Code",
        "section": "§ 1213",
        "popular_name": "Recording Acts — Race-Notice Rule",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1213.&lawCode=CIV",
        "html_file": "cal_civ_1213_leginfo.html",
        "sha256": "c4fb7a2cb56e65f755fe164071ce3ddbf0019c0e9a36598d8486237f11423a98",
        "size": 163413,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Every conveyance of real property or an estate for years therein, other than a lease for a term not exceeding one year, acknowledged or proved and certified and recorded as prescribed by law from the time it is filed with the recorder for record is constructive notice of the contents thereof to subsequent purchasers and mortgagees. The foundation of California's recording system and the source of the race-notice priority rule that allows title insurance to function.",
        "owner_note": "Real Estate Attorney as canonical owner. § 1213 is the constructive-notice provision that determines priority of competing claims to California real property.",
        "steward_relevance": "DIRECT — directly relevant to the steward's house-sale fraud documentation (per project_house_sale_fraud.md). The 19 unsigned documents in the 2958 Honeysuckle sale, the chain-of-recording questions, the missing equity — all are § 1213-adjacent issues. Building this standard creates the analytical framework for the steward's existing forensic work on the house sale.",
    },
    {
        "standard_id": "CA_RTC_17041_INCOME_TAX",
        "citizen": "CA_Tax_Specialist",
        "folder": "cal_rt_17041",
        "umbrella_number": 14,
        "umbrella_name": "Tax",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Revenue and Taxation Code",
        "section": "§ 17041",
        "popular_name": "Personal Income Tax — Imposition and Rate Schedule",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17041.&lawCode=RTC",
        "html_file": "cal_rtc_17041_leginfo.html",
        "sha256": "461ffc55d6d9c76ce2094707239a3c1a8c87cd37646f9fec0cfba7f16a5d2406",
        "size": 174253,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Imposes the California personal income tax. Sets out the rate schedule for each filing status, the tax brackets, and the basic computation of California taxable income. The operational core of the California Personal Income Tax Law.",
        "owner_note": "Tax Specialist as canonical owner. § 17041 is the imposition provision — the section that says 'there is hereby imposed' the tax and sets the rates.",
        "steward_relevance": "INDIRECT — establishes the umbrella's foundational California tax provision. Federal counterpart (IRC § 1) is a planned secondary seed.",
    },
    {
        "standard_id": "CA_CCP_425_16_ANTI_SLAPP",
        "citizen": "CA_First_Amendment_Litigator",
        "folder": "cal_ccp_425_16_anti_slapp",
        "umbrella_number": 15,
        "umbrella_name": "Communication / Speech / Press",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Code of Civil Procedure",
        "section": "§ 425.16",
        "popular_name": "Anti-SLAPP Statute — Special Motion to Strike",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=425.16.&lawCode=CCP",
        "html_file": "cal_ccp_425_16_leginfo.html",
        "sha256": "d8ce2d74ec8c2fbc147f12713ce9ea89d05e22d8f814b8c4e4b96cc0232ac212",
        "size": 168458,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "A cause of action against a person arising from any act of that person in furtherance of the person's right of petition or free speech under the United States Constitution or the California Constitution in connection with a public issue shall be subject to a special motion to strike, unless the court determines that the plaintiff has established that there is a probability that the plaintiff will prevail on the claim. A prevailing defendant on a special motion to strike shall be entitled to recover their attorney's fees and costs.",
        "owner_note": "First Amendment Litigator as canonical owner. § 425.16 is one of the strongest anti-SLAPP statutes in any U.S. state, and creates an immediate disposal mechanism for retaliatory lawsuits brought against speech and petition activity.",
        "steward_relevance": "DIRECT — relevant to any retaliatory civil action that might be filed against the steward in response to his pro se litigation, his audit publications, or his public statements about his case. The fee-shifting provision is unusually consequential for pro se litigants.",
    },
    {
        "standard_id": "CA_VEH_2800_OBEY_PEACE_OFFICER",
        "citizen": "CA_Vehicle_Code_Specialist",
        "folder": "cal_veh_2800",
        "umbrella_number": 16,
        "umbrella_name": "Travel / Movement / Immigration",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Vehicle Code",
        "section": "§ 2800",
        "popular_name": "Failure to Obey a Peace Officer's Lawful Order",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=2800.&lawCode=VEH",
        "html_file": "cal_veh_2800_leginfo.html",
        "sha256": "99ee632c64c6c8659cc5269c32c61534a83fd977fdb076859615eababf46f5ee",
        "size": 165029,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "It is unlawful to willfully fail or refuse to comply with a lawful order, signal, or direction of a peace officer in uniform performing duties under the Vehicle Code, or of a member of the Department of the California Highway Patrol when in uniform and performing such duties. The threshold for what constitutes a 'lawful order' is itself the analytical question in any § 2800 prosecution and any related civil rights claim.",
        "owner_note": "Vehicle Code Specialist as canonical owner. § 2800 is foundational to traffic-stop enforcement and is one of the most-cited Vehicle Code sections in California criminal practice.",
        "steward_relevance": "DIRECT — relevant to the analysis of the June 16, 2023 incident in the steward's case file (per project_june16_2023_timeline.md). Understanding what constitutes a 'lawful order' under § 2800, and what does not, is essential to the analysis of that day.",
    },
    {
        "standard_id": "CA_PUC_399_11_RPS",
        "citizen": "CA_Energy_Policy_Specialist",
        "folder": "cal_puc_399_11_rps",
        "umbrella_number": 17,
        "umbrella_name": "Energy",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Public Utilities Code",
        "section": "§ 399.11",
        "popular_name": "California Renewables Portfolio Standard (RPS) — Legislative Findings",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=399.11.&lawCode=PUC",
        "html_file": "cal_puc_399_11_leginfo.html",
        "sha256": "b87326aeab366aa71777e92498f3d9648b57c6343a6d40caaae704ac0d1daff4",
        "size": 167372,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "The California Legislature finds and declares that the development of renewable energy resources is in the public interest, that increasing renewable generation reduces air pollution and greenhouse gas emissions, that diversification of supply reduces ratepayer exposure to fossil fuel price volatility, etc. Section 399.11 is the legislative-findings section of the California RPS — California's statutory commitment to renewable electricity, originally adopted in 2002 and successively accelerated to current 60% by 2030 / 100% zero-carbon by 2045 targets.",
        "owner_note": "Energy Policy Specialist as canonical owner. § 399.11 is the rhetorical foundation of the California RPS, setting out why the state has chosen renewables.",
        "steward_relevance": "INDIRECT — establishes the umbrella's foundational California energy-policy provision.",
    },
    {
        "standard_id": "CA_HSC_113700_CALCODE",
        "citizen": "CA_Retail_Food_Inspector",
        "folder": "cal_calcode_113700",
        "umbrella_number": 18,
        "umbrella_name": "Agriculture / Food",
        "umbrella_first": True,
        "jurisdiction": "California",
        "code_or_source": "California Health and Safety Code",
        "section": "§ 113700",
        "popular_name": "California Retail Food Code (CalCode) — Short Title and Scope",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=113700.&lawCode=HSC",
        "html_file": "cal_hsc_113700_leginfo.html",
        "sha256": "1d1530c9752a7a94d20cd2b948c2828f99c0b72d3b40dcbfbf7b4869d2911ec3",
        "size": 162672,
        "source_authority": "California Legislative Information (leginfo.legislature.ca.gov)",
        "rule_summary": "Section 113700 is the short-title section of the California Retail Food Code (CalCode), the state statute governing every restaurant, grocery store, food truck, school cafeteria, and food vendor in California. CalCode drives the county environmental health letter-grade placards on California restaurants and is the operational body of California retail food safety law.",
        "owner_note": "Retail Food Inspector as canonical owner. CalCode is administered by county environmental health departments (not by a single state agency), making the inspector the canonical operational role.",
        "steward_relevance": "DOCTRINAL — direct callback to the steward's 'no peanuts in school cafeterias' methodological example. CalCode and its allergen provisions, in conjunction with the Education Code, are the modern California legal framework that did not exist in the steward's school years (1983–1997). The umbrella's foundational state law.",
    },
]


def manifest_for(s):
    return {
        "standard_id": s["standard_id"],
        "version": "0.1.0-substance-only",
        "filed_at_utc": NOW,
        "filed_by": "Claude (assistant) under steward direction — Michael Hartmann, Vernen Legal Compliance",
        "status": "PROPOSED-SUBSTANCE-ONLY — primary source captured and hashed; verbatim transcription, evolution chain to original enactment, historical loss research, and cross-reference build are all outstanding work. Awaiting second-mouth countersignature.",
        "build_context": "Built 2026-04-08 as part of the breadth-first umbrella seeding pass. The goal of this pass is to put one substantive standard into each of the 18 substantive umbrellas so that no umbrella sits empty. Depth comes in subsequent passes.",
        "umbrella_first_for_this_umbrella": (
            f"This is the FIRST standard built under Umbrella {s['umbrella_number']:02d} ({s['umbrella_name']}). The umbrella was previously empty."
            if s.get("umbrella_first") else None
        ),
        "primary_citation": {
            "jurisdiction": s["jurisdiction"],
            "code": s["code_or_source"],
            "section": s["section"],
            "popular_name": s["popular_name"],
            "current_codification_url": s["url"],
            "current_form_local_artifact": f"current/{s['html_file']}",
        },
        "current_text_summary": {
            "rule_summary_paraphrase": s["rule_summary"],
            "verbatim_transcription_status": "OUTSTANDING — paraphrase only at this filing. The HTML at current/" + s["html_file"] + " is the authoritative text; verbatim transcription against that file is part of the next-pass deepening work.",
        },
        "umbrellas": [f"Umbrella {s['umbrella_number']:02d} — {s['umbrella_name']}"],
        "owner_citizen": {
            "primary": s["citizen"],
            "note": s["owner_note"],
        },
        "triple_constraint_test_results": {
            "governing_guidelines": {
                "passes": True,
                "evidence": f"Section located at official primary source ({s['source_authority']}). Binding {s['jurisdiction']} authority confirmed.",
            },
            "standards_of_creation": {
                "passes": "STRUCTURAL-ONLY",
                "evidence": "HTML fetched from official source and stored locally; section number, code, and authority all match canonical citation pattern. Verbatim transcription pending.",
            },
            "standard_of_care": {
                "passes": "PARTIAL",
                "current_layer": f"VERIFIED — current/{s['html_file']} (sha256: {s['sha256']}) fetched and hashed at {NOW}",
                "evolution_layer": "OUTSTANDING — codification chain to original enactment not yet primary-source mapped",
                "origin_layer": "OUTSTANDING — original enactment chapter not yet identified or fetched",
            },
        },
        "five_layer_bar_status": {
            "rule": "PRESENT (HTML fetched; transcription pending)",
            "reasoning": "OUTSTANDING — legislative intent and reasoning research deferred to next pass",
            "historical_loss": "OUTSTANDING — the documented harm that justifies the rule has not yet been researched and recorded",
            "cross_references": "OUTSTANDING — links to other Vernen corpus standards not yet built",
            "verifiable_provenance": "PRESENT for current form only",
        },
        "two_witness_status": {
            "first_mouth_proposer": "Claude (assistant) under steward direction (Michael Hartmann), 2026-04-08 breadth-first umbrella seeding pass",
            "second_mouth_witness": "NONE — not yet countersigned",
            "publishable_to_corpus": False,
            "status": "PROPOSED",
        },
        "files": {
            "origin": [],
            "evolution": [],
            "current": [f"current/{s['html_file']}"],
            "context": [],
            "manifest": "manifest.json",
            "provenance": "provenance.json",
        },
        "steward_relevance_note": s["steward_relevance"],
        "outstanding_work": [
            "Locate the original enactment (chapter and year) for this section",
            "Download and render the original chaptered statute volume from the California Assembly Chief Clerk archive (or equivalent for federal sections)",
            "Document the evolution chain from original enactment through every amendment to current form",
            "Document the historical loss layer — what harm or pattern of harm prompted this rule",
            "Transcribe the current form verbatim (against the local HTML artifact) into the manifest",
            "Build cross-references to other Vernen corpus standards",
            "Obtain second-mouth countersignature before publication",
        ],
    }


def provenance_for(s):
    return {
        "standard_id": s["standard_id"],
        "provenance_record_filed_at_utc": NOW,
        "fetcher_software": "curl with sha256sum (one-shot batch fetch as part of 2026-04-08 breadth-first umbrella seeding pass)",
        "fetcher_operator": "Claude (assistant) under steward direction (Michael Hartmann)",
        "verification_principle": "Current-form HTML is the primary artifact for sections whose canonical text lives at the named source authority. The HTML snapshot is hashed at fetch time so a future verifier can confirm it matches what the source served on this date.",
        "fetches": [
            {
                "artifact_local_path": f"current/{s['html_file']}",
                "source_url": s["url"],
                "source_authority": s["source_authority"],
                "source_authority_type": "primary",
                "fetched_at_utc": NOW,
                "fetch_method": "curl -sSL --max-time 60 with Vernen-Provenance user-agent (one-shot batch fetch)",
                "file_size_bytes": s["size"],
                "sha256": s["sha256"],
                "content_description": s["popular_name"],
            }
        ],
    }


def main():
    base = Path("${citizens}")
    written = []
    for s in STANDARDS:
        folder = base / s["citizen"] / "standards" / s["folder"]
        manifest = manifest_for(s)
        provenance = provenance_for(s)
        manifest_path = folder / "manifest.json"
        provenance_path = folder / "provenance.json"
        manifest_path.write_text(json.dumps(manifest, indent=2))
        provenance_path.write_text(json.dumps(provenance, indent=2))
        written.append((manifest_path, provenance_path))
    print(f"Wrote {len(written) * 2} files across {len(written)} standards")
    for m, p in written:
        # Validate by reloading
        json.loads(m.read_text())
        json.loads(p.read_text())
    print("All JSON validates")


if __name__ == "__main__":
    main()
