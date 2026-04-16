#!/usr/bin/env python3
"""
_deepen_umbrella11_second_seeds.py

Generates fully-deepened manifests for the three Umbrella 11 (Family /
Personal Status) second occupants added on 2026-04-08:
  - Cal. Probate Code § 1801 (Conservatorship appointment standards)
  - Cal. Family Code § 6203 (DVPA definition of abuse)
  - Cal. Family Code § 3020 (Custody policy — frequent contact + safety)

Each manifest includes a steward case relevance audit calibrated to the
case file artifacts that the standard touches directly.
"""

import json
from pathlib import Path

NOW = "2026-04-08T14:50:00Z"
BASE = Path("${citizens}")


PROB_1801 = {
    "standard_id": "CA_PROB_1801_CONSERVATORSHIP_APPOINTMENT",
    "citizen": "CA_Conservator_Investigator",
    "folder": "cal_prob_1801_conservatorship_appointment",
    "primary_citation": {
        "jurisdiction": "California",
        "code": "California Probate Code",
        "section": "§ 1801",
        "popular_name": "Conservatorship Appointment Standards (Persons for Whom Conservator May Be Appointed)",
        "current_codification_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1801.&lawCode=PROB",
        "current_form_local_artifact": "current/cal_prob_1801_leginfo.html",
        "verbatim_text_extracted_artifact": "current/cal_prob_1801_leginfo.txt",
    },
    "structural_location": {
        "code": "California Probate Code",
        "division": "DIVISION 4. GUARDIANSHIP, CONSERVATORSHIP, AND OTHER PROTECTIVE PROCEEDINGS [1400 - 3925]",
        "division_history": "Division 4 enacted by Stats. 1990, Ch. 79",
        "part": "PART 3. CONSERVATORSHIP [1800 - 2033]",
        "chapter": "CHAPTER 1. Establishment of Conservatorship [1800 - 1849.5]",
        "article": "ARTICLE 1. Persons for Whom Conservator May Be Appointed [1800 - 1804]",
        "section_history": "Most recent amendment: Stats. 1995, Ch. 842, Sec. 7. Effective January 1, 1996",
    },
    "verbatim_factor_inventory": {
        "subject_to_clause": "Subject to Section 1800.3 (cross-reference must be fetched as next-step)",
        "subdivisions": [
            {
                "id": "(a) Conservator of the person",
                "verbatim": "A conservator of the person may be appointed for a person who is unable to provide properly for his or her personal needs for physical health, food, clothing, or shelter, except as provided for the person as described in subdivision (b) or (c) of Section 1828.5.",
                "elements": [
                    "ELEMENT — Unable to provide properly for personal needs (physical health OR food OR clothing OR shelter). Inability must be substantial; isolated lapses are not enough.",
                ],
            },
            {
                "id": "(b) Conservator of the estate",
                "verbatim": "A conservator of the estate may be appointed for a person who is substantially unable to manage his or her own financial resources or resist fraud or undue influence, except as provided for that person as described in subdivision (b) or (c) of Section 1828.5. Substantial inability may not be proved solely by isolated incidents of negligence or improvidence.",
                "elements": [
                    "ELEMENT 1 — Substantial inability to manage own financial resources OR resist fraud or undue influence",
                    "ELEMENT 2 — STATUTORY EXCLUSION: substantial inability MAY NOT BE PROVED SOLELY BY ISOLATED INCIDENTS of negligence or improvidence. The petitioner must show a pattern, not isolated lapses.",
                ],
            },
            {
                "id": "(c) Combined conservator of person and estate",
                "verbatim": "A conservator of the person and estate may be appointed for a person described in subdivisions (a) and (b).",
            },
            {
                "id": "(d) Limited conservatorship for developmentally disabled adults",
                "verbatim": "A limited conservator of the person or of the estate, or both, may be appointed for a developmentally disabled adult. A limited conservatorship may be utilized only as necessary to promote and protect the well-being of the individual, shall be designed to encourage the development of maximum self-reliance and independence of the individual, and shall be ordered only to the extent necessitated by the individual's proven mental and adaptive limitations. The conservatee of the limited conservator shall not be presumed to be incompetent and shall retain all legal and civil rights except those which by court order have been designated as legal disabilities and have been specifically granted to the limited conservator. The intent of the Legislature, as expressed in Section 4501 of the Welfare and Institutions Code, that developmentally disabled citizens of this state receive services resulting in more independent, productive, and normal lives is the underlying mandate of this division in its application to adults alleged to be developmentally disabled.",
                "elements": [
                    "PROTECTIVE FRAMING — limited conservatorship must encourage MAXIMUM SELF-RELIANCE and independence",
                    "PROTECTIVE FRAMING — only to the extent NECESSITATED BY PROVEN mental and adaptive limitations (not assumed, not presumed)",
                    "PROTECTIVE FRAMING — conservatee SHALL NOT BE PRESUMED TO BE INCOMPETENT",
                    "PROTECTIVE FRAMING — conservatee retains ALL legal and civil rights EXCEPT those specifically designated as legal disabilities and specifically granted to the conservator (a list-based, not a blanket, deprivation)",
                ],
            },
            {
                "id": "(e) BURDEN OF PROOF",
                "verbatim": "The standard of proof for the appointment of a conservator pursuant to this section shall be clear and convincing evidence.",
                "doctrinal_significance": "CLEAR AND CONVINCING EVIDENCE is the second-highest civil burden of proof in California (between preponderance of the evidence and beyond a reasonable doubt). For ANY conservatorship appointment under § 1801, the petitioner must satisfy this elevated burden as to ALL applicable elements (whether (a), (b), (c), or (d) is being invoked). The clear-and-convincing standard exists because conservatorship is a fundamental deprivation of liberty and autonomy.",
            },
        ],
    },
    "amendment_history": [
        {"year": 1990, "stats": "Stats. 1990, Ch. 79", "event": "Original enactment of the modern conservatorship framework as part of the comprehensive Probate Code recodification"},
        {"year": 1995, "stats": "Stats. 1995, Ch. 842, Sec. 7", "event": "Most recent amendment, effective January 1, 1996"},
    ],
    "audit_purpose": "Map § 1801 against the conservatorship discovery (project_conservatorship_discovery.md and project_conservatorship_breakthrough.md). The audit asks: if a conservatorship has been opened on the steward, was the § 1801(e) clear-and-convincing-evidence burden actually satisfied at the time of appointment? Were the protective framings of (d) (if a limited conservatorship is involved) followed?",
    "audit_items": [
        {
            "id": "Existence of conservatorship",
            "rec": "Per project_conservatorship_breakthrough.md, the steward has discovered evidence consistent with a long-standing conservatorship arrangement involving him. The first investigatory question is whether such a conservatorship actually exists as a court order in any California probate court (or in another state's court). California probate court records are public records and can be searched by name in any county where a conservatorship petition might have been filed. Searching the Contra Costa, Alameda, San Francisco, and adjacent county Superior Court probate dockets is a concrete next step.",
            "status": "CRITICAL — load-bearing investigatory step. Establish existence/nonexistence first; everything else flows from that.",
        },
        {
            "id": "(e) Burden of proof — clear and convincing evidence",
            "rec": "If a conservatorship exists, the appointment had to satisfy the clear-and-convincing-evidence standard. The court file should contain (i) the petition, (ii) the supporting capacity declaration (Probate Code § 1821 form GC-310), (iii) the court investigator's report (per Probate Code §§ 1826, 1851), (iv) the probate examiner's notes, and (v) the order of appointment with findings. Each of these should reflect the elevated burden. Reviewing the petition and the order for explicit clear-and-convincing-evidence findings is the audit step.",
            "status": "CRITICAL — once existence is confirmed, the burden audit is the next investigatory step.",
        },
        {
            "id": "(d) Limited conservatorship protective framing",
            "rec": "If the conservatorship is a limited conservatorship under (d), the protective framings apply: the conservatee is NOT presumed incompetent; retains ALL rights except those specifically designated; the conservatorship must encourage maximum self-reliance; only to the extent necessitated by PROVEN limitations. If any of these protective framings was disregarded, that's a structural defect in the conservatorship.",
            "status": "FLAGGED — applies only if the conservatorship is limited rather than general.",
        },
        {
            "id": "(b) Estate conservatorship — substantial inability and the isolated-incidents exclusion",
            "rec": "If the conservatorship is of the estate (or combined under (c)), the (b) elements require SUBSTANTIAL inability to manage finances or resist fraud, AND the statute explicitly says inability MAY NOT BE PROVED SOLELY BY ISOLATED INCIDENTS of negligence or improvidence. The audit asks: did the petitioner show a pattern, or did they rely on isolated incidents? Reliance on isolated incidents is statutorily prohibited.",
            "status": "FLAGGED — applies only if estate or combined conservatorship is at issue.",
        },
        {
            "id": "Cross-reference to § 1800.3 'Subject to' clause",
            "rec": "§ 1801 opens with 'Subject to Section 1800.3' — meaning § 1800.3 conditions or limits § 1801. § 1800.3 must be fetched as next-step deepening to understand the full conservatorship-appointment framework.",
            "status": "OUTSTANDING",
        },
        {
            "id": "Bridge to CMIA § 56.10(c)(12)",
            "rec": "If a probate court investigator has been investigating any conservatorship proceeding involving the steward, that investigator was authorized under CMIA § 56.10(c)(12) to obtain the steward's medical records without his consent. The (c)(12) audit item in the CMIA manifest cross-references back to this § 1801 question.",
            "status": "CRITICAL — DOCTRINAL BRIDGE between this standard and CMIA § 56.10",
        },
    ],
    "umbrellas": ["Family / Personal Status (Umbrella 11) — primary", "Authority / Governing Law (Umbrella 01) — secondary"],
    "owner_citizen": "CA_Conservator_Investigator",
    "sha256": "09b2089dda7231bdc8936a8ab258ea3ac2d8c9f334bebe0c0ed956afbf5d610b",
    "umbrella_position": "second occupant under Umbrella 11 (first occupant: CA_FAMILY_CODE_3011_BEST_INTEREST)",
}


FAM_6203 = {
    "standard_id": "CA_FAM_6203_DVPA_ABUSE_DEFINITION",
    "citizen": "CA_Family_Law_Litigator",
    "folder": "cal_fam_6203_dvpa_abuse_definition",
    "primary_citation": {
        "jurisdiction": "California",
        "code": "California Family Code",
        "section": "§ 6203",
        "popular_name": "Domestic Violence Prevention Act (DVPA) — Definition of 'Abuse'",
        "current_codification_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=6203.&lawCode=FAM",
        "current_form_local_artifact": "current/cal_fam_6203_leginfo.html",
        "verbatim_text_extracted_artifact": "current/cal_fam_6203_leginfo.txt",
    },
    "structural_location": {
        "code": "California Family Code",
        "division": "DIVISION 10. PREVENTION OF DOMESTIC VIOLENCE [6200 - 6460]",
        "division_history": "Division 10 repealed and added by Stats. 1993, Ch. 219, Sec. 154 (the comprehensive 1993 Family Code recodification)",
        "part": "PART 1. SHORT TITLE AND DEFINITIONS [6200 - 6219]",
        "section_history": "Most recent amendment: Stats. 2015, Ch. 303, Sec. 149 (AB 731) Effective January 1, 2016",
    },
    "verbatim_factor_inventory": {
        "preamble": "(a) For purposes of this act, 'abuse' means any of the following:",
        "definitional_categories": [
            {
                "id": "(a)(1) Bodily injury",
                "verbatim": "To intentionally or recklessly cause or attempt to cause bodily injury.",
                "elements": [
                    "ELEMENT 1 — INTENT OR RECKLESSNESS (NOT mere negligence; not accident)",
                    "ELEMENT 2 — CAUSE OR ATTEMPT TO CAUSE bodily injury (attempt is sufficient even without actual injury)",
                ],
            },
            {
                "id": "(a)(2) Sexual assault",
                "verbatim": "Sexual assault.",
                "elements": ["ELEMENT — sexual assault as defined under California criminal law"],
            },
            {
                "id": "(a)(3) Reasonable apprehension of imminent serious bodily injury",
                "verbatim": "To place a person in reasonable apprehension of imminent serious bodily injury to that person or to another.",
                "elements": [
                    "ELEMENT 1 — REASONABLE apprehension (not subjective panic; an objectively reasonable person would have apprehension)",
                    "ELEMENT 2 — IMMINENT (not future, not hypothetical, but immediate or about-to-occur)",
                    "ELEMENT 3 — SERIOUS bodily injury (not minor)",
                    "ELEMENT 4 — May be apprehension of injury TO THAT PERSON OR TO ANOTHER (third-party threats count)",
                ],
            },
            {
                "id": "(a)(4) Catchall — § 6320 enjoinable behavior",
                "verbatim": "To engage in any behavior that has been or could be enjoined pursuant to Section 6320.",
                "elements": [
                    "ELEMENT — Behavior of any kind that has been enjoined OR could be enjoined under § 6320 (which is a broad list including molesting, attacking, striking, stalking, threatening, sexually assaulting, battering, harassing, telephoning, destroying personal property, contacting, coming within a specified distance of, or disturbing the peace of the other party)",
                ],
                "note": "The (a)(4) catchall is the broadest of the four definitional categories. § 6320 itself must be fetched to understand the full scope of (a)(4).",
            },
        ],
        "subdivision_b": {
            "verbatim": "Abuse is not limited to the actual infliction of physical injury or assault.",
            "doctrinal_significance": "Subdivision (b) is the legislative declaration that abuse under DVPA is BROADER than physical injury. Reasonable apprehension under (a)(3) and § 6320 enjoinable conduct under (a)(4) capture non-physical forms of abuse.",
        },
    },
    "amendment_history": [
        {"year": 1993, "stats": "Stats. 1993, Ch. 219, Sec. 154", "event": "Original DVPA enactment as Division 10 of the new Family Code (the 1993 recodification that consolidated family law from the Civil Code)"},
        {"year": 2015, "stats": "Stats. 2015, Ch. 303, Sec. 149 (AB 731)", "event": "Most recent amendment, effective January 1, 2016"},
    ],
    "audit_purpose": "Map § 6203 against the abuse-history factor of Family Code § 3011(a)(2)(B) and the steward's case file. § 6203 is the definitional gate. For each alleged 'abuse' in the case file, the audit asks: did the conduct meet § 6203's specific definitions? If not, the (a)(2)(A)/(B) abuse-history factor of § 3011 was structurally inapplicable regardless of corroboration.",
    "audit_items": [
        {
            "id": "(a)(1) intent/recklessness element",
            "rec": "For each (a)(1)-type allegation in the case file, the petitioner had to plead and prove INTENT OR RECKLESSNESS. Pure accident, mistake, or simple negligence does not satisfy (a)(1). For each filing alleging (a)(1) abuse against the steward, the audit asks: was the conduct intentional or reckless under the statutory definition?",
            "status": "FLAGGED — requires steward review of each alleged (a)(1) incident.",
        },
        {
            "id": "(a)(3) reasonable-imminent-serious test",
            "rec": "For each (a)(3)-type allegation (apprehension of harm), the petitioner had to plead and prove ALL FOUR elements: (1) reasonable apprehension, (2) imminent harm, (3) serious bodily injury, (4) by/to the person or another. Speculative, future, minor, or hypothetical fears do not satisfy (a)(3). The 'reasonable' element is objective — a subjective fear that no reasonable person would have shared is not enough.",
            "status": "FLAGGED — many DVRO petitions in family law turn on (a)(3); requires per-incident review.",
        },
        {
            "id": "(a)(4) § 6320 catchall — must fetch § 6320",
            "rec": "The (a)(4) catchall imports the entire scope of behaviors enjoinable under § 6320. § 6320 must be fetched as next-step deepening to understand what (a)(4) actually covers in the steward's case context.",
            "status": "OUTSTANDING — § 6320 is the next standard to fetch in this umbrella deepening.",
        },
        {
            "id": "Bridge to Family Code § 3011(a)(2)(B)",
            "rec": "§ 3011(a)(2)(B) explicitly cross-references § 6203 for the definition of abuse against persons enumerated in clauses (ii) and (iii) of (A). This means: even if alleged 'abuse history' was raised in custody proceedings against the steward, the (a)(2)(B) factor only applies if the alleged conduct fell within § 6203's specific definitions. Allegations that don't meet § 6203 cannot trigger § 3011(a)(2). The audit step is: for each (a)(2) allegation in the steward's custody case file, identify which § 6203 category was invoked and verify whether the conduct actually met that category's elements.",
            "status": "CRITICAL — DOCTRINAL BRIDGE between this standard and Family Code § 3011 (the first occupant of Umbrella 11).",
        },
        {
            "id": "OPD records pickup — § 6203 and § 3011 audits combined",
            "rec": "The October 2025 OPD records pickup proved the related 6/2/2009 OPD report does not exist in OPD records. The combined audit is: (1) for each filing that invoked § 3011(a)(2), identify the alleged abuse conduct; (2) classify it under § 6203's categories; (3) verify whether the cited corroborating OPD report actually exists in OPD records; (4) verify whether the alleged conduct, as described in the report (if it exists), actually meets § 6203's elements. Failure at any step means § 3011(a)(2) was structurally inapplicable.",
            "status": "CRITICAL — DOCTRINAL BRIDGE to the OPD records pickup investigatory finding.",
        },
    ],
    "umbrellas": ["Family / Personal Status (Umbrella 11) — primary", "Authority / Governing Law (Umbrella 01) — secondary"],
    "owner_citizen": "CA_Family_Law_Litigator",
    "sha256": "6819693aa157c7a0f97f232be98d46e8f518db71cb91b8b85600973549bea036",
    "umbrella_position": "second occupant under Umbrella 11 (definitional bridge from § 3011)",
}


