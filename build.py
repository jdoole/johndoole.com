#!/usr/bin/env python3
"""Wrap src/page.html (artifact fragment) into a standalone index.html for Render/GitHub Pages."""
import pathlib, re
src = pathlib.Path(__file__).parent / "src" / "page.html"
out = pathlib.Path(__file__).parent / "index.html"
frag = src.read_text()
# split head-ish tags (title/meta/link/style) from body content
m = re.search(r"</style>\s*", frag)
head, body = frag[:m.end()], frag[m.end():]
head = head.replace('<meta name="claude:viewport-fit-sides" content="cover">\n', "")
html = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
{head}
</head>
<body>
{body}
</body>
</html>
"""
out.write_text(html)
print(f"wrote {out} ({len(html):,} bytes)")
