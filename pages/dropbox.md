---
title: Dropbox
section: Integrations
order: 2
blurb: Planned. How a hosted Denospace will read your folder.
---

# Dropbox

> **Not built yet.** This page describes the design of the next significant piece of work, so you can see what it will and will not do before it exists. Today, [self-hosting](/docs/self-hosting/) is the way to run Denospace.

## The idea

A hosted Denospace that reads a folder in your Dropbox. You run no server. Your notes stay in your own Dropbox account, where they already are, synced by Dropbox's own client — which you are probably already running.

Emacs edits the folder on your laptop. Dropbox moves it. Denospace reads it through Dropbox's API. Writes go back the same way.

Nothing in that path is a sync engine written by us, which is the point. See [Sync and conflicts](/docs/sync-and-conflicts/).

## What it will be able to see

**Only your Denospace folder.** The integration will request app-folder scope, which means Dropbox grants access to a single directory created for this purpose and nothing else in your account. The rest of your Dropbox is not visible to the application, by construction rather than by promise.

## What it will not do

- **Merge conflicts.** Dropbox writes a *conflicted copy* file; Denospace shows you both. It will not pick a winner.
- **Hold the only copy.** The canonical files stay in your Dropbox. Denospace keeps a working copy to serve and index from, and that copy is disposable.

## Latency

Dropbox notifies the server that something changed, and the server then asks what. That is a round trip rather than a push, so expect a few seconds between saving in Emacs and seeing it in the browser — fine for notes, and not the same thing as live collaborative editing, which this is not.

## Google Drive

Planned after Dropbox and honestly harder: Drive addresses files by opaque identifiers rather than paths, so it needs a mapping layer that Dropbox does not. It will come once Dropbox is proven.
