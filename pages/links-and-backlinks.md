---
title: Links and backlinks
section: Start here
order: 4
blurb: Linking notes, and seeing what links back.
---

# Links and backlinks

## Making a link

Press `Alt-i`. You get a picker of existing notes; choose one and a link is inserted. Type a name that doesn't exist and it offers to create that note and link to it in one step.

If the cursor is already inside a link, `Alt-i` edits that link instead of inserting a new one.

`Shift-Alt-i` inserts a web link and fetches the page's own `<title>` as the description, so you get a readable link rather than a bare URL.

## What a link looks like on disk

Ordinary Org link syntax, which is the point:

```org
[[denote:20240125T164237][Court Costs]]
[[file:notes/roof.org][the roof note]]
[[https://example.com][a web page]]
```

A `denote:` link addresses a note by its **identifier**, not its filename. Rename the note, retitle it, move it to another directory — the link still resolves, because the identifier never changes. That is the single best reason to use the naming scheme.

A `file:` link addresses a path, and breaks if the file moves. Denospace draws a link that resolves in the normal text colour and one that doesn't in a way you can see at a glance, so a broken link looks broken.

## Backlinks

Every note shows what points at it. Open any note and the mentions panel lists the notes linking to it, with the sentence around each link so you can tell why.

This is built from the index rather than by searching, so it is instant on a large library and it survives renames.

> Known gap: only `denote:` links are indexed as relations today. A bare Org link to another file is followed correctly but does not yet produce a backlink.

## Renaming

Rename a note and the links to it keep working, because they point at the identifier. If you rename a note that is linked by `file:` path, those links will break — Denospace will show them as broken rather than silently swallowing them.
