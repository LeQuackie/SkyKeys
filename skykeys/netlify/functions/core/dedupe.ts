/**
 * Offer deduplication utilities for Netlify Functions.
 *
 * Maintain the canonical key strategy (shop_domain, platform, region,
 * canonical_title) when filtering aggregated offers.
 */

// TODO: Export functions that accept normalized offers and return a filtered
// array sorted by price_total_eur, keeping the cheapest option per dedupe key.

// TODO: Provide helper to derive canonical_title using the same stopword and
// normalization rules defined in the MVP brief.
