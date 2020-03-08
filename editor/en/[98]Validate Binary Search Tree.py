# Given a binary tree, determine if it is a valid binary search tree (BST). 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the node's
#  key. 
#  The right subtree of a node contains only nodes with keys greater than the no
# de's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
# 
#  Example 1: 
# 
#  
#     2
#    / \
#   1   3
# 
# Input: [2,1,3]
# Output: true
#  
# 
#  Example 2: 
# 
#  
#     5
#    / \
#   1   4
#      / \
#     3   6
# 
# Input: [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
#  Related Topics Tree Depth-first Search

class TreeNode(object):
    def __init__(self, v, l, r):
        self.val = v
        self.left = l
        self.right = r


def toTree(arr, s):
    n = len(arr)
    if arr[s]:
        l = 2 * s + 1
        r = 2 * s + 2
        return TreeNode(arr[s], toTree(arr, l) if l < n else None, toTree(arr, r) if r < n else None)

null  = None

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def valid(n):
    if n:
        r_is_valid, r_min_val, r_max_val = valid(n.right)
        l_is_valid, l_min_val, l_max_val = valid(n.left)
        if r_is_valid and l_is_valid and (not l_max_val or l_max_val < n.val) and (not r_min_val or r_min_val > n.val):
            ret = True, (l_min_val or n.val), (r_max_val or n.val)
        else:
            ret = False, None, None
    else:
        ret = True, None, None
    return ret


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        ret, _, _ = valid(root)
        return ret

# leetcode submit region end(Prohibit modification and deletion)

