class Solution:
    def reverseKGroup(self, head, k):
        def reverse(start, end):
            prev = None
            curr = start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while True:
            node = prev
            for _ in range(k):
                node = node.next
                if not node:
                    return dummy.next
            start = prev.next
            end = node.next
            new_head = reverse(start, end)
            prev.next = new_head
            start.next = end
            prev = start