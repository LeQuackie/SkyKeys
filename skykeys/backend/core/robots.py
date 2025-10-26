"""Robots.txt compliance helpers for the SkyKeys scrapers."""

from __future__ import annotations

# TODO: add utilities that fetch and cache robots.txt directives, honor
# crawl-delay rules, and expose helper functions to check if scraping a
# given path is allowed for the SkyKeys user agent.


def is_allowed(url: str) -> bool:
    """Placeholder for permission checks."""

    raise NotImplementedError
