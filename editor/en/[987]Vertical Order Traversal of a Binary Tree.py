# Given a binary tree, return the vertical order traversal of its nodes values. 
# 
# 
#  For each node at position (X, Y), its left and right children respectively wi
# ll be at positions (X-1, Y-1) and (X+1, Y-1). 
# 
#  Running a vertical line from X = -infinity to X = +infinity, whenever the ver
# tical line touches some nodes, we report the values of the nodes in order from t
# op to bottom (decreasing Y coordinates). 
# 
#  If two nodes have the same position, then the value of the node that is repor
# ted first is the value that is smaller. 
# 
#  Return an list of non-empty reports in order of X coordinate. Every report wi
# ll have a list of values of nodes. 
# 
#  
# 
#  Example 1: 
# 
#  
# 
#  
#  
# Input: [3,9,20,null,null,15,7]
# Output: [[9],[3,15],[20],[7]]
# Explanation: 
# Without loss of generality, we can assume the root node is at position (0, 0):
# 
# Then, the node with value 9 occurs at position (-1, -1);
# The nodes with values 3 and 15 occur at positions (0, 0) and (0, -2);
# The node with value 20 occurs at position (1, -1);
# The node with value 7 occurs at position (2, -2).
#  
# 
#  
#  Example 2: 
# 
#  
# 
#  
# Input: [1,2,3,4,5,6,7]
# Output: [[4],[2],[1,5,6],[3],[7]]
# Explanation: 
# The node with value 5 and the node with value 6 have the same position accordi
# ng to the given scheme.
# However, in the report "[1,5,6]", the node value of 5 comes first since 5 is s
# maller than 6.
#  
# 
#  
#  
# 
#  Note: 
# 
#  
#  The tree will have between 1 and 1000 nodes. 
#  Each node's value will be between 0 and 1000. 
#  
#  
# 
#  
#  
#  
#  Related Topics Hash Table Tree
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
        return TreeNode(arr[s], toTree(arr, l) if l < n else None, toTree(arr, r) if r < n else None)


null = None


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def gen_node_hashes(n, x, y):
    if n is not None:
        yield x, -y, n.val
        for v in gen_node_hashes(n.left, x - 1, y - 1):
            yield v
        for v in gen_node_hashes(n.right, x + 1, y - 1):
            yield v


from itertools import groupby


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        return [[v for _, _, v in x_group] for _, x_group in
                groupby(sorted(gen_node_hashes(root, 0, 0)), key=lambda x: x[0])]


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([3, 9, 20, null, null, 15, 7], [[9], [3, 15], [20], [7]]),
          ([1, 2, 3, 4, 5, 6, 7], [[4], [2], [1, 5, 6], [3], [7]])]
    s = Solution()
    for input, ans in ts:
        actual = s.verticalTraversal(toTree(input, 0))
        print(ans, actual)
        assert ans == actual
