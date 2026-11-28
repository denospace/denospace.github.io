---
title: Commands
section: Reference
order: 2
blurb: The command palette, by namespace.
---

# Commands

`Ctrl-/` opens the palette. Everything is reachable from it; type any fragment of a name.

Commands are grouped by namespace. There are just under two hundred of them; the ones worth knowing by name are below, with their Emacs counterparts.

Everything that acts on a note is under `Note:`. There is no `Denote:` namespace — every note here is a Denote note, so that prefix named the Emacs package a command came from rather than anything you need to know. If you used an earlier build and bound keys to the old names, those overrides are stored by command name and will need rebinding.

## Creating notes

`denote-prompts` is the whole of Denote's creation design: `denote` asks what the list says, and every variant is that same list with **one prompt appended**. Denospace works the same way — one pipeline, and a command says only which prompt it exists for.

| Command | Appends | Emacs |
|---|---|---|
| `Note: New` | — | `denote` |
| `Note: New with Signature` | the signature | `denote-signature` |
| `Note: New of Type` | the file format | `denote-type` |
| `Note: New with Date` | the date the identifier is minted from | `denote-date` |
| `Note: New in Subdirectory` | the directory to write into | `denote-subdirectory` |
| `Note: New from Template` | the body to start with | `denote-template` |
| `Note: New from Region` | — (the selection becomes the body) | `denote-region` |

Set `denote.prompts` to change what **every** one of them asks, and in what order:

```lua
config.set("denote.prompts", { "title", "keywords", "subdirectory" })
```

The names are the ones `denote-prompts` uses — `title`, `keywords`, `signature`, `date`, `file-type`, `subdirectory` and `template` — so a value copied out of an Emacs config translates across unchanged. An unrecognised name is dropped and reported rather than silently ignored.

`Note: Extract` is the eighth, and it is not in the table because it is not `denote` with a prompt appended. It is `denote-org-extract-org-subtree`: the section the cursor is in leaves the page and becomes a note of its own, taking its title from the heading, its keywords from the heading's tags, and its date from a `DATE` or `CREATED` property or a `CLOSED` stamp. Only what the heading leaves unsaid is asked for, so an annotated heading extracts without a keystroke. A link by identifier is left where the section was.

## Notes

| Command | Emacs equivalent |
|---|---|
| `Note: Insert or Edit Link` (`Alt-i`) | `denote-link-or-create`, `org-insert-link` |
| `Note: Insert Web Link` (`Shift-Alt-i`) | `org-insert-link`, `org-cliplink` |
| `Note: Toggle Link Display` | `org-toggle-link-display` |
| `Note: Rename` | `denote-rename-file` |
| `Note: Rename from Front Matter` | `denote-rename-file-using-front-matter` |
| `Note: Set Keywords` | `denote-rename-file-keywords` |
| `Note: Set Signature` | `denote-rename-file-signature` |
| `Note: Browse by Signature` | `denote-sort-dired` |
| `Note: Signature Parent` / `Children` / `Siblings` / `Next` / `Previous` | `denote-sequence-find` |
| `Note: New Child` / `New Sibling` | `denote-sequence-new-child-of-current` / `-sibling-of-current` |
| `Note: Find Link` / `Find Backlink` | `denote-find-link` / `denote-find-backlink` |
| `Note: Random` | `denote-explore-random-note` |
| `Note: Signatures Page`, `Keywords Page`, `Library Health` | `denote-sequence-dired`, `denote-explore-*` |
| `Note: Update Dynamic Blocks` | `org-update-all-dblocks` |
| `Note: Insert Links Block` and three siblings | `denote-org-extras-dblock-insert-*` |

`Note: Set Keywords` is one command rather than Denote's add/remove pair, because the same prompt does both: keywords the note already carries are listed first, and taking one takes it off. Denote's `-add-keywords` and `-remove-keywords` are for files marked in Dired, not for the file in front of you.

## Searching and browsing

| Command | Emacs equivalent |
|---|---|
| `Navigate: Search Notes` (`Alt-/`) | `denote-grep`, `consult-denote-grep` |
| `Navigate: Signature Browser` (`Shift-Alt-t`) | `denote-sequence-dired` |
| `Search: Exclude Files` / `Only Include Files` | `denote-query-exclude-files` / `-only-include` |
| `Search: Exclude Keyword` / `Only Keyword` | `denote-query-*-keywords` |
| `Search: Clear Filters` | — |
| `Navigate: Collapse All` / `Expand All` (`Shift-Left` / `Shift-Right`) | — |

One search, two ways in, as Denote has: as a modal it closes on the match you take; docked left or right it stays open while you walk the matches. The filters are buffer-local the way Denote's are — part of the search in front of you, gone next time.

Any tree — the signature browser, the journal, the space tree — collapses whole with `Shift-Left` and opens again with `Shift-Right`, at every depth. The two commands do the same thing from the palette, for when the tree does not have focus; neither carries a key of its own, because an unmodified keystroke never leaves the panel's filter box. With a filter typed both refuse and say so: a filtered tree is expanded to show its matches, so the change would be invisible now and a surprise later. What you collapse is remembered per view.

## Journal

| Command | Emacs equivalent |
|---|---|
| `Journal: Today` (`Ctrl-q j`) | `denote-journal-new-or-existing-entry` |
| `Journal: Previous Day` (`Ctrl-q p`) / `Next Day` (`Ctrl-q n`) | — |
| `Journal: Open Date` | — |
| `Journal: Calendar` | `denote-journal-calendar` |
| `Journal: Picker` | — |

## Zotero

| Command | Emacs equivalent |
|---|---|
| `Zotero: Insert Citation` | `citar-insert-citation` |
| `Zotero: New Reference Note` | `citar-denote-create-note` |
| `Zotero: Add File` | — |
| `Zotero: Sync Reference Notes` | — |
| `Zotero: Sync Library` / `Resync Library` | — |

## What is deliberately not offered

Seven commands SilverBullet ships are withdrawn, because they think in **paths** while a Denote library is addressed by **identifier**.

`Page: Rename` prompted for a whole file name, which here is a name you are not meant to type; `Page: Batch Rename Prefix` and `Page: Rename Linked Page` reorganise folders in a library that has none; `Document: Rename Document` is the same thing for attachments. `Note: Rename` asks instead for the title, keywords and signature a name is *built* from, and the top bar still renames a file directly.

`Page: Copy` went for a sharper reason: it wrote the page back verbatim with the current name prefilled, so it could mint two notes carrying one identifier — which the Denote manual calls the thing that breaks linking, and it breaks it silently.

`Page: Extract` named the new page by whatever was typed at its prompt, so it minted a page with no identifier, outside the naming scheme and unreachable by every `denote:` link. `Note: Extract` replaces it.

`Text: Link Selection` wrote `[text](url)` whatever page it was on, which in an Org note is something neither format can follow. `Note: Insert or Edit Link` and `Note: Insert Web Link` write a link in the page's own syntax.

## Everything else

`Editor:`, `Navigate:`, `Page:`, `Space:`, `Outline:`, `Library:`, `Blog:` and a dozen more are discoverable from the palette.

> This page lists the commands worth knowing by name. It is **not** the complete registry: commands are declared in five different places in the codebase — plug manifests, library Lua, view and navigator definitions, and two files of client TypeScript — so a trustworthy exhaustive list has to be dumped from the running application rather than written by hand. Generating that page automatically is a known task; until it exists, the palette is the authority.
