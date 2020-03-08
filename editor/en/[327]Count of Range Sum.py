# Given an integer array nums, return the number of range sums that lie in [lowe
# r, upper] inclusive. 
# Range sum S(i, j) is defined as the sum of the elements in nums between indice
# s i and j (i ≤ j), inclusive. 
# 
#  Note: 
# A naive algorithm of O(n2) is trivial. You MUST do better than that. 
# 
#  Example: 
# 
#  
# Input: nums = [-2,5,-1], lower = -2, upper = 2,
# Output: 3 
# Explanation: The three ranges are : [0,0], [2,2], [0,2] and their respective s
# ums are: -2, -1, 2.
#  Related Topics Binary Search Divide and Conquer Sort Binary Indexed Tree Segm
# ent Tree

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
import bisect


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        count = 0
        if len(nums) == 0:
            return count

        N = len(nums)
        prefixSums = [0 for _ in range(N + 1)]

        for n in range(N):
            prefixSums[n + 1] = prefixSums[n] + nums[n]

        rightList = [prefixSums[-1]]
        for idx in reversed(range(len(prefixSums) - 1)):
            lowerIdx = bisect.bisect_left(rightList, lower + prefixSums[idx])
            upperIdx = bisect.bisect_right(rightList, upper + prefixSums[idx])
            count += (upperIdx - lowerIdx)
            insertIdx = bisect.bisect_left(rightList, prefixSums[idx])
            rightList.insert(insertIdx, prefixSums[idx])

        return count
# leetcode submit region end(Prohibit modification and deletion)
