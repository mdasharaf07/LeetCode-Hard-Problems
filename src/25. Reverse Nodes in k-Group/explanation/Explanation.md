# Approach Overview:

**Python Logic Explanation**

Reverse Helper Function:

Reverses nodes between start and end (not inclusive of end).

Dummy Node:

Simplifies handling head changes after reversal.

Group Detection:

For every iteration, move node forward k steps.

If fewer than k nodes left → break and return the list.

Reversal Process:

Reverse the identified group of k nodes using the helper.

Connect previous section → reversed part → remaining list.

Repeat:

Continue until end of list reached.

✅ Complexity:

Time: O(N) — each node visited once.

Space: O(1) — in-place reversal.

**C++ Logic Explanation**

Count k nodes from the current head. If fewer than k remain → return as-is.

If there are at least k nodes, reverse exactly k nodes:

Use three pointers: prev, curr, and forward to reverse links.

After reversing k nodes, recursively call reverseKGroup on the remaining part.

Connect the tail of the reversed group (head) to the next reversed group.

Return prev — the new head of the reversed section.

✅ Complexity:

Time: O(N) — each node is visited once.

Space: O(N/k) (recursion stack).

**Java Logic Explanation**

Dummy Setup:
A dummy (left) node simplifies connecting reversed segments.

Group Counting:

Use count to detect when a group of k nodes is complete.

Reversal:

When k nodes are found:

Temporarily detach that group.

Reverse it using a helper function.

Reconnect reversed part with previous and next segments.

Recursive Helper:

Reverses one node at a time by updating next pointers recursively.

Traversal:

Continue this for all groups until the list ends.

✅ Complexity:

Time: O(N)

Space: O(N/k) (recursion stack in helper)