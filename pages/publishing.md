---
title: Publishing a site
section: Publishing
order: 1
blurb: Turning notes into a website.
---

# Publishing a site

Denospace can render notes to HTML and publish them as a website, committed straight to a git repository.

> Publishing is a separate product from the editor and will be priced separately. See [Pricing](/pricing/).

## How it works

You mark which notes are published. `Blog: Publish` renders them to HTML, applies a template, and commits the result to the repository that serves your site — GitHub Pages, or anything else that serves a directory.

The whole publish is **one commit** built on the existing tree, so the history stays readable and a publish that changes nothing makes no commit at all.

## Drafts

Notes can be drafted locally and omitted from a production build, so you can write in the open without publishing in the open.

## What gets published

Only what you mark. The default is that a note is private: a publishing tool that defaults the other way is a privacy incident waiting for a bad afternoon.

Attachments referenced by published notes are published alongside them. Attachments referenced only by private notes are not.

## Why this exists

The notes are already written, already structured, already in a format that renders. The distance between a good Org library and a readable website is mostly plumbing, and this is the plumbing.
