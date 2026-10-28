# Storage and external SSD decisions

Read during every Mac rescue storage assessment. These rules do not grant standing deletion or transfer permission.

## Measure and classify

- Measure the APFS container and Data volume separately from folders. System, Preboot, Recovery, VM, snapshots, hard links, clones, sparse files, and concurrent work can make `du` differ from reclaimed space. Use available bytes from `df` or `statvfs` before and after actions. Avoid summing overlapping parent/child folders.
- Prefer sizes and metadata to content reads. Inspect recent large files, generated builds, updater/download caches, and verified duplicate extractions. Report inaccessible areas such as protected Trash instead of changing permissions.
- File age and clean Git status do not establish a backup. For project/archive candidates, check branches, worktrees, submodules, untracked/ignored sources, unpushed commits, and restoration evidence. Preserve Git metadata and worktree registrations unless separately approved.
- SSD candidates are inactive durable data with understood access and restore needs. Deletion candidates are verified disposable files or exact redundant copies with a verified retained source. Size alone is insufficient.
- Account for major storage categories, then drill into the largest. Keep receipts private. Never print credentials, tokens, cookies, session material, vault contents, or private keys.

## Protected by default

Preserve projects and uncommitted work, personal documents/media, Downloads, browser profiles and logins, Codex sessions, T3 history/userdata, vaults and credentials, Keychain, app databases, current AI/dictation models, installed apps, recovery archives, and container volumes. They can be assessed for an exact currently approved move/deletion; they are never generic cache targets.

Updater roots may contain active staging. Inspect the exact inactive subtree rather than removing a common `Installation` parent. npm/npx folders can support active agent tools. Follow Osiris's Bun rules before JS tooling. Never manually delete swap or macOS-managed System Data.

## Discover an external destination

1. List `/Volumes`, then use `diskutil info` and `df` to prove a real mounted external device. Record volume name, device/volume identity, filesystem, writable status, free bytes, and proposed destination. Revalidate identity before writes and source removal; a matching mount name alone is insufficient.
2. Inspect existing archive maps and receipts. For Crucial X6, look for `Mac Archive/Active Data - MacBook/START HERE - 2026-10-22 Mac transfer.md`. This records earlier work and a protected restore flow, not permission for a new move.
3. Allow for destination reserve and temporary verification space. Sparse VM disks may need far more restore space than their allocated size suggests.
4. Moving to one external drive is relocation, not an independent backup. State retained physical-copy counts and how an unplugged drive affects access.

## Include all stages in the single approval

For each transfer, specify source, destination, allocated/logical sizes, why it is inactive, copy/archive format, encryption decision, verification, restore path, and whether verified source removal is included. Use a unique dated destination; preserve existing archives and avoid overwrites.

Use encrypted archives for sensitive workspaces, app state, and recovery data. Reuse the documented protected key flow without printing/copying the key or inventing a credential. Plain working copies may suit explicitly approved ordinary media. If a key or destination is unavailable, leave that item unchanged and continue the rest of the plan.

## Copy, verify, then remove only the approved original

1. Quiesce the approved source and record metadata/inventory. Keep active apps, databases, and VM disks out of ordinary live copies; stop them only if that was included.
2. Copy/archive to a unique `.partial` destination. Preserve required metadata and literal AppleDouble sidecars with `COPYFILE_DISABLE=1` when native tar is used. ExFAT differs in Unix metadata behavior; use a suitable archive instead of assuming directory copies preserve ownership, symlinks, and executable bits.
3. Verify completeness and checksums. For encrypted archives, authenticate decryption and read back the contents. A ciphertext checksum alone does not prove restoration. Keep keys outside chat, logs, and the drive unless a separate protected key-backup flow was approved.
4. Verify representative native opening/restoration. For sparse VM disks, require a native restore and logical-byte comparison; Python tar/PAX sparse metadata alone is insufficient. Log results without private contents.
5. Recheck destination mount identity and source stability. Finalize the destination after verification. Remove the exact original only if included in approval. Partial/interrupted transfers never justify source removal.
6. Measure internal and external free-space changes. Save inventories, checksums, timestamps, source-removal status, retained-copy counts, and restore instructions. Remove only agent-created temporary verification files, preserving retained archives.

## Long transfers

Prefer a supported resumable transfer/backup tool. A user-runnable workflow should show exact sources/destinations, progress, logs, retries, verification, and a fail-closed source-removal condition. Avoid unbounded chat polling and completion claims while `.partial` output remains.
