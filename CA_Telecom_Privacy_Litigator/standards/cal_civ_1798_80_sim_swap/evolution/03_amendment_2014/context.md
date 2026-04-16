# Context — 2014 Amendment (AB 1710) — The Security Mandate

## The shift: from notification to prevention

The 2003 original law said: tell people when their data is stolen. The 2014 amendment said: don't let it get stolen in the first place.

AB 1710 added the critical "reasonable security" mandate — businesses must implement and maintain security procedures appropriate to the nature of the information they hold. This is the provision that directly reaches carrier liability for SIM swap attacks. A carrier that performs a SIM swap based on a fraudulent request, without adequate authentication, has failed to maintain "reasonable security procedures appropriate to the nature of the information" — because the information at risk is the customer's phone number identity, which is the gateway to all phone-based authentication.

## Why "login credentials" expansion matters

AB 1710 also added username/password combinations and security questions to the definition of "personal information." A SIM swap does not just steal a phone number — it hijacks phone-based two-factor authentication tokens (SMS codes) that function as temporary login credentials. By capturing these codes, the attacker gains access to the actual usernames and passwords behind each account. This makes the SIM swap both: (1) a § 1798.81.5 security failure (reasonable security not implemented), AND (2) a § 1798.82 notification-triggering event (login credentials compromised by unauthorized acquisition).

## Practical chain of causation

1. Carrier fails to authenticate SIM swap request → § 1798.81.5 violation
2. Unauthorized party receives SMS authentication codes → unauthorized acquisition of "personal information" (login credentials)
3. Carrier has duty to notify customer under § 1798.82
4. Customer has private right of action under § 1798.84 for carrier's breach of § 1798.81.5 and § 1798.82

## Diff from prior state

Prior: No affirmative security mandate; only notification after a breach. After: Affirmative duty to implement reasonable security. Businesses (including carriers) can now be sued for failing to prevent a breach, not only for failing to notify about it.
