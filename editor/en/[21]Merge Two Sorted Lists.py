# Merge two sorted linked lists and return it as a new list. The new list should
#  be made by splicing together the nodes of the first two lists. 
# 
#  Example:
#  
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#  
#  Related Topics Linked List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
import heapq as h


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        x = []
        tails = {}
        if l1:
            h.heappush(x, (l1.val, 1))
            tails[1] = l1
        if l2:
            h.heappush(x, (l2.val, 2))
            tails[2] = l2

        head = None
        cur = None
        while len(x) != 0:
            _, nxt_id = h.heappop(x)
            nxt = tails[nxt_id]
            if nxt.next:
                tails[nxt_id] = nxt.next
                h.heappush(x, (nxt.next.val, nxt_id))
            else:
                del tails[nxt_id]
            if head is None:
                head = nxt
            if cur:
                cur.next = nxt
            cur = nxt
        return head

# leetcode submit region end(Prohibit modification and deletion)
