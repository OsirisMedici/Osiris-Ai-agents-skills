# Skill sync, 31 October 2026

Added the locally created Feedback-to-issue, issue cleanup, proof-backed issue work log, faithful issue PDF export and client issue-report PDF skills. These are separate workflows with separate mutation boundaries. Creating a report does not edit an issue or activate a campaign.

Added the adapted Unslop package because issue cleanup calls it. Its existing Lauren Tan MIT license is retained. Other upstream engineering collections and system/plugin caches remain outside this collection. No new license is applied to custom packages.

Updated Council with its local instruction to resolve known review issues before an audit. Updated Full Stop so its trigger also covers closing emphasis. These small refinements apply cleanly to the existing published packages. Public-safe packaging differences in the other installed skills are preserved rather than overwritten from private installations.

The JSON inventory records source and published hashes. No client reports, screenshots, account mappings, credentials, private issue URLs, browser state or customer records are included. The installed source packages remain unchanged.

The PDF renderers require Python with ReportLab, pypdf and Pillow, plus a Unicode TrueType font. The report renderer can accept explicit font paths and otherwise looks for the bundled runtime or system fonts. Browser export uses the supported in-app Browser. These packages do not include those runtimes or signed-in sessions.

The eight added or updated packages passed Skill Creator validation, YAML parsing, Python syntax and relative-reference checks. The report renderer was exercised on the client issue report, and the faithful-export helper was checked with a continuous-PDF fixture. Offline validation does not establish provider delivery or browser acceptance on another machine.

The faithful PDF joiner was also checked against a real multi-section browser export. Its integrity check now compares every non-whitespace character, because pypdf can infer different line-break spacing after a coordinate transform. Visual QA remains required; this does not relax image or layout checks.
