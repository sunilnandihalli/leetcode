# In a given array nums of positive integers, find three non-overlapping subarra
# ys with maximum sum. 
# 
#  Each subarray will be of size k, and we want to maximize the sum of all 3*k e
# ntries. 
# 
#  Return the result as a list of indices representing the starting position of 
# each interval (0-indexed). If there are multiple answers, return the lexicograph
# ically smallest one. 
# 
#  Example: 
# 
#  
# Input: [1,2,1,2,6,7,5,1], 2
# Output: [0, 3, 5]
# Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indic
# es [0, 3, 5].
# We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicogra
# phically larger.
#  
# 
#  
# 
#  Note: 
# 
#  
#  nums.length will be between 1 and 20000. 
#  nums[i] will be between 1 and 65535. 
#  k will be between 1 and floor(nums.length / 3). 
#  
# 
#  
#  Related Topics Array Dynamic Programming

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def sum_upto_and_including(self, i):
        n = len(self.nums)
        if i < 0:
            return 0
        elif i >= n:
            return self.sum_upto_and_including(n - 1)
        else:
            return self.sum_upto_and_including(i - 1) + self.nums[i]

    @lru_cache(None)
    def sumK(self, i):  # k sum starting at startIndex
        return self.sum_upto_and_including(i + self.k - 1) - self.sum_upto_and_including(i - 1)

    @lru_cache(None)
    def maxSumKStartingFrom(self, start_index, num_subarrays):
        if num_subarrays == 0 or start_index > len(self.nums) - self.k * num_subarrays:
            return 0, []

        sum1, indices1 = self.maxSumKStartingFrom(start_index + 1, num_subarrays)
        sum2, indices2 = self.maxSumKStartingFrom(start_index + self.k, num_subarrays - 1)
        csum = self.sumK(start_index)
        if csum + sum2 >= sum1:
            return csum + sum2, [start_index] + indices2
        else:
            return sum1, indices1

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        self.nums = nums
        self.k = k
        for num_subarrays in range(1, 4):
            for start_index in range(len(nums) - num_subarrays * k - 1, -1, -1):
                self.maxSumKStartingFrom(start_index, num_subarrays)
        return self.maxSumKStartingFrom(0, 3)[1]


# leetcode submit region end(Prohibit modification and deletion)

def test():
    ts = [([1, 2, 1, 2, 6, 7, 5, 1], 2, [0, 3, 5])]
    s = Solution()
    for nums, k, ans in ts:
        actual = s.maxSumOfThreeSubarrays(nums, k)
        print(nums, k, ans, actual)
        assert actual == ans
