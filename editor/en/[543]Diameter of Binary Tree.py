# 
# Given a binary tree, you need to compute the length of the diameter of the tre
# e. The diameter of a binary tree is the length of the longest path between any t
# wo nodes in a tree. This path may or may not pass through the root.
#  
# 
#  
# Example: 
# Given a binary tree 
#  
#           1
#          / \
#         2   3
#        / \     
#       4   5    
#  
#  
#  
# Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
#  
# 
#  Note:
# The length of path between two nodes is represented by the number of edges bet
# ween them.
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dia(r):
    if r:
        lmaxLegLength, lmaxPathLength = dia(r.left)
        rmaxLegLength, rmaxPathLength = dia(r.right)
        return max(lmaxLegLength + 1, rmaxLegLength + 1), max(lmaxPathLength, rmaxPathLength,
                                                              lmaxLegLength + rmaxLegLength + 1)
    else:
        return 0, 0


class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        x = max(dia(root))
        return x - 1 if x > 0 else 0
# leetcode submit region end(Prohibit modification and deletion)
