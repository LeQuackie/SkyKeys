"""Shared utility helpers for SkyKeys backend modules."""

from __future__ import annotations

# TODO: collect helpers such as async retry/backoff wrappers, Playwright
# browser context management, random delay generation, and domain parsing
# utilities.


def parse_shop_domain(url: str) -> str:
    """Extract normalized shop domain from a URL.

    TODO: implement using TLD parsing while gracefully handling missing
    schemes and subdomains.
    """

    raise NotImplementedError
