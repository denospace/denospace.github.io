---
title: Zotero
section: Integrations
order: 3
blurb: Optional. Reference notes and citations from your library.
---

# Zotero

Optional, and deliberately so. Denospace works fully without a Zotero account; this is for people who already keep references there.

## What it does

Syncs your Zotero library so that references are available inside your notes:

- `Zotero: Insert Citation` — pick a reference and insert a citation
- `Zotero: New Reference Note` — create a note attached to a reference
- `Zotero: Sync Library` — pull the library; `Resync Library` rebuilds it
- `Zotero: Add File` — attach a file to a reference

## Interoperability with citar-denote

Reference notes carry `#+reference: citekey` and the `bib` keyword, which is the `citar-denote` convention. That means `citar-denote-open-note` in Emacs finds the same notes Denospace creates, and vice versa.

If you use `citar` and `citar-denote` already, the two sides agree without configuration.

## Credentials

Syncing needs a Zotero API key, which lives in your space configuration on the server. Treat that file as a secret: it grants read access to your Zotero library.

## Attachments

PDFs and other attachments can be pulled from Zotero on demand rather than mirrored wholesale. A large library is a lot of bytes, and most of them are files you will never open from a browser.
