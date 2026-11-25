---
title: How links resolve
section: Concepts
order: 2
blurb: Why identifier links survive renames and path links do not.
---

# How links resolve

There are two kinds of link to another note, and they fail differently.

## Path links

```org
[[file:projects/roof.org][the roof note]]
```

This names a location. It works until the file moves, and then it doesn't. Denospace follows it by resolving the path relative to the current page, and if nothing is there it draws the link as broken rather than pretending.

## Identifier links

```org
[[denote:20240125T164237][Court Costs]]
```

This names a *note*, by the identifier minted when it was created. Resolving it means scanning the library for a file whose name carries that identifier.

The consequence is the useful part: **rename the note, retitle it, add keywords, move it to another directory — the link still resolves.** Nothing about the file's location or name is encoded in the link, so nothing about the link breaks when they change.

This is why the naming scheme is worth adopting even if you dislike the filenames. It is the only way to have links that survive your own reorganising.

## Resolution is first-match-wins

An identifier is scanned for across the library, in name order, and the first file carrying it wins.

In normal use identifiers are unique and this never matters. It matters in exactly one situation: if a stale copy of a note lingers — a file deleted behind the client's back, a conflict copy that kept its identifier — and its name sorts earlier, it captures every link to that identifier. The symptom is a note whose backlinks are mysteriously empty.

The fix is to remove the duplicate. Reindexing alone will not help, because reindexing faithfully reproduces whatever the file list says.

## Backlinks

Backlinks are built from the index at write time rather than by searching at read time. That is why they are instant on a large library, and why they survive renames: the relation is stored against the identifier, not the filename.

> Known gap: only `denote:` links currently produce backlinks. A bare Org link to another file resolves and is clickable, but does not yet register as a relation.
