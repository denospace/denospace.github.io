#!/usr/bin/env python3
"""Build the Denospace site from pages/*.md.

Each page starts with a `---` front-matter block (title, nav, order, blurb).
Markdown is deliberately a small subset -- headings, paragraphs, lists, tables,
fenced code, blockquotes, links, inline code, bold and italic -- because the
whole point of a generator this size is that you can read it in one sitting.
"""
import os, re, html, json, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
PAGES = os.path.join(ROOT, "pages")
TEMPLATE = open(os.path.join(ROOT, "_template.html"), encoding="utf8").read()

SECTIONS = ["Start here", "Concepts", "Reference", "Integrations", "Publishing"]


def front_matter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise SystemExit("missing front matter")
    meta = {}
    for line in m.group(1).split("\n"):
        if not line.strip():
            continue
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, m.group(2)


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r"`([^`]+)`", lambda m: "<code>" + m.group(1) + "</code>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    return s


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def render(md):
    out, lines, i = [], md.split("\n"), 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("```"):
            lang = line[3:].strip()
            body = []
            i += 1
            while i < len(lines) and not lines[i].startswith("```"):
                body.append(lines[i]); i += 1
            cls = f' class="lang-{lang}"' if lang else ""
            out.append(f"<pre{cls}><code>" + html.escape("\n".join(body)) + "</code></pre>")
        elif line.startswith("|"):
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                rows.append(lines[i]); i += 1
            i -= 1
            cells = [[c.strip() for c in r.strip().strip("|").split("|")] for r in rows]
            cells = [c for c in cells if not all(set(x) <= set("-: ") for x in c)]
            head, body = cells[0], cells[1:]
            t = ["<table><thead><tr>"] + [f"<th>{inline(c)}</th>" for c in head] + ["</tr></thead><tbody>"]
            for r in body:
                t += ["<tr>"] + [f"<td>{inline(c)}</td>" for c in r] + ["</tr>"]
            out.append("".join(t + ["</tbody></table>"]))
        elif re.match(r"^#{1,4} ", line):
            lvl = len(line) - len(line.lstrip("#"))
            txt = line[lvl:].strip()
            out.append(f'<h{lvl} id="{slugify(txt)}">{inline(txt)}</h{lvl}>')
        elif re.match(r"^[-*] ", line) or re.match(r"^\d+\. ", line):
            ordered = bool(re.match(r"^\d+\. ", line))
            items = []
            while i < len(lines) and (re.match(r"^[-*] ", lines[i]) or re.match(r"^\d+\. ", lines[i])):
                items.append(re.sub(r"^([-*]|\d+\.) ", "", lines[i])); i += 1
            i -= 1
            tag = "ol" if ordered else "ul"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(x)}</li>" for x in items) + f"</{tag}>")
        elif line.startswith("> "):
            body = []
            while i < len(lines) and lines[i].startswith("> "):
                body.append(lines[i][2:]); i += 1
            i -= 1
            out.append("<blockquote>" + inline(" ".join(body)) + "</blockquote>")
        elif line.strip():
            para = [line]
            while i + 1 < len(lines) and lines[i + 1].strip() and not re.match(r"^([-*>#|]|\d+\.|```)", lines[i + 1]):
                i += 1; para.append(lines[i])
            out.append("<p>" + inline(" ".join(para)) + "</p>")
        i += 1
    return "\n".join(out)


def main():
    docs = []
    for f in sorted(os.listdir(PAGES)):
        if not f.endswith(".md"):
            continue
        meta, body = front_matter(open(os.path.join(PAGES, f), encoding="utf8").read())
        meta["slug"] = f[:-3]
        meta["body"] = body
        docs.append(meta)

    # sidebar, grouped by section in declared order
    nav = []
    for sec in SECTIONS:
        inside = sorted([d for d in docs if d.get("section") == sec], key=lambda d: int(d.get("order", 99)))
        if not inside:
            continue
        nav.append(f"<li class='nav-section'>{html.escape(sec)}</li>")
        for d in inside:
            nav.append(f"<li><a href=\"/docs/{d['slug']}/\" data-slug=\"{d['slug']}\">{html.escape(d['title'])}</a></li>")
    nav_html = "<ul class='nav'>" + "".join(nav) + "</ul>"

    for d in docs:
        page_nav = nav_html.replace(f'data-slug="{d["slug"]}"', 'class="here" aria-current="page"')
        out = (TEMPLATE
               .replace("{{title}}", html.escape(d["title"]))
               .replace("{{blurb}}", html.escape(d.get("blurb", "")))
               .replace("{{nav}}", page_nav)
               .replace("{{content}}", render(d["body"])))
        dest = os.path.join(ROOT, "docs", d["slug"])
        os.makedirs(dest, exist_ok=True)
        open(os.path.join(dest, "index.html"), "w", encoding="utf8").write(out)

    # docs index
    idx = ["<h1>Documentation</h1>"]
    for sec in SECTIONS:
        inside = sorted([d for d in docs if d.get("section") == sec], key=lambda d: int(d.get("order", 99)))
        if not inside:
            continue
        idx.append(f"<h2>{html.escape(sec)}</h2><ul class='index'>")
        for d in inside:
            idx.append(f"<li><a href=\"/docs/{d['slug']}/\">{html.escape(d['title'])}</a>"
                       f"<span>{html.escape(d.get('blurb',''))}</span></li>")
        idx.append("</ul>")
    out = (TEMPLATE.replace("{{title}}", "Documentation")
           .replace("{{blurb}}", "How to use Denospace.")
           .replace("{{nav}}", nav_html)
           .replace("{{content}}", "".join(idx)))
    os.makedirs(os.path.join(ROOT, "docs"), exist_ok=True)
    open(os.path.join(ROOT, "docs", "index.html"), "w", encoding="utf8").write(out)
    print(f"built {len(docs)} doc pages + index")


if __name__ == "__main__":
    main()
