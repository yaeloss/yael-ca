#!/usr/bin/env python3
"""Verify media navigation, post membership, and redirects in a built site."""
import json
import sys
from pathlib import Path
from urllib.parse import unquote

from check_seo import Head
from generate_redirects import build_redirects


def main(destination):
    root = Path(destination)
    manifest = json.loads((root / "legacy-redirects.json").read_text())
    post_urls = {entry["url"] for entry in manifest["posts"]}

    def page(url):
        return Head((root / unquote(url).lstrip("/") / "index.html").read_text())

    media = ["/categories/interviews/", "/categories/talks-panels/", "/formats/video/"]
    members = {}
    for url in media:
        archive = page(url)
        assert set(media) <= set(archive.links), (url, "Missing media navigation")
        members[url] = post_urls & set(archive.links)
        assert members[url], (url, "Empty archive")
        for post in members[url]:
            assert url in page(post).links, (post, "Missing category or format link", url)
    for url in ["/posts/", "/categories/"]:
        assert set(media) <= set(page(url).links), (url, "Missing archive navigation")

    # Representative distinctions: interview, conference panel, testimony, standalone video.
    examples = {
        "is-your-password-healthy-yael-ossowski-on-dc-news-nows-tech-talk": media[0],
        "btc-prague-panel-investment-in-over-regulated-environment": media[1],
        "yael-ossowski-fda-testimony-on-smart-cbd-regulation": media[1],
        "vapelive-yael-ossowski-on-the-consumer-choice-center-us-vaping-index": media[1],
        "covid-19-liability-shields-shaping-our-legal-system-to-withstand-pandemic-lawsuits": media[1],
    }
    for slug, category in examples.items():
        post = f"/posts/{slug}/"
        assert post in members[category] and post in members[media[2]], slug
        other = media[1] if category == media[0] else media[0]
        assert post not in members[other], (slug, "Incorrect media category")
    standalone = "/posts/urban-exploring-in-detroit/"
    assert standalone in members[media[2]]
    assert all(standalone not in members[category] for category in media[:2])

    redirects = build_redirects(manifest)
    for old, target in manifest["archiveMoves"].items():
        assert redirects[old] == target
        assert redirects[old.replace("/categories/", "/category/")] == target
        assert redirects[old + "page/1/"] == target
        assert all(old not in page(post).links for post in post_urls), old
    assert redirects["/category/videos/page/6/"] == "/formats/video/"
    for url, posts in members.items():
        print(f"Passed: {len(posts)} posts in {url}")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "public")
