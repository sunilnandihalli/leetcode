# Suppose an array sorted in ascending order is rotated at some pivot unknown to
#  you beforehand. 
# 
#  (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]). 
# 
#  You are given a target value to search. If found in the array return its inde
# x, otherwise return -1. 
# 
#  You may assume no duplicate exists in the array. 
# 
#  Your algorithm's runtime complexity must be in the order of O(log n). 
# 
#  Example 1: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1 
#  Related Topics Array Binary Search

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
from bisect import bisect


def binsearch(nums, x, s, e):
    if s == e:
        return -1
    elif s + 1 == e:
        if nums[s] == x:
            return s
        else:
            return -1
    else:
        mid = (s + e) // 2
        mv = nums[mid]
        if mv >= nums[s]:
            if x >= mv or x < nums[s]:
                return binsearch(nums, x, mid, e)
            else:
                return binsearch(nums, x, s, mid)
        else:
            if mv <= x < nums[s]:
                return binsearch(nums, x, mid, e)
            else:
                return binsearch(nums, x, s, mid)


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return binsearch(nums, target, 0, len(nums))


# leetcode submit region end(Prohibit modification and deletion)
from random import randint


def test():
    ts = [([4, 5, 6, 7, 0, 1, 2], 0, 4), ([4, 5, 6, 7, 0, 1, 2], 3, -1)]
    s = Solution()
    for arr, target, ans in ts:
        actual = s.search(arr, target)
        print(arr, target, ans, actual)
        assert ans == actual
    num_tests = 100
    m = 100
    n = 10
    for i in range(num_tests):
        x = sorted([randint(0, m) for i in range(n)])
        p = randint(0, n)
        nums = x[p:] + x[:p]
        target = randint(-100, 200)
        ans = binsearch(nums, target, 0, len(nums))
        if target not in nums:
            assert ans == -1
        else:
            assert nums[ans] == target
