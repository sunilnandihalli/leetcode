# Given an array which consists of non-negative integers and an integer m, you c
# an split the array into m non-empty continuous subarrays. Write an algorithm to 
# minimize the largest sum among these m subarrays.
#  
# 
#  Note: 
# If n is the length of array, assume the following constraints are satisfied:
#  
#  1 ≤ n ≤ 1000 
#  1 ≤ m ≤ min(50, n) 
#  
#  
# 
#  Examples: 
#  
# Input:
# nums = [7,2,5,10,8]
# m = 2
# 
# Output:
# 18
# 
# Explanation:
# There are four ways to split nums into two subarrays.
# The best way is to split it into [7,2,5] and [10,8],
# where the largest sum among the two subarrays is only 18.
#  
#  Related Topics Binary Search Dynamic Programming
from typing import List


def test():
    ts = [([7, 2, 5, 10, 8], 2, 18)]
    s = Solution()
    for arr, m, ans in ts:
        actual = s.splitArray(arr, m)
        print(arr, m, ans, actual)
        assert actual == ans


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def min_max_sum(s, e, f, n):
    ret = None
    if e - s < n:
        ret = float('inf')
    elif e - s == n:
        ret = max([f(i, i + 1) for i in range(s, e)])
    elif n == 1:
        ret = f(s, e)
    else:
        for i in range(s + 1, e):
            max_sum = max(f(s, i), min_max_sum(i, e, f, n - 1))
            ret = min(ret, max_sum) if ret else max_sum
        ret = ret
    return ret


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        acc = [0]
        for x in nums:
            acc.append(acc[-1] + x)

        def msum(i, j):  # [i,j)
            return (acc[j] - acc[i]) if j > i else 0

        return min_max_sum(0, len(nums), msum, m)
# leetcode submit region end(Prohibit modification and deletion)
