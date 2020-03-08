# Serialization is the process of converting a data structure or object into a s
# equence of bits so that it can be stored in a file or memory buffer, or transmit
# ted across a network connection link to be reconstructed later in the same or an
# other computer environment. 
# 
#  Design an algorithm to serialize and deserialize a binary tree. There is no r
# estriction on how your serialization/deserialization algorithm should work. You 
# just need to ensure that a binary tree can be serialized to a string and this st
# ring can be deserialized to the original tree structure. 
# 
#  Example: 
# 
#  
# You may serialize the following tree:
# 
#     1
#    / \
#   2   3
#      / \
#     4   5
# 
# as "[1,2,3,null,null,4,5]"
#  
# 
#  Clarification: The above format is the same as how LeetCode serializes a bina
# ry tree. You do not necessarily need to follow this format, so please be creativ
# e and come up with different approaches yourself. 
# 
#  Note: Do not use class member/global/static variables to store states. Your s
# erialize and deserialize algorithms should be stateless. 
#  Related Topics Tree Design


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# leetcode submit region end(Prohibit modification and deletion)
