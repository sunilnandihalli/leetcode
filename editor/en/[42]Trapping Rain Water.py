# Given n non-negative integers representing an elevation map where the width of
#  each bar is 1, compute how much water it is able to trap after raining. 
# 
#  
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In 
# this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos
#  for contributing this image! 
# 
#  Example: 
# 
#  
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6 
#  Related Topics Array Two Pointers Stack

from typing import List


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) < 2:
            return 0
        h = height
        i = 0
        j = 0

        area = 0

        while i < len(h) and j < len(h):
            j = i + 1
            while j < len(h) and h[j] < h[i]:
                j += 1
            if j != len(h):
                x = i + 1
                while x < j:
                    area += h[i] - h[x]
                    x += 1
                i = j
            else:
                rightmost_max_loc = i

        i = len(h) - 1
        j = len(h) - 1
        while i >= rightmost_max_loc and j >= rightmost_max_loc:
            j = i - 1
            while j >= rightmost_max_loc and h[j] < h[i]:
                j -= 1
            x = i - 1
            while x > j:
                area += h[i] - h[x]
                x -= 1
            i = j
        return area


# leetcode submit region end(Prohibit modification and deletion)
def test():
    ts = [([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6), ([1, 1], 0), ([3, 2, 6], 1), ([6, 3, 4], 1)]
    s = Solution()
    for arr, ans in ts:
        actual = s.trap(arr)
        print(arr, ans, actual)
        assert ans == actual
