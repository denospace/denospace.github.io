---
title: Templates and shortcodes
section: Publishing
order: 2
blurb: Controlling how published pages look.
---

# Templates and shortcodes

## Shortcodes

Published notes can carry shortcodes that render to richer HTML than Org alone describes. The supported set follows the Tufte conventions the author's own site is built on:

| Shortcode | Renders |
|---|---|
| `{{< marginnote >}}…{{< /marginnote >}}` | A note in the margin, beside the text rather than below it |
| `{{< figure src="…" caption="…" >}}` | A figure with its caption in the gutter |
| `{{< figure src="…" full >}}` | A full-width figure |
| `{{< vimeo id >}}` | An embedded video |

A `marginnote` may contain a `figure`, so the pairing is matched before the standalone form.

## Why these and not a template language

Because these are the ones the content already uses. A generator that ignored them would quietly flatten half the writing it was given — margin notes are not decoration in a Tufte-styled site, they are where a good deal of the argument lives.

## The Tufte view

The editor itself has a third display mode that matches the published result: the same serif, the same measure, the same hierarchy of size and italics rather than weight. Writing in it means what you see while drafting is close to what a reader gets.

It is a view of the file, not a change to it. Nothing about the Org source differs between modes.
