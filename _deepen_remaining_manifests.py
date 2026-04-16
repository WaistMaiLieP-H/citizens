#!/usr/bin/env python3
"""
_deepen_remaining_manifests.py

One-shot deepening of the 8 substance-only standards that did not get
individual deepening earlier in the 2026-04-08 session. Each entry below
contains the verbatim text reference, the structural location, the
amendment history visible on leginfo, and a steward case relevance audit
calibrated to the standard's actual case-file relevance (most of these
are INDIRECT — included for umbrella completeness).

Run from ${citizens}/.
"""

import json
from pathlib import Path

NOW = "2026-04-08T11:00:00Z"
BASE = Path("${citizens}")


STANDARDS = [
    {
        "standard_id": "CA_HSC_109925_SHERMAN_LAW",
        "citizen": "CA_Food_Safety_Specialist",
        "folder": "sherman_law_hsc_109925",
        "umbrella_number": 3,
        "umbrella_name": "Substance / Specification",
        "code": "California Health and Safety Code",
        "section": "§ 109925",
        "popular_name": "Sherman Food, Drug, and Cosmetic Law — Definition of 'Drug'",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=109925.&lawCode=HSC",
        "html_file": "cal_hsc_109925_leginfo.html",
        "txt_file": "cal_hsc_109925_leginfo.txt",
        "sha256": "f83dbe9faddecdffb3a876d7e514e62de54e254719f9a74514a91134f8df9621",
        "structural": {
            "division": "DIVISION 104. ENVIRONMENTAL HEALTH [106500 - 119406]",
            "division_history": "Division 104 added by Stats. 1995, Ch. 415, Sec. 6",
            "part": "PART 5. SHERMAN FOOD, DRUG, AND COSMETIC LAWS [109875 - 111929.5]",
            "part_history": "Part 5 added by Stats. 1995, Ch. 415, Sec. 6",
            "chapter": "CHAPTER 1. General Provisions and Definitions [109875 - 110040]",
            "section_history": "Most recent amendment: Stats. 2017, Ch. 27, Sec. 160 (SB 94) Effective June 27, 2017"
        },
        "verbatim_summary": "Defines 'drug' for the purposes of California's Sherman Food, Drug, and Cosmetic Law: (a) any article (1) recognized in an official compendium, (2) used or intended for use in diagnosis/cure/mitigation/treatment/prevention of disease in humans or animals, (3) other than food, used or intended to affect the structure or any function of the body, or (4) used as a component of any of the above. (b) Excludes devices. (c) Foods making approved health claims under federal labeling rules are not drugs. (d) Cannabis products (including external use) are not drugs.",
        "amendment_history": [
            {"year": 1995, "stats": "Stats. 1995, Ch. 415, Sec. 6", "event": "Original enactment as part of the Sherman Law's 1995 codification into Division 104"},
            {"year": 2017, "stats": "Stats. 2017, Ch. 27, Sec. 160 (SB 94)", "event": "Most recent amendment, adding the cannabis-product exclusion (d), effective June 27, 2017"}
        ],
        "audit_purpose": "The Sherman Law's drug definition is the operational gate for California drug regulation. Map against medical fraud documentation only where drug-classification questions are at issue.",
        "audit_items": [
            {"id": "Drug definition scope", "rec": "INDIRECT — relevant if any prescription/non-prescription substance in the steward's medical fraud timeline was misclassified or dispensed outside the Sherman Law framework", "status": "FLAGGED"},
            {"id": "Cannabis exclusion (d) — added 2017", "rec": "Not applicable to the steward's case file", "status": "NOT APPLICABLE"},
            {"id": "Federal-by-reference adoption", "rec": "DOCTRINAL — California's pattern of adopting FDA standards by reference is the structural backdrop for several other steward-relevant standards (food labeling, drug compounding, etc.)", "status": "DOCTRINAL"}
        ]
    },
    {
        "standard_id": "CA_BPC_12001_WEIGHTS_AND_MEASURES",
        "citizen": "CA_Weights_Measures_Inspector",
        "folder": "cal_bp_12001",
        "umbrella_number": 4,
        "umbrella_name": "Measurement / Metrology",
        "code": "California Business and Professions Code",
        "section": "§ 12001",
        "popular_name": "California Weights and Measures Law — Definitions Scope",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=12001.&lawCode=BPC",
        "html_file": "cal_bpc_12001_leginfo.html",
        "txt_file": "cal_bpc_12001_leginfo.txt",
        "sha256": "558eadeb5ebcd36c6bc700f35762924711c517dfa4b38b49cd4fb371dbf74549",
        "structural": {
            "division": "DIVISION 5. WEIGHTS AND MEASURES [12001 - 13800]",
            "division_history": "Division 5 added by Stats. 1939, Ch. 43",
            "chapter": "CHAPTER 1. General Provisions [12001 - 12027]",
            "section_history": "Added by Stats. 1939, Ch. 43. Never amended — section is in its original 1939 form."
        },
        "verbatim_summary": "Single-sentence definitional-scope provision: 'The definitions in this chapter apply to this division only and do not affect the provisions of any other division.' This is a structural housekeeping section that establishes the scope of the Weights and Measures Law's definitional framework, separating it from definitions used in other Business and Professions Code divisions.",
        "amendment_history": [
            {"year": 1939, "stats": "Stats. 1939, Ch. 43", "event": "Original enactment of the entire Division 5 Weights and Measures Law. § 12001 has never been amended."}
        ],
        "audit_purpose": "§ 12001 itself is a structural scope provision, not a substantive rule. The substantive rules of weights and measures are in subsequent sections (§§ 12002 et seq. for definitions; §§ 12100 et seq. for the State Sealer; §§ 12200 et seq. for inspection; etc.). Building § 12001 occupies the umbrella but the operative rules are downstream.",
        "audit_items": [
            {"id": "Scope-of-definitions doctrine", "rec": "STRUCTURAL — establishes that California weights-and-measures definitions are domain-bounded; not directly steward-relevant", "status": "ROUTINE"},
            {"id": "Next-step deepening", "rec": "Future deepening should fetch §§ 12002-12027 (definitions) and §§ 12100+ (State Sealer authority), which are the operative provisions", "status": "OUTSTANDING"}
        ]
    },
    {
        "standard_id": "CA_GOV_11135_NONDISCRIMINATION",
        "citizen": "CA_Civil_Rights_Compliance_Specialist",
        "folder": "cal_gov_11135",
        "umbrella_number": 7,
        "umbrella_name": "Access / Inclusion",
        "code": "California Government Code",
        "section": "§ 11135",
        "popular_name": "Nondiscrimination in State-Funded Programs",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=11135.&lawCode=GOV",
        "html_file": "cal_gov_11135_leginfo.html",
        "txt_file": "cal_gov_11135_leginfo.txt",
        "sha256": "62aa59c964cbeb980c7a9d5e5d37177faaf80aaee78d9924167c1a82481e3a92",
        "structural": {
            "title": "TITLE 2. GOVERNMENT OF THE STATE OF CALIFORNIA [8000 - 22980]",
            "division": "DIVISION 3. EXECUTIVE DEPARTMENT [11000 - 15990.3]",
            "part": "PART 1. STATE DEPARTMENTS AND AGENCIES [11000 - 11908]",
            "chapter": "CHAPTER 1. State Agencies [11000 - 11148.5]",
            "article": "ARTICLE 9.5. Discrimination [11135 - 11139]",
            "article_history": "Article 9.5 added by Stats. 1977, Ch. 972",
            "section_history": "Most recent amendment: Stats. 2016, Ch. 870, Sec. 4 (SB 1442) Effective January 1, 2017"
        },
        "verbatim_summary": "(a) No person in California shall, on the basis of any protected characteristic (sex, race, color, religion, ancestry, national origin, ethnic group identification, age, mental disability, physical disability, medical condition, genetic information, marital status, or sexual orientation) be unlawfully denied full and equal access to the benefits of, or be unlawfully subjected to discrimination under, any program or activity that is conducted, operated, or administered by the state, funded directly by the state, or that receives any state financial assistance. Applies to the California State University. (b) For disability discrimination, the protections and prohibitions of ADA Title II § 202 (42 U.S.C. § 12132) and federal implementing regulations apply, with stronger California protections superseding where applicable. (c) Protected bases have the same meanings as in Gov. Code § 12926 (FEHA). (d) Protected bases include perception and association.",
        "amendment_history": [
            {"year": 1977, "stats": "Stats. 1977, Ch. 972", "event": "Original enactment of Article 9.5 as California's state-level civil rights non-discrimination statute for state-funded programs"},
            {"year": 2016, "stats": "Stats. 2016, Ch. 870, Sec. 4 (SB 1442)", "event": "Most recent amendment, expanding protected bases and clarifying CSU coverage"}
        ],
        "audit_purpose": "§ 11135 is the California state-level analog to federal Title VI and Title IX. It binds every state agency, every state-funded program, and every entity that receives state financial assistance. POTENTIALLY DIRECT for the steward's case if any state-funded program (court services, social services, schools, public health, etc.) discriminated against him on a protected basis.",
        "audit_items": [
            {"id": "State-funded program coverage", "rec": "Identifies whether the state actors in the steward's case file (family courts, social services, county agencies) are 'programs or activities' subject to § 11135", "status": "FLAGGED"},
            {"id": "Disability protected basis (incorporates ADA Title II)", "rec": "Subdivision (b) directly incorporates federal ADA Title II protections — bridges § 11135 to the federal disability framework. Relevant if disability is a basis for any treatment in the case file", "status": "FLAGGED"},
            {"id": "Perception and association (subdivision (d))", "rec": "Protections extend to PERCEIVED protected characteristics and association with protected persons. Relevant if any treatment was based on perception (e.g., perceived mental health) rather than fact", "status": "CRITICAL — directly relevant given the conservatorship discovery and any 'IT' (Intensive Treatment) or mental-health framing in the case file"},
            {"id": "Cross-reference to FEHA § 12926", "rec": "Protected-basis definitions are imported from FEHA — fetching FEHA § 12926 is the next-step deepening", "status": "OUTSTANDING"}
        ]
    },
    {
        "standard_id": "CA_PRC_21000_CEQA",
        "citizen": "CA_CEQA_Consultant",
        "folder": "cal_prc_21000",
        "umbrella_number": 8,
        "umbrella_name": "Environmental / External Impact",
        "code": "California Public Resources Code",
        "section": "§ 21000",
        "popular_name": "California Environmental Quality Act (CEQA) — Legislative Findings",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=21000.&lawCode=PRC",
        "html_file": "cal_prc_21000_leginfo.html",
        "txt_file": "cal_prc_21000_leginfo.txt",
        "sha256": "aa9580c278895048c58616ab494e67162ab8db4722fc33b467895a3bfcf70669",
        "structural": {
            "division": "DIVISION 13. ENVIRONMENTAL QUALITY [21000 - 21189.91]",
            "division_history": "Division 13 added by Stats. 1970, Ch. 1433 — this is CEQA's original 1970 enactment",
            "chapter": "CHAPTER 1. Policy [21000 - 21006]",
            "section_history": "Amended by Stats. 1979, Ch. 947"
        },
        "verbatim_summary": "Legislative findings supporting CEQA. The Legislature finds that: (a) maintenance of a quality environment for the people of this state now and in the future is a matter of statewide concern; (b) it is necessary to provide a high-quality environment that at all times is healthful and pleasing to the senses and intellect of man; (c) there is a need to understand the relationship between high-quality ecological systems and the general welfare; (d) the capacity of the environment is limited and the state must take immediate steps to identify critical thresholds and prevent them from being reached; (e) every citizen has a responsibility to contribute to environmental preservation; (f) environmental management requires systematic public-private effort; (g) it is the intent of the Legislature that all state agencies regulating activities affecting environmental quality shall give major consideration to preventing environmental damage while providing a decent home and satisfying living environment for every Californian.",
        "amendment_history": [
            {"year": 1970, "stats": "Stats. 1970, Ch. 1433", "event": "Original CEQA enactment, modeled on federal NEPA (1969). California Environmental Quality Act became one of the most consequential environmental review statutes in the U.S."},
            {"year": 1979, "stats": "Stats. 1979, Ch. 947", "event": "Most recent amendment to § 21000 (the findings section). The substantive CEQA review provisions in §§ 21001-21189.91 have been amended many times since."}
        ],
        "audit_purpose": "CEQA is the California environmental review framework. Not directly steward-relevant unless his case touches a project subject to CEQA review. Included for umbrella completeness and as the doctrinal example of 'good intentions outrunning standards at scale.'",
        "audit_items": [
            {"id": "Statewide concern doctrine (a)", "rec": "Establishes environmental quality as a matter of statewide concern, preempting local-government laxity. Doctrinally important but not steward-direct", "status": "DOCTRINAL"},
            {"id": "Critical-thresholds identification (d)", "rec": "Anticipates the precautionary principle — the state must identify critical thresholds before they are reached. Structurally analogous to the SOC-001 doctrine but applied to environmental harm", "status": "DOCTRINAL"},
            {"id": "Next-step deepening", "rec": "The operative CEQA review provisions are in §§ 21002-21177 (substantive rules), §§ 21080-21099 (project review), §§ 21100-21154 (EIR requirements). Fetching the operative provisions is outstanding work", "status": "OUTSTANDING"}
        ]
    },
    {
        "standard_id": "CA_RTC_17041_INCOME_TAX",
        "citizen": "CA_Tax_Specialist",
        "folder": "cal_rt_17041",
        "umbrella_number": 14,
        "umbrella_name": "Tax",
        "code": "California Revenue and Taxation Code",
        "section": "§ 17041",
        "popular_name": "Personal Income Tax — Imposition and Rate Schedule",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=17041.&lawCode=RTC",
        "html_file": "cal_rtc_17041_leginfo.html",
        "txt_file": "cal_rtc_17041_leginfo.txt",
        "sha256": "461ffc55d6d9c76ce2094707239a3c1a8c87cd37646f9fec0cfba7f16a5d2406",
        "structural": {
            "division": "DIVISION 2. OTHER TAXES [6001 - 61050]",
            "part": "PART 10. PERSONAL INCOME TAX [17001 - 18181]",
            "part_history": "Part 10 added by Stats. 1943, Ch. 659 — California enacted the Personal Income Tax in 1943",
            "chapter": "CHAPTER 2. Imposition of Tax [17041 - 17061]",
            "chapter_history": "Chapter 2 repealed and added by Stats. 1955, Ch. 939",
            "section_history": "Most recent amendment: Stats. 2010, Ch. 14, Sec. 5 (SB 401) Effective January 1, 2011. Note: Section was amended on June 8, 1982, by initiative Prop. 7 (different Prop 7 than the 1974 Constitutional one)"
        },
        "verbatim_summary": "Imposes the California Personal Income Tax with rate schedules for: (a) residents who are not heads of household, (b) nonresidents and part-year residents, (c) heads of household residents, (d) head-of-household nonresidents, (e) estates/trusts/common trust funds. Rate brackets range from 1% on income up to $3,650 to 9.3% on income over $23,950 (single filer base brackets, before annual inflation adjustment under (h)). Subdivision (h) requires annual inflation adjustment based on California CPI. Subdivision (i) defines 'taxable income of a nonresident or part-year resident' for nonresident calculations.",
        "amendment_history": [
            {"year": 1943, "stats": "Stats. 1943, Ch. 659", "event": "Original enactment of California's Personal Income Tax (Part 10 of the Revenue and Taxation Code). California enacted the personal income tax during World War II."},
            {"year": 1955, "stats": "Stats. 1955, Ch. 939", "event": "Chapter 2 (Imposition of Tax) repealed and re-added — major mid-century recodification"},
            {"year": 1982, "stats": "Initiative Prop. 7 (June 8, 1982)", "event": "Amended by ballot initiative — DIFFERENT Prop 7 than the 1974 Constitutional rights Prop 7"},
            {"year": 2010, "stats": "Stats. 2010, Ch. 14, Sec. 5 (SB 401)", "event": "Most recent amendment, effective January 1, 2011"}
        ],
        "audit_purpose": "§ 17041 is the operational core of the California personal income tax. Not directly steward-relevant unless his case touches tax compliance or refund issues.",
        "audit_items": [
            {"id": "Residency determination", "rec": "California vs nonresident vs part-year resident determinations are tax-consequential. Not currently steward-relevant", "status": "ROUTINE"},
            {"id": "Inflation adjustment mechanism", "rec": "Subdivision (h) annual CPI-based bracket adjustment is administered by FTB; relevant for any historical tax-year reconstruction", "status": "ROUTINE"},
            {"id": "Stale rate brackets in statute", "rec": "The base brackets in the statute are from a much earlier era (the $3,650-$23,950 base values). The actual current brackets are computed via the (h) inflation factor. Historical bracket reconstruction would require both the base brackets and the FTB's annual factor", "status": "OUTSTANDING"}
        ]
    },
    {
        "standard_id": "CA_CCP_425_16_ANTI_SLAPP",
        "citizen": "CA_First_Amendment_Litigator",
        "folder": "cal_ccp_425_16_anti_slapp",
        "umbrella_number": 15,
        "umbrella_name": "Communication / Speech / Press",
        "code": "California Code of Civil Procedure",
        "section": "§ 425.16",
        "popular_name": "Anti-SLAPP Statute — Special Motion to Strike",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=425.16.&lawCode=CCP",
        "html_file": "cal_ccp_425_16_leginfo.html",
        "txt_file": "cal_ccp_425_16_leginfo.txt",
        "sha256": "d8ce2d74ec8c2fbc147f12713ce9ea89d05e22d8f814b8c4e4b96cc0232ac212",
        "structural": {
            "part": "PART 2. OF CIVIL ACTIONS [307 - 1062.34]",
            "title": "TITLE 6. OF THE PLEADINGS IN CIVIL ACTIONS [420 - 475]",
            "chapter": "CHAPTER 2. Pleadings Demanding Relief [425.10 - 429.30]",
            "article": "ARTICLE 1. General Provisions [425.10 - 425.55]",
            "article_history": "Article 1 added by Stats. 1971, Ch. 244",
            "section_history": "Most recent amendment: Stats. 2024, Ch. 444, Sec. 1 (SB 577) Effective January 1, 2025"
        },
        "verbatim_summary": "(a) Legislative findings: lawsuits brought primarily to chill the valid exercise of free speech and petition rights are increasing; statute construed broadly. (b) Special motion to strike available for any cause of action arising from an act in furtherance of free speech or petition rights in connection with a public issue, unless plaintiff establishes probability of prevailing. (c) PREVAILING DEFENDANT IS ENTITLED TO ATTORNEY'S FEES AND COSTS — fee-shifting is mandatory. Frivolous motions can be sanctioned with fees to plaintiff. (d) Public-prosecutor enforcement actions are exempt. (e) Definition of 'act in furtherance' is broad: statements before official proceedings, statements connected to issues under official review, statements in public forums, and other conduct in furtherance of speech or petition rights. (f) 60-day filing window (court discretion to extend). (g) AUTOMATIC DISCOVERY STAY upon filing the motion. (i) Order on the motion is immediately appealable. (j) Notice to Judicial Council required.",
        "amendment_history": [
            {"year": 1992, "stats": "Stats. 1992, Ch. 726", "event": "Original enactment of California's anti-SLAPP statute"},
            {"year": 2024, "stats": "Stats. 2024, Ch. 444, Sec. 1 (SB 577)", "event": "Most recent amendment, effective January 1, 2025"}
        ],
        "audit_purpose": "§ 425.16 is California's strong anti-SLAPP statute. POTENTIALLY DIRECT for the steward if any party files a retaliatory civil action against him in response to his pro se litigation, his audit publications, or his public statements about his case. The fee-shifting and discovery-stay provisions are unusually consequential procedural levers.",
        "audit_items": [
            {"id": "Fee-shifting (c)", "rec": "Mandatory fee award to a prevailing defendant. For a pro se litigant, this is one of the most powerful procedural protections in California civil practice", "status": "CRITICAL — directly available to the steward if anyone sues him over his pro se filings or public statements"},
            {"id": "Discovery stay (g)", "rec": "Automatic discovery stay upon filing the motion. Stops a retaliatory plaintiff from running up the steward's costs through pre-motion discovery", "status": "CRITICAL — directly procedural protection"},
            {"id": "Broad construction (a)", "rec": "Statute is to be 'construed broadly' per the Legislature's express intent. Courts apply this in favor of speech/petition defendants", "status": "DOCTRINAL"},
            {"id": "60-day filing window (f)", "rec": "The motion must be filed within 60 days of service unless the court extends. This is the operational time-pressure constraint", "status": "ROUTINE"},
            {"id": "Public-prosecutor exemption (d)", "rec": "Anti-SLAPP not available against AG/DA/CA enforcement actions. Not applicable to private retaliatory suits", "status": "NOT APPLICABLE"}
        ]
    },
    {
        "standard_id": "CA_PUC_399_11_RPS",
        "citizen": "CA_Energy_Policy_Specialist",
        "folder": "cal_puc_399_11_rps",
        "umbrella_number": 17,
        "umbrella_name": "Energy",
        "code": "California Public Utilities Code",
        "section": "§ 399.11",
        "popular_name": "California Renewables Portfolio Standard (RPS) — Legislative Findings",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=399.11.&lawCode=PUC",
        "html_file": "cal_puc_399_11_leginfo.html",
        "txt_file": "cal_puc_399_11_leginfo.txt",
        "sha256": "b87326aeab366aa71777e92498f3d9648b57c6343a6d40caaae704ac0d1daff4",
        "structural": {
            "division": "DIVISION 1. REGULATION OF PUBLIC UTILITIES [201 - 3299.100]",
            "division_history": "Division 1 enacted by Stats. 1951, Ch. 764",
            "part": "PART 1. PUBLIC UTILITIES ACT [201 - 2120]",
            "chapter": "CHAPTER 2.3. Electrical Restructuring [330 - 400.3]",
            "chapter_history": "Chapter 2.3 added by Stats. 1996, Ch. 854, Sec. 10",
            "article": "ARTICLE 16. California Renewables Portfolio Standard Program [399.11 - 399.33]",
            "article_history": "Article 16 added by Stats. 2002, Ch. 516, Sec. 3",
            "section_history": "Most recent amendment: Stats. 2018, Ch. 312, Sec. 2 (SB 100) Effective January 1, 2019"
        },
        "verbatim_summary": "Legislative findings for the California Renewables Portfolio Standard. (a) Targets: 20% renewables by 12/31/2013, 33% by 12/31/2020, 50% by 12/31/2026, 60% by 12/31/2030. (b) Nine independently-justifying benefits enumerated: (1) displacing fossil fuel; (2) adding new generation in WECC; (3) reducing air pollution and toxics; (4) meeting climate goals; (5) promoting stable retail rates; (6) energy generation diversity; (7) resource adequacy; (8) grid reliability; (9) transmission and land-use planning. (c) Complements the Energy Commission's Renewable Energy Resources Program (PRC § 25740). (d) New transmission may be needed. (e) Out-of-state renewables count equally and disadvantaged-community air-quality benefits flagged.",
        "amendment_history": [
            {"year": 2002, "stats": "Stats. 2002, Ch. 516, Sec. 3 (SB 1078)", "event": "Original enactment of California RPS — first renewable portfolio mandate"},
            {"year": 2018, "stats": "Stats. 2018, Ch. 312, Sec. 2 (SB 100)", "event": "Most recent amendment. SB 100 set the 100% zero-carbon by 2045 target as California's clean-energy commitment"}
        ],
        "audit_purpose": "The RPS is foundational California energy policy but not directly steward-relevant.",
        "audit_items": [
            {"id": "Trajectory targets (a)", "rec": "20% / 33% / 50% / 60% trajectory has been the policy backbone of California renewable energy investment for two decades", "status": "ROUTINE"},
            {"id": "Disadvantaged community air quality (e)(1)", "rec": "RPS implementation must consider disadvantaged community air quality. Not currently steward-relevant", "status": "ROUTINE"},
            {"id": "Next-step deepening", "rec": "The operative RPS provisions (compliance percentages, RECs, banking, alternative compliance) are in §§ 399.12-399.33. Fetching is outstanding work", "status": "OUTSTANDING"}
        ]
    },
    {
        "standard_id": "CA_HSC_113700_CALCODE",
        "citizen": "CA_Retail_Food_Inspector",
        "folder": "cal_calcode_113700",
        "umbrella_number": 18,
        "umbrella_name": "Agriculture / Food",
        "code": "California Health and Safety Code",
        "section": "§ 113700",
        "popular_name": "California Retail Food Code (CalCode) — Short Title",
        "url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=113700.&lawCode=HSC",
        "html_file": "cal_hsc_113700_leginfo.html",
        "txt_file": "cal_hsc_113700_leginfo.txt",
        "sha256": "1d1530c9752a7a94d20cd2b948c2828f99c0b72d3b40dcbfbf7b4869d2911ec3",
        "structural": {
            "division": "DIVISION 104. ENVIRONMENTAL HEALTH [106500 - 119406]",
            "part": "PART 7. CALIFORNIA RETAIL FOOD CODE [113700 - 114437]",
            "part_history": "Part 7 repealed and added by Stats. 2006, Ch. 23, Sec. 2 — CalCode in its current form dates from 2006",
            "chapter": "CHAPTER 1. General Provisions [113700 - 113725.3]",
            "section_history": "Repealed and added by Stats. 2006, Ch. 23, Sec. 2. Effective January 1, 2007. Operative July 1, 2007"
        },
        "verbatim_summary": "Single-sentence short-title section: 'These provisions shall be known, and may be cited, as the California Retail Food Code, hereafter referred to as \"this part.\"' Establishes the popular citation form for the entire CalCode (Part 7 of Division 104, §§ 113700-114437).",
        "amendment_history": [
            {"year": 2006, "stats": "Stats. 2006, Ch. 23, Sec. 2", "event": "CalCode in its current form was enacted in 2006, repealing and replacing the prior California Uniform Retail Food Facilities Law (CURFFL). Effective January 1, 2007; operative July 1, 2007."}
        ],
        "audit_purpose": "CalCode governs every restaurant, grocery store, food truck, school cafeteria, and food vendor in California. § 113700 is the short-title provision; the operative rules are in subsequent sections. The school food allergy example the steward raised earlier in this build session is governed by the intersection of CalCode, Education Code, and H&S Code food allergen provisions.",
        "audit_items": [
            {"id": "Short-title doctrine", "rec": "Establishes citable name 'California Retail Food Code' / 'CalCode'. Not substantively load-bearing", "status": "ROUTINE"},
            {"id": "School cafeteria food safety (steward's peanut-law example)", "rec": "DOCTRINAL — bridges to the steward's 'no peanuts in school cafeterias' methodological example. The operative allergen provisions are downstream in CalCode (e.g., § 114094 menu labeling, § 113816 employee health) and in Education Code provisions on school nutrition", "status": "DOCTRINAL — bridges to steward's methodological example"},
            {"id": "Next-step deepening", "rec": "Fetch the operative CalCode provisions (definitions § 113789, food safety §§ 113980+, employee health § 113816, food sources § 114021, school cafeteria-specific rules)", "status": "OUTSTANDING"}
        ]
    },
]


def deepen(s):
    folder = BASE / s["citizen"] / "standards" / s["folder"]
    manifest_path = folder / "manifest.json"

    # Build the deepened manifest
    manifest = {
        "standard_id": s["standard_id"],
        "version": "0.2.0-verbatim-and-substance-audited",
        "filed_at_utc": "2026-04-08T09:23:00Z",
        "deepened_at_utc": NOW,
        "filed_by": "Claude (assistant) under steward direction — Michael Hartmann, Vernen Legal Compliance",
        "status": "PROPOSED-DEEPENED-COMPACT — verbatim text extracted, brief substance audit completed. Standard is in an umbrella with INDIRECT relevance to the steward's case file; the audit is calibrated accordingly. Awaiting second-mouth countersignature.",
        "build_context": f"Originally built 2026-04-08 as part of the breadth-first umbrella seeding pass (Umbrella {s['umbrella_number']:02d} {s['umbrella_name']} first occupant). Deepened later same day with verbatim text and brief substance audit via _deepen_remaining_manifests.py.",
        "primary_citation": {
            "jurisdiction": "California",
            "code": s["code"],
            "section": s["section"],
            "popular_name": s["popular_name"],
            "current_codification_url": s["url"],
            "current_form_local_artifact": f"current/{s['html_file']}",
            "verbatim_text_extracted_artifact": f"current/{s['txt_file']}",
        },
        "structural_location": s["structural"],
        "verbatim_summary": s["verbatim_summary"],
        "amendment_history_visible_on_leginfo": s["amendment_history"],
        "substance_audit": {
            "purpose": s["audit_purpose"],
            "audit_filed_at_utc": NOW,
            "audit_filed_by": "Claude (assistant) at first-mouth level; steward review required",
            "audit_items": [
                {
                    "audit_id": item["id"],
                    "recommendation": item["rec"],
                    "audit_status": item["status"],
                }
                for item in s["audit_items"]
            ],
        },
        "umbrellas": [f"{s['umbrella_name']} (Umbrella {s['umbrella_number']:02d}) — primary"],
        "owner_citizen": {"primary": s["citizen"]},
        "triple_constraint_test_results": {
            "governing_guidelines": {"passes": True, "evidence": f"{s['code']} {s['section']} located at official primary source; binding California authority confirmed; verbatim text extracted to current/{s['txt_file']}"},
            "standards_of_creation": {"passes": True, "evidence": "Section is well-formed and properly codified."},
            "standard_of_care": {
                "passes": "PARTIAL",
                "current_layer": f"VERIFIED — current form fetched, hashed (sha256: {s['sha256']}), and verbatim-extracted",
                "evolution_layer": "PARTIAL — amendment history captured at manifest level; primary-source amendment volumes not yet downloaded",
                "origin_layer": f"IDENTIFIED — original enactment recorded in amendment_history; primary-source not yet fetched",
            },
        },
        "five_layer_bar_status": {
            "rule": "PRESENT — verbatim text extracted",
            "reasoning": "PARTIAL — recorded in legislative findings where applicable",
            "historical_loss": "OUTSTANDING",
            "cross_references": "PARTIAL",
            "verifiable_provenance": "PRESENT for current form; ABSENT for evolution and origin layers",
        },
        "two_witness_status": {
            "first_mouth_proposer": "Claude (assistant) under steward direction (Michael Hartmann), 2026-04-08",
            "second_mouth_witness": "NONE — not yet countersigned",
            "publishable_to_corpus": False,
            "status": "PROPOSED-DEEPENED-COMPACT",
        },
        "files": {
            "origin": [],
            "evolution": [],
            "current": [f"current/{s['html_file']}", f"current/{s['txt_file']}"],
            "context": [],
            "manifest": "manifest.json",
            "provenance": "provenance.json",
        },
        "outstanding_work": [
            "Locate and fetch primary-source statute volumes for the original enactment and key amendments",
            "Document the historical-loss layer — what specific incidents drove the section's enactment",
            "Fetch operative downstream sections in the same article/chapter as integrity-tracked HTML markers",
            "Build cross-references to other Vernen corpus standards where applicable",
            "Obtain second-mouth countersignature on the standard",
        ],
    }

    manifest_path.write_text(json.dumps(manifest, indent=2))
    return manifest_path


def main():
    written = []
    for s in STANDARDS:
        p = deepen(s)
        written.append(p)
        # Validate by reloading
        json.loads(p.read_text())
    print(f"Deepened {len(written)} manifests")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
