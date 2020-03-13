# You are a professional robber planning to rob houses along a street. Each hous
# e has a certain amount of money stashed, the only constraint stopping you from r
# obbing each of them is that adjacent houses have security system connected and i
# t will automatically contact the police if two adjacent houses were broken into 
# on the same night. 
# 
#  Given a list of non-negative integers representing the amount of money of eac
# h house, determine the maximum amount of money you can rob tonight without alert
# ing the police. 
# 
#  Example 1: 
# 
#  
# Input: [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
#              Total amount you can rob = 1 + 3 = 4. 
# 
#  Example 2: 
# 
#  
# Input: [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 
# (money = 1).
#              Total amount you can rob = 2 + 9 + 1 = 12.
#  
#  Related Topics Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def rob(nums, i):
    if i < 0:
        return 0
    elif i == 0:
        return nums[0]
    elif i == 1:
        return nums[1]
    elif i == 2:
        return nums[2] + nums[0]
    else:
        return max(rob(nums, i - 3), rob(nums, i - 2)) + nums[i]


class Solution:
    def rob(self, nums: List[int]) -> int:
        nums = tuple(nums)
        n = len(nums)
        for i in range(n):
            rob(nums, i)
        return max(rob(nums, n - 1), rob(nums, n - 2))

# leetcode submit region end(Prohibit modification and deletion)
