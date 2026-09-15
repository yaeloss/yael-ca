#!/usr/bin/env python3
"""Verify generated assets and image loading without external dependencies."""
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.images, self.scripts, self.frames, self.styles = [], [], [], []
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "img": self.images.append(attrs)
        if tag == "script" and "src" in attrs: self.scripts.append(attrs)
        if tag == "iframe": self.frames.append(attrs)
        if tag == "link" and attrs.get("rel") == "stylesheet": self.styles.append(attrs)


def local_file(root, page_url, src):
    url = urlsplit(urljoin("https://yael.ca" + page_url, src))
    if url.netloc != "yael.ca":
        return None
    return root / unquote(url.path).lstrip("/")


def main(destination):
    root = Path(destination)
    manifest = json.loads((root / "legacy-redirects.json").read_text())
    index = json.loads((root / "index.json").read_text())
    assert len(index) == len(manifest["posts"]), "Incomplete search index"
    responsive = frames = 0
    for url in ["/", "/about/"] + [entry["url"] for entry in manifest["posts"]]:
        page = Page((root / unquote(url).lstrip("/") / "index.html").read_text())
        for script in page.scripts:
            src = script["src"]
            assert "cdn.jsdelivr.net" not in src, (url, src)
            assert "fuse-7.1.0" not in src, "Search library must load on demand"
            if "/js/search.min." in src:
                assert url == "/" and "defer" in script, (url, src)
                assert local_file(root, url, script["data-fuse-url"]).is_file()
            if "/js/main.min." in src or "/js/search-back.min." in src:
                assert "defer" in script, (url, src)
            local = local_file(root, url, src)
            if local:
                assert local.is_file(), local
        for style in page.styles:
            assert "fonts.googleapis.com" not in style["href"]
            assert local_file(root, url, style["href"]).is_file()
        for frame in page.frames:
            assert frame.get("loading") == "lazy", url
            frames += 1
        for img in page.images:
            if "srcset" not in img or "_hu_" not in img["src"]:
                continue
            assert int(img["width"]) > 0 and int(img["height"]) > 0, (url, img)
            assert img.get("decoding") == "async", (url, img)
            if img.get("fetchpriority") == "high":
                assert img.get("loading", "eager") != "lazy", (url, img)
            for candidate in img["srcset"].split(","):
                src, _ = candidate.strip().split()
                assert local_file(root, url, src).is_file(), (url, src)
            responsive += 1
    assert responsive > 400, "Responsive image coverage unexpectedly dropped"
    assert frames > 100, "Embedded player coverage unexpectedly dropped"
    assert len(list((root / "fonts").glob("*.woff2"))) == 4
    print(f"Passed: {responsive} responsive images, {frames} lazy embeds, local fonts, deferred scripts, complete search index.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
