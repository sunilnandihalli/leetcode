# Given two sequences pushed and popped with distinct values, return true if and
#  only if this could have been the result of a sequence of push and pop operation
# s on an initially empty stack. 
# 
#  
# 
#  
#  Example 1: 
# 
#  
# Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
# Output: true
# Explanation: We might do the following sequence:
# push(1), push(2), push(3), push(4), pop() -> 4,
# push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1
#  
# 
#  
#  Example 2: 
# 
#  
# Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
# Output: false
# Explanation: 1 cannot be popped before 2.
#  
# 
#  
# 
#  Note: 
# 
#  
#  0 <= pushed.length == popped.length <= 1000 
#  0 <= pushed[i], popped[i] < 1000 
#  pushed is a permutation of popped. 
#  pushed and popped have distinct values. 
#  
#  
#  Related Topics Stack
def test():
    ts = [([1, 2, 3, 4, 5], [4, 5, 3, 2, 1], True), ([1, 2, 3, 4, 5], [4, 3, 5, 1, 2], False)]
    for a, b, ans in ts:
        s = Solution()
        actual = s.validateStackSequences(a, b)
        print(a, b, ans, actual)
        assert actual == ans


from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        i = 0
        j = 0
        stk = []
        while i < len(pushed) or j < len(popped):
            progress = False
            while len(stk) > 0 and j < len(popped) and stk[-1] == popped[j]:
                progress = True
                stk.pop()
                j += 1
            while i < len(pushed) and (len(stk) == 0 or stk[-1] != popped[j]):
                stk.append(pushed[i])
                progress = True
                i += 1
            if not progress:
                return False
        return True

# leetcode submit region end(Prohibit modification and deletion)
