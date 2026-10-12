# P/PN Part I — Research Dossier

**Author:** Philippe Beauchamp · **DOI:** [10.5281/zenodo.23196136](https://doi.org/10.5281/zenodo.23196136)

## Integral exterior projection

Let $L_6\simeq\mathbb Z^6$. The canonical map is $\pi:L_6\otimes L_6\to\Lambda^2L_6$, $\pi(x\otimes y)=x\wedge y$. For the recorded relations $a=b$, $c=2d-a$, $P=a\otimes b$, $Q=c\otimes b$, and $R=(P+Q)/2=d\otimes b$, set $v=d\wedge b$. The stated projections are $\pi(P)=0$, $\pi(Q)=2v$, and $\pi(R)=v$. These identities depend on the specified relations.

## Primitive bivector

In the standard lexicographic basis of $\Lambda^2\mathbb Z^6$, the recorded vector is $v=e_{12}-e_{14}+e_{15}-e_{16}-e_{23}+e_{34}-e_{35}+e_{36}$, with coordinate vector $(1,0,-1,1,-1,-1,0,0,0,1,-1,1,0,0,0)$. Its coordinate gcd is 1, so this vector is primitive in the stated free abelian group.

## Matrix invariants

The certificate record states $\operatorname{SNF}(M_{PR})=\operatorname{diag}(1,1,0,\ldots,0)$. The full matrix and basis ordering are necessary for independent reproduction. The recorded saturated Gram matrix is $G_{sat}=\begin{pmatrix}36&12\\12&0\end{pmatrix}$, with determinant $-144$, stated SNF $\operatorname{diag}(12,12)$, and associated group $(\mathbb Z/12\mathbb Z)^2$. These are arithmetic statements about specified inputs; they do not prove geometric realization.

## Open identification gate

The public record does not supply a verified map $M_\iota:\mathbb Z^6\to H^1(E^4,\mathbb Z)\simeq\mathbb Z^8$. No map is guessed or reconstructed. The geometric/cohomological identification remains **OPEN** until the original source basis, map, and compatibility conditions are supplied and checked.

## Reproduction checklist

1. Confirm basis ordering for $L_6$ and $\Lambda^2L_6$.
2. Reconstruct source tensors from original data.
3. Recompute exterior projections and coordinate gcd.
4. Recompute SNF from the complete integer matrix.
5. Recompute determinant and SNF of $G_{sat}$.
6. Keep arithmetic invariants separate from geometric identification.

**Evidence labels:** DERIVED for projection identities; COMPUTATIONALLY VERIFIED relative to specified inputs for integer invariants; OPEN for ambient identification. This dossier is a public companion, not a claim that the open problem is solved.