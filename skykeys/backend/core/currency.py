"""Currency conversion helpers for SkyKeys."""

from __future__ import annotations

# TODO: load static rates from ``config/rates.json`` with caching and
# expose async-safe helper functions for converting arbitrary currencies
# to EUR. Consider handling stale rates and logging warnings.


def convert_to_eur(amount: float, currency: str) -> float:
    """Placeholder for currency conversion logic."""

    raise NotImplementedError("Currency conversion pending implementation")
