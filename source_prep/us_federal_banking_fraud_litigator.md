# SOURCE PREP: US_Federal_Banking_Fraud_Litigator
## Pre-Build Intelligence File
**Prepared:** 2026-04-12 | **Status:** PENDING — all federal USC sections blocked by MCP tool; statutes identified, not yet fetched
**Do not modify during build. Terminal claiming this Citizen reads this file at session start.**

---

## CASE COVERAGE

**Primary cases:**
- Treasury securities identity theft — 4 contradictory responses; bonds under Michael's name attributed to "another individual"; SSN theft
- Northern Trust variable product / UIT — HILLBERGMANN compound identity on State Farm policy; Northern Trust variable annuity; possible fraudulent beneficiary designation
- Ann Hillberg State Farm — UIT (Unit Investment Trust); possible securities fraud / identity manipulation on financial products
- SIM swap / communications fraud enabling financial fraud — Ryan McClaran digital infrastructure
- Christina $73K crypto fraud + $25K spine surgery (money not from Honeysuckle sale proceeds)

**Boundary rule:**
- US_Federal_Financial_Fraud_Litigator OWNS: wire fraud (18 USC §1343); mail fraud (§1341); identity theft (18 USC §1028A); computer fraud (18 USC §1030); conspiracy (18 USC §1349)
- CA_Insurance_Compliance_Litigator OWNS: CDI enforcement; insurance bad faith; variable annuity as insurance product
- THIS CITIZEN OWNS: Bank fraud (18 USC §1344); false statements to banks (18 USC §1014); bank secrecy/AML violations (31 USC §§5311-5324); FinCEN Suspicious Activity Reports; federal bank examination regulatory framework; FDIC/OCC/Federal Reserve enforcement; mortgage fraud (18 USC §1014); CFPB jurisdiction

---

## ANCHOR STATUTES — FETCH REQUIRED (ALL BLOCKED BY MCP TOOL)

### 18 USC § 1344 — Bank fraud
- **What it does:** Knowingly executing scheme to defraud financial institution, or to obtain money/property of financial institution by false representations — felony; up to 30 years; fines up to $1M
- **Elements:** (1) knowingly executed scheme; (2) to defraud financial institution OR obtain property by false representations; (3) financial institution federally insured or chartered
- **Fetch:** uscode.house.gov → Title 18 → § 1344
- **Standard ID:** `usc_18_1344_bank_fraud`

### 18 USC § 1014 — False statements to federally insured financial institution
- **What it does:** Knowingly making false statement for purpose of influencing any federally insured financial institution on: loan applications, credit applications, real estate transactions, etc. — felony; up to 30 years
- **Application:** False statements in connection with Honeysuckle sale financing; false statements re: identity on financial accounts
- **Fetch:** uscode.house.gov → Title 18 → § 1014
- **Standard ID:** `usc_18_1014_false_statements_financial`

### 31 USC § 5318 — Bank Secrecy Act — financial institution compliance requirements
- **What it does:** Financial institutions must maintain records; file Currency Transaction Reports (CTR) for transactions >$10K; file Suspicious Activity Reports (SAR); AML program requirements; Know Your Customer (KYC)
- **Application:** If fraudulent transactions involving large amounts were conducted without SAR filing by receiving institution = BSA violation; SAR records are discoverable in litigation
- **Fetch:** uscode.house.gov → Title 31 → § 5318
- **Standard ID:** `usc_31_5318_bsa_compliance`

### 31 USC § 5324 — Structuring to evade reporting
- **What it does:** Structuring transactions to avoid CTR filing = crime; aiding or assisting structuring = crime
- **Application:** If financial fraud proceeds were structured to avoid reporting — this is the trigger; SAR/CTR absence combined with suspicious transfer pattern
- **Fetch:** uscode.house.gov → Title 31 → § 5324
- **Standard ID:** `usc_31_5324_structuring`

### 12 USC § 1818 — FDIC enforcement powers
- **What it does:** FDIC authority to issue cease and desist orders, remove officers and directors, impose civil money penalties against institutions and individuals for unsafe/unsound practices
- **Fetch:** uscode.house.gov → Title 12 → § 1818
- **Standard ID:** `usc_12_1818_fdic_enforcement`

### 15 USC §§ 78j(b) + 17 CFR § 240.10b-5 — Securities fraud (Exchange Act)
- **What it does:** Rule 10b-5 fraud in connection with purchase or sale of security; material misrepresentation; scheme to defraud; insider trading; Northern Trust variable products are securities
- **NOTE:** 17 CFR § 240.10b-5 is the SEC rule; 15 USC § 78j(b) is the enabling statute
- **Fetch:** uscode.house.gov → Title 15 → § 78j; ecfr.gov → 17 CFR § 240.10b-5
- **Standard ID:** `exchange_act_10b5_securities_fraud`

---

## CASE LAW SEEDS

