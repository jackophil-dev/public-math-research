# CERT-004 — Invariant Preservation

**Class:** Verification specification  
**Status:** SPECIFICATION / OPEN VALIDATION

For a stated invariant $I$ and each admissible transition $T$, $I(T(s))=I(s)$ must hold on the declared domain, subject to explicit hypotheses.

## Evidence required

- Exact definition of each invariant.
- Domain and admissible transition class.
- Proof or reproducible test for preservation.
- Treatment of rounding, measurement error, and external inputs.

Energy and material-conservation claims require their own balance laws and physical assumptions. Listing an invariant does not establish that an implementation preserves it.