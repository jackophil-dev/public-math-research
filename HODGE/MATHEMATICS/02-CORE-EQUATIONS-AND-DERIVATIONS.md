# Hodge — Core Equations and Derivations

The recorded rank-two Gram matrix is
\[
G=\begin{pmatrix}36&12\\12&0\end{pmatrix}.
\]
Thus \(\det G=36\cdot0-12^2=-144\), so the discriminant group has order 144.

The recorded Smith normal form is \(D=\operatorname{diag}(12,12)\). If verified by unimodular row and column operations, it gives
\[
A_L\cong\operatorname{coker}(G)\cong
\mathbb Z/12\mathbb Z\oplus\mathbb Z/12\mathbb Z.
\]
The diagonal product equals \(|\det G|\), a consistency check but not by itself a complete SNF proof.

If \(L\subset L'\) are full-rank lattices of index \(m\), with the same rational bilinear form, then \(|\det G_L|=m^2|\det G_{L'}|\). A proposed index-two extension such as \(R=(P+Q)/2\) therefore requires an explicit basis and integrality check.

The arithmetic above concerns the specified matrix. To infer a statement about algebraic cycles, one must additionally prove the embedding into ambient integral cohomology and the relevant geometric identification.