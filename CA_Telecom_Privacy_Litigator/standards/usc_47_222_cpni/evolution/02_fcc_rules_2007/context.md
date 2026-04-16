# Context — FCC CPNI Authentication Rules (2007)

## What the 2007 rules did

The FCC's 2007 CPNI order was a response to documented pretexting abuses — most famously, Hewlett-Packard's 2006 scandal where HP hired investigators who obtained board members' call records by impersonating them to AT&T. The wound was clear: carriers were handing over call records to anyone who could provide basic account information (name + last 4 digits of SSN).

The 2007 rules required carriers to authenticate callers before releasing CPNI. This was a significant improvement over the prior state (no authentication requirement at all).

## The SIM swap gap

The 2007 rules addressed disclosure of CPNI (call records, usage data). They did not address the modification of the account itself — specifically, the SIM card change that assigns a phone number to a different device. Carriers treated SIM swaps as a separate operational process governed by their own internal policies, not by the CPNI rules.

This created the SIM swap attack vector: an attacker could walk into a carrier store or call customer service, provide minimal identifying information, claim to have lost their phone, and get a new SIM card with the victim's phone number — all outside the CPNI authentication framework.

## Why this matters for the steward

The SIM swaps against the steward's AT&T, Verizon, and T-Mobile accounts occurred between approximately 2018 and 2022 — before the 2024 rules explicitly addressed SIM swap authentication. The carrier liability argument for this period runs through: (1) the § 222 general duty to protect CPNI + (2) the FCC 2007 rules' authentication requirements as applied to account modifications as a class, combined with (3) the carriers' own voluntarily adopted policies and the reasonable care standard.

## Diff from prior
Prior: No authentication requirement at all — carriers could disclose CPNI to anyone. After: Must authenticate before releasing CPNI. Still does NOT explicitly require authentication for SIM swaps.
