# Given an unsorted array nums, reorder it such that nums[0] < nums[1] > nums[2]
#  < nums[3].... 
# 
#  Example 1: 
# 
#  
# Input: nums = [1, 5, 1, 1, 6, 4]
# Output: One possible answer is [1, 4, 1, 5, 1, 6]. 
# 
#  Example 2: 
# 
#  
# Input: nums = [1, 3, 2, 2, 3, 1]
# Output: One possible answer is [2, 3, 1, 3, 1, 2]. 
# 
#  Note: 
# You may assume all input has valid answer. 
# 
#  Follow Up: 
# Can you do it in O(n) time and/or in-place with O(1) extra space? Related Topi
# cs Sort
from hypothesis import given, strategies as st, example
from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return None

        i = 1
        gt = lambda x, y: x >= y
        lt = lambda x, y: x <= y

        def swap(i, j):
            x = nums[i]
            nums[i] = nums[j]
            nums[j] = x

        op = 0
        ops = [lt, gt]
        while i < len(nums):
            if not ops[op](nums[i - 1], nums[i]):
                swap(i - 1, i)
            i += 1
            op = (op + 1) % 2


# leetcode submit region end(Prohibit modification and deletion)
@given(arr=st.lists(st.integers()))
@example([0, 1])
def test(arr):
    s = Solution()
    print(arr)
    s.wiggleSort(arr)
    print(arr)
    i = 1
    gt = lambda x, y: x >= y
    lt = lambda x, y: x <= y
    op = 0
    ops = [lt, gt]
    while i < len(arr):
        assert ops[op](arr[i - 1], arr[i])
        op = (op + 1) % 2
        i += 1
