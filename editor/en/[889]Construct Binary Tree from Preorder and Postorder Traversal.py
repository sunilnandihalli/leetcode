# Return any binary tree that matches the given preorder and postorder traversal
# s. 
# 
#  Values in the traversals pre and post are distinct positive integers. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: pre = [1,2,4,5,3,6,7], post = [4,5,2,6,7,3,1]
# Output: [1,2,3,4,5,6,7]
#  
# 
#  
# 
#  Note: 
# 
#  
#  1 <= pre.length == post.length <= 30 
#  pre[] and post[] are both permutations of 1, 2, ..., pre.length. 
#  It is guaranteed an answer exists. If there exists multiple answers, you can 
# return any of them. 
#  
#  
#  Related Topics Tree


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


from random import random
from graphviz import Digraph


def gen_tree(cur_val, new_node_prob=1.0):
    f = 0.7
    if random() < new_node_prob:
        left_node, next_val = gen_tree(cur_val + 1, new_node_prob * f)
        right_node, next_val = gen_tree(next_val, new_node_prob * f)
        return TreeNode(cur_val, left_node, right_node), next_val
    else:
        return None, cur_val


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

def preorder(tree):
    return [tree.val] + preorder(tree.left) + preorder(tree.right) if tree else []

def postorder(tree):
    return postorder(tree.left) + postorder(tree.right) + [tree.val] if tree else []

null = None


def test():
    for n in range(10):
        cur_tree,_ = gen_tree(1)
        pre_tree = preorder(cur_tree)
        post_tree = postorder(cur_tree)
        print(pre_tree, post_tree)
        render(cur_tree, 'tree_%d' % n)

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        pass
# leetcode submit region end(Prohibit modification and deletion)
