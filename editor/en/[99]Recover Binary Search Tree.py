# Two elements of a binary search tree (BST) are swapped by mistake. 
# 
#  Recover the tree without changing its structure. 
# 
#  Example 1: 
# 
#  
# Input: [1,3,null,null,2]
# 
#    1
#   /
#  3
#   \
#    2
# 
# Output: [3,1,null,null,2]
# 
#    3
#   /
#  1
#   \
#    2
#  
# 
#  Example 2: 
# 
#  
# Input: [3,1,4,null,null,2]
# 
#   3
#  / \
# 1   4
#    /
#   2
# 
# Output: [2,1,4,null,null,3]
# 
#   2
#  / \
# 1   4
#    /
#   3
#  
# 
#  Follow up: 
# 
#  
#  A solution using O(n) space is pretty straight forward. 
#  Could you devise a constant space solution? 
#  
#  Related Topics Tree Depth-first Search
import random as r


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def random_bst(sorted_vals):
    if len(sorted_vals) == 0:
        return None
    p = r.randint(0, len(sorted_vals) - 1)
    ret = TreeNode(sorted_vals[p])
    ret.right = random_bst(sorted_vals[p + 1:])
    ret.left = random_bst(sorted_vals[:p])
    return ret


def rand_swap(x):
    i = r.randint(0, len(x) - 1)
    j = r.randint(0, len(x) - 1)
    tmp = x[i]
    x[i] = x[j]
    x[j] = tmp


def test_inp(n):
    x = list(range(n))
    rand_swap(x)
    return random_bst(x)


def inorder(r):
    if r:
        return preorder(r.left) + [r.val] + preorder(r.right)
    else:
        []


def is_sorted(x):
    for i in range(1, len(x)):
        if x[i - 1] > x[i]:
            return False
    return True


from graphviz import Digraph


def render_helper(node, g):
    if node:
        g.node(str(node.val))
        if node.left:
            render_helper(node.left, g)
            g.edge(str(node.val), str(node.left.val))
        if node.right:
            render_helper(node.right, g)
            g.edge(str(node.val), str(node.right.val))


def render(tree, name):
    g = Digraph(comment=name)
    render_helper(tree, g)
    g.render(name, '/home/sunilsn/leetcode/graphs')


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def inorder_generator(r):
    if r:
        for x in inorder_generator(r.left):
            yield x
        yield r.val
        for x in inorder_generator(r.right):
            yield x


right = 'right'
left = 'left'
from collections import namedtuple


def begin_iterator(r):
    if r:
        if r.left:
            return [r, left] + begin_iterator(r.left)
        else:
            return [r]
    else:
        return []


def end_iterator(r):
    if r:
        if r.right:
            return [r, right] + end_iterator(r.right)
        else:
            return [r]
    else:
        return []


def deref_iterator(iter):
    if len(iter) > 0:
        return iter[-1]
    else:
        return None


def decrement_iterator(iter):
    if len(iter) > 0:
        r = iter[-1]
        if r.left:
            return True, iter + [left] + end_iterator(r.left)
        elif len(iter) > 1:
            dir = iter[-2]
            if dir == right:
                return True, iter[:-2]
            elif dir == left:
                return False, []
        else:
            return False, []
    else:
        return False, []

def increment_iterator(iter):
    if len(iter) > 0:
        r = iter[-1]
        if r.right:
            return iter + [right] + begin_iterator(r.right)
        e

class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

# leetcode submit region end(Prohibit modification and deletion)
