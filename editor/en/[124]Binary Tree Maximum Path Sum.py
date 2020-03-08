# Given a non-empty binary tree, find the maximum path sum. 
# 
#  For this problem, a path is defined as any sequence of nodes from some starti
# ng node to any node in the tree along the parent-child connections. The path mus
# t contain at least one node and does not need to go through the root. 
# 
#  Example 1: 
# 
#  
# Input: [1,2,3]
# 
#        1
#       / \
#      2   3
# 
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: [-10,9,20,null,null,15,7]
# 
#    -10
#    / \
#   9  20
#     /  \
#    15   7
# 
# Output: 42
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
minf = -99999999999999


def msum(r):
    if r:
        lmLegSum, lmPathSum = msum(r.left)
        rmLegSum, rmPathSum = msum(r.right)
        mLegSums = []
        if lmLegSum:
            mLegSums.append(lmLegSum + r.val)
        if rmLegSum:
            mLegSums.append(rmLegSum + r.val)
        mLegSums.append(r.val)
        mPathSums = []
        if lmPathSum:
            mPathSums.append(lmPathSum)
        if rmPathSum:
            mPathSums.append(rmPathSum)
        mPathSums.append((lmLegSum or 0) + (rmLegSum or 0) + r.val)
        mPathSums.append(r.val)
        return max(mLegSums), max(mPathSums)
    else:
        return None, None


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        mLegSum, mPathSum = msum(root)
        return max(mLegSum, mPathSum)


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([1, 2, 3], 6), ([-10, 9, 20, null, null, 15, 7], 42), ([-2, 6, null, 0, -6], 6), ([-1,null,9,-6,3,null,null,null,-2],12)]
    s = Solution()
    for arr, ans in ts:
        actual = s.maxPathSum(toTree(arr, 0))
        print(actual, ans, arr)
        assert actual == ans
