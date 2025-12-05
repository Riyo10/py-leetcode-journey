class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def rev(h: Optional[ListNode]) -> Optional[ListNode]:
            prev = None
            cur = h
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev

        dummy = ListNode(0, head)
        pre = dummy
        while True:
            tail = pre
            for _ in range(k):
                tail = tail.next
                if not tail:
                    return dummy.next
            nxt = tail.next
            tail.next = None
            h = pre.next
            pre.next = rev(h)
            h.next = nxt
            pre = h
