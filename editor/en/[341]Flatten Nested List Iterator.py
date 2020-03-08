# Given a nested list of integers, implement an iterator to flatten it. 
# 
#  Each element is either an integer, or a list -- whose elements may also be in
# tegers or other lists. 
# 
#  Example 1: 
# 
#  
#  
# Input: [[1,1],2,[1,1]]
# Output: [1,1,2,1,1]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,1,2,1,1]. 
# 
#  
#  Example 2: 
# 
#  
# Input: [1,[4,[6]]]
# Output: [1,4,6]
# Explanation: By calling next repeatedly until hasNext returns false, 
#              the order of elements returned by next should be: [1,4,6].
#  
#  
#  
#  Related Topics Stack Design


# leetcode submit region begin(Prohibit modification and deletion)
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """


def generator(nestedList):
    for x in nestedList:
        if x.isInteger():
            yield x
        else:
            for y in generator(x.getList()):
                yield y


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.g = generator(nestedList)
        self.next_val = None

    def next(self) -> int:
        if self.next_val:
            ret = self.next_val
            self.next_val = None
        else:
            ret = next(self.g)
        return ret

    def hasNext(self) -> bool:
        try:
            self.next_val = next(self.g)
            return True
        except StopIteration:
            self.next_val = None
            return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
# leetcode submit region end(Prohibit modification and deletion)
