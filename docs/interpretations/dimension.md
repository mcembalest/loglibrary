# Dimension and capacity

A space of dimension $d$ holds exactly $d$ mutually orthogonal directions. If directions need only be *nearly* orthogonal, the number that fit grows exponentially in $d$: roughly $e^{cd}$ vectors with pairwise inner product below a fixed tolerance (Johnson–Lindenstrauss). The dimension is then the logarithm of the number of distinguishable directions:

$$ d \approx \tfrac{1}{c}\,\log(\text{capacity}). $$

Related facts:

- $n$ bits index $2^n$ states; the Boolean cube $\{0,1\}^n$ has $2^n$ vertices, and $n = \log_2$ of that count.
- $n$ qubits span a $2^n$-dimensional Hilbert space; the [Holevo bound](https://en.wikipedia.org/wiki/Holevo%27s_theorem) limits the classical information recoverable from them to $n$ bits.
- **Superposition** — networks represent many more features than dimensions by assigning nearly-orthogonal directions to features that are rarely active at once.

## References

- W. B. Johnson, J. Lindenstrauss, "Extensions of Lipschitz mappings into a Hilbert space" (1984).
- Elhage et al., "Toy Models of Superposition" (2022). <https://transformer-circuits.pub/2022/toy_model/index.html>

## See also

- [Complexity and addressing](complexity.md)
- [Information and entropy](entropy.md)
