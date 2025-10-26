"""Caching interface for storing SkyKeys search results."""

from __future__ import annotations

# TODO: define async cache abstraction that supports 45 minute TTL for
# search results. Start with SQLite and design for future Redis option.


def get_cached_results(query: str):
    """Retrieve cached entries for a given search term.

    TODO: implement SQLite-backed query with TTL validation. Return
    ``None`` when cache is stale or missing.
    """

    raise NotImplementedError


def set_cached_results(query: str, data: dict) -> None:
    """Persist search results into the cache store.

    TODO: store normalized offers, best offer metadata, and scrape flags
    with an expiration timestamp. Ensure writes are atomic.
    """

    raise NotImplementedError
