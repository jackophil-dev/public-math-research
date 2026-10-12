# Navier–Stokes — Core Equations and Derivations

Taking curl of momentum removes pressure:
\[
\partial_t\omega+(u\cdot\nabla)\omega=(\omega\cdot\nabla)u+\nu\Delta\omega.
\]
Multiply by \(\omega\) and integrate, assuming sufficient smoothness and boundary conditions that remove transport and diffusion boundary terms:
\[
\frac12\frac{d}{dt}\|\omega\|_2^2=\int\omega_i\omega_j\partial_j u_i\,dx-\nu\|\nabla\omega\|_2^2.
\]
Because \(\omega_i\omega_j\) is symmetric, its contraction with the antisymmetric part of \(\nabla u\) vanishes. Thus the stretching term equals \(\int\omega^TS\omega\,dx\), where \(S=(\nabla u+\nabla u^T)/2\).

Also \(|\omega^TS\omega|\le |S||\omega|^2\). If \(S\in L^\infty\), then
\[
\left|\int\omega^TS\omega\,dx\right|\le\|S\|_\infty\|\omega\|_2^2.
\]
This bound alone does not close global regularity unless \(\|S\|_\infty\) is controlled suitably.