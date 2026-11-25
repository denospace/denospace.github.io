---
title: What Denospace is
section: Start here
order: 1
blurb: A browser for a folder of Org files you already have.
---

# What Denospace is

Denospace is a web interface to a folder of **Org mode** files.

Point it at a directory of `.org` files and every one becomes a page you can read and edit in a browser — on a laptop that doesn't have your Emacs config, on a phone, on a machine you don't control.

Nothing is imported and nothing is converted. The files on disk stay exactly what Emacs wrote them as. Emacs keeps editing them. Denospace is another window onto the same directory, not a new home for your notes.

## What that buys you

Org is the best plain-text format there is for notes, and it is almost unusable away from Emacs. Every other tool that claims to read it flattens it into Markdown, loses your TODO keywords, mangles your drawers and writes the file back wrong.

Denospace parses Org properly — headings, folding, tables, source blocks, TODO sequences, footnotes, links, keywords, drawers — and writes back files Emacs is happy to reopen.

## What it is not

- **Not a sync service.** Your files get where they need to be by whatever you already use: a folder on a server, Syncthing, or (soon) Dropbox. See [Sync and conflicts](/docs/sync-and-conflicts/).
- **Not a replacement for Emacs.** It is deliberately the second-best place to edit your notes. Emacs is the first.
- **Not a database.** There is no import step and no lock-in. Delete Denospace and you are left with the directory you started with.

## Denote, if you use it

If your filenames follow the [Denote](https://protesilaos.com/emacs/denote) naming scheme, Denospace reads it: identifiers, titles, keywords and signatures become real structure, and `denote:` links resolve and become bidirectional.

That is a feature, not a requirement. Plain Org files in a plain directory work fine. See [The naming scheme](/docs/the-naming-scheme/) if you want it.

## Status

Denospace is early. It reads and edits a real four-thousand-note library every day, and there are parts of Org it does not cover yet. The [source](https://github.com/denospace/denospace) is honest about which.
