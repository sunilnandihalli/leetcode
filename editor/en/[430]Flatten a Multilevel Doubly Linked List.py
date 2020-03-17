# You are given a doubly linked list which in addition to the next and previous 
# pointers, it could have a child pointer, which may or may not point to a separat
# e doubly linked list. These child lists may have one or more children of their o
# wn, and so on, to produce a multilevel data structure, as shown in the example b
# elow. 
# 
#  Flatten the list so that all the nodes appear in a single-level, doubly linke
# d list. You are given the head of the first level of the list. 
# 
#  
#  Example 1: 
# 
#  
# Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
# Output: [1,2,3,7,8,11,12,9,10,4,5,6]
# Explanation:
# 
# The multilevel linked list in the input is as follows:
# 
# 
# 
# After flattening the multilevel linked list it becomes:
# 
# 
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1,2,null,3]
# Output: [1,3,2]
# Explanation:
# 
# The input multilevel linked list is as follows:
# 
#   1---2---NULL
#   |
#   3---NULL
#  
# 
#  Example 3: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  
# 
#  How multilevel linked list is represented in test case: 
# 
#  We use the multilevel linked list from Example 1 above: 
# 
#  
#  1---2---3---4---5---6--NULL
#          |
#          7---8---9---10--NULL
#              |
#              11--12--NULL 
# 
#  The serialization of each level is as follows: 
# 
#  
# [1,2,3,4,5,6,null]
# [7,8,9,10,null]
# [11,12,null]
#  
# 
#  To serialize all levels together we will add nulls in each level to signify n
# o node connects to the upper node of the previous level. The serialization becom
# es: 
# 
#  
# [1,2,3,4,5,6,null]
# [null,null,7,8,9,10,null]
# [null,11,12,null]
#  
# 
#  Merging the serialization of each level and removing trailing nulls we obtain
# : 
# 
#  
# [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12] 
# 
#  
#  Constraints: 
# 
#  
#  Number of Nodes will not exceed 1000. 
#  1 <= Node.val <= 10^5 
#  
#  Related Topics Linked List Depth-first Search

cval = 1


class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


from random import randint, random


def random_mdlist():
    val = cval
    cval += 1
    next_prob = 0.8
    child_prob = 0.3
    next_mdlist = random_mdlist() if random() < next_prob else None
    child_mdlist = random_mdlist() if random() < child_prob else None
    ret = Node(val, None, next_mdlist, child_mdlist)
    if next_mdlist is not None:
        next_mdlist.prev = ret
    return ret

def test():


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""


def flatten_mdlist(head):  # assumed that head is not None
    cur = head
    while True:
        nxt = cur.next
        if cur.child:
            child_head, child_last = flatten_mdlist(cur.child)
            cur.next = child_head
            child_head.prev = cur
            if nxt:
                nxt.prev = child_last
                child_last.next = nxt
                cur.child = None
                cur = child_last
        if nxt is None:
            return head, cur
        else:
            cur = nxt


def check_dlist(h):
    cur = h
    assert h.prev is None
    while cur:
        assert cur.next is None or cur.next.prev == cur
        assert cur.child is None
        cur = cur.next


class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        head = flatten_mdlist(head)[0]
# leetcode submit region end(Prohibit modification and deletion)
