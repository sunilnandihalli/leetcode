# Convert a Binary Search Tree to a sorted Circular Doubly-Linked List in place.
#  
# 
#  You can think of the left and right pointers as synonymous to the predecessor
#  and successor pointers in a doubly-linked list. For a circular doubly linked li
# st, the predecessor of the first element is the last element, and the successor 
# of the last element is the first element. 
# 
#  We want to do the transformation in place. After the transformation, the left
#  pointer of the tree node should point to its predecessor, and the right pointer
#  should point to its successor. You should return the pointer to the smallest el
# ement of the linked list. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [4,2,5,1,3]
# 
# 
# Output: [1,2,3,4,5]
# 
# Explanation: The figure below shows the transformed BST. The solid line indica
# tes the successor relationship, while the dashed line means the predecessor rela
# tionship.
# 
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,1,3]
# Output: [1,2,3]
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: []
# Explanation: Input is an empty tree. Output is also an empty Linked List.
#  
# 
#  Example 4: 
# 
#  
# Input: root = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  -1000 <= Node.val <= 1000 
#  Node.left.val < Node.val < Node.right.val 
#  All values of Node.val are unique. 
#  0 <= Number of Nodes <= 2000 
#  
#  Related Topics Linked List Divide and Conquer Tree


# leetcode submit region begin(Prohibit modification and deletion)
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left (prev)
        self.right = right (next)
"""


def toCList(n):
    if n:
        toCList(n.left)
        toCList(n.right)
        if n.left and n.right:
            l = n.left
            r = n.right
            n.right.left.right = n.left.right

        elif n.right:
            pass
        elif n.left:
            pass



class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        start,_ = toList(root)
        return start
    # leetcode submit region end(Prohibit modification and deletion)
