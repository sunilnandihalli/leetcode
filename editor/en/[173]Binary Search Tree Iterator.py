# Implement an iterator over a binary search tree (BST). Your iterator will be i
# nitialized with the root node of a BST. 
# 
#  Calling next() will return the next smallest number in the BST. 
# 
#  
# 
#  
#  
# 
#  Example: 
# 
#  
# 
#  
# BSTIterator iterator = new BSTIterator(root);
# iterator.next();    // return 3
# iterator.next();    // return 7
# iterator.hasNext(); // return true
# iterator.next();    // return 9
# iterator.hasNext(); // return true
# iterator.next();    // return 15
# iterator.hasNext(); // return true
# iterator.next();    // return 20
# iterator.hasNext(); // return false
#  
# 
#  
# 
#  Note: 
# 
#  
#  next() and hasNext() should run in average O(1) time and uses O(h) memory, wh
# ere h is the height of the tree. 
#  You may assume that next() call will always be valid, that is, there will be 
# at least a next smallest number in the BST when next() is called. 
#  
#  Related Topics Stack Tree Design


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def iterateBst(root):
    if root:
        iterateBst(root.left)
        yield root.val
        iterateBst(root.right)


class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stk=[]
        r = root
        while r:
            self.stk.append(r)
            r = r.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        if len(self.stk)>0:

        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
# leetcode submit region end(Prohibit modification and deletion)
