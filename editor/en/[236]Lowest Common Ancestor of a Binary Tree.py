# Given a binary tree, find the lowest common ancestor (LCA) of two given nodes 
# in the tree. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p and
#  q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  Given the following binary tree: root = [3,5,1,6,2,0,8,null,null,7,4] 
# 
#  
# 
#  Example 1: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
# Output: 3
# Explanation: The LCA of nodes 5 and 1 is 3.
#  
# 
#  Example 2: 
# 
#  
# Input: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
# Output: 5
# Explanation: The LCA of nodes 5 and 4 is 5, since a node can be a descendant o
# f itself according to the LCA definition.
#  
# 
#  
# 
#  Note: 
# 
#  
#  All of the nodes' values will be unique. 
#  p and q are different and both values will exist in the binary tree. 
#  
#  Related Topics Tree


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def lca(r, nodes_to_find):
    if r is not None:
        lval, l_nodes_found = lca(r.left, nodes_to_find)
        if not all(l_nodes_found):
            rval, r_nodes_found = lca(r.right, nodes_to_find)
            if all(r_nodes_found):
                return rval, r_nodes_found
            else:
                return r, [x or y or r == z for x, y, z in zip(l_nodes_found, r_nodes_found, nodes_to_find)]
        else:
            return lval, l_nodes_found
    else:
        return None, [False] * len(nodes_to_find)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return lca(root, [p, q])[0]
# leetcode submit region end(Prohibit modification and deletion)
