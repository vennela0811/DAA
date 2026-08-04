Linear Search sequentially inspects each element of a collection from start to finish until a match is found or the list ends.
It yields a linear time complexity of $O(n)$ for average and worst cases, though it achieves an optimal $O(1)$ best-case when the target is first.
It operates entirely in-place with an auxiliary space complexity of $O(1)$ and imposes no structural constraints like sorting.
While inefficient for large datasets, it remains the only viable search strategy for entirely unsorted or linked sequential data.
In DAA, it provides the fundamental baseline for brute-force sequential search against which logarithmic techniques are measured.