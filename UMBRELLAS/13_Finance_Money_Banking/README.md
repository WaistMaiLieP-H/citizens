# Umbrella 13 — Finance / Money / Banking

**Definition.** Banking regulation, securities, currency, monetary policy, lending standards, consumer credit, anti-money-laundering, payment systems, contractor and surety bonds. The rules that govern how money is created, moved, lent, invested, and protected.

**Scope.** Commercial banking, investment banking, securities issuance and trading, broker-dealer regulation, investment adviser regulation, consumer credit, mortgages, predatory lending, bankruptcy, debt collection, anti-money-laundering, sanctions, currency controls, payment systems, cryptocurrency, surety bonds.

**Examples.**
- Securities Act of 1933 (15 USC § 77a et seq.) — registration of securities offerings
- Securities Exchange Act of 1934 (15 USC § 78a et seq.) — secondary market regulation, SEC creation
- Investment Company Act of 1940
- Investment Advisers Act of 1940
- Glass-Steagall Act of 1933 (since substantially repealed by Gramm-Leach-Bliley 1999)
- Bank Holding Company Act of 1956
- Truth in Lending Act (TILA) and Regulation Z
- Real Estate Settlement Procedures Act (RESPA)
- Bank Secrecy Act (BSA, 31 USC § 5311 et seq.) and FinCEN regulations
- Dodd-Frank Wall Street Reform and Consumer Protection Act (2010)
- Fair Debt Collection Practices Act (FDCPA)
- Bankruptcy Code (Title 11, USC)
- California Financial Code (the entire code)
- California Department of Financial Protection and Innovation (DFPI) regulations
- California Commercial Code (UCC as adopted in California)
- 31 CFR Chapter X (FinCEN AML rules)

**Canonical Citizen owners.**
- Bank Compliance Officer
- Securities Lawyer / Securities Compliance Officer
- AML / BSA Compliance Officer
- Consumer Credit Compliance Specialist
- Bankruptcy Trustee
- Surety Bond Specialist (relevant to CSLL 1929 contractor bonds)
- Payment Systems Specialist
- Debt Collection Compliance Specialist
- FISCARA (existing Vernen catalog persona for financial work)

**Candidate seed standard for first build.**

**Securities Act of 1933, Section 5 (15 USC § 77e — Prohibitions relating to interstate commerce and the mails).** Section 5 is the operational core of the entire 1933 Act: it prohibits the offer or sale of any security through interstate commerce or the mails unless a registration statement has been filed and is in effect (with limited exemptions). Every securities-fraud case in the United States runs through Section 5 or one of its enumerated exemptions.

**Primary-source URL:**
- https://www.law.cornell.edu/uscode/text/15/77e
- https://www.sec.gov/about/laws/sa33.pdf (SEC's official text of the entire Securities Act)

**Why this seed:** The Securities Act of 1933 was passed the same year as the Field Act and the Riley Act, in the same wave of New Deal legislation responding to a national failure (the 1929 stock market crash and the Pecora investigation). It is the federal companion to the same 1933 California legislative response. Building this standard alongside the Field Act creates a 1933-cohort cluster that demonstrates how multiple jurisdictions and substantive areas all responded to the same crisis era.

**Secondary seed candidate.** California Financial Code § 22000 et seq. (California Financing Law, formerly the California Finance Lenders Law) — California's general consumer-lender licensing statute, administered by DFPI.

**Tertiary seed candidate.** Bank Secrecy Act § 5311 (anti-money-laundering reporting) and 31 CFR § 1010 (FinCEN reporting rules) — relevant to the steward's Treasury fraud documentation.

**Status.** No standards built yet under this umbrella. Note that Vernen has multiple existing pipelines (FAC, EDGAR, Treasury, USAspending) that produce intelligence relevant to this umbrella per `project_intelligence_pipelines.md`.

**Cross-cutting notes.**
- Finance overlaps Authority (01) heavily — every Finance standard is itself a statute or regulation.
- Finance overlaps Integrity (09) — banking and securities both run on chain-of-custody for transactions and instruments.
- Finance overlaps Tax (Umbrella 14) so much that some catalogs treat them as a single umbrella; this catalog separates them because they are administered by different agencies and require different specialty expertise.
- The steward's existing memory artifacts touching this umbrella: `project_treasury_audit.md`, `project_property_financial_fraud.md`, `project_uit_investigation.md`, `project_communications_fraud.md`.
