# Given an integer array nums, find the contiguous subarray (containing at least
#  one number) which has the largest sum and return its sum. 
# 
#  Example: 
# 
#  
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#  
# 
#  Follow up: 
# 
#  If you have figured out the O(n) solution, try coding another solution using 
# the divide and conquer approach, which is more subtle. 
#  Related Topics Array Divide and Conquer Dynamic Programming

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
def test():
    ts = [([-1], -1), ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6)]
    s = Solution()
    for arr, ans in ts:
        actual = s.maxSubArray(arr)
        print(actual, ans, arr)
        assert actual == ans


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        acc = [0]

        for i in range(len(nums)):
            acc.append(acc[-1] + nums[i])

        m = acc[1] - acc[0]
        cmin = min(acc[0], acc[1])
        for x in acc[2:]:
            m = max(m, x - cmin)
            cmin = min(cmin, x)

        return m

# leetcode submit region end(Prohibit modification and deletion)
