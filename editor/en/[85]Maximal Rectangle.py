# Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle c
# ontaining only 1's and return its area. 
# 
#  Example: 
# 
#  
# Input:
# [
#   ["1","0","1","0","0"],
#   ["1","0","1","1","1"],
#   ["1","1","1","1","1"],
#   ["1","0","0","1","0"]
# ]
# Output: 6
#  
#  Related Topics Array Hash Table Dynamic Programming Stack


# leetcode submit region begin(Prohibit modification and deletion)
from functools import lru_cache


class Solution:
    @lru_cache(None)
    def max_width(self, i, j):
        if i<0 or j<0:
            return 0
        if self.m[i][j] == '0':
            return 0
        else:
            return self.max_width(i, j - 1) + 1
        
    @lru_cache(None)
    def max_rectangle_hlr(self, i, j):
        if self.m[i][j] == '0':
            return i, j, j
        imin, jmin, jmax = self.max_rectangle_hlr(i - 1, j)
        cj = j - 1
        while cj < jmax:
            cimin, cjmin, cjmax = self.max_rectangle_hlr(i, cj)
            if cimin > i:
                cj = cjmax
            else:
                return

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        self.m = matrix
        self.p = len(matrix)
        if self.p > 0:
            self.q = len(matrix[0])
        for i in range(self.p):
            for j in range(self.q):
                self.num_ones(i, j)

# leetcode submit region end(Prohibit modification and deletion)
