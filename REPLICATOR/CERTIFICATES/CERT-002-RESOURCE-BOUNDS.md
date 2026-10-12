# CERT-002 — Resource Bounding and Limits

**Class:** Verification specification  
**Status:** SPECIFICATION / OPEN VALIDATION

Declare and test hard bounds for execution depth, memory, numerical precision, and other resources required by the implementation. Examples include $N\le N_{max}$ and $M_{alloc}\le M_{limit}$. Any precision requirement must include a justified error model and an explanation of how rounding or accumulated error is bounded.

## Evidence required

- Chosen bounds and units.
- A specified workload or execution horizon.
- Measurement method and logs.
- Error analysis showing the stated precision is adequate.

A declared number such as $10^{-12}$ is a parameter requirement, not automatically a proved numerical property.