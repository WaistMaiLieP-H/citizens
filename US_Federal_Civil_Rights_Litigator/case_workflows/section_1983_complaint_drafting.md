# Section 1983 Complaint Drafting

Operational workflow for drafting a complaint under 42 U.S.C. Section 1983.

---

## Step 1: Identify the Defendants

Name every person who participated in the constitutional violation. For each defendant, state the capacity you are suing them in:

- **Individual capacity** means you are suing the person for what they personally did. This is where money damages come from.
- **Official capacity** means you are suing the government office through the person. This is functionally a suit against the entity itself and is used for injunctive or declaratory relief.
- **Municipal entity** means you are suing the city, county, or agency directly. This requires a separate theory (see Step 7).

Always name defendants in individual capacity first. Add official capacity only if you need an injunction against the office.

Corpus reference: `standards/42_usc_1983/`

---

## Step 2: Establish Federal Jurisdiction

The complaint must invoke two jurisdictional statutes:

1. **28 U.S.C. Section 1343(a)(3)** — grants district courts jurisdiction over civil rights actions to redress deprivation of rights under color of state law.
2. **28 U.S.C. Section 1331** — general federal question jurisdiction.

Cite both. Section 1343 is the specific grant; Section 1331 is the backup that covers any claim arising under federal law.

Corpus reference: `standards/28_usc_1343/`

---

## Step 3: Allege "Under Color of" State Law

For each defendant, explain how they acted under color of state law. This means the person used their government position, authority, badge, or office to do what they did.

A police officer making an arrest acts under color of law. A social worker removing a child acts under color of law. A private person acting jointly with a state official can also act under color of law.

If a defendant is purely private with no state connection, Section 1983 does not reach them. Consider Section 1985(3) instead (see `case_workflows/section_1985_conspiracy_pleading.md`).

---

## Step 4: Identify the Constitutional Right Violated

State the specific constitutional provision that was violated. Common violations:

- **Fourth Amendment** — unreasonable search or seizure, excessive force, false arrest
- **Fifth Amendment** — due process deprivation by federal actors (use Bivens, not 1983)
- **Eighth Amendment** — cruel and unusual punishment (applies only to convicted prisoners)
- **Fourteenth Amendment, Due Process Clause** — deprivation of life, liberty, or property without due process; covers most state-actor misconduct
- **Fourteenth Amendment, Equal Protection Clause** — intentional discrimination based on race, sex, or other protected class

Do not cite the amendment in the abstract. State the specific clause and what it protects.

Corpus reference: `standards/42_usc_1983/`, `standards/bivens_doctrine/`

---

## Step 5: Allege Causation

Connect each defendant's specific acts or failures to act to the constitutional injury. Do not lump defendants together. Each defendant must have personally participated in, directed, or knowingly acquiesced in the violation.

Supervisory liability requires more than being someone's boss. Allege that the supervisor set a policy, created a custom, was deliberately indifferent, or personally directed the unconstitutional conduct.

---

## Step 6: Plead Around Qualified Immunity

Qualified immunity will be raised as a defense. Anticipate it in the complaint by:

1. Describing the facts with enough specificity that the violation is obvious on the face of the complaint.
2. Citing a case that was decided before the incident that involved materially similar facts and held the conduct unconstitutional.
3. Alternatively, if the conduct was so egregious that no reasonable officer could have thought it lawful, say so explicitly (the Taylor v. Riojas exception).

The standard from Anderson v. Creighton (1987): a right is clearly established when existing precedent placed the constitutional question "beyond debate" in the specific factual context.

See `case_workflows/qualified_immunity_analysis.md` for the full defensive analysis.

---

## Step 7: Municipal Liability (Monell Claims)

If suing a city, county, or agency, you cannot rely on respondeat superior. The Supreme Court in Monell v. Department of Social Services (1978) requires one of:

1. **Official policy** — a formally adopted rule, regulation, or decision by a final policymaker.
2. **Custom or practice** — a pattern of unconstitutional conduct so persistent and widespread that it effectively has the force of policy.
3. **Failure to train** — deliberate indifference to a known risk that the lack of training would cause constitutional violations (City of Canton v. Harris).
4. **Ratification** — a final policymaker reviewed the specific misconduct and approved it.

Plead which theory applies and identify the final policymaker by name or title.

---

## Step 8: Prayer for Relief

State what you are asking the court to award:

- **Compensatory damages** — for the actual harm suffered (pain, suffering, economic loss, emotional distress).
- **Punitive damages** — available against individual defendants who acted with reckless or callous disregard for rights (Smith v. Wade). Not available against municipalities.
- **Declaratory relief** — a court declaration that the defendants violated the Constitution.
- **Injunctive relief** — a court order requiring the defendants to stop unconstitutional conduct or take corrective action. Note: under the 1996 PLRA amendments, injunctive relief against judges in their judicial capacity is not available under Section 1983.
- **Nominal damages** — if you cannot prove compensable injury but want a judicial finding that a violation occurred (Uzuegbunam v. Preczewski, 2021).

---

## Step 9: Attorney's Fee Demand Under Section 1988

Include a demand for reasonable attorney's fees and costs under 42 U.S.C. Section 1988(b). This statute allows the prevailing party in a Section 1983 action to recover fees.

Even pro se litigants should include this demand. If counsel is retained later, the demand is already preserved. Fees are calculated using the lodestar method (hours reasonably expended multiplied by a reasonable hourly rate).

Corpus reference: `standards/42_usc_1988/`

---

## Step 10: Verify Cross-References

Before filing, confirm every legal citation in the complaint resolves to a standard built in this Citizen's corpus:

| Citation | Corpus Location |
|---|---|
| 42 U.S.C. 1983 | `standards/42_usc_1983/` |
| 42 U.S.C. 1985(3) | `standards/42_usc_1985_3/` |
| 42 U.S.C. 1988 | `standards/42_usc_1988/` |
| 28 U.S.C. 1343 | `standards/28_usc_1343/` |
| 29 U.S.C. 794 (Rehab Act) | `standards/29_usc_794/` |
| 42 U.S.C. 12132 (ADA Title II) | `standards/42_usc_12132/` |
| Bivens doctrine | `standards/bivens_doctrine/` |

If a citation does not resolve, either build the standard first or remove the citation. No unanchored references in a filed document.
