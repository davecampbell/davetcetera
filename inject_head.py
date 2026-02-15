#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(".").resolve()
HEAD_SNIPPET = ROOT / "site-lib/html/custom-head-content-content.html"

snippet = HEAD_SNIPPET.read_text(encoding="utf-8")

# Inject into all top-level html files (adjust glob if you have subfolders)
html_files = list(ROOT.rglob("*.html"))

for p in html_files:
    # skip the snippet file itself
    if p.resolve() == HEAD_SNIPPET.resolve():
        continue

    txt = p.read_text(encoding="utf-8", errors="ignore")
    if "custom-head-content-content.html" in txt or snippet.strip() in txt:
        continue  # already injected

    if "</head>" not in txt:
        continue

    txt2 = txt.replace("</head>", snippet + "\n</head>", 1)
    p.write_text(txt2, encoding="utf-8")

print(f"Injected into {len(html_files)} html files.")