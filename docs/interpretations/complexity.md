# Complexity and addressing

To specify one item out of $N$ requires $\log_2 N$ bits — the length of an address, or the number of yes/no questions in an optimal search.

- **Binary search** locates an item in a sorted array of $n$ elements in $O(\log n)$ comparisons, halving the range at each step.
- **Tree height.** A balanced binary tree over $n$ leaves has height $\Theta(\log n)$.
- **LOGSPACE (L)** is the class of problems solvable with $O(\log n)$ working memory — enough to hold a constant number of pointers into the input, but not to copy it.

$O(\log n)$ is the cost of *locating* something among $n$ items, as distinct from *reading* them ($O(n)$).

## See also

- [Information and entropy](entropy.md)
- [Dimension and capacity](dimension.md)
