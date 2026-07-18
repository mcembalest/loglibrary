# Information and entropy

The information content of an event of probability $p$ is $-\log_b p$; with $b = 2$ it is measured in bits. Rarer events carry more information.

The Shannon entropy of a distribution is the expected information:

$$ H = -\sum_i p_i \log_b p_i. $$

For $N$ equally likely outcomes, $H = \log_b N$. The logarithm is forced by the requirement that information from independent sources add: $I(pq) = I(p) + I(q)$ — see [from products to sums](../foundations/product-to-sum.md).

## References

- R. V. L. Hartley, "Transmission of Information" (1928).
- C. E. Shannon, "A Mathematical Theory of Communication" (1948).

## See also

- [Complexity and addressing](complexity.md)
- [Dimension and capacity](dimension.md)
