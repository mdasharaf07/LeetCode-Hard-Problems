# Approach Overview:

**Python Logic Explanation**

Base Case:
If the input list array is empty, return None.

Pairwise Merging:

Merge the lists two at a time until only one remains.

After each round, store the merged results in temp and repeat.

Helper Function (merge_lists):

Works like the “merge” step in merge sort.

Compares current nodes of both lists, attaches the smaller one, and moves forward.

Final Output:
The merged list is stored in lists[0].

✅ Complexity:

Time → O(N log k)

Space → O(1) (iterative merging)

**C++ Logic Explanation**

Divide and Conquer Approach:

Recursively split the list of linked lists into halves.

Merge each half until only one list remains.

mergeTwoLists:

Merges two sorted lists using recursion.

Picks the smaller head and continues recursively.

Recursive Merge (divideAndConquer):

Splits [left, right] range into two halves.

Combines results using mergeTwoLists.

Why Divide and Conquer?

Reduces total comparisons compared to merging sequentially.

Similar to merge sort’s efficiency.

✅ Complexity:

Time → O(N log k)

Space → O(log k) (recursion depth)

**Java Logic Explanation**

Base Case:
If the array of lists is empty, return null.

Divide and Conquer:

Split the array into halves recursively (left, mid, right).

Merge each half until a single sorted list remains.

mergeTwoLists Function:

Recursively merges two sorted lists.

Returns the smaller node as the new head each time.

Efficiency:

Reduces unnecessary merges compared to linear combining.

Balances the merging steps for performance.

✅ Complexity:

Time → O(N log k)

Space → O(log k)