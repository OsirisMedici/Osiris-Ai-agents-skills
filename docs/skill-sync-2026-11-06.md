# Skill sync, 6 November 2026

The Mac Codex collection adds `osiris-skills-sync`, `chat-rescue`,
`osiris-t3`, and `whatsapp-catchup`. It also restores executable permission on
`babysit-pr/scripts/pr-wait`. The [sync inventory](skill-sync-inventory.json)
records the published paths, hashes, and executable bits.

`chat-rescue` and `osiris-skills-sync` match their Mac sources. The public
`osiris-t3` package discovers its setup locally. It replaces fixed host and
Claude CLI settings with configuration, and leaves the installation record
and account identity on the owner’s machine. `whatsapp-catchup` points to the
reader documentation in the authorized Writer checkout. It requires that
reader and a locally configured WhatsApp archive. The library contains no
message data or archive.

Seven previous public variants remain as packaged. They omit private session
references, account and client mappings, or depend on the repository’s browser
policy. The existing inventory excludes system and plugin packages, upstream
collections, and older Claude-only skills. This sync checked the Mac Codex
directory. VPS coverage comes from the earlier VPS inventory.

The sync helper was tested with a temporary Git remote and two separate skills
directories. Checks covered fresh install, publishing, upgrading a tracked
copy, preserving a local edit, backup creation, repeat runs, and rejection of
a private environment file. The five changed packages passed Skill Creator
validation and Gitleaks. The Python helpers passed syntax checks, and Bun
bundled the T3 provider helper. Live T3 and WhatsApp operations were outside
this sync.