1. **Loughrin v. United States**, 573 U.S. 351 (2014) — Bank fraud §1344; "scheme to defraud" interpreted broadly; §1344(2) (false representations to obtain bank property) does not require the bank itself to be victimized — any transaction using bank property qualifies
2. **Shaw v. United States**, 580 U.S. 63 (2016) — Bank fraud targeting bank depositor's account IS bank fraud against the bank; §1344 protects banks not just as lender but as custodian of depositor funds
3. **United States v. Neder**, 527 U.S. 1 (1999) — Mail fraud, wire fraud, and bank fraud all require materiality of the false statement; immaterial misrepresentation is not fraud
4. **Williams v. United States**, 458 U.S. 279 (1982) — False statements to federally insured institution (§1014) do not require that the institution actually be deceived; knowing falsity + intent sufficient
5. **Reves v. Ernst & Young**, 507 U.S. 170 (1993) — RICO "operation or management" test; participation in enterprise's affairs through a pattern of racketeering activity; accountants/advisors can be liable if they participated in operation or management
6. **United States v. Santos**, 553 U.S. 507 (2008) — Money laundering "proceeds": in context of illegal gambling, "proceeds" means profits, not gross receipts; narrow reading of proceeds in money laundering statute

---

## STANDARDS OF CREATION (document types this Citizen audits)

- **SAR (Suspicious Activity Report)** — FinCEN Form 111; filed by financial institution; not disclosed to subject; but discoverable in litigation via subpoena to FinCEN or as part of institutional record
- **CTR (Currency Transaction Report)** — FinCEN Form 112; filed for cash transactions > $10K; mandatory; structuring to avoid = 31 USC §5324 crime
- **Bank statements and account records** — Authentication via §1560 subpoena; chain of custody; reconciliation with known transactions
- **Wire transfer records** — SWIFT/Fedwire records; timestamps; originating/beneficiary account identification
- **Loan application documents** — §1014 false statement vehicle; must verify: stated income, stated identity, stated purpose of loan
- **Securities account statements** — Northern Trust variable product; FINRA Account Activity Report; trade confirmations

---

## SOC CONTROLS

- **FinCEN (Financial Crimes Enforcement Network)** — Treasury bureau; SAR/CTR repository; AML enforcement; 31 USC §5318 enforcement authority
- **FDIC** — Bank examination; civil money penalties; cease and desist; 12 USC §1818
- **OCC (Office of the Comptroller of the Currency)** — National bank examination; enforcement
- **Federal Reserve** — Bank holding company supervision
- **SEC** — Securities fraud enforcement; Exchange Act Rule 10b-5; Northern Trust variable products
- **FINRA** — Broker-dealer regulation; variable annuity suitability requirements; FINRA Rule 2330 (variable annuity supervision)
- **CFPB** — Consumer financial protection; mortgage servicer oversight; debt collection

---

## FIVE-LAYER STANDARDS TO BUILD

| Standard ID | Statute/Rule | Priority |
|---|---|---|
| `usc_18_1344_bank_fraud` | 18 USC §1344 — bank fraud (fetch needed) | BUILD FIRST |
| `usc_18_1014_false_statements_financial` | 18 USC §1014 — false statements (fetch needed) | BUILD SECOND |
| `usc_31_5318_bsa_compliance` | 31 USC §5318 — BSA/AML (fetch needed) | BUILD THIRD |
| `exchange_act_10b5_securities_fraud` | 15 USC §78j + Rule 10b-5 (fetch needed) | BUILD FOURTH |
| `usc_31_5324_structuring` | 31 USC §5324 — structuring (fetch needed) | BUILD FIFTH |

---

## TREASURY SECURITIES CASE — SPECIFIC FINDINGS

The 4-letter pattern from Treasury (4 contradictory responses; bonds under Michael's name attributed to "another individual") is a §1344 fact pattern:
1. Identity used to open/register securities account without authorization = §1344 bank fraud (if financial institution was defrauded in connection with transaction)
2. False representation about bond ownership identity = §1014 false statement in connection with financial institution
3. SSN used by "another individual" for Treasury Direct account = 18 USC §1028A (identity theft — already in Financial Fraud Citizen) + §1344 if bank-related
4. Treasury Direct is not a "financial institution" under §1344 — but if bonds were purchased through brokerage or financial institution, §1344 is triggered; if purchased directly, the fraud is §1028A + §1001 (false statements to federal agency)

**Coordinate with US_Federal_Financial_Fraud_Litigator** — Treasury case overlaps both Citizens; this Citizen owns the bank/securities fraud instruments; Financial Fraud Citizen owns the identity theft predicate.

---

## HISTORICAL CHAIN SEED

**The wound:** Bank fraud was added to the federal criminal code in 1984 after prosecutors discovered that existing mail fraud and wire fraud statutes had gaps when the scheme did not involve mail or wire. The same year, the federal government was reeling from the savings and loan crisis — institutions were being looted from within by their own officers using elaborate fraudulent schemes. 18 USC §1344 was designed to cast the widest possible net. The wound in this case is the inverse: the fraud was not inside the institution but through it — financial institutions as instruments of identity theft, as unwitting conduits for fraudulent transactions using a stolen SSN, as the paper trail of a compound identity's financial life. The SAR/CTR absence is itself evidence: either the institution failed to file mandatory reports (BSA violation), or the transactions were structured to evade them.

---

## CROSS-REFERENCES

- `US_Federal_Financial_Fraud_Litigator` → 18 USC §1028A identity theft; wire/mail fraud; RICO; computer fraud
- `CA_Insurance_Compliance_Litigator` → Northern Trust variable product as insurance product; FINRA parallel track
- `US_Federal_ERISA_Litigator` → Northern Trust variable product as pension/retirement asset; ERISA fiduciary duty
- `CA_Elder_Law_Litigator` → Ann Hillberg financial elder abuse; Northern Trust / UIT targeting
- `HERALD` → Will witness Treasury Securities letters, SAR/CTR records (if obtained), wire transfer records
