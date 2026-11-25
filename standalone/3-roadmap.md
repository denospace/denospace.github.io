---
title: Roadmap
blurb: What is being built, in what order, and what is deliberately not being built.
path: roadmap/index.html
---

# Roadmap

In order. No dates — this is built by very few people, and a date would be a guess dressed up as a promise.

## 1. The web app, made genuinely good

In progress. The thing is used daily by the person building it, which is the only reliable way design problems get found. This comes first because every later client inherits the decisions made here.

## 2. Dropbox

So that hosting can exist at all. Today Denospace reads a directory, which means running a server. Reading a folder in your own Dropbox removes that requirement without taking custody of your files. See [Dropbox](/docs/dropbox/).

Google Drive follows, and is honestly harder.

## 3. Agenda

`SCHEDULED:` and `DEADLINE:` timestamps, repeaters, and agenda views across a date range.

TODO keywords, your own `#+TODO:` sequences, priority cookies and headline tags already work and are indexed. The agenda is the missing half, and it is built once, in the web app, where the parser already lives — so every client gets it.

## 4. A native iOS client

The largest piece, and the reason subscriptions exist. A native text editor rather than a browser engine, because that is the difference between adequate and good on a phone. See [Pricing](/pricing/) for why this is the thing the money is for.

Not an attempt to displace the dedicated Org task apps. The aim is narrower and more useful: your whole linked library in your pocket, with an agenda that works.

## What is deliberately not on this list

- **A sync engine.** Never. Your files move by tools that already do this well. See [Sync and conflicts](/docs/sync-and-conflicts/).
- **Converting your notes.** No import step, no proprietary format, nothing to migrate out of.
- **A free hosted tier.** Self-hosting is free and always will be; hosting other people's files is not.
