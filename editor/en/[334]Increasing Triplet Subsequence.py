# Given an unsorted array return whether an increasing subsequence of length 3 e
# xists or not in the array. 
# 
#  Formally the function should: 
# 
#  Return true if there exists i, j, k 
# such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false
# . 
# 
#  Note: Your algorithm should run in O(n) time complexity and O(1) space comple
# xity. 
# 
#  
#  Example 1: 
# 
#  
# Input: [1,2,3,4,5]
# Output: true
#  
# 
#  
#  Example 2: 
# 
#  
# Input: [5,4,3,2,1]
# Output: false
#  
#  
# 

from typing import List

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')
        for x in nums:
            if min1 > x:
                min1 = x

            if x > min1:
                if min2 > x:
                    min2 = x

            if x > min2:
                return True
        return False


def test():
    ts = [([1, 2, 3, 4, 5], True), ([5, 4, 3, 2, 1], False), ([1, -1, -2, 3, -4, 5], True)]
    sol = Solution()
    for arr,ans in ts:
        actual = sol.increasingTriplet(arr)
        assert actual == ans
# leetcode submit region end(Prohibit modification and deletion)
