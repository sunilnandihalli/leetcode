# Given a binary tree, return the level order traversal of its nodes' values. (i
# e, from left to right, level by level). 
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
# return its level order traversal as: 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics Tree Breadth-first Search
from typing import List

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
        return TreeNode(arr[s],
                        toTree(arr, l) if l < n else None,
                        toTree(arr, r) if r < n else None)


null = None

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict


def lorder(n, ret, d):
    if n:
        ret[d].append(n.val)
        lorder(n.left, ret, d + 1)
        lorder(n.right, ret, d + 1)

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ret = defaultdict(list)
        lorder(root, ret, 0)
        return [ret[i] for i in range(len(ret))]



# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([3, 9, 20, null, null, 15, 7], [[3], [9, 20], [15, 7]])]
    s = Solution()
    for arr, ans in ts:
        actual = s.levelOrder(toTree(arr, 0))
        print(actual, ans)
        assert actual == ans
