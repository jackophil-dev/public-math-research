# Replicator — Computational Verification

A concrete test suite should check: state/control dimensions; admissible-control constraints; invariant preservation; resource counters; safety-gate rejection when predicates fail; and conservation residuals with units, tolerance, and uncertainty.

For finite-state models, enumerate every admissible transition. For continuous or hybrid models, sampled simulations cover only sampled cases; they do not prove a universal property. Analytical proof, adversarial testing, and numerical experiments should be reported separately.

Each verification record should include model version, parameter values and units, software version, seeds where relevant, coverage, counterexamples, tolerances, and logs. Distinguish simulation from physical measurement.

**Current status:** public certificates describe architecture-level obligations. This folder does not claim a new run, validated hardware, or successful physical replication. Implementation-wide verification remains **OPEN**.