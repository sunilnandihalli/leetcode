# Given an array nums of n integers, are there elements a, b, c in nums such tha
# t a + b + c = 0? Find all unique triplets in the array which gives the sum of ze
# ro. 
# 
#  Note: 
# 
#  The solution set must not contain duplicate triplets. 
# 
#  Example: 
# 
#  
# Given array nums = [-1, 0, 1, 2, -1, -4],
# 
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#  Related Topics Array Two Pointers


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    def nsum(self, target_sum):
        ret = []
        for i, x in enumerate(self.nums):
            for j, y in enumerate(self.nums[i + 1:], i + 1):
                for k, z in enumerate(self.nums[j + 1:], j + 1):
                    if x + y + z == target_sum:
                        ret.append([x, y, z])
        return ret

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.nums = nums
        return self.nsum(0)
# leetcode submit region end(Prohibit modification and deletion)
