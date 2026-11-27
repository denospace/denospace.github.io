---
title: Keybindings
section: Reference
order: 1
blurb: Default keys, and their Emacs equivalents.
---

# Keybindings

Outline motions follow `evil-org`. Folding follows `org-cycle`.

| Key | Does | Emacs equivalent |
|---|---|---|
| `Tab` | Fold cycle on a headline: folded → children → subtree | `org-cycle` |
| `Shift-Tab` | Whole buffer: overview → contents → show all | `org-shifttab` |
| `Alt-j` / `Alt-k` | Move item down / up | `org-metadown` / `org-metaup` |
| `Alt-l` / `Alt-h` | Indent / outdent item | `org-metaright` / `org-metaleft` |
| `Alt-i` | Insert a link, or edit the one at the cursor | `denote-link-or-create` / `org-insert-link` |
| `Shift-Alt-i` | Insert a web link, described by the page's own title | `org-cliplink` |
| `Return` | Follow the link under the cursor (vim normal mode) | `org-return-follows-link` |
| `Ctrl-k` | Page picker | — |
| `Ctrl-/` | Command palette | `M-x` |
| `Alt-/` | Search the library, line by line | `denote-grep` / `consult-denote-grep` |
| `Ctrl-q j` | Today's journal entry | `denote-journal-new-or-existing-entry` |
| `Ctrl-q p` / `Ctrl-q n` | Previous / next journal entry that exists | — |
| `Shift-Alt-t` | Signature browser, docked | `denote-sequence-dired` |

## Alt on macOS

`Alt-<letter>` needs care on macOS. Option composes characters — `⌥J` arrives as `∆`, `⌥⇧I` as a dead `ˆ` — and the editor deliberately will not fall back to the base layout.

These bindings are therefore matched on `event.code`, the physical key, with and without Shift. If a binding still misbehaves under an unusual layout, `Mod-. j` and the arrow-key forms work everywhere.

## Vim mode

Off by default; enable it from the command palette. Contexts are `normal`, `insert` and `visual`.

To move by visual line rather than by paragraph — the equivalent of remapping `evil-next-line` to `evil-next-visual-line` — bind `j` and `k` to `gj` and `gk` in your space config, for normal and visual mode.

One difference from Emacs worth knowing: evil's operator-pending state inherits your motion remaps, so `dj` in Emacs deletes a *visual* line. The editor here exposes no operator-pending context, so `dj` stays linewise. Everything else matches.
