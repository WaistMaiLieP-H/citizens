# Historical Chain — 18 U.S.C. §§3121-3127 (Pen Register Act)

## The Two-Stage Evolution

### Stage 01 — 1986 Origin: ECPA Title III

Smith v. Maryland (1979) established no Fourth Amendment protection for dialed phone
numbers — metadata had no constitutional protection. Congress responded in 1986 with
the Pen Register Act: statutory protection for metadata, requiring court orders for
law enforcement pen registers, but with no civil damages provision.

The content/metadata distinction was embedded in the ECPA framework from the beginning:
- Content: strong protection (Wiretap Act $10K civil; SCA $1K civil)
- Metadata: lighter statutory protection (Pen Register Act; criminal enforcement only)

---

### Stage 02 — 2001 PATRIOT Act: Internet Routing Added

The PATRIOT Act expanded pen register coverage to include internet routing information —
IP addresses, email headers, URL addresses. The expansion also added multi-district
jurisdiction for pen register orders.

**The URL debate (unresolved):** Whether detailed URL paths (revealing the specific
pages a user accesses, not just the website) constitute "content" or "routing information"
remains a contested question in the courts. The 9th Circuit in Forrester (2008) held
IP addresses and email headers are routing information but left the URL question open.

---

## The ECPA Three-Title Structure — Complete Picture

| Title | Statute | Covers | Civil Remedy | Government Standard |
|-------|---------|--------|-------------|---------------------|
| I | §§2510-2522 | Content — real-time | §2520: $10,000/event | Full probable cause warrant |
| II | §§2701-2712 | Content — stored | §2707: $1,000/event | Warrant/order/subpoena (tiered) |
| III | §§3121-3127 | Routing metadata | None | Court order (relevance, not probable cause) |

## The Pen Register Act's Role in Civil Litigation

No civil damages, but critical for:
1. **Evidence collection:** AT&T call records documenting SIM swap period
2. **Violation counting:** Routing data reveals how many calls/messages were intercepted
3. **Criminal prosecution support:** §3121 criminal violation characterization of SIM swap attack
4. **URL content argument:** If URL accesses during account takeover = content, those may be §2511 violations adding $10,000/event damages

## Key Cases

| Case | Year | Contribution |
|------|------|-------------|
| Smith v. Maryland, 442 U.S. 735 | 1979 | No Fourth Amendment protection for dialed numbers; prompted ECPA §§3121-3127 |
| Carpenter v. United States, 585 U.S. 296 | 2018 | Narrowed third-party doctrine; long-term CSLI requires warrant; Smith not overruled but limited |
| United States v. Forrester, 512 F.3d 500 (9th Cir.) | 2008 | IP addresses and email headers = routing information; URL question unresolved |
