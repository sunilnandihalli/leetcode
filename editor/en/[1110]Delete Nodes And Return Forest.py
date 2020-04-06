# Given the root of a binary tree, each node in the tree has a distinct value. 
# 
#  After deleting all nodes with a value in to_delete, we are left with a forest
#  (a disjoint union of trees). 
# 
#  Return the roots of the trees in the remaining forest. You may return the res
# ult in any order. 
# 
#  
#  Example 1: 
# 
#  
# 
#  
# Input: root = [1,2,3,4,5,6,7], to_delete = [3,5]
# Output: [[1,2,null,4],[6],[7]]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the given tree is at most 1000. 
#  Each node has a distinct value between 1 and 1000. 
#  to_delete.length <= 1000 
#  to_delete contains distinct values between 1 and 1000. 
#  Related Topics Tree Depth-first Search
from typing import List


class TreeNode(object):
    def __init__(self, v, l, r):
        self.val = v
        self.left = l
        self.right = r


def toTree(arr, s):
    n = len(arr)
    if arr[s] is not None:
        l = 2 * s + 1
        r = 2 * s + 2
        return TreeNode(arr[s],
                        toTree(arr, l) if l < n else None,
                        toTree(arr, r) if r < n else None)


def inorder(r):
    if r:
        return inorder(r.left) + [r.val] + inorder(r.right)
    else:
        return []


def test():
    t = toTree(list(range(10)),0)
    s = Solution()
    inorder_t = inorder(t)
    ans = []
    for r in s.delNodes(t, [3,5,8]):
        ans.append(inorder(r))
    print(ans, inorder_t)


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def delete_nodes(r, to_delete, ret):
    retv = None
    if r:
        r.right = delete_nodes(r.right, to_delete, ret)
        r.left = delete_nodes(r.left, to_delete, ret)
        if r.val in to_delete:
            if r.right:
                ret.append(r.right)
            if r.left:
                ret.append(r.left)
            retv = None
        else:
            retv = r
    else:
        retv = None
    return retv

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        ret = []
        root = delete_nodes(root, to_delete, ret)
        if root:
            ret.append(root)
        return ret

# leetcode submit region end(Prohibit modification and deletion)
