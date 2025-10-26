"""Base adapter definitions for scraping external price sources."""

from __future__ import annotations

# TODO: define an abstract async adapter interface that coordinates
# Playwright context creation, rate limiting, retry logic, and parsing via
# YAML-driven selectors.


class BaseSourceAdapter:
    """Scaffold for implementing concrete source scrapers."""

    # TODO: declare async `search` method signature, configuration loading
    # helpers, and instrumentation hooks (logging metrics to scrape_logs).

    raise NotImplementedError
