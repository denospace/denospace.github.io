---
title: Org mode in the browser
blurb: A web interface to a folder of Org files. Nothing is converted; Emacs keeps editing them.
path: index.html
layout: home
---

<header style="display:flex;align-items:center;gap:0.9rem;margin-bottom:2.4rem">
<img src="/logo.svg" alt="" width="56" height="56" style="border-radius:12px" />
<div><h1 style="font-size:2.1rem;margin:0;line-height:1">Denospace</h1>
<p style="color:var(--muted);font-style:italic;margin:.3rem 0 0;font-size:1rem">Org mode in the browser.</p></div>
</header>

A web interface to a folder of **Org mode** files. Point it at a directory and every `.org` file becomes a page you can read and edit from a browser — on a laptop without your config, on a phone, anywhere.

Nothing is imported and nothing is converted. The files stay exactly what Emacs wrote. Emacs keeps editing them. Denospace is another window onto the same directory.

**Markdown and plain text work too.** Org is the hard part and the reason this exists — but `.md` and `.txt` libraries are read and written just as happily, with front matter in Org keywords, YAML or TOML, sniffed per file.

## Org, parsed properly

Not Markdown with a different extension. Headings and folding, tables, source blocks, your own `#+TODO:` sequences, priorities, footnotes, drawers, links and inline images — parsed by a parser written for Org, and written back as files Emacs reopens unchanged.

## Your files stay yours

There is no sync engine here and there never will be. Your notes move between machines by whatever you already use — Syncthing, a server, git. The canonical copy is a folder on your own disk. If this project stopped tomorrow, nothing would need exporting.

## Denote, if you want it

If your filenames follow the [Denote](https://protesilaos.com/emacs/denote) scheme, Denospace reads it exactly: identifiers, keywords, signatures, and `denote:` links that survive renames. Byte-identical filenames to `denote.el`, checked against 1,713 recorded cases on every build.

A feature, not a requirement. Plain files in a plain directory work fine.

> **Early days.** It reads and edits a real four-thousand-note library every day, and parts of Org are still missing. Self-hosting works now; hosting is not open yet. See the [roadmap](/roadmap/).

<p style="margin-top:2.4rem">
<a href="/docs/" style="display:inline-block;text-decoration:none;border:1px solid var(--ink);border-radius:4px;padding:.5rem 1.1rem;font-size:.92em">Read the docs &rarr;</a>
&nbsp;&nbsp;<a href="https://github.com/denospace/denospace" style="font-size:.92em">Source on GitHub</a>
</p>
