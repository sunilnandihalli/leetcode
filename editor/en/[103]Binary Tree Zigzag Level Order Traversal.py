# Given a binary tree, return the zigzag level order traversal of its nodes' val
# ues. (ie, from left to right, then right to left for the next level and alternat
# e between). 
# 
#  
# For example: 
# Given binary tree [3,9,20,null,null,15,7], 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
#  
#  
# return its zigzag level order traversal as: 
#  
# [
#   [3],
#   [20,9],
#   [15,7]
# ]
#  
#  Related Topics Stack Tree Breadth-first Search


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def lorder(n, ret, d):
    if n:
        ret[d].append(n.val)
        lorder(n.left, ret, d + 1)
        lorder(n.right, ret, d + 1)

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        
# leetcode submit region end(Prohibit modification and deletion)