FAM_3020 = {
    "standard_id": "CA_FAM_3020_CUSTODY_POLICY",
    "citizen": "CA_Family_Law_Litigator",
    "folder": "cal_fam_3020_custody_policy",
    "primary_citation": {
        "jurisdiction": "California",
        "code": "California Family Code",
        "section": "§ 3020",
        "popular_name": "Custody Policy — Health/Safety/Welfare Primary; Frequent and Continuing Contact; Conflict-Resolution Rule",
        "current_codification_url": "https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=3020.&lawCode=FAM",
        "current_form_local_artifact": "current/cal_fam_3020_leginfo.html",
        "verbatim_text_extracted_artifact": "current/cal_fam_3020_leginfo.txt",
    },
    "structural_location": {
        "code": "California Family Code",
        "division": "DIVISION 8. CUSTODY OF CHILDREN [3000 - 3465]",
        "division_history": "Division 8 enacted by Stats. 1992, Ch. 162, Sec. 10",
        "part": "PART 2. RIGHT TO CUSTODY OF MINOR CHILD [3020 - 3204]",
        "chapter": "CHAPTER 1. General Provisions [3020 - 3032]",
        "section_history": "Most recent amendment: Stats. 2019, Ch. 551, Sec. 2 (SB 495) Effective January 1, 2020",
    },
    "verbatim_factor_inventory": {
        "structure": "Section 3020 contains 4 subdivisions: (a) safety primary, (b) frequent and continuing contact, (c) CONFLICT-RESOLUTION RULE, (d) anti-discrimination prohibition.",
        "subdivisions": [
            {
                "id": "(a) Health/safety/welfare primary",
                "verbatim": "The Legislature finds and declares that it is the public policy of this state to ensure that the health, safety, and welfare of children shall be the court's primary concern in determining the best interests of children when making any orders regarding the physical or legal custody or visitation of children. The Legislature further finds and declares that children have the right to be safe and free from abuse, and that the perpetration of child abuse or domestic violence in a household where a child resides is detrimental to the health, safety, and welfare of the child.",
                "doctrinal_significance": "Subdivision (a) declares that health, safety, and welfare are the COURT'S PRIMARY CONCERN — not just one factor among many. This is the textual basis for treating safety as a trump factor when § 3011(a) factors point in different directions.",
            },
            {
                "id": "(b) Frequent and continuing contact policy",
                "verbatim": "The Legislature finds and declares that it is the public policy of this state to ensure that children have frequent and continuing contact with both parents after the parents have separated or dissolved their marriage, or ended their relationship, and to encourage parents to share the rights and responsibilities of child rearing in order to effect this policy, except when the contact would not be in the best interests of the child, as provided in subdivisions (a) and (c) of this section and Section 3011.",
                "doctrinal_significance": "Subdivision (b) is the 'frequent and continuing contact' policy that California family law presumptively favors — children should have meaningful contact with both parents after separation. This policy is SUBJECT TO the safety priority of (a) and the conflict-resolution rule of (c).",
            },
            {
                "id": "(c) CONFLICT-RESOLUTION RULE — load-bearing",
                "verbatim": "When the policies set forth in subdivisions (a) and (b) of this section are in conflict, a court's order regarding physical or legal custody or visitation shall be made in a manner that ensures the health, safety, and welfare of the child and the safety of all family members.",
                "doctrinal_significance": "Subdivision (c) is the operational tiebreaker. When safety (a) and frequent contact (b) conflict, the court's order MUST ensure safety AND THE SAFETY OF ALL FAMILY MEMBERS. The 'safety of all family members' phrase explicitly extends safety beyond just the child to other household members. This is the textual mechanism by which a court can restrict (b) frequent contact when (a) safety so requires.",
            },
            {
                "id": "(d) Anti-discrimination",
                "verbatim": "The Legislature finds and declares that it is the public policy of this state to ensure that the sex, gender identity, gender expression, or sexual orientation of a parent, legal guardian, or relative is not considered in determining the best interests of the child.",
                "doctrinal_significance": "Subdivision (d) is the policy declaration corresponding to the prohibition in § 3011(b). § 3011(b) is the binding rule; § 3020(d) is the policy basis.",
            },
        ],
    },
    "amendment_history": [
        {"year": 1992, "stats": "Stats. 1992, Ch. 162, Sec. 10", "event": "Original enactment as part of the new Family Code (the 1992 consolidation from the Civil Code)"},
        {"year": 2019, "stats": "Stats. 2019, Ch. 551, Sec. 2 (SB 495)", "event": "Most recent amendment, effective January 1, 2020. SB 495 added the anti-discrimination policy declaration in (d), the policy companion to § 3011(b)'s binding rule."},
    ],
    "audit_purpose": "Map § 3020 against the steward's 16-year custody history. § 3020 is the policy foundation under which § 3011 is interpreted. The audit asks whether (a)/(b)/(c) were applied correctly in each custody decision, particularly whether the (c) conflict-resolution rule was used to restrict the steward's frequent and continuing contact with his child without adequate (a) safety justification.",
    "audit_items": [
        {
            "id": "(a) safety priority",
            "rec": "The steward held sole custody for 16 years (2009–2025). Sole custody is consistent with the (a) safety priority being applied — i.e., the court determined that safety required restricting the other parent's contact. The audit asks: was the (a) safety determination supported by the actual record, or was it formulaic?",
            "status": "FLAGGED — requires review of the original 2009 custody determination.",
        },
        {
            "id": "(b) frequent and continuing contact policy",
            "rec": "Per (b), children should have FREQUENT AND CONTINUING CONTACT with BOTH parents. The steward's sole custody for 16 years means the OTHER parent's contact was the limited side. The audit asks: did the visitation arrangements honor the (b) policy as much as the (a)/(c) safety analysis allowed? If the (b) policy was treated as fully overridden rather than as restricted-but-honored, that's a doctrinal error.",
            "status": "FLAGGED — requires review of visitation orders.",
        },
        {
            "id": "(c) conflict-resolution rule",
            "rec": "When (a) and (b) conflict, the court's order shall ensure 'the health, safety, and welfare of the child AND THE SAFETY OF ALL FAMILY MEMBERS.' The 'all family members' phrase is doctrinally significant: it extends the safety analysis beyond just the child. In the steward's case, if the safety analysis included ONLY the child and not the steward himself or other household members, that's an incomplete (c) analysis.",
            "status": "CRITICAL — the 'safety of all family members' clause is a doctrinal lever the steward can use to argue that his own safety (as the custodial parent) was a relevant factor under (c). If the orchestration pattern documented in project_familylaw_orchestration.md threatened the steward's safety, that's a (c) consideration.",
        },
        {
            "id": "(d) anti-discrimination",
            "rec": "Subdivision (d) was added in 2019 by SB 495. It is NOT retroactive to pre-2020 custody determinations in the steward's case. For any post-2020 custody proceedings or current/future proceedings, this prohibition applies.",
            "status": "FORWARD-LOOKING — not retroactive.",
        },
        {
            "id": "Bridge to Family Code § 3011",
            "rec": "§ 3011 is interpreted within the policy framework of § 3020. Specifically, § 3011 itself opens with 'consistent with Section 3020' — meaning § 3011's factors are weighted within the § 3020 (a)/(b)/(c) framework. Any audit of § 3011 application in the case file must also audit whether the § 3020 framework was correctly applied.",
            "status": "CRITICAL — DOCTRINAL BRIDGE to § 3011 (the first occupant of Umbrella 11). The two sections must be read together.",
        },
    ],
    "umbrellas": ["Family / Personal Status (Umbrella 11) — primary", "Authority / Governing Law (Umbrella 01) — secondary"],
    "owner_citizen": "CA_Family_Law_Litigator",
    "sha256": "53f9bf7383b1f8215913f15c0cc05b10e48f7ee0c75ea7f4d597a32bfd00194c",
    "umbrella_position": "second occupant under Umbrella 11 (policy foundation for § 3011)",
}


