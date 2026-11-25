---
title: Your first note
section: Start here
order: 3
blurb: Creating, naming and finding notes.
---

# Your first note

Press `Ctrl-k` to open the page picker. Type a name that doesn't exist yet and the first row offers to create it.

That is the whole loop: everything in Denospace is reached by typing part of its name.

## What gets written

A new note is a `.org` file with Org keywords at the top:

```org
#+title:      Roof repair
#+date:       [2026-11-25 Tue 14:02]
#+filetags:   :house:maintenance:
#+identifier: 20261125T140233
```

If you are not using the Denote naming scheme, the file is named after the title and the `#+identifier:` is harmless. If you are, the filename carries that identifier and the keywords too — see [The naming scheme](/docs/the-naming-scheme/).

## Editing

The editor is Org-aware rather than Org-flavoured:

- `Tab` cycles folding on a headline — folded, children, subtree. `Shift-Tab` does the whole buffer.
- `Alt-j` / `Alt-k` move an item down or up; `Alt-l` / `Alt-h` indent and outdent. These follow `evil-org`.
- TODO keywords cycle, and your own `#+TODO:` sequence is respected.
- Tables, source blocks, footnotes and drawers all parse.

There is a vim mode. It is off by default and there is a command to turn it on; `j` and `k` can be bound to move by visual line the way `evil-cross-lines` does in Emacs.

## Finding things again

- `Ctrl-k` — pages by name
- `Ctrl-/` — the command palette
- `Ctrl-j` — jump within the current page

The picker matches on fragments, so `roo rep` finds `Roof repair`. If you use Denote keywords or signatures, those are searchable too.

## Attachments

Paste an image and it is written next to your notes as a file and linked with `[[file:...]]`. Set a width with an Org attribute line directly above the link:

```org
#+ATTR_ORG: :width 400
[[file:20261125T140233--roof-damage.jpg]]
```

That is standard Org, and Emacs honours it too.
