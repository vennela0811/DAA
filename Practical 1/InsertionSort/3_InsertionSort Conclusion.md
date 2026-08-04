Insertion Sort builds the final sorted array one element at a time by repeatedly shifting larger elements to make room for the current item.
It excels on small data sets or nearly sorted inputs, achieving an efficient $O(n)$ best-case time complexity.
For average and worst-case scenarios with randomized or reverse-ordered data, its time complexity drops to $O(n^2)$.
It operates entirely in-place requiring $O(1)$ auxiliary space and preserves the relative order of identical elements as a stable algorithm.
In DAA, it illustrates the incremental decrease-and-conquer paradigm, demonstrating high efficiency when the input is already partially ordered.