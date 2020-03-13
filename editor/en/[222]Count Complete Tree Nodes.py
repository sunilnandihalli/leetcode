# Given a complete binary tree, count the number of nodes. 
# 
#  Note: 
# 
#  Definition of a complete binary tree from Wikipedia: 
# In a complete binary tree every level, except possibly the last, is completely
#  filled, and all nodes in the last level are as far left as possible. It can hav
# e between 1 and 2h nodes inclusive at the last level h. 
# 
#  Example: 
# 
#  
# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6
# 
# Output: 6 
#  Related Topics Binary Search Tree
class TreeNode(object):
    def __init__(self, v, l, r):
        self.val = v
        self.left = l
        self.right = r


def toTree(arr, s):
    n = len(arr)
    if s < n:
        if arr[s]:
            l = 2 * s + 1
            r = 2 * s + 2
            return TreeNode(arr[s],
                            toTree(arr, l) if l < n else None,
                            toTree(arr, r) if r < n else None)
    else:
        return None


null = None


def test():
    for i in range(40):
        s = Solution()
        arr = list(range(100, 100 + i))
        tn = toTree(arr, 0)
        print(i)
        assert s.countNodes(tn) == len(arr)


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def get_unavailable_node(r):
    unavailable_node = 0
    while r:
        unavailable_node = unavailable_node * 2 + 1
        r = r.left
    return unavailable_node


def present(r, path):
    right = lambda x: x.right
    left = lambda x: x.left
    legs = [left, right]
    stk = []
    while path > 0:
        path, legid = divmod(path - 1, 2)
        stk.append(legs[legid])
    while len(stk) > 0:
        r = stk[-1](r)
        stk.pop()
    return bool(r)


def search_last_present_node(r, s, e):  # [s(present) ,e(absent))
    if s + 1 == e:
        return s
    else:
        mid = (s + e) // 2
        if present(r, mid):
            return search_last_present_node(r, mid, e)
        else:
            return search_last_present_node(r, s, mid)


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        e = get_unavailable_node(root)
        if e == 0:
            return 0
        s = e // 2
        last_present_node = search_last_present_node(root, s, e)
        return last_present_node + 1
# leetcode submit region end(Prohibit modification and deletion)
