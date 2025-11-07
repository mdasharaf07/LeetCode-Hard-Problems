# Approach Overview:

**Python Logic Explanation**

Initialize two pointers, p1 and p2, starting from 0 for both arrays.

Define a helper function get_min() that:

Compares the current elements of both arrays.

Returns the smaller value and moves that array’s pointer forward.

Handles cases where one array is exhausted.

Calculate total length m + n:

If odd, move halfway through using get_min() until the median index.

If even, move to one index before the middle, take the next two get_min() results, and average them.

Key Idea:
Instead of merging both arrays, only simulate the merge process up to the median point, which reduces unnecessary operations.

Time Complexity: O(m + n)
Space Complexity: O(1)


**C++ Logic Explanation**

Use two pointers p1 and p2 as class variables to maintain state between function calls.

Define getMin() to:

Compare elements at current pointers.

Return the smaller one and increment the corresponding pointer.

Handle array boundaries (when one array finishes first).

In findMedianSortedArrays():

Compute total elements m + n.

If even, skip the first (m+n)/2 - 1 elements, take two next minimums, and compute their average.

If odd, skip (m+n)/2 elements and return the next minimum.

Highlights:

Uses integer operations with explicit type casting for averaging.

Efficient use of in-place traversal — no extra space required.

Time Complexity: O(m + n)
Space Complexity: O(1)

**Java Logic Explanation**


Maintain two index pointers p1 and p2 as class variables.

Define getMin() to:

Return the smaller value among nums1[p1] and nums2[p2].

Increment the pointer of the chosen array.

Handle when one array is fully traversed.

In findMedianSortedArrays():

Determine if total length is odd or even.

For even, iterate (m+n)/2 - 1 times, discard values, then average next two minimums.

For odd, iterate (m+n)/2 times, discard values, then return next minimum.

Highlights:

Clean and readable pointer manipulation.

Uses clear integer arithmetic and type casting for double median calculation.

Mirrors Python/C++ logic but with Java syntax and conventions.

Time Complexity: O(m + n)
Space Complexity: O(1)