# Given a binary search tree and a node in it, find the in-order successor of th
# at node in the BST. 
# 
#  The successor of a node p is the node with the smallest key greater than p.va
# l. 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [2,1,3], p = 1
# Output: 2
# Explanation: 1's in-order successor node is 2. Note that both p and the return
#  value is of TreeNode type.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [5,3,6,2,4,null,null,1], p = 6
# Output: null
# Explanation: There is no in-order successor of the current node, so the answer
#  is null.
#  
# 
#  
# 
#  Note: 
# 
#  
#  If the given node has no in-order successor in the tree, return null. 
#  It's guaranteed that the values of the tree are unique. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        if p.right is not None:
            x = p.right
            while x.left is not None:
                x = x.left
            return x
        else:
            path = []
            cur = root
            while cur != p:
                if p.val > cur.val:
                    cur = cur.right
                elif p.val < cur.val:
                    path.append(cur)
                    cur = cur.left
            return path[-1] if len(path)>0 else None


# leetcode submit region end(Prohibit modification and deletion)
