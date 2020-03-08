# Given a triangle, find the minimum path sum from top to bottom. Each step you 
# may move to adjacent numbers on the row below. 
# 
#  For example, given the following triangle 
# 
#  
# [
#      [2],
#     [3,4],
#    [6,5,7],
#   [4,1,8,3]
# ]
#  
# 
#  The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11). 
# 
#  Note: 
# 
#  Bonus point if you are able to do this using only O(n) extra space, where n i
# s the total number of rows in the triangle. 
#  Related Topics Array Dynamic Programming


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


@lru_cache(None)
def sum(m, i, j):
    if i < len(m):
        return min(sum(m, i + 1, j), sum(m, i + 1, j + 1)) + m[i][j]
    else:
        return 0


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = tuple([tuple(x) for x in triangle])
        return sum(m, 0, 0)
# leetcode submit region end(Prohibit modification and deletion)
