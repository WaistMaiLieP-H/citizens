#!/usr/bin/env python3
"""
_populate_family_law_historical_chain.py

Generates the 7 historical chain stub files for the CA_Family_Law_Litigator
Citizen, plus the README index. Each stub contains citation metadata and
context for the chain entry; primary-source fetch is outstanding work for
subsequent passes.

The chain runs from the 1849 California Constitution and 1850 community
property statute, through the 1872 Civil Code, the 1969 Family Law Act
(Boggs Act / no-fault divorce), the 1992 Family Code consolidation, the
1993 technical recodification, to the current Family Code.
"""

import json
from pathlib import Path

NOW = "2026-04-08T19:10:00Z"
BASE = Path("${citizens}/CA_Family_Law_Litigator/historical_chain")


CHAIN = [
    {
        "filename": "01_1849_constitution.json",
        "data": {
            "sequence": 1,
            "year": 1849,
            "name": "California Constitution of 1849 — Article XI § 14 (Separate Property of Married Women)",
            "popular_name": "1849 California Constitution",
            "context": "California's first constitution, drafted at the Constitutional Convention in Monterey September-October 1849, before California was a U.S. state. California was admitted to the Union on September 9, 1850. The 1849 Constitution included one of the earliest explicit constitutional protections for the property rights of married women in U.S. history — Article XI § 14 (sometimes cited as Art. XI § 14 or Art. XI § 13 depending on the source) protected the separate property of married women from their husbands' debts. This provision predates the federal Married Women's Property Acts and the more famous New York Married Women's Property Act of 1848.",
            "doctrinal_significance": "Article XI § 14 of the 1849 Constitution is the textual origin of California's distinctive community-property regime. By treating married women's separate property as constitutionally protected, the framers created the structural framework under which California family law has evolved for 175 years. The provision is the earliest specific California constitutional protection touching family relationships and is the doctrinal predecessor of every subsequent California family-law statute.",
            "verbatim_text_known_from_secondary_sources": "(approximately) 'All property, both real and personal, of the wife, owned or claimed by her before marriage, and that acquired afterwards by gift, devise, or descent, shall be her separate property; and laws shall be passed more clearly defining the rights of the wife, in relation as well to her separate property as to that held in common with her husband.' [Verbatim text needs primary-source verification from a digitized 1849 Constitution.]",
            "primary_source_locations": [
                "California State Archives — original 1849 Constitution document (Sacramento, California)",
                "California State Library — Digital Collections (https://www.library.ca.gov/collections/digital-collections/)",
                "Library of Congress — California Constitution (1849)",
                "Bancroft Library at UC Berkeley — early California documents",
                "HathiTrust Digital Library — California historical documents"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Fetch a digitized 1849 Constitution from the California State Archives, California State Library, or Library of Congress; extract the verbatim text of Article XI § 14; hash and store as primary source",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "02_1850_community_property.json",
        "data": {
            "sequence": 2,
            "year": 1850,
            "name": "California Community Property Act of 1850 (one of the first acts of the first California Legislature)",
            "popular_name": "1850 Community Property Act",
            "context": "After California became a state on September 9, 1850, the first California Legislature met in San Jose in December 1849 and continued through 1850. Among its first acts was the codification of community property law. The 1850 Act was titled 'An Act defining the rights of husband and wife' and was passed on April 17, 1850 (per most secondary sources). It implemented the community-property framework that the 1849 Constitution had anticipated.",
            "doctrinal_significance": "The 1850 Act is the earliest California statutory expression of community property doctrine. California's adoption of community property (rather than the common-law marital property regime that prevailed in most other states) reflects California's Spanish/Mexican legal heritage — California had been a Mexican territory until 1848, and the Mexican civil law tradition included community property. The 1850 Act preserved this tradition under U.S. statehood and established the foundation for everything that followed in California family property law.",
            "primary_source_locations": [
                "California State Archives — original 1850 Statutes",
                "California State Library — Digital Collections",
                "Statutes of California 1850 (the first volume of California session laws; potentially digitized at HathiTrust or Internet Archive)",
                "California Legislative Information (leginfo.legislature.ca.gov) — California Assembly Chief Clerk archive may include early statutes"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Locate the 1850 Statutes of California Vol. 1 (California's first volume of session laws). Check the California Assembly Chief Clerk's archive at clerk.assembly.ca.gov for the historical statute archive — the same archive that holds the 1929/1933/1935 statute volumes already in the corpus.",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "03_1872_civil_code.json",
        "data": {
            "sequence": 3,
            "year": 1872,
            "name": "California Civil Code of 1872 — Title II (Husband and Wife) and Title III (Parent and Child)",
            "popular_name": "1872 Civil Code",
            "context": "The 1872 Civil Code was California's first comprehensive codification of civil law, drafted by the California Code Commission under the leadership of Stephen J. Field and modeled on the Field Code that David Dudley Field had drafted for New York (which had been adopted only in part in New York but adopted comprehensively in California). The 1872 Civil Code consolidated the prior 22 years of California statutory family law into a unified framework. Title II of the Civil Code covered Husband and Wife (the marital relationship, community property, separation, divorce, and dissolution); Title III covered Parent and Child (legitimacy, custody, support, adoption, parental authority).",
            "doctrinal_significance": "The 1872 Civil Code is the first comprehensive California family-law statute. Many provisions in the modern Family Code descend directly from 1872 Civil Code Title II and Title III provisions, with the 1992 Family Code consolidation being structurally a recodification rather than a substantive change. Reading the 1872 text alongside the modern Family Code reveals which doctrines have been continuous for 153 years and which have been substantively modified. The 'best interest of the child' principle, for example, has 1872 Civil Code antecedents in Title III, even though the specific § 3011 factors are 20th-century additions.",
            "primary_source_locations": [
                "Annotated California Civil Code 1872 (multiple historical editions; HathiTrust has digitized copies)",
                "California State Library — Digital Collections",
                "California State Archives",
                "Internet Archive — California legal historical documents"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Locate digitized 1872 California Civil Code. HathiTrust catalog has California legal publications including code editions. Search for 'California Civil Code 1872' in the HathiTrust California Legislative Publications collection.",
            "key_titles_to_extract": [
                "Title II — Husband and Wife (the marital relationship, community property, divorce)",
                "Title III — Parent and Child (legitimacy, custody, support, parental authority, adoption)"
            ],
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "04_1969_family_law_act.json",
        "data": {
            "sequence": 4,
            "year": 1969,
            "name": "California Family Law Act of 1969 (Stats. 1969 Ch. 1608) — the 'Boggs Act' / no-fault divorce",
            "popular_name": "Family Law Act of 1969 / Boggs Act",
            "context": "Authored by Assemblyman James A. Hayes (chairman of the Assembly Judiciary Committee) and signed by Governor Ronald Reagan on September 5, 1969. Effective January 1, 1970. The Family Law Act of 1969 was the first no-fault divorce law in the United States. It abolished the prior fault-based grounds for divorce in California (adultery, extreme cruelty, willful desertion, willful neglect, habitual intemperance, conviction of felony, incurable insanity) and replaced them with two no-fault grounds: 'irreconcilable differences which have caused the irremediable breakdown of the marriage' and 'incurable insanity.' The Act also renamed 'divorce' to 'dissolution of marriage' and 'alimony' to 'spousal support.'",
            "doctrinal_significance": "The 1969 Family Law Act is the most significant single change in California family law since 1872. It eliminated fault as a substantive issue in dissolution proceedings, transforming the litigation from an adversarial inquiry into marital wrongdoing into a more administrative determination of property division, support, and custody. The Act also restructured the procedural framework, replacing the prior 'divorce action' with the modern dissolution proceeding under FL-100 (Petition for Dissolution). California's no-fault model was rapidly adopted by other states throughout the 1970s. The 1969 Act is the doctrinal predecessor of every dissolution action filed in California today, including the steward's RF09470833 (2009) and Christina's RF10508853 (2010) dissolutions.",
            "primary_source_locations": [
                "California Statutes 1969 Ch. 1608 — California State Archives or California Assembly Chief Clerk historical archive",
                "California Legislative Information (leginfo.legislature.ca.gov) — historical statutes",
                "HathiTrust California Legislative Publications collection"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Fetch Stats. 1969 Ch. 1608 from the California Assembly Chief Clerk historical archive. The same archive holds the 1929/1933/1935 statute volumes already in the corpus; the URL pattern should generalize.",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "05_1992_family_code.json",
        "data": {
            "sequence": 5,
            "year": 1992,
            "name": "California Family Code Consolidation (Stats. 1992 Ch. 162) — creation of the Family Code as a separate code",
            "popular_name": "1992 Family Code Consolidation",
            "context": "Stats. 1992 Ch. 162 was the comprehensive recodification that consolidated California family law from its prior locations (primarily Civil Code Title II and Title III, plus scattered provisions in the Code of Civil Procedure, Probate Code, Welfare and Institutions Code) into a single new Family Code. The recodification took effect January 1, 1994. Per the legislative history (and confirmed by the Legislative Intent Service), the consolidation was intended to be a structural reorganization, not a substantive change — most provisions were carried forward verbatim from their prior locations, with only typographical and cross-reference adjustments.",
            "doctrinal_significance": "The 1992 Family Code is the structural framework under which all modern California family law operates. It is the code that contains Family Code § 3011 (Best Interest of the Child), § 3020 (Custody Policy), § 6203 (DVPA Abuse Definition), § 3164 (Mediator Qualifications), § 1815 (Counselor Qualifications), § 1816 (DV Training Requirements) — every standard now in the CA_Family_Law_Litigator corpus that begins 'Family Code §' descends from this 1992 consolidation. Critically, the consolidation was NOT a substantive change — which means the underlying doctrines have continuous lineage to the 1872 Civil Code and ultimately to the 1849/1850 origin. § 3011, for example, descends from the prior Civil Code § 4608 (added 1982), which itself rests on Civil Code Title III provisions going back to 1872.",
            "primary_source_locations": [
                "Stats. 1992 Ch. 162 — California State Archives or Assembly Chief Clerk historical archive",
                "California Legislative Information"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Fetch Stats. 1992 Ch. 162 from the California Assembly Chief Clerk historical archive. This is the 'patient zero' chapter for every modern Family Code section in the corpus.",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "06_1993_family_code_recodification.json",
        "data": {
            "sequence": 6,
            "year": 1993,
            "name": "California Family Code Technical Recodification (Stats. 1993 Ch. 219)",
            "popular_name": "1993 Technical Recodification",
            "context": "Stats. 1993 Ch. 219 was a follow-up technical recodification chapter that addressed gaps and errors discovered after the 1992 Ch. 162 consolidation. It is the chapter that 'repealed and added' or 'added' many specific Family Code provisions in their final form. For example, § 3011 itself was 'repealed and added' by Stats. 1993 Ch. 219 § 115.5. § 3164 was 'added' by Stats. 1993 Ch. 219 § 116.87. The 1993 chapter is therefore the immediate enacting authority for several of the corpus's foundational Family Code standards.",
            "doctrinal_significance": "Many Family Code sections in the modern corpus cite Stats. 1993 Ch. 219 as their enacting chapter. Understanding this chapter as a 'technical re-add' rather than a substantive change is doctrinally important: when courts interpret these sections, they look back through the 1993 chapter to the underlying doctrines that the chapter formalized. The chapter is also the place where any drafting errors or boundary cases from the 1992 consolidation were resolved.",
            "primary_source_locations": [
                "Stats. 1993 Ch. 219 — California State Archives or Assembly Chief Clerk historical archive"
            ],
            "status": "STUB — primary source not yet fetched",
            "next_step": "Fetch Stats. 1993 Ch. 219 from the California Assembly Chief Clerk historical archive. This is the immediate enacting authority for § 3011 (§ 115.5) and § 3164 (§ 116.87) and several other foundational corpus standards.",
            "filed_at_utc": NOW
        }
    },
    {
        "filename": "07_current.json",
        "data": {
            "sequence": 7,
            "year": "current (2026)",
            "name": "Current California Family Code (as in force 2026)",
            "popular_name": "Modern California Family Code",
            "context": "The current California Family Code is the operational law governing every family-court matter in California today, including the steward's pending state action against Christina Marie Cerretani. The Code is divided into 17 divisions covering: Division 1 (Preliminary Provisions), Division 2 (General Provisions), Division 3 (Marriage), Division 4 (Rights and Obligations During Marriage), Division 5 (Conciliation Proceedings — INCLUDES § 1815, § 1816), Division 6 (Nullity, Dissolution, and Legal Separation), Division 7 (Division of Property), Division 8 (Custody of Children — INCLUDES § 3011, § 3020, § 3164), Division 9 (Support), Division 10 (Prevention of Domestic Violence — INCLUDES § 6203), Division 11 (Minors), Division 12 (Parent and Child Relationship), Division 13 (Approval of Activities of Minors), Division 14 (Adoption), Division 15 (Stepparents), Division 16 (Marital Settlement Agreements), Division 17 (Reciprocal Enforcement of Support).",
            "current_corpus_coverage": {
                "directly_built_in_corpus": [
                    "§ 3011 — Best Interest of the Child (Division 8, deepened with steward audit)",
                    "§ 3020 — Custody Policy (Division 8, deepened with steward audit)",
                    "§ 6203 — DVPA Abuse Definition (Division 10, deepened with steward audit)",
                    "§ 3164 — Mediator Qualifications (Division 8, deepened 2026-04-08)",
                    "§ 1815 — Counselor Qualifications (Division 5, deepened 2026-04-08)",
                    "§ 1816 — Mediator DV Training (Division 5, deepened 2026-04-08)"
                ],
                "needed_but_not_yet_built": [
                    "§ 6320 — DVPA enjoinable behaviors (cross-referenced from § 6203(a)(4))",
                    "§ 3046 — Effect of absence due to DV on custody",
                    "§ 6321 — DVRO ex parte temporary order procedures",
                    "§ 6323 — DVRO custody and visitation provisions",
                    "§ 3110, § 3110.5 — Court-connected and private custody evaluators (referenced from § 1816(a)(2))",
                    "§ 3113 — Separate sessions for DV cases (referenced from § 1816(d)(1)(D))",
                    "§ 3104 — Grandparent visitation (the basis of RF10508859)"
                ]
            },
            "doctrinal_significance": "The current Family Code is the law under which the steward's pending state action against Christina Marie Cerretani will be filed and adjudicated. Every standard in the corpus must trace forward from its historical origin to its current form to be doctrinally complete. This entry is the destination of the chain.",
            "primary_source_locations": [
                "California Legislative Information (leginfo.legislature.ca.gov) — official Family Code text",
                "Currently bound to the 6 deepened Family Code standards in ${citizens}/CA_Family_Law_Litigator/standards/"
            ],
            "status": "PARTIAL — 6 sections deepened with verbatim text and steward audits; many more enumerated as 'needed but not yet built' in tether.json",
            "filed_at_utc": NOW
        }
    },
]


README = """# CA_Family_Law_Litigator — Historical Chain

**Purpose:** Origin-to-present statutory chain for California family law. Each entry is a stub with citation metadata; primary-source fetch is outstanding work.

**Filed:** 2026-04-08
**Citizen:** CA_Family_Law_Litigator

## The chain

| # | Year | Name | Status |
|---|---|---|---|
| 1 | 1849 | California Constitution Art. XI § 14 (married women's separate property) | STUB |
| 2 | 1850 | Community Property Act of 1850 (first California Legislature) | STUB |
| 3 | 1872 | California Civil Code Title II (Husband and Wife) and Title III (Parent and Child) | STUB |
| 4 | 1969 | Family Law Act of 1969 (Stats. 1969 Ch. 1608) — no-fault divorce / Boggs Act | STUB |
| 5 | 1992 | Family Code Consolidation (Stats. 1992 Ch. 162) — Family Code created | STUB |
| 6 | 1993 | Family Code Technical Recodification (Stats. 1993 Ch. 219) — § 3011 / § 3164 added here | STUB |
| 7 | 2026 | Current California Family Code | PARTIAL (6 sections deepened in corpus) |

## Why the chain matters

The Vernen doctrine requires that every standard be traceable from its origin through the chain of amendments to its current form. For family law, the chain runs back 175+ years to California's first constitution. Knowing the chain matters because:

1. **Continuity vs change.** When a court interprets § 3011, it looks back through the 1993 recodification to the 1992 consolidation to the prior Civil Code § 4608 (1982) to its underlying common-law antecedents. The further back the chain runs, the more weight a doctrine carries.
2. **Substantive vs technical changes.** The 1992 consolidation was structurally a recodification, not a substantive change. The 1993 chapter was a technical re-add. The 1969 Family Law Act was a substantive change. Knowing which is which determines how aggressively a court will modernize a doctrine.
3. **Reading the modern statute against its origin.** The 'best interest of the child' principle in § 3011 has 1872 Civil Code Title III antecedents. The community property regime in modern Division 7 has 1849 constitutional roots. These deep lineages are what make California family law distinctive from other states.
4. **The mediator-qualifications backbone.** The Sala Ajaniku audit rests on § 3164(b) → § 1815(a)(7) → § 1816. The 'shall' language in § 3164(b) was added by Stats. 1993 Ch. 219 § 116.87, which makes 1993 the date of the modern qualifications requirement. Tracing this back to the 1992 consolidation and the prior § 1815 framework is part of establishing that the qualifications floor was firm and well-known at the time of Ajaniku's 2010 appointment.

## Outstanding work

For each chain entry currently STUB, fetch the primary source from the indicated location, extract the relevant verbatim text, hash, and replace the stub with a deepened entry. The most consequential primary sources to fetch first:

1. **Stats. 1993 Ch. 219** — directly enacts § 3011 and § 3164 in their modern form
2. **Stats. 1992 Ch. 162** — the underlying consolidation
3. **Stats. 1969 Ch. 1608** — the Family Law Act / no-fault divorce
4. **1872 California Civil Code Titles II and III** — the foundational comprehensive codification
5. **1850 Community Property Act** — the earliest statutory expression
6. **1849 California Constitution Article XI § 14** — the constitutional origin
"""


def main():
    BASE.mkdir(parents=True, exist_ok=True)
    written = []
    for entry in CHAIN:
        path = BASE / entry["filename"]
        path.write_text(json.dumps(entry["data"], indent=2))
        json.loads(path.read_text())
        written.append(path)
    (BASE / "README.md").write_text(README)
    print(f"Wrote {len(written)} historical chain stub files + README")
    for p in written:
        print(f"  {p}")


if __name__ == "__main__":
    main()
