# Context — California Penal Code § 502 Computer Data Access and Fraud Act

## The wound and the promise

**The wound:** As California's economy became computing-dependent, a class of crimes emerged for which the existing theft and fraud statutes were inadequate: unauthorized access to computer systems, data theft without physical taking, account takeover using stolen credentials. Traditional theft law required a physical taking; § 502 was enacted to fill the gap for intangible digital property.

**The promise:** § 502 promises that unauthorized access to a computer system — even without physical theft of a device — is a crime, and that victims have a direct civil right of action for compensatory damages, injunctive relief, and attorney fees.

## The critical provision for SIM swap cases — subd. (c)(1)

The most powerful provision for the steward's cases is § 502(c)(1): knowingly accessing a computer without permission to execute a scheme to defraud or to wrongfully control property or data.

**Applied to SIM swap fraud:**
1. **The SIM swapper accesses the carrier's systems** without the account holder's permission — by impersonating the account holder to the carrier
2. **The purpose is to execute a scheme** — to intercept communications, to access financial and government accounts, to deny the victim access to services
3. **The result is wrongful control** over the victim's phone number, digital identity, and any accounts accessed via the intercepted MFA codes

Each step of the SIM swap chain is a § 502(c)(1) violation:
- Accessing the carrier's account management system without permission → violation
- Accessing the victim's email via intercepted password reset → violation
- Accessing the victim's banking app via intercepted MFA → violation
- Accessing any government account (SSA, IRS, disability) via intercepted authentication → violation

## The civil private right of action — subd. (e)(1)

Section 502(e)(1) gives the victim a direct civil cause of action for:
- **Compensatory damages** — all losses caused by the unauthorized access
- **Injunctive relief** — court order stopping the access
- **Attorney fees** — available under the provision
- **Cost of verification** — what it cost to determine whether data was altered or accessed

**The negligence standard:** Subdivision (e)(1) expressly provides that "negligent access and alteration" is sufficient for civil liability. This is a lower threshold than the criminal standard — civil liability under § 502 does not require proof of criminal intent.

## The Ryan McClaran application

For case #31 (Ryan McClaran as IT operator behind digital surveillance):

McClaran's alleged conduct — implementing the surveillance infrastructure, facilitating the SIM swap, maintaining proxy communication networks — constitutes multiple § 502 violations:

1. **Unauthorized access to the steward's devices** if any remote access or device control was implemented
2. **Unauthorized access to the steward's accounts** via SIM-intercepted credentials
3. **Accessing computer services without permission** — using the steward's account resources without authorization

**§ 502 + § 182 conspiracy:** If McClaran acted in concert with Christina (and others), the entire conspiracy is liable for the § 502 violations under § 502(c)(2) (making use of data from an accessed system) and the general conspiracy statute.

## Damages framework

| Damage Category | § 502 Availability |
|---|---|
| Cost of remediation (new devices, security) | Yes |
| Cost of credit/account monitoring | Yes |
| Lost access to financial accounts | Yes |
| Intercepted communications value | Yes |
| Cost to verify what was accessed | Expressly included in (e)(1) |
| Attorney fees | Yes |
| Injunctive relief | Yes |

## Statute of limitations

Three years from the date the victim discovered or should have discovered the unauthorized access. The discovery rule applies — for ongoing, concealed SIM swap attacks, the SOL runs from discovery, not from the initial act.

For the steward's 2018 SIM swap beginning: if discovery occurred closer to 2022-2025 (when communications fraud was identified as a pattern), the SOL runs from that discovery date.

## Bilateral analysis

**As complainant:** Every unauthorized access to the steward's devices, accounts, or communications via SIM swap or other means is a § 502(c) violation giving rise to civil liability and criminal referral.

**As respondent:** The steward's legitimate access to their own accounts and devices is not a § 502 violation. § 502 targets unauthorized access — access to one's own property is never unauthorized.
