# Given a singly linked list, group all odd nodes together followed by the even 
# nodes. Please note here we are talking about the node number and not the value i
# n the nodes. 
# 
#  You should try to do it in place. The program should run in O(1) space comple
# xity and O(nodes) time complexity. 
# 
#  Example 1: 
# 
#  
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->NULL
#  
# 
#  Example 2: 
# 
#  
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL
#  
# 
#  Note: 
# 
#  
#  The relative order inside both the even and odd groups should remain as it wa
# s in the input. 
#  The first node is considered odd, the second node even and so on ... 
#  
#  Related Topics Linked List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        odd_head = None
        even_head = None
        odd_last_node = None
        even_last_node = None
        iter = head
        i = 0
        while iter:
            if i % 2 == 0:
                if odd_head is None:
                    odd_head = iter
                    odd_last_node = iter
                else:
                    odd_last_node.next = iter
                    odd_last_node = iter
            else:
                if even_head is None:
                    even_head = iter
                    even_last_node = iter
                else:
                    even_last_node.next = iter
                    even_last_node = iter
            iter = iter.next
            i += 1

        odd_last_node.next = even_head
        if even_last_node:
            even_last_node.next = None
        return odd_head
# leetcode submit region end(Prohibit modification and deletion)
