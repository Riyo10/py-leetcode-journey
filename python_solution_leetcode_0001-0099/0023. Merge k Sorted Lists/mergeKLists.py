class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        from heapq import heappush, heappop
        pq = []
        c = 0
        for node in lists:
            if node:
                heappush(pq, (node.val, c, node))
                c += 1
        dummy = cur = ListNode(0)
        while pq:
            _, _, node = heappop(pq)
            if node.next:
                heappush(pq, (node.next.val, c, node.next))
                c += 1
            cur.next = node
            cur = cur.next
        return dummy.next
