# Navier–Stokes — Definitions and Hypotheses

The three-dimensional incompressible Navier–Stokes system is
\[
\partial_tu+(u\cdot\nabla)u=-\nabla p+\nu\Delta u,\quad \nabla\cdot u=0.
\]
The domain and boundary conditions matter: periodic, whole-space decay, and bounded-domain cases have different boundary terms.

Vorticity is \(\omega=\nabla\times u\); strain is \(S=(\nabla u+\nabla u^T)/2\). The enstrophy norm is \(\|\omega\|_2^2=\int_\Omega|\omega|^2dx\).

The identities below are classical for sufficiently smooth solutions, or for weak solutions only where the relevant operations are justified. Integration by parts must not be applied formally without boundary and regularity control.

Where \(\rho=|\omega|>0\), one may write \(\omega=\rho\xi\) with \(|\xi|=1\); this direction field is undefined at zero-vorticity points and requires care there.