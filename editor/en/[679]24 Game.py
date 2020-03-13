# 
# You have 4 cards each containing a number from 1 to 9. You need to judge wheth
# er they could operated through *, /, +, -, (, ) to get the value of 24.
#  
# 
#  Example 1: 
#  
# Input: [4, 1, 8, 7]
# Output: True
# Explanation: (8-4) * (7-1) = 24
#  
#  
# 
#  Example 2: 
#  
# Input: [1, 2, 1, 2]
# Output: False
#  
#  
# 
#  Note: 
#  
#  The division operator / represents real division, not integer division. For e
# xample, 4 / (1 - 2/3) = 12. 
#  Every operation done is between two numbers. In particular, we cannot use - a
# s a unary operator. For example, with [1, 1, 1, 1] as input, the expression -1 -
#  1 - 1 - 1 is not allowed. 
#  You cannot concatenate numbers together. For example, if the input is [1, 2, 
# 1, 2], we cannot write this as 12 + 12. 
#  
#  
#  Related Topics Depth-first Search

def test():
    ts = [([1, 2, 8], True), ([2, 3, 4], True), ([4, 1, 8, 7], True), ([1, 2, 1, 2], False)]
    for arr, ans in ts:
        s = Solution()
        actual = s.judgePoint24(arr)
        print(arr, ans, actual)
        assert ans == actual


from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
mul = lambda a, b: a * b
div = lambda a, b: a / b
add = lambda a, b: a + b
sub = lambda a, b: a - b
ops = [mul, div, add, sub]
from fractions import Fraction as frac


def permute(nums):
    if len(nums) == 0:
        yield []
    else:
        for i, x in enumerate(nums):
            for p in permute(nums[:i] + nums[i + 1:]):
                yield [x] + p


def all_possible(nums):
    if len(nums) == 1:
        yield frac(nums[0])
    else:
        for i in range(1, len(nums)):
            for x in all_possible(nums[:i]):
                for y in all_possible(nums[i:]):
                    for op in ops:
                        try:
                            yield op(x, y)
                        except:
                            pass


class Solution:
    def judgePoint24(self, nums: List[int]) -> bool:
        for p in permute(nums):
            for x in all_possible(p):
                if x == 24:
                    return True
        return False

# leetcode submit region end(Prohibit modification and deletion)
