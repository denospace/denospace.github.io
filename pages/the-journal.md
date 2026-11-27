---
title: The journal
section: Start here
order: 5
blurb: Dated entries, and how the day is decided.
---

# The journal

`Ctrl-q j` opens today's journal entry, creating it if it doesn't exist.

Entries live in their own directory, carry a `journal` keyword, and are titled from a date format you choose. All three are configurable.

## How the day is decided

By the entry's **identifier**, not by its front matter.

This matters more than it sounds. An identifier is a timestamp baked into the filename at creation — `20261125T140233`. The front-matter `#+date:` can be edited, copied from another note, or left wrong. The identifier cannot drift. So "today's entry" means "the entry whose identifier falls on today", which is the same rule `denote-journal` uses in Emacs.

The practical consequence: Emacs and Denospace agree on which file is today's, always, without coordinating.

## Moving around

| Command | What it does |
|---|---|
| `Journal: Today` (`Ctrl-q j`) | Open or create today's entry |
| `Journal: Open Date` | Pick any date |
| `Journal: Next Day` (`Ctrl-q n`) / `Previous Day` (`Ctrl-q p`) | Walk entries that exist, skipping empty days |
| `Journal: Calendar` | A year at a glance, with the days that have entries |
| `Journal: Picker` | Every entry, newest first |

## Configuration

Set in your space config:

| Setting | Default | Emacs equivalent |
|---|---|---|
| `denote.journalDirectory` | `journal` | `denote-journal-directory` |
| `denote.journalKeyword` | `journal` | `denote-journal-keyword` |
| `denote.journalTitleFormat` | `day-date-month-year-24h` | `denote-journal-title-format` |

Match these to your Emacs settings and the two will write identical files. Mismatch them and you will get two parallel journals that never meet, which is a confusing afternoon.
