---
title: Sync and conflicts
section: Concepts
order: 4
blurb: Denospace does not sync your files. Here is what does, and what happens when two machines disagree.
---

# Sync and conflicts

**Denospace has no sync engine and will never have one.** This is a deliberate decision, not a missing feature.

Your files move between machines by something that already exists and already does this well — Syncthing, Dropbox, git, a network mount. Denospace reads and writes a directory. Whatever keeps that directory in step with your laptop is a separate concern, chosen by you, replaceable by you.

## Why it is built this way

Writing a sync engine means writing conflict resolution, and conflict resolution for other people's notes is a way to lose their work. Tools that already solve it have had years of edge cases beaten out of them.

It also means **your notes are never hostage to Denospace**. The canonical copy is a folder on your own disk, in your own account. If this project stops tomorrow, nothing needs exporting, because nothing was ever imported.

## What happens on a conflict

The same thing that happens without Denospace. Edit the same note on two machines before they sync, and your sync tool writes a second file alongside the first:

```
20240322T131856--roof-repair.org
20240322T131856--roof-repair.sync-conflict-20261125-140233-A7B3C9.org
```

Denospace does not merge these and does not hide them. They appear as what they are: two notes, both present, for you to reconcile.

Note that the conflict copy keeps the identifier. If it sorts earlier than the original, it will capture `denote:` links aimed at that note — see [How links resolve](/docs/how-links-resolve/). Resolve conflicts promptly for this reason, not just for tidiness.

## Two problems specific to mixed platforms

If you sync between macOS and Linux — which includes most self-hosting setups — you will meet both of these eventually.

**Case collisions.** macOS filesystems are case-insensitive; Linux is not. A directory created as `Journal/` on one and `journal/` on the other cannot coexist, and the sync stalls with an error naming both. The fix is to rename one side. The prevention is to be consistent about capitalisation in directory names.

**Unicode normalisation.** macOS stores filenames decomposed — `ü` as `u` plus a combining diaeresis — and Linux stores them composed. The same name can appear as two files, and a computed name may not match the name on disk even though they look identical. Denospace compares normalised forms when matching, but your sync tool may not.

Neither is caused by Denospace and neither can be fixed by it. They are listed here because they are the two things most likely to confuse you, and knowing the names makes them searchable.
