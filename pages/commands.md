---
title: Commands
section: Reference
order: 2
blurb: The command palette, by namespace.
---

# Commands

`Ctrl-/` opens the palette. Everything is reachable from it; type any fragment of a name.

Commands are grouped by namespace. The largest are `Editor`, `Denote`, `Navigate`, `Revision` and `Zotero`.

## Denote

| Command | Emacs equivalent |
|---|---|
| `Denote: New Note` | `denote` |
| `Denote: New Note with Signature` | `denote-signature` |
| `Denote: Insert or Edit Link` (`Alt-i`) | `denote-link-or-create`, `org-insert-link` |
| `Denote: Insert Web Link` (`Shift-Alt-i`) | `org-insert-link`, `org-cliplink` |
| `Denote: Toggle Link Display` | `org-toggle-link-display` |
| `Denote: Rename` | `denote-rename-file` |
| `Denote: Rename File from Front Matter` | `denote-rename-file-using-front-matter` |
| `Denote: Add Keywords` / `Remove Keywords` | `denote-keywords-add` / `-remove` |
| `Denote: Set Signature` | `denote-rename-file-signature` |
| `Denote: Browse by Signature` | `denote-sort-dired` |
| `Denote: Signature Parent` / `Children` / `Siblings` / `Next` / `Previous` | `denote-sequence-find` |
| `Denote: New Child Note` / `New Sibling Note` | `denote-sequence-new-child-of-current` / `-sibling-of-current` |
| `Denote: Find Link` / `Find Backlink` | `denote-find-link` / `denote-find-backlink` |
| `Denote: Random Note` | `denote-explore-random-note` |
| `Denote: Signatures Page`, `Keywords Page`, `Library Health` | `denote-sequence-dired`, `denote-explore-*` |
| `Denote: Journal Calendar` / `Journal Open Date` | `denote-journal-calendar` |
| `Denote: Update Dynamic Blocks` | `org-update-all-dblocks` |
| `Denote: Insert Links Block` and siblings | `denote-org-extras-dblock-insert-*` |

## Zotero

| Command | Emacs equivalent |
|---|---|
| `Zotero: Insert Citation` | `citar-insert-citation` |
| `Zotero: New Reference Note` | `citar-denote-create-note` |
| `Zotero: Add File` | — |
| `Zotero: Sync Reference Notes` | — |
| `Zotero: Sync Library` / `Resync Library` | — |

## Everything else

`Editor:`, `Navigate:`, `Page:`, `Space:`, `Outline:`, `Revision:`, `Blog:` and others are discoverable from the palette.

> This page lists the commands worth knowing by name and their Emacs counterparts. It is **not** the complete registry — commands are declared in three different places in the codebase, so a trustworthy exhaustive list has to be dumped from the running application rather than written by hand. Generating that page automatically is a known task; until it exists, the palette itself is the authority.
