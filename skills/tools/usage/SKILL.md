---
name: usage
description: "Check Claude usage limits and reset times through the user's authorized signed-in account."
---

# Claude usage check

Check the usage page for the account the user selected. Discover a suitable
connected tool first. If it cannot read usage, use the visible in-app Browser
and the user's authorized signed-in account to inspect Claude's official usage
settings. Verify the displayed account identity before reading its limits.

Report the displayed usage measure, limit window, reset time and timezone. If
the page gives a percentage rather than a remaining message count, preserve
that measure. Do not calculate a message or token balance from a percentage.
Timestamp the observation and identify any missing or inaccessible account.

If sign-in or verification is required, let the user complete it through the
provider's normal interface. Do not read browser cookie databases, export
sessions, collect verification codes in chat, or copy another browser's profile.
For several accounts, inspect only the identities the user authorized and keep
their readings separate. This public package contains no account registry,
browser-state file or credential-reading helper.
