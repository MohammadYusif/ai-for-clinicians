#!/usr/bin/env python3
"""Audit the rendered site. Every internal link, image, script, stylesheet and #fragment in
_site/ must resolve; a root-relative link (/foo) is an error, because this site is served
from a sub-path on GitHub Pages and such a link would go nowhere.

    python tools/check_links.py             # internal links only; exit 1 on any break
    python tools/check_links.py --external  # also list external URLs and check them (needs network)

Run `quarto render` first. Audit the rendered HTML, not the source: pandoc changes
structure in ways the .qmd does not show.
"""
from __future__ import annotations

import argparse
import sys
import urllib.error
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
SITE = ROOT / "_site"

SKIP_SCHEMES = ("mailto:", "tel:", "javascript:", "data:", "sms:")


class Page(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.refs: list[tuple[str, str]] = []
        self.ids: set[str] = set()

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if tag == "a" and a.get("name"):
            self.ids.add(a["name"])
        if tag in ("a", "link") and a.get("href") is not None:
            self.refs.append((tag, a["href"]))
        elif tag in ("img", "script", "source", "iframe", "video", "audio") and a.get("src"):
            self.refs.append((tag, a["src"]))


def parse(path: Path) -> Page:
    p = Page()
    p.feed(path.read_text(encoding="utf-8", errors="ignore"))
    return p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--external", action="store_true", help="also check external URLs (network)")
    args = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")

    if not SITE.is_dir():
        print("no _site/ directory: run `quarto render` first", file=sys.stderr)
        return 2

    pages = {p.resolve(): parse(p) for p in SITE.rglob("*.html")}
    broken: list[str] = []
    external: dict[str, str] = {}
    checked = 0

    for path, page in pages.items():
        rel = path.relative_to(SITE.resolve()).as_posix()
        for tag, ref in page.refs:
            ref = ref.strip()
            if not ref or ref.lower().startswith(SKIP_SCHEMES):
                continue
            parts = urlsplit(ref)
            if parts.scheme in ("http", "https"):
                external.setdefault(ref.split("#")[0], rel)
                continue
            if parts.scheme or parts.netloc:
                continue
            checked += 1
            raw = unquote(parts.path)
            if raw.startswith("/"):
                broken.append(f"{rel}: <{tag}> root-relative link {ref!r} (would resolve outside the site)")
                continue
            target = path if not raw else (path.parent / raw).resolve()
            if target.is_dir():
                target = target / "index.html"
            if not target.exists():
                broken.append(f"{rel}: <{tag}> {ref!r} -> missing file")
                continue
            frag = unquote(parts.fragment)
            if frag and target.suffix == ".html":
                other = pages.get(target.resolve())
                if other is None:
                    other = parse(target)
                if frag not in other.ids:
                    broken.append(f"{rel}: <{tag}> {ref!r} -> no id '{frag}' in {target.name}")

    print(f"{len(pages)} pages, {checked} internal references checked, {len(external)} distinct external URLs")

    ext_failures: list[str] = []
    if args.external:
        for url, where in sorted(external.items()):
            try:
                req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": "Mozilla/5.0 (link-audit)"})
                with urllib.request.urlopen(req, timeout=12) as resp:
                    status = resp.status
            except urllib.error.HTTPError as exc:
                status = exc.code
            except Exception as exc:  # DNS failure, timeout, TLS
                ext_failures.append(f"{where}: {url} -> {type(exc).__name__}")
                continue
            if status in (404, 410) or status >= 500:
                ext_failures.append(f"{where}: {url} -> HTTP {status}")
            elif status in (401, 403, 405, 429, 999):
                print(f"  note: {url} answered HTTP {status} (blocked or rate-limited; check by hand)")
    else:
        for url, where in sorted(external.items()):
            print(f"  external: {url}  (first seen on {where})")

    if broken or ext_failures:
        print("\nBROKEN LINKS:", file=sys.stderr)
        for row in broken + ext_failures:
            print(f"  {row}", file=sys.stderr)
        return 1
    print("links: every internal reference and #fragment resolves" + ("; external URLs reachable" if args.external else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