def deepen(s):
    folder = BASE / s["citizen"] / "standards" / s["folder"]
    manifest_path = folder / "manifest.json"
    provenance_path = folder / "provenance.json"

    manifest = {
        "standard_id": s["standard_id"],
        "version": "0.1.0-substance-and-steward-audited-second-seed",
        "filed_at_utc": NOW,
        "filed_by": "Claude (assistant) under steward direction — Michael Hartmann, Vernen Legal Compliance",
        "status": "PROPOSED-DEEPENED — second occupant of Umbrella 11 (Family / Personal Status). Verbatim text extracted at first filing; steward case relevance audit included from inception. Awaiting second-mouth countersignature.",
        "build_context": s["umbrella_position"],
        "primary_citation": s["primary_citation"],
        "structural_location": s["structural_location"],
        "verbatim_factor_inventory": s["verbatim_factor_inventory"],
        "amendment_history_visible_on_leginfo": s["amendment_history"],
        "steward_case_relevance_audit": {
            "purpose": s["audit_purpose"],
            "audit_filed_at_utc": NOW,
            "audit_filed_by": "Claude (assistant) at first-mouth level; steward review required",
            "factor_audits": [
                {
                    "factor_id": item["id"],
                    "audit_recommendation": item["rec"],
                    "audit_status": item["status"],
                }
                for item in s["audit_items"]
            ],
        },
        "umbrellas": s["umbrellas"],
        "owner_citizen": {"primary": s["owner_citizen"]},
        "triple_constraint_test_results": {
            "governing_guidelines": {"passes": True, "evidence": f"{s['primary_citation']['code']} {s['primary_citation']['section']} located at official California Legislative Information; binding state authority confirmed; verbatim text extracted"},
            "standards_of_creation": {"passes": True, "evidence": "Section is well-formed and properly codified"},
            "standard_of_care": {
                "passes": "PARTIAL",
                "current_layer": f"VERIFIED — current form fetched, hashed (sha256: {s['sha256']}), and verbatim-extracted",
                "evolution_layer": "PARTIAL — amendment history captured at manifest level; primary-source amendment volumes not yet downloaded",
                "origin_layer": "IDENTIFIED — recorded in amendment_history",
            },
        },
        "five_layer_bar_status": {
            "rule": "PRESENT — verbatim text extracted with element-by-element structural breakdown",
            "reasoning": "PRESENT — legislative findings or doctrinal significance captured per subdivision",
            "historical_loss": "OUTSTANDING",
            "cross_references": "PARTIAL — explicit cross-reference to § 3011 (the first Umbrella 11 occupant) noted in audit",
            "verifiable_provenance": "PRESENT for current form",
        },
        "two_witness_status": {
            "first_mouth_proposer": "Claude (assistant) under steward direction (Michael Hartmann), 2026-04-08",
            "second_mouth_witness": "NONE — not yet countersigned",
            "publishable_to_corpus": False,
            "status": "PROPOSED-DEEPENED",
        },
        "files": {
            "origin": [],
            "evolution": [],
            "current": [s["primary_citation"]["current_form_local_artifact"], s["primary_citation"]["verbatim_text_extracted_artifact"]],
            "context": [],
            "manifest": "manifest.json",
            "provenance": "provenance.json",
        },
        "outstanding_work": [
            "Locate and fetch the original-enactment statute volume for primary-source verification",
            "Fetch each cross-referenced section identified in the audit (Probate § 1800.3 / 1828.5 / 1821 / 1826 / 1851 for § 1801; Family Code § 6320 for § 6203)",
            "Document the historical-loss layer — specific incidents driving the original enactment",
            "STEWARD: Execute the audit items above against the case file",
            "Obtain second-mouth countersignature before publication",
        ],
    }

    provenance = {
        "standard_id": s["standard_id"],
        "provenance_record_filed_at_utc": NOW,
        "fetcher_software": "curl with sha256sum",
        "fetcher_operator": "Claude (assistant) under steward direction (Michael Hartmann)",
        "fetches": [
            {
                "artifact_local_path": s["primary_citation"]["current_form_local_artifact"],
                "source_url": s["primary_citation"]["current_codification_url"],
                "source_authority": "California Legislative Information (leginfo.legislature.ca.gov), maintained by the Office of Legislative Counsel of California",
                "source_authority_type": "primary",
                "fetched_at_utc": NOW,
                "fetch_method": "curl -sSL --max-time 60",
                "sha256": s["sha256"],
                "content_description": s["primary_citation"]["popular_name"],
            }
        ],
    }

    manifest_path.write_text(json.dumps(manifest, indent=2))
    provenance_path.write_text(json.dumps(provenance, indent=2))
    return manifest_path


def main():
    written = []
    for s in [PROB_1801, FAM_6203, FAM_3020]:
        p = deepen(s)
        written.append(p)
        json.loads(p.read_text())
    print(f"Wrote {len(written)} second-occupant manifests")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
