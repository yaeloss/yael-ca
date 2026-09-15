#!/usr/bin/env python3
"""Check rendered SEO metadata, sitemap coverage, images, and redirect targets."""
import json
import sys
import xml.etree.ElementTree as ET
from collections import defaultdict
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
from urllib.robotparser import RobotFileParser


class Head(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.meta = defaultdict(list)
        self.schemas = []
        self.canonical = []
        self.author_links = []
        self.links = []
        self.json_text = None
        self.feed(text)

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        if tag == "meta":
            self.meta[attrs.get("property", attrs.get("name", attrs.get("http-equiv")))].append(attrs.get("content"))
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical.append(attrs["href"])
        if tag == "a" and attrs.get("rel") == "author":
            self.author_links.append(attrs["href"])
        if tag == "a" and "href" in attrs:
            self.links.append(attrs["href"])
        if tag == "script" and attrs.get("type") == "application/ld+json":
            self.json_text = ""

    def handle_data(self, text):
        if self.json_text is not None:
            self.json_text += text

    def handle_endtag(self, tag):
        if tag == "script" and self.json_text is not None:
            self.schemas.append(json.loads(self.json_text))
            self.json_text = None


def main(destination):
    root = Path(destination)
    manifest = json.loads((root / "legacy-redirects.json").read_text())
    base = manifest["baseURL"].rstrip("/")
    fallback_images = 0
    for entry in manifest["posts"]:
        path = root / unquote(entry["url"]).lstrip("/") / "index.html"
        head = Head(path.read_text())
        assert head.canonical == [base + entry["url"]], path
        assert head.author_links == ["/about/"], path
        assert head.meta["og:type"] == ["article"], path
        assert head.meta["og:url"] == head.canonical, path
        assert len(head.meta["article:published_time"]) == 1, path
        assert not head.meta["og:article:published_time"], path
        assert len(head.schemas) == 1, path
        schema = head.schemas[0]
        assert schema["@type"] == "Article", path
        assert schema["author"]["name"] == "Yaël Ossowski", path
        assert schema["author"]["@id"] == base + "/#person", path
        assert len(schema["author"]["sameAs"]) >= 4, path
        assert schema["description"] and head.meta["description"] == [schema["description"]], path
        assert schema["mainEntityOfPage"]["@id"] == head.canonical[0], path
        assert head.meta["og:image"] == head.meta["twitter:image"] == [schema["image"]], path
        image = urlsplit(schema["image"])
        if image.netloc == urlsplit(base).netloc:
            assert (root / unquote(image.path).lstrip("/")).is_file(), (path, image.path)
        fallback_images += image.path == "/images/og-home.jpg"

    for url, page_type in [("/", "WebPage"), ("/about/", "ProfilePage"), ("/posts/", None)]:
        head = Head((root / url.lstrip("/") / "index.html").read_text())
        assert head.meta["og:type"] == ["website"], url
        assert head.meta["og:url"] == [base + url], url
        assert not head.meta["article:published_time"], url
        if page_type:
            assert head.schemas[0]["@type"] == page_type, url
            assert head.schemas[0]["mainEntity"]["@id"] == base + "/#person", url
        else:
            assert not head.schemas, url

    urls = {element.text for element in ET.parse(root / "sitemap.xml").iter("{http://www.sitemaps.org/schemas/sitemap/0.9}loc")}
    posts = {base + entry["url"] for entry in manifest["posts"]}
    assert posts <= urls, "Posts missing from sitemap"
    hubs = {base + f"/tags/{slug}/" for slug in ["bitcoin", "tech", "legal-reform"]}
    archives = {url for url in urls if url.startswith((base + "/tags/", base + "/categories/"))}
    assert archives == hubs, archives
    assert "Sitemap: " + base + "/sitemap.xml" in (root / "robots.txt").read_text()
    assert "Disallow: /" not in (root / "robots.txt").read_text()
    robots = RobotFileParser()
    robots.parse((root / "robots.txt").read_text().splitlines())
    for bot in ["Googlebot", "Bingbot", "OAI-SearchBot", "ChatGPT-User", "PerplexityBot", "Claude-SearchBot"]:
        for url in urls:
            assert robots.can_fetch(bot, url), (bot, url)

    from generate_redirects import build_redirects
    redirects = build_redirects(manifest)
    for source, target in redirects.items():
        head = Head((root / unquote(source).lstrip("/") / "index.html").read_text())
        assert head.canonical == [base + target], source
        assert head.meta["refresh"] == ["0; url=" + base + target], source
        assert base + source not in urls, source
    assert redirects["/tag/blog/page/12/"] == "/tags/blog/"
    assert redirects["/tags/class-action-2/"] == "/tags/class-action/"
    cover = Head((root / "posts/legal-advertising-needs-to-be-ready-for-ai-boom/index.html").read_text())
    assert cover.meta["og:image"] == [base + "/posts/legal-advertising-needs-to-be-ready-for-ai-boom/images/ai-law.png"]
    assert len(cover.meta["og:image:width"]) == len(cover.meta["og:image:height"]) == 1
    assert "/tags/legal-reform/" in cover.links
    print(f"Passed: {len(posts)} articles, {len(urls)} sitemap URLs, {len(hubs)} topic hubs, {len(redirects)} redirects.")
    print(f"Social images: {len(posts) - fallback_images} article images; {fallback_images} use the site fallback.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
