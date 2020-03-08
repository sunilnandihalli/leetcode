# Given an integer n, generate all structurally unique BST's (binary search tree
# s) that store values 1 ... n. 
# 
#  Example: 
# 
#  
# Input: 3
# Output:
# [
#   [1,null,3,2],
#   [3,2,null,1],
#   [3,1,null,null,2],
#   [2,1,3],
#   [1,null,2,null,3]
# ]
# Explanation:
# The above output corresponds to the 5 unique BST's shown below:
# 
#    1         3     3      2      1
#     \       /     /      / \      \
#      3     2     1      1   3      2
#     /     /       \                 \
#    2     1         2                 3
#  
#  Related Topics Dynamic Programming Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from functools import lru_cache


def tree_node(val, left, right):
    ret = TreeNode(val)
    ret.right = right
    ret.left = left
    return ret


def bst(lst, s, e):
    if s == e:
        yield None
    else:
        for i in range(s, e):
            left_trees = list(bst(lst, s, i))
            right_trees = list(bst(lst, i + 1, e))
            for l in left_trees:
                for r in right_trees:
                    yield tree_node(lst[i], l, r)


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if n>0:
            return list(bst(tuple(list(range(1, n + 1))), 0, n))
        else:
            return []
# leetcode submit region end(Prohibit modification and deletion)
