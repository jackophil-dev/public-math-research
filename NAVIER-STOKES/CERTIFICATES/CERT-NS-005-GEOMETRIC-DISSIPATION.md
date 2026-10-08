# CERT-NS-005 — Geometric Dissipation Lemma

**Status:** VERIFIED — ANALYTICAL  
**Scope:** Local identity on the regular vorticity set only

## Claim

For \(\omega=\rho\xi\), \(\rho=|\omega|>0\), and \(|\xi|=1\),
\[
\xi\cdot\Delta\omega=\Delta\rho-\rho|\nabla\xi|^2.
\]
Therefore \(N=\nu\rho|\nabla\xi|^2\ge0\) when \(\nu>0\).

## Verification steps

1. Expand \(\Delta(\rho\xi)=(\Delta\rho)\xi+2\sum_j(\partial_j\rho)(\partial_j\xi)+\rho\Delta\xi\).
2. Differentiate \(\xi\cdot\xi=1\) to obtain \(\xi\cdot\partial_j\xi=0\).
3. Apply \(\Delta\) to \(\xi\cdot\xi=1\), giving \(\xi\cdot\Delta\xi=-|\nabla\xi|^2\).
4. Contract the product expansion with \(\xi\). The cross term vanishes and the stated identity follows.
5. Since \(\nu>0\), \(\rho>0\), and \(|\nabla\xi|^2\ge0\), conclude \(N\ge0\).

## Audit boundary

This is an analytical derivation, not a numerical or software test. No computational test is claimed. The certificate does not establish a bound on vortex stretching or global regularity and makes no assertion on the set \(\rho=0\).
