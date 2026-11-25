---
title: What Org support covers
section: Concepts
order: 1
blurb: Which parts of Org are parsed, and which are not.
---

# What Org support covers

Org is parsed by a real parser written for it, not by translating to Markdown first. That distinction is why round-tripping works: a file you edit here reopens in Emacs unchanged except for what you actually changed.

## Structure

Headlines to any depth, with folding. `Tab` cycles a headline through folded, children and subtree; `Shift-Tab` does the same for the whole buffer, exactly as `org-cycle` and `org-shifttab` do.

Plain lists, ordered lists and nesting by indentation. Checkbox items (`- [ ]`, `- [X]`) are tasks and are indexed as such.

## Inline markup

`*bold*`, `/italic/`, `_underline_`, `+strikethrough+`, `=verbatim=` and `~code~`.

## Blocks

Source blocks with language highlighting, quote blocks, tables (including alignment rows), comment lines, property drawers and footnotes.

## TODO keywords

`* TODO Write the spec` is recognised as a keyword, not swallowed into the headline text. Your own `#+TODO:` sequence is read from the file, so a project with `TODO NEXT WAITING | DONE CANCELLED` cycles through your states rather than a default set.

## Keywords and front matter

`#+title:`, `#+filetags:`, `#+date:`, `#+identifier:` and friends are read as the page's metadata: the title becomes the page title, filetags become tags.

## Links

Covered in detail in [Links and backlinks](/docs/links-and-backlinks/). `denote:`, `file:` and web links all resolve, render with their description text, and are clickable. Images are shown inline, and `#+ATTR_ORG: :width` is honoured.

## What is not covered

Denospace is early and the honest answer is that this list changes faster than a docs page can. As of now, the significant omissions are macros, `#+INCLUDE:`, inline LaTeX, and Org's scheduling timestamps (`SCHEDULED:`, `DEADLINE:`) — they are preserved in the file but not acted on.

Emphasis spanning more than one line is not recognised, which is a parser limitation rather than a decision.

> The authoritative, current list lives with the code in [docs/Org Mode.md](https://github.com/denospace/denospace/blob/org-denote/docs/Org%20Mode.md) in the repository. If it disagrees with this page, believe the repository.
