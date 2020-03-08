# Given an array of integers and an integer k, you need to find the total number
#  of continuous subarrays whose sum equals to k. 
# 
#  Example 1: 
#  
# Input:nums = [1,1,1], k = 2
# Output: 2
#  
#  
# 
#  Note: 
#  
#  The length of the array is in range [1, 20,000]. 
#  The range of numbers in the array is [-1000, 1000] and the range of the integ
# er k is [-1e7, 1e7]. 
#  
#  
#  Related Topics Array Hash Table
from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from collections import defaultdict
import bisect as b


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        acc = [0]
        for x in nums:
            acc.append(acc[-1] + x)
        prefix_sum_indexes = defaultdict(list)
        for i, s in enumerate(acc):
            prefix_sum_indexes[s].append(i)
        count = 0
        for i in range(len(acc) - 1, -1, -1):
            s_end = acc[i]
            s_begin = s_end - k
            index_list = prefix_sum_indexes.get(s_begin, [])
            count += b.bisect_left(index_list, i)
        return count


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [([1, 1, 1], 2, 2), ([1, 2, 3], 3, 2), ([1], 0, 0)]
    s = Solution()
    for arr, k, ans in ts:
        actual = s.subarraySum(arr, k)
        print(arr, k, actual, ans)
        assert actual == ans
