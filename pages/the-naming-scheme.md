---
title: The naming scheme
section: Concepts
order: 3
blurb: Denote filenames, and why you might want them.
---

# The naming scheme

Optional. Plain Org files in a plain directory work. This page is about what you get if you adopt [Denote](https://protesilaos.com/emacs/denote)'s convention, which Denospace implements exactly.

## The idea

A note's metadata lives in its **filename**:

```
20240322T131856==sig--some-title__topic1_topic2.org
└ identifier ─┘  └sig┘ └ title ┘  └── keywords ──┘
```

Four components, each introduced by a doubled delimiter. You can read a note's identity, title and keywords from `ls` alone, with no tool and no database — including in ten years, on a machine that has never heard of Denospace.

## What each part does

**Identifier** — a creation timestamp. Never changes. This is what `denote:` links point at, which is why they survive renames.

**Signature** — an optional ordering key. `21=14=3` is a place in a tree, and a Johnny Decimal address like `21=14` is the same idea. Denospace reads these as sequences: a note knows its own parent, children, siblings, next and previous.

**Title** — the sluggified title.

**Keywords** — tags, joined by underscores.

## Interoperability is exact

Denospace produces byte-identical filenames to `denote.el`. This is not approximate: the sluggification rules were derived from 1,713 recorded input/output pairs of the real tool and are checked against them on every build, plus a four-thousand-note library as an independent test.

That matters because the alternative is a library where half the files were named by Emacs and half by something that was *nearly* right, which is a mess you cannot undo by hand.

## Renaming

`Denote: Rename` and `Denote: Rename File from Front Matter` rewrite the filename from the note's own metadata. Change the title in the front matter, run the command, and the filename follows — keeping the identifier, so nothing that links to it breaks.

## If you don't use it

Everything else works. Links by path, backlinks for those that are indexed, the journal, publishing, Org parsing. You lose rename-proof links and signature sequences, which are the two things the scheme buys.
