# Evolution Stage 02 — 2007 CPNI Order + 2023 SIM Swap Action

### THE WOUND (PRE-2007)

After the initial 1999 CPNI rules, pretexting attacks continued. The gap: the rules
established the duty to protect CPNI but did not specify how carriers must authenticate
callers before disclosing CPNI or making account changes. Carriers were using "readily
available biographical information" (last four of SSN, date of birth, mother's maiden
name) for authentication — information that could be obtained through pretexting,
data breaches, or public records.

The 2006 Hewlett-Packard pretexting scandal (HP hired investigators who used pretexting
to obtain phone records of journalists and board members) brought CPNI/pretexting
into national prominence. Congress held hearings. The FCC responded with the 2007 order.

### DESIGN RESPONSE — 2007

**FCC Report and Order FCC 07-22 (2007) — "In the Matter of Implementation of the Telecommunications Act of 1996: Telecommunications Carriers' Use of Customer Proprietary Network Information and Other Customer Information":**

**Authentication rules (47 C.F.R. §64.2010):**
- Carriers must use passwords, personal identification numbers, or other shared secrets for authentication
- "Readily available biographical information" alone (SSN, DOB, mother's maiden name) is insufficient for authentication
- Carriers must establish customer-selected passwords for online and telephone access to CPNI

**Breach notification (47 C.F.R. §64.2011):**
- Carriers must notify the FBI and Secret Service within 7 business days of discovering a CPNI breach
- After law enforcement notification period, carriers must notify affected customers

**Proprietary network information protection:**
Strengthened rules against social engineering attacks that obtain CPNI through manipulation
of carrier employees.

### 2023 SIM SWAP ACTION

**FCC 23-67 / FCC Declaratory Ruling (2023):**
The FCC specifically addressed SIM swap fraud as a CPNI issue. The order:
1. Confirmed that SIM swaps and port-out fraud are violations of carriers' CPNI obligations
2. Required carriers to implement enhanced verification before processing SIM swaps
3. Required carriers to notify customers immediately when a SIM swap is requested
4. Required carriers to pause SIM swaps for a verification period when suspicious activity is detected

**Effect on AT&T liability:** The FCC's 2023 action confirms that SIM swap prevention
is within carriers' CPNI duties. AT&T's failure to implement adequate SIM swap
protections during the period of the attack — when the FCC had already identified SIM
swap fraud as a CPNI issue — strengthens the negligence per se argument.

### LOGICAL DELTA

| Element | Pre-2007 | Post-2007 (FCC 07-22) | Post-2023 (SIM Swap) |
|---------|----------|----------------------|----------------------|
| Authentication | Biographical info acceptable | Password/PIN required; biographical alone insufficient | Enhanced SIM swap-specific verification required |
| Breach notification | Not specifically required | FBI/Secret Service 7-day notice required | Customer immediate notification for SIM swap events |
| SIM swap | Not specifically addressed | Covered by general CPNI rules | Specifically identified as CPNI violation; enhanced duties |

### PROVENANCE

FCC Report and Order FCC 07-22 (Feb. 22, 2007)
47 C.F.R. §§64.2010, 64.2011 (implementing 47 U.S.C. §222)
FCC Declaratory Ruling FCC 23-67 (2023) — SIM swap specific
