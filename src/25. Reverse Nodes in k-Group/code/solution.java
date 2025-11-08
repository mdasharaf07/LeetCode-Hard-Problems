class Solution {
    public ListNode reverseKGroup(ListNode head, int k) {
        // Base case: if list is empty or k <= 1, no need to reverse
        if (head == null || k <= 1) return head;

        // Dummy node to simplify edge cases (reversal starting from head)
        ListNode left = new ListNode(-1);
        left.next = head;

        // Pointer to traverse the list
        ListNode right = head;

        // To store the final modified head after reversal
        ListNode ans = head;

        int count = 1; // Counter to track group size

        // Traverse the linked list
        while (right != null) {
            // When a full group of k nodes is found
            if (count % k == 0) {
                ListNode rev = left.next;  // Start of the current group
                ListNode temp = right.next; // Node after the current group

                // Disconnect the current group from the rest of the list
                left.next = null;
                right.next = null;

                // Reverse the current group
                ListNode revAns = helper(rev, null);

                // Connect the reversed group back to the list
                left.next = revAns;

                // For the first reversal, update the answer pointer
                if (count - k == 0) ans = left;

                // Move to the end of the reversed group
                if (revAns != null) {
                    while (revAns.next != null) revAns = revAns.next;
                    revAns.next = temp; // Connect with the next part
                }

                // Update pointers for the next group
                right = revAns;
                left = revAns;
            }

            count++; // Move to next node
            if (right != null) right = right.next;
        }

        // Return the actual head (next of dummy node)
        return ans.next;
    }

    // Recursive helper function to reverse a linked list
    public ListNode helper(ListNode node, ListNode prev) {
        if (node == null) return prev; // Base case: reached end of list
        ListNode temp = node.next;     // Store next node
        node.next = prev;              // Reverse pointer
        prev = node;                   // Move prev forward
        node = temp;                   // Move current forward
        return helper(node, prev);     // Recursive call
    }
}