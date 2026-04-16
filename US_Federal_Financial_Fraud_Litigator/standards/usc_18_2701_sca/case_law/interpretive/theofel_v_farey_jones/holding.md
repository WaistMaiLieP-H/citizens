# Theofel v. Farey-Jones — Holding

**Citation:** Theofel v. Farey-Jones, 359 F.3d 1066 (9th Cir. 2004)
**Court:** United States Court of Appeals for the Ninth Circuit
**Decided:** 2004
**Author:** Kozinski, J.

## Facts

In the course of civil litigation, the defendant's attorney issued an overly broad
civil subpoena to the plaintiff's internet service provider (ISP) demanding production
of all emails. The ISP complied and produced the emails without the plaintiffs'
knowledge or consent. The subpoena was facially invalid — it was not properly limited
in scope or authorized by the court.

The plaintiffs sued under the SCA, arguing that the attorney's use of an invalid
subpoena to obtain their stored emails from the ISP constituted unauthorized access
to stored communications under §2701.

## Holding

**Obtaining stored emails from an ISP through an invalid, overbroad subpoena constitutes
"unauthorized access" to stored communications under 18 U.S.C. §2701 — even though
the ISP voluntarily complied with the subpoena.**

The court held that the SCA's prohibition on unauthorized access is not limited to
hacking or technical intrusion. Obtaining stored communications through legal process
that is facially invalid and exceeds proper authorization is also "without authorization"
within the meaning of §2701.

The court also addressed the "electronic storage" definition: emails that have been
delivered and remain on the server (available for rereading by the subscriber) are still
in "electronic storage" for purposes of §2701's backup protection provision — even after
the subscriber has read them.

## Rules Distilled

1. **"Without authorization" is not limited to hacking:** Any method of obtaining stored
   communications that lacks proper legal authorization violates §2701 — including
   facially invalid legal process
2. **Backup protection storage:** Emails that remain on a server after delivery and
   reading are in "electronic storage" under the backup protection prong of §2510(17)(B)
   — the SCA continues to protect them
3. **Civil liability for legal actors:** Attorneys, parties, or others who obtain stored
   communications through improper legal process can be liable under §2707
4. **Overly broad subpoena = unauthorized access:** The authorization conferred by legal
   process is limited to its valid scope; process that exceeds its authority provides no
   authorization for the excess
5. **No technical intrusion required:** §2701 does not require hacking, password cracking,
   or technical circumvention of security — any unauthorized access to stored communications
   is covered

## Significance for SIM Swap and Account Takeover Claims

Theofel establishes two principles critical for SIM swap SCA claims:

**1. "Without authorization" scope:** The attacker who gains access to email accounts
using intercepted 2FA codes (obtained through SIM swap) is acting "without authorization"
even though the email provider's system accepted the login credentials — the attacker
had no actual authorization, only stolen access. Theofel's broad reading of "without
authorization" supports this theory.

**2. Stored email after reading remains protected:** Emails that Michael had already
read but that remained in his Gmail/email account are still protected "electronic
storage" under Theofel's backup protection analysis. The attacker who accessed
and read those stored emails violated §2701 for each communication accessed.

## Verification Note

Theofel v. Farey-Jones at 359 F.3d 1066 — verify citation before use in filed documents.
