/**
 * Offer normalization helpers for Netlify Functions.
 *
 * Translate raw adapter payloads into the canonical SkyKeys offer schema,
 * including currency conversion, fee placeholders, and metadata flags.
 */

// TODO: Define TypeScript interfaces for raw adapter output and normalized
// offers to enforce shape consistency across the pipeline.

// TODO: Port normalization steps from the Python scaffolding, ensuring
// price_total_eur = price_eur + fees_eur and flags.fees_estimated semantics are
// preserved.
