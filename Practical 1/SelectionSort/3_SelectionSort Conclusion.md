Selection Sort repeatedly scans the unsorted portion of the array to locate the minimum element and places it at the correct position.
It exhibits a fixed time complexity of $O(n^2)$ across best, average, and worst cases due to its mandatory complete scans.
It operates completely in-place with an optimal space complexity of $O(1)$ and minimizes total writes by performing at most $n$ swaps.
However, it is an unstable sorting algorithm and fails to take advantage of partially sorted inputs like insertion sort does.
In DAA, it serves as a classic example of iterative design, contrasting with efficient divide-and-conquer sorting strategies.