# Historical Chain — 18 U.S.C. §§2701-2712 (Stored Communications Act)

## The Two-Stage Evolution

### Stage 01 — 1986 Origin: ECPA Title II

Congress enacted the Stored Communications Act as Title II of ECPA in 1986 to fill
the gap between the 1968 Wiretap Act (real-time interception) and emerging digital
storage. Email, voicemail, and bulletin board messages sitting on servers had no
specific legal protection. The third-party doctrine threatened to eliminate Fourth
Amendment protection entirely.

The SCA created:
- §2701: Prohibition on unauthorized access to stored communications (criminal + civil)
- §2702: Voluntary disclosure prohibition (service providers cannot freely disclose)
- §2703: Government access procedures (tiered: warrant vs. court order vs. subpoena
  depending on communication type and age)
- §2707: Civil action with $1,000 minimum damages per violation

**The age-based design problem:** The 180-day rule assumed email would be deleted or
retrieved quickly. As email became a permanent communication medium, the 180-day tier
became legally problematic (ultimately held constitutionally infirm by Warshak).

---

### Stage 02 — 2001 PATRIOT Act + Warshak Constitutional Interpretation

The PATRIOT Act expanded government emergency access and modernized subscriber record
definitions. The civil action framework (§2707) was not changed.

The Warshak decision (6th Cir. 2010) established that stored email has full Fourth
Amendment protection, effectively superseding the 180-day age-based distinction for
government access purposes. The DOJ adopted a national warrant policy.

For civil claims: the civil §2707 framework is unchanged from 1986; $1,000 minimum
per violation remains operative. Warshak strengthens the seriousness of private
unauthorized access claims.

---

## The ECPA Three-Title Structure

| Title | Statute | Covers | Civil Minimum |
|-------|---------|--------|---------------|
| I | §§2510-2522 (Wiretap Act) | Real-time interception in transit | $10,000/violation |
| II | §§2701-2712 (SCA) | Stored communications at rest | $1,000/violation |
| III | §§3121-3127 (Pen Register) | Non-content routing data | No civil minimum |

For SIM swap claims: Titles I and II both apply. Each covers a different phase of the
same attack chain, and the remedies are cumulative.

## Key Cases in the Evolution

| Case | Year | Contribution |
|------|------|-------------|
| Theofel v. Farey-Jones, 359 F.3d 1066 (9th Cir.) | 2004 | "Without authorization" is broad; stored emails after reading remain in electronic storage (backup protection prong); 9th Circuit (binding in California) |
| United States v. Warshak, 631 F.3d 266 (6th Cir.) | 2010 | Fourth Amendment requires warrant for stored email; SCA 180-day rule unconstitutional for content; constitutional weight of stored email privacy (persuasive in 9th Circuit) |
