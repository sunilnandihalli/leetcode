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
    def __init__(self, v):
        self.val = v


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
        tr = TreeNode(cur_val)
        tr.left = left_node
        tr.right = right_node
        return tr, next_val
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
        cur_tree, _ = gen_tree(1)
        pre_tree = preorder(cur_tree)
        post_tree = postorder(cur_tree)
        print(pre_tree, post_tree)
        render(cur_tree, 'tree_%d' % n)
        s = Solution()
        reconstructed_tree = s.constructFromPrePost(pre_tree, post_tree)
        assert preorder(reconstructed_tree) == pre_tree
        assert postorder(reconstructed_tree) == post_tree


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def prepost(pre, post, post_index, s_pre, e_pre, s_post, e_post):
    if s_pre < e_pre:
        node = TreeNode(pre[s_pre])
        ls_pre = s_pre + 1
        le_post = post_index[pre[ls_pre]] + 1 if ls_pre < e_pre else e_post - 1
        le_pre = ls_pre + (le_post - s_post)
        ls_post = s_post
        node.left = prepost(pre, post, post_index, ls_pre, le_pre, ls_post, le_post)
        rs_pre = le_pre
        re_pre = e_pre
        rs_post = le_post
        re_post = e_post - 1
        node.right = prepost(pre, post, post_index, rs_pre, re_pre, rs_post, re_post)
        return node
    else:
        return None


class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        post_index = {x: i for i, x in enumerate(post)}
        n = len(pre)
        return prepost(pre, post, post_index, 0, n, 0, n)

# leetcode submit region end(Prohibit modification and deletion)
