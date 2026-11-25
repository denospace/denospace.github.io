---
title: Connect your folder
section: Start here
order: 2
blurb: Getting Denospace pointed at your Org files.
---

# Connect your folder

Denospace reads a directory. How that directory reaches the server is up to you, and the options differ in how much you have to run yourself.

## Today: a directory on a machine you run

The one path that works right now. You run Denospace on a server — a VPS, a home machine, a seedbox — and give it a path:

```
denospace --space /home/you/org
```

It serves at `127.0.0.1:27438` by default. Put a reverse proxy in front of it for TLS. See [Self-hosting](/docs/self-hosting/) for the full setup.

How the files get to that directory is a question Denospace stays out of:

- **Syncthing** keeps a folder on your laptop and a folder on the server in step. No account, no third party, and it is what the author runs. Covered in [Self-hosting](/docs/self-hosting/).
- **git**, if your notes are already a repository and you don't mind committing.
- **Nothing at all** — edit over SSH, or just use the browser as the only client.

## Soon: Dropbox

A hosted Denospace that reads your Dropbox folder directly, so there is no server for you to run. This is **not built yet**; it is the next significant piece of work. [Dropbox](/docs/dropbox/) describes how it will work and what it will be able to see.

## Which files it picks up

Every `.org` file under the directory, recursively, plus any attachments they reference. Subdirectories become part of the page name, so `projects/roof.org` is the page `projects/roof`.

Files beginning with a dot are skipped. Emacs backup and lock files (`*~`, `#*#`, `.#*`) should be excluded at the sync layer rather than synced and then ignored — there is a `.stignore` for Syncthing in [Self-hosting](/docs/self-hosting/).

## A warning worth reading once

If you sync a folder between macOS and Linux, you will eventually hit two problems that are not Denospace's doing and that it cannot fix for you:

- **Case.** macOS treats `Journal/` and `journal/` as the same directory. Linux does not. A sync between them stalls with an error naming both.
- **Unicode.** macOS stores filenames decomposed (`u` + combining diaeresis); Linux stores them composed (`ü`). The same name can appear twice.

Both are covered in [Sync and conflicts](/docs/sync-and-conflicts/).
