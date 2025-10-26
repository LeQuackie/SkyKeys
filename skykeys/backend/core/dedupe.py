"""Deduplication strategies for SkyKeys offers."""

from __future__ import annotations

# TODO: introduce data structures representing dedupe keys and selection
# strategies (e.g., lowest total price wins). Ensure logic remains
# deterministic and unit-testable.


def dedupe_offers(offers: list[dict]) -> list[dict]:
    """Resolve duplicates across shop/platform/region/title combinations.

    TODO: Implement grouping by the canonical dedupe key and choose the
    offer with the minimal ``price_total_eur`` while preserving metadata
    about discarded entries for logging.
    """

    raise NotImplementedError("Deduplication logic pending implementation")
